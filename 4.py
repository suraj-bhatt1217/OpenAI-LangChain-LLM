"""Create a vector store and perform similarity search"""

from dotenv import load_dotenv
from colorama import Fore
import os

from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS


load_dotenv()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}?Only give joke.")

llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
output_parser = StrOutputParser()

# create a vector store and embeddings
vectorstore = FAISS.from_texts(["harrison worked on kensho"], embedding=OpenAIEmbeddings())

# querying the vector store
query = "Where did Harrison work?"
docs = vectorstore.similarity_search(query, top_k=1)
print(docs[0].page_content)