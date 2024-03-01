from db import handle_query
import os
import warnings

import streamlit as st

from langchain import hub
from langchain.chains import RetrievalQA 
from langchain_openai import OpenAI
from langchain_core._api.deprecation import LangChainDeprecationWarning

from langchain_community.vectorstores import Chroma

from helper import openai_embedding, persist_dir, open_api_key

#remove warnings
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

#connect smith langchain
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
os.environ['LANGCHAIN_API_KEY'] = "ls__13dffee5efc3450c9a11e6dcd52a1796"


#connect to db (in this case its on disk)
db = Chroma(
    persist_directory = persist_dir, 
    embedding_function = openai_embedding
)


#llm, retriever, prompt
llm = OpenAI(
    openai_api_key = open_api_key,
    # temperature=1,
)

retriever = db.as_retriever(
    search_kwargs={'k':2} 
)

prompt = hub.pull(
    "rag-0-1/skuska_01_en", #the prompt name here
    api_url="https://api.hub.langchain.com"
)

#chain for question-answer with index
pdf_qa = RetrievalQA.from_chain_type(
    llm = llm, 
    retriever = retriever,
    chain_type_kwargs = {
        "prompt": prompt
    },
)

def get_session():
    if "my_session_state" not in st.session_state:
        st.session_state.my_session_state = {"chat_history": []}
    return st.session_state.my_session_state

def main():
    session_state = get_session()

    st.title("RAG")
    
    query = st.text_input("Question:")
    
    if st.button("Submit"):
        if query:
            result = handle_query(query, pdf_qa)

            session_state["chat_history"].append({"question": query, "answer": result})

            st.write("-------")
            for msg in enumerate(session_state["chat_history"]):
                st.write(f"Questions: {msg[1].get('question')}") 
                st.write("Answer:", msg[1].get('answer'))
                st.write("-------")
                

if __name__ == "__main__":
    main()
