"""Create a vector store and perform similarity search"""

from dotenv import load_dotenv
from colorama import Fore
import os

from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough


load_dotenv()

model = OpenAI()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
output_parser = StrOutputParser()

# create a vector store and embeddings
vectorstore = FAISS.from_texts(["harrison worked on kensho"], embedding=OpenAIEmbeddings())

# querying the vector store
query = "Where did Harrison work?"
# docs = vectorstore.similarity_search(query, top_k=1)
# print(docs[0].page_content)

# querying as retriever
retriever = vectorstore.as_retriever()
# docs = retriever.invoke(query, top_k=1)
# print(docs[0].page_content)

retriever_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)

response = retriever_chain.invoke(query)
print(response)