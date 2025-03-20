# Land System Workflow

The following diagram illustrates the automated land search and inquiry system workflow:

```mermaid
flowchart TD
    %% Main node style
    classDef process fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef decision fill:#e1f5fe,stroke:#333,stroke-width:1px,color:#000
    classDef endpoint fill:#e8f5e9,stroke:#333,stroke-width:1px
    
    %% Land_searcher agent
    A[Land_searcher Start] --> B[Get land info]
    B --> C{Info available?}
    C -->|Yes| D[Check realtor]
    C -->|No| Z[Cannot proceed]:::endpoint
    
    D --> E{Available?}
    E -->|No| Z
    E -->|Yes| F[Check maps for structures]
    
    F --> G{No structures?}
    G -->|No| Z
    G -->|Yes| H[Get owner info]
    
    H --> J[Get land documents]
    J --> N[Land package complete]
    
    %% Email_creator agent
    N --> O[Email_creator Start]
    O --> Q[Create Outlook email]
    Q --> S[Email credentials ready]
    
    %% Email_sender agent
    S --> V[Email_sender Start]
    V --> Y[Compose & send inquiry]
    Y --> AC[Record communication]
    AC --> AE[Inquiry sent]
    
    %% Apply styles
    class A,B,D,F,H,J,N,O,Q,S,V,Y,AC,AE process
    class C,E,G decision
    class Z,AE endpoint