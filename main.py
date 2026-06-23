from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
loader = PyPDFLoader("laxmiprasad.pdf")
documents = loader.load()

print(len(documents))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(len(chunks))
# creating the embeddings 
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
#vectordb
vectorstore=FAISS.from_documents(chunks,embeddings)

vectorstore.save_local("faiss_index")
print("emdeding successfully done")
#creating the retriver 
retriever=vectorstore.as_retriever(search_kwargs={"k":3})
#testing the retrival
query=" when was devkota born ?"
docs=retriever.invoke(query)
context="\n\n".join([doc.page_content for doc in docs])
prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{query}

Answer:
"""
#adding the llm 

llm=ChatGroq(
    api_key="your_api_key",
    model="llama-3.3-70b-versatile"
)
response=llm.invoke(prompt)
print(response.content)
