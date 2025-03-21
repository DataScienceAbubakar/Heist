# Land System Workflow

The following diagram illustrates the automated land search and inquiry system workflow:

```mermaid
flowchart TD
    %% Main styles
    classDef process fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef decision fill:#e1f5fe,stroke:#333,stroke-width:1px,color:#000
    classDef endpoint fill:#e8f5e9,stroke:#333,stroke-width:1px,color:#000
    classDef subproc fill:#fff8e1,stroke:#333,stroke-width:1px

    %% Start process
    A[Start: Land_searcher] --> B[Select target county]
    B --> C[Search for available land parcels in county]
    C --> D{Land parcels found?}
    D -->|No| E[Try different county]
    E --> B
    D -->|Yes| F[Select land parcel for investigation]
    
    %% Google Earth check
    F --> G[Get coordinates/location of land parcel]
    G --> H[Access Google Earth satellite view]
    H --> I[Analyze aerial imagery of property]
    I --> J{Any structures visible from satellite?}
    J -->|Yes| K[Mark property as unsuitable]
    K --> F
    
    %% Google Maps street view check
    J -->|No| L[Access Google Maps street view]
    L --> M{Street view available?}
    M -->|No| O[Note: Cannot confirm via street view]
    M -->|Yes| N[Analyze street view of property]
    N --> O
    O --> P{Any structures visible from street view?}
    P -->|Yes| K
    
    %% Property listing search
    P -->|No| Q[Extract property address]
    Q --> R[Search property on Zillow]
    R --> S[Search property on Redfin]
    S --> T[Search property on Realtor.com]
    T --> U[Search other USA marketing sites]
    
    %% Check if property is "off market"
    U --> V{Property listed as OFF MARKET?}
    V -->|No| W[Mark as potentially active listing]
    W --> K
    
    %% Truthfinder verification
    V -->|Yes| X[Access Truthfinder API]
    X --> Y[Search for property owner]
    Y --> Z{Owner information found?}
    Z -->|No| AA[Note: Cannot verify owner]
    AA --> K
    
    %% Owner age verification
    Z -->|Yes| AB[Retrieve owner's age]
    AB --> AC{Owner's age obtained?}
    AC -->|No| AD[Note: Age verification failed]
    AD --> K
    
    %% County records verification
    AC -->|Yes| AE[Access county property records]
    AE --> AF[Compare owner name from Truthfinder with county records]
    AF --> AG{Names match?}
    AG -->|No| AH[Note: Owner name mismatch]
    AH --> K
    
    %% Address verification
    AG -->|Yes| AI[Compare address information]
    AI --> AJ{Addresses match?}
    AJ -->|No| AK[Note: Address mismatch]
    AK --> K
    
    %% Property details verification
    AJ -->|Yes| AL[Compare property details]
    AL --> AM{Property details match?}
    AM -->|No| AN[Note: Property details mismatch]
    AN --> K
    
    %% Data collection
    AM -->|Yes| AO[Create comprehensive property profile]
    AO --> AP[Collect owner's full name]
    AP --> AQ[Collect owner's age]
    AQ --> AR[Collect property address]
    AR --> AS[Collect property dimensions]
    AS --> AT[Collect property zoning information]
    AT --> AU[Collect tax information]
    AU --> AV[Collect property history]
    
    %% Completion
    AV --> AW[Compile all land information into package]
    AW --> AX[End: Complete land information ready for next stage]:::endpoint
    
    %% Apply styles
    class A,B,C,F,G,H,I,L,N,O,Q,R,S,T,U,X,Y,AB,AE,AF,AI,AL,AO,AP,AQ,AR,AS,AT,AU,AV,AW process
    class D,J,M,P,V,Z,AC,AG,AJ,AM decision
    class K,E,W,AA,AD,AH,AK,AN,AX endpoint