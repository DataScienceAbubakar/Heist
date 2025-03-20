# flowchart TD
    subgraph "Client Layer"
        UI[User Interface]
        WebRTC[WebRTC Client]
        ML_Client[ML Client Processing]
    end

    subgraph "Server Layer"
        API[API Gateway]
        AuthService[Authentication Service]
        SessionManager[Session Manager]
        MediaServer[Media Processing Server]
    end

    subgraph "AI Processing Layer"
        ML_Models[ML Model Service]
        BackgroundReplace[Background Replacement]
        GestureRecog[Gesture Recognition]
        FaceDetect[Face Detection & Smart Framing]
        AudioEnhance[Audio Enhancement]
    end

    subgraph "Data Layer"
        UserDB[(User Database)]
        SessionDB[(Session Database)]
        ML_Storage[(ML Model Storage)]
        RecordingStorage[(Recording Storage)]
    end

    %% Client connections
    UI --> WebRTC
    UI --> ML_Client
    WebRTC --> API
    ML_Client --> API

    %% Server connections
    API --> AuthService
    API --> SessionManager
    SessionManager --> MediaServer
    
    %% AI layer connections
    MediaServer <--> ML_Models
    ML_Models --> BackgroundReplace
    ML_Models --> GestureRecog
    ML_Models --> FaceDetect
    ML_Models --> AudioEnhance
    
    %% Data layer connections
    AuthService --> UserDB
    SessionManager --> SessionDB
    ML_Models --> ML_Storage
    MediaServer --> RecordingStorage
    
    %% External Services
    CloudInfra[Cloud Infrastructure]
    CDN[Content Delivery Network]
    
    MediaServer --> CloudInfra
    CloudInfra --> CDN
    CDN --> WebRTC