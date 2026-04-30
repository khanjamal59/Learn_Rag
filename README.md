        ┌──────────────┐
        │   User Query │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │  Retriever   │  ← Finds relevant data
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │  Documents   │  (PDF, DB, text)
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │     LLM      │  ← Generates answer
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   Response   │
        └──────────────┘
