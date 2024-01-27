import os
# from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
# from langchain_community.utilities import SQLDatabase
# from langchain.chains import LLMChain
from langchain_experimental.sql import SQLDatabaseChain
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain


# Make sure to set your OpenAI API key in your .env file
openai_api_key = os.getenv('OPENAI_API_KEY')

def process_natural_language_query(query):
    # llm = OpenAI(model_name = 'gpt-4-1106-preview', temperature=0)
    llm = OpenAI(model_name = 'gpt-3.5-turbo-16k', temperature=0)
    db_uri = os.getenv('DATABASE_URL')
    db = SQLDatabase.from_uri(db_uri)
    
    # llm_chain = LLMChain(llm=llm, llm_kwargs={"max_tokens": 4096}, database=db)  
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
    response = db_chain.run(query)
    return response


