import random

questions = {
    "What is RAG?": "retrieval augmented generation",
    "What is a transformer?": "transformer",
    "What is fine-tuning?": "fine tuning",
    "What is an embedding?": "embedding",
    "What is hallucination in LLMs?": "hallucination",
    "What is a token?": "token",
    "What is a vector database?": "vector database",
    "What is prompt engineering?": "prompt engineering",
    "What is self-attention?": "self attention",
    "What is the difference between RAG and fine-tuning?": "rag vs fine tuning",
}

explanations = {
    "retrieval augmented generation": "RAG: LLM retrieves relevant docs from a knowledge base before generating — improves accuracy, reduces hallucination.",
    "transformer": "Self-attention based architecture (2017) — foundation of GPT/LLaMA and modern LLMs.",
    "fine tuning": "Continued training of a pretrained model on smaller task-specific data — no retraining from scratch.",
    "embedding": "Dense numerical vector (768/1536 dims) representing semantic meaning — enables similarity search.",
    "hallucination": "Model generates plausible-sounding but false/fabricated content.",
    "token": "Basic text unit an LLM processes — word/subword; context windows measured in tokens.",
    "vector database": "DB (Pinecone/Weaviate/Milvus) optimized for fast similarity search over embeddings.",
    "prompt engineering": "Crafting instructions to get accurate, useful outputs from an LLM.",
    "self attention": "Each token attends to every other token with learned weights.",
    "rag vs fine tuning": "RAG = retrieval at inference time, weights unchanged. Fine-tuning = weights updated with task data.",
}

items = list(questions.items())
random.shuffle(items)
wrong = []
score = 0

print("=== AI INTERVIEW PREP QUIZ ===\n")

for q, a in items:
    try:
        user_answer = input(q + ":")
        if user_answer.strip() == "":
            print("(skipped)\n")
            wrong.append((q, a))
            continue
        if user_answer.strip().lower() == a.lower():
            score += 1
            print("✅ Correct!\n")
        else:
            print(f"❌ Wrong. Answer: {a}")
            print(f"   {explanations[a]}\n")
            wrong.append((q, a))
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        break

print(f"\n=== Final: {score}/{len(questions)} ===")
if wrong:
    print("Revise these:")
    for q, a in wrong:
        print(f"  - {q} → {a}")
