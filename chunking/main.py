# from dotenv import load_dotenv
# load_dotenv()


# from langchain_community.document_loaders import UnstructuredMarkdownLoader

# loader = UnstructuredMarkdownLoader("chunking/data/company_info.md")

# docs = loader.load()

# print(docs[0].page_content)
# print(docs[0].metadata)


############################################################################
# Chunking
############################################################################

# from dotenv import load_dotenv
# load_dotenv()

# from langchain_community.document_loaders import UnstructuredMarkdownLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = UnstructuredMarkdownLoader("chunking/data/company_info.md")

# docs = loader.load()

# spliter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=40)

# chunks = spliter.split_documents(docs)
# print(len(chunks))

# for i in range(len(chunks)):
#     print(f"\n chunk {i + 1} \n")
#     print(chunks[i].page_content)


############################################################################
# Embedding
############################################################################
# from dotenv import load_dotenv
# load_dotenv()

# from google import genai
# EMBEDDING_MODEL = "gemini-embedding-001"

# client = genai.Client()

# text = "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints."

# result = client.models.embed_content(
#     model=EMBEDDING_MODEL,
#     contents=text
# )

# # print(result.embeddings[0].values)

# embeding = result.embeddings[0].values

# print(embeding)

############################################################################
############################################################################

# from dotenv import load_dotenv
# load_dotenv()

# from google import genai
# from langchain_community.document_loaders import UnstructuredMarkdownLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# EMBEDDING_MODEL = "gemini-embedding-001"

# client = genai.Client()

# loader = UnstructuredMarkdownLoader("chunking/data/company_info.md")

# docs = loader.load()

# spliter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=40)

# chunks = spliter.split_documents(docs)

# texts = [chunk.page_content for chunk in chunks]


# result = client.models.embed_content(
#     model=EMBEDDING_MODEL,
#     contents=texts
# )


# embeddings = [item.values for item in result.embeddings]

# print(len(embeddings))

############################################################################
# Semantic Search
############################################################################

from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

EMBEDDING_MODEL = "gemini-embedding-001"

loader = UnstructuredMarkdownLoader("chunking/data/company_info.md")

docs = loader.load()

spliter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=40)

chunks = spliter.split_documents(docs)

texts = [chunk.page_content for chunk in chunks]

result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=texts
)

# print(result.embeddings[0].values)

embedding = [item.values for item in result.embeddings]

# print(embedding)
# print(len(embedding))

question = "რა არის კომპანიის მისია?"

query_result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=question
)

embedding_query = query_result.embeddings[0].values

similarity_score = cosine_similarity([embedding_query], embedding)[0]

# print(similarity_score)

results = sorted(zip(chunks, similarity_score), key= lambda x: x[1], reverse=True)

# print(results)

for chunk, score in results:
    print(chunk.page_content)
    print(score)
    print("=" * 100)


