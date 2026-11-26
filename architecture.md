# Architecture

```mermaid
flowchart TD
    A[Public appointment dataset] --> B[Clean and EDA]
    B --> C[Patient-grouped split and baseline]
    C --> D[MLP train and tune]
    D --> E[Verified MLflow model and inference]
    E --> F[Synthetic booking scores and fixtures]
    G[Approved non-PHI corpus] --> H[Chunking, dense retrieval and grounding]
    F --> I[Role-scoped read-only agents and gateway]
    E --> I
    H --> I
    I --> J[Dashboard and website interfaces]
    J --> K[Internal deployment tests]
```

The original gateway performs authorization and read-only tool checks; it uses a privately supplied API contract in demo mode. The website interface trusts server-supplied roles; actual Firebase verification must be implemented at the external boundary. Do not deploy notebook functions as an unauthenticated service. The no-show score is not calibrated and is intended only for human-reviewed follow-up.
