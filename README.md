# Land System Workflow

The following diagram illustrates the automated land search and inquiry system workflow:

```mermaid
flowchart TD
    %% Main styles
    classDef process fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef decision fill:#e1f5fe,stroke:#333,stroke-width:1px,color:#000
    classDef endpoint fill:#e8f5e9,stroke:#333,stroke-width:1px,color:#000
    classDef data fill:#e8f4f8,stroke:#333,stroke-width:1px
    classDef subproc fill:#fff8e1,stroke:#333,stroke-width:1px

    %% Initialization process
    A[Start: Land_searcher] --> B[Access Wikipedia]
    B --> C[Extract list of all US states]
    C --> D[For each state, extract all counties]
    D --> E[Create state-county database]
    E --> F[Initialize search criteria/preferences]
    
    %% County selection process
    F --> G[Select state from database]
    G --> H[Select county from state]
    H --> I[Check if county has been searched before]
    I --> J{County already processed?}
    J -->|Yes| K[Select next county]
    K --> I
    
    %% Propstream search
    J -->|No| L[Access Propstream]
    L --> M[Input county into Propstream]
    M --> N[Search for vacant/undeveloped land]
    N --> O{Land parcels found?}
    O -->|No| P[Mark county as processed]
    P --> K
    
    %% Land parcel selection & filtering
    O -->|Yes| Q[Filter parcels by criteria in Propstream]
    Q --> R[Select land parcel for investigation]
    R --> S[Mark parcel as under investigation]
    
    %% Google Earth check
    S --> T[Get coordinates/location of land parcel]
    T --> U[Access Google Earth satellite view]
    U --> V[Analyze aerial imagery of property]
    V --> W{Any structures visible from satellite?}
    W -->|Yes| X[Mark property as unsuitable]
    X --> Y[Update database with reason]
    Y --> R
    
    %% Google Maps street view check
    W -->|No| Z[Access Google Maps street view]
    Z --> AA{Street view available?}
    AA -->|No| AB[Note: Cannot confirm via street view]
    AA -->|Yes| AC[Analyze street view of property]
    AC --> AB
    AB --> AD{Any structures visible from street view?}
    AD -->|Yes| X
    
    %% Property listing search
    AD -->|No| AE[Extract property address]
    AE --> AF[Search property on Zillow]
    AF --> AG[Search property on Redfin]
    AG --> AH[Search property on Realtor.com]
    AH --> AI[Search property on Trulia]
    AI --> AJ[Search property on LoopNet]
    AJ --> AK[Search property on LandWatch]
    
    %% Check if property is off-market
    AK --> AL{Property listed as off-market?}
    AL -->|No| AM[Mark as potentially active listing]
    AM --> Y
    
    %% Truthfinder verification - Enhanced
    AL -->|Yes| AN[Access Truthfinder API]
    AN --> AO[Search for property owner]
    AO --> AP{Owner information found?}
    AP -->|No| AQ[Try alternative people search APIs]
    AQ --> AR{Owner found through alternatives?}
    AR -->|No| AS[Note: Cannot verify owner]
    AS --> Y
    
    %% Owner detailed verification
    AR -->|Yes| AT[Retrieve owner's information]
    AP -->|Yes| AT
    AT --> AU[Extract owner's age]
    AU --> AV{Owner's age obtained?}
    AV -->|No| AW[Note: Age verification failed]
    AW --> Y
    
    %% Owner assets verification - CORRECTED
    AV -->|Yes| AX[Check owner's currently & previously owned properties]
    AX --> BD[Deduplicate: If property in both lists, count as currently owned only]
    BD --> BE[Count unique currently owned properties]
    BE --> BF{Unique currently owned properties ≤ 2?}
    BF -->|No| BG[Note: Owner has too many properties]
    BG --> Y
    
    BF -->|Yes| BH[Count unique previously owned properties]
    BH --> BI{Unique previously owned properties ≤ 2?}
    BI -->|No| BJ[Note: Owner has too many past properties]
    BJ --> Y
    
    %% County records verification
    BI -->|Yes| BK[Access county property records]
    BK --> BL[Compare owner name with county records]
    BL --> BM{Names match?}
    BM -->|No| BN[Note: Owner name mismatch]
    BN --> Y
    
    %% Address verification
    BM -->|Yes| BO[Compare address information]
    BO --> BP{Addresses match?}
    BP -->|No| BQ[Note: Address mismatch]
    BQ --> Y
    
    %% Property details verification
    BP -->|Yes| BR[Compare property details]
    BR --> BS{Property details match?}
    BS -->|No| BT[Note: Property details mismatch]
    BT --> Y
    
    %% Tax status verification
    BS -->|Yes| BU[Check tax payment status]
    BU --> BV{Taxes current?}
    BV -->|No| BW[Note: Tax issues]
    BW --> Y
    
    %% Lien verification
    BV -->|Yes| BX[Check for liens against property]
    BX --> BY{Any liens found?}
    BY -->|Yes| BZ[Note: Liens present]
    BZ --> Y
    
    %% Data collection
    BY -->|No| CA[Create comprehensive property profile]
    CA --> CB[Collect owner's full name]
    CB --> CC[Collect owner's age]
    CC --> CD[Collect owner's contact information if available]
    CD --> CE[Collect property address]
    CE --> CF[Collect property dimensions]
    CF --> CG[Collect property zoning information]
    CG --> CH[Collect tax information]
    CH --> CI[Collect property history]
    CI --> CJ[Collect nearby property values]
    CJ --> CK[Research potential uses for land]
    
    %% Completion
    CK --> CL[Compile all land information into package]
    CL --> CM[Mark property as verified in database]
    CM --> CN[End: Complete land information]:::endpoint
    
    %% Apply styles
    class A,B,C,D,E,F,G,H,I,L,M,N,Q,R,S,T,U,V,Z,AC,AB,AE,AF,AG,AH,AI,AJ,AK,AN,AO,AQ,AT,AU,AX,BD,BE,BH,BK,BL,BO,BR,BU,BX,CA,CB,CC,CD,CE,CF,CG,CH,CI,CJ,CK,CL,CM process
    class J,O,W,AA,AD,AL,AP,AR,AV,BF,BI,BM,BP,BS,BV,BY decision
    class K,P,X,Y,AM,AS,AW,BG,BJ,BN,BQ,BT,BW,BZ,CN endpoint
    class E data
