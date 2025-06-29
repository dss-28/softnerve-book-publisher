import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromaDB client (new API)
client = chromadb.PersistentClient(path="chromadb_store")

# Set embedding function (default for demo purposes)
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

# Get or create collection
collection = client.get_or_create_collection(name="books", embedding_function=embedding_fn)

def store_final_text(filepath="output/final_draft.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    collection.add(documents=[text], ids=["chapter1"])
    print("\n✅ Final version saved in ChromaDB.")

def retrieve(query):
    results = collection.query(query_texts=[query], n_results=1)
    print("\n=== 🔍 Top Retrieved Chapter ===\n")
    print(results['documents'][0][0])

if __name__ == "__main__":
    store_final_text()
    retrieve("sunrise and ocean")
