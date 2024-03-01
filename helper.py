from langchain_community.embeddings.openai import OpenAIEmbeddings


persist_dir = "./vector_on_disk"
docs_folder = "docs_en" #change to docs for slovak, but remove vector_on_disk file first
open_api_key = "" #open api key here

openai_embedding = OpenAIEmbeddings(openai_api_key=open_api_key)