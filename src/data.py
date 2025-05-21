from typing import Dict, List
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import chromadb
chromadb_client = chromadb.PersistentClient(settings=Settings(
    anonymized_telemetry=False,
))
# chromadb_client = chromadb.Client()
default_ef = embedding_functions.DefaultEmbeddingFunction()
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="intfloat/multilingual-e5-large"
)


def get_collection():
  collection = chromadb_client.get_or_create_collection(
    name="pdfq",
    embedding_function=sentence_transformer_ef
  )
  return collection


collection = get_collection()

# print(collection.peek())


def query(query: str, filename: str, n: int = 3) -> Dict:
  results = collection.query(
    query_texts=[query],
    n_results=n,
    where={"filename": filename}
  )
  return results


def add_subjects(subjects: List[str], filename: str):
  collection.add(
    documents=subjects,
    metadatas=[{"title": i.split("\n")[0], "filename": filename}
               for i in subjects],
    ids=[str(i) for i in range(len(subjects))],
  )
  return True
