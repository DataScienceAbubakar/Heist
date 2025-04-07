import librosa
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

def load_audio(file_path, sr=22050):
    audio, _ = librosa.load(file_path, sr=sr)
    return audio
 model = Sequential([
        LSTM(128, input_shape=input_shape, return_sequences=True),
        Dropout(0.2),
        LSTM(64, return_sequences=False),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dense(input_shape[0], activation='tanh')
    ])
def extract_features(audio, sr=22050, n_mfcc=40):
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfccs.T, axis=0)
 model = Sequential([
        LSTM(128, input_shape=input_shape, return_sequences=True),
        Dropout(0.2),
        LSTM(64, return_sequences=False),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dense(input_shape[0], activation='tanh')
    ])
def build_model(input_shape):
    model = Sequential([
        LSTM(128, input_shape=input_shape, return_sequences=True),
        Dropout(0.2),
        LSTM(64, return_sequences=False),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dense(input_shape[0], activation='tanh')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def change_voice(audio, model, sr=22050):
    features = extract_features(audio, sr=sr)
    features = features.reshape(1, features.shape[0], 1)
    transformed_features = model.predict(features)
    return librosa.feature.inverse.mfcc_to_audio(transformed_features[0])

if __name__ == "__main__":
    # Load and preprocess audio
    input_audio_path = "input_audio.wav"
    output_audio_path = "output_audio.wav"
    audio = load_audio(input_audio_path)

    # Build and train the model (dummy training for demonstration)
    features = extract_features(audio)
    model = build_model((features.shape[0], 1))
    model.fit(np.array([features]).reshape(-1, features.shape[0], 1), 
              np.array([features]).reshape(-1, features.shape[0]), 
              epochs=10, verbose=1)

    # Transform the voice
    transformed_audio = change_voice(audio, model)

    # Save the transformed audio
    librosa.output.write_wav(output_audio_path, transformed_audio, sr=22050)