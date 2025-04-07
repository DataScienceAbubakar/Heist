git clone https://github.com/AliaksandrSiarohin/first-order-model.git
cd first-order-model
conda create -n fomm python=3.8 -y
conda activate fomm
pip install -r requirements.txt
mkdir -p checkpoints/vox
cd checkpoints/vox
wget https://github.com/AliaksandrSiarohin/first-order-model/blob/master/vox-cpk.pth.tar?raw=true -O vox-cpk.pth.tar
cd ../../

import os
import sys
import imageio
import numpy as np
import cv2
import torch
from skimage.transform import resize
from demo import load_checkpoints, make_animation
from PIL import Image

# Load source image (the face to animate)
source_image_path = 'target.png'
source_image = imageio.imread(source_image_path)
source_image = resize(source_image, (256, 256))[..., :3]

# Start webcam
cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Webcam not accessible"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
                                          checkpoint_path='checkpoints/vox/vox-cpk.pth.tar')

print("Model loaded. Starting real-time animation...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize webcam frame
        driving_frame = resize(frame[:, :, ::-1], (256, 256))[..., :3]

        # Animate
        predictions = make_animation(source_image, [driving_frame], generator, kp_detector, relative=True)
        output_frame = predictions[0]
        output_frame = (output_frame * 255).astype(np.uint8)
        
        # Show animated face
        cv2.imshow("Deepfake Avatar", cv2.cvtColor(output_frame, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
