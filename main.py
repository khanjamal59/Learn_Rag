from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
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
query=" what does Puskar Shumsher Rana challenged ?"
docs=retriever.invoke(query)
for doc in docs:
    print(doc.page_content)
    print("-"*50)
