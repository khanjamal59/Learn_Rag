<h2>Rag Architecture</h2>
<hr>

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
<h2>Full pipeline</h2>

                OFFLINE STAGE
        ┌─────────────────────────┐
        │ Load Documents          │
        │ Chunk Text              │
        │ Create Embeddings       │
        │ Store in Vector DB      │
        └────────────┬────────────┘
                     ↓
                ONLINE STAGE
        ┌─────────────────────────┐
        │ User Query              │
        │ Embed Query             │
        │ Retrieve Top Chunks     │
        │ Send to LLM             │
        │ Generate Answer         │
        └─────────────────────────┘
