# RAG 0.1

## Getting started

Firstly, it is necessary to download Python 3.10.0. Subsequently when the installation of python is complete, clonee the project into the desired directory.

```
git clone https://github.com/petriknovis/rag_0.1.git
cd .\rag_0.1\
```

Upon entering the folder, the primary task entails the installation of the necessary requirements to ensure the proper functioning of this project.

```
pip install -r requirements.txt
```

Upon the completion of downloading and installing the packages listed in the requirements, you may proceed to the subsequent step. Access the helper.py file and assign your Open API key to the designated variable.
You can create an api key [Here](https://platform.openai.com/api-keys). Save the file.

## Creating VectorDB

Upon completion of the preceding steps, proceed to open the db.py file. Within this file, you have the option to modify parameters such as the chunk size, chunk overlap, or the persistence directory where the vector database will be stored. Should you opt not to make any changes, you may proceed with running the program as is.

```
python db.py
```

Upon completion of the program, you will observe the creation of a new folder in the root directory. This indicates successful creation of the database, obviating the need to rerun the program unless the folder is deleted and database recreation is required. Additionally, you have the option to create another folder, designated for a different language, and generate a database specific to that language.

## RAG

Upon completion of the preceding steps, we can now proceed to the main application. Here, you have the flexibility to adjust parameters such as temperature, search keywords arguments, and the prompt name according to your preferences. Once you have set the desired parameters, you may execute the program.

```
streamlit run .\app.py
```

Upon initiation, a new browser tab will be opened, facilitating the testing of your application. Following the closure of the application, it will be necessary to rerun the code in order to access the testing environment once more.
You can also monitor the progress in Langchain Smith. [Smith](https://platform.openai.com/api-keys).

Good luck!
