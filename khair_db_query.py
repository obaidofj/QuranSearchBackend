from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import create_sql_query_chain
import psycopg2


#
# Documentation of LangChain
# https://python.langchain.com/docs/get_started/introduction.html

load_dotenv()

# dburi = os.getenv("DATABASE_URL")
# dburi = "sqlite:///academy/academy.db"
# db = SQLDatabase.from_uri(dburi)

# dburi = "sqlite:///c:/AlRaqeem/Database/Quran_MetaData_Khair_v7_77407.sqlite.db"
# dburi = "sqlite:///c:/AlRaqeem/Database/Quran_MetaData_Khair_v7_77444.sqlite.db"

# dburi = "sqlite:///c:/AlRaqeem/Database/Quran_MetaData_Khair_v7_77407_tashkeel.sqlite.db"
# dburi = "sqlite:///c:/AlRaqeem/Database/Quran_MetaData_Khair_v7_77444_tashkeel.sqlite.db"

# dburi = "postgresql://postgres:Quran@localhost:5432/Quran_MetaData_Khair_v7_77407.postgres"

# dburi = "postgresql://postgres:Quran@localhost:5432/Quran_MetaData_Khair_Arabic_v7_77407.postgres"

dburi = "postgresql://postgres:Quran@68.123.129.210:5432/quran_database_v7_77444_structured"

# dburi = "postgresql://postgres:Quran@localhost:5432/Quran_MetaData_Khair_v7_77444.postgres"
# dburi = "postgresql://postgres:Quran@localhost:5432/AlShamela_1"

# dburi = "postgresql://postgres:Quran@localhost:5432/Quran_MetaData_Khair_v7_77407_tashkeel.postgres"


db = SQLDatabase.from_uri(dburi)


### OpenAI models
# gpt-3.5-turbo-16k    16,384 tokens
# gpt-4                8,192 tokens
# gpt-4-0613           8,192 tokens
# gpt-4-32k            32,768 tokens
# gpt-4-32k-0613       32,768 tokens

llm = OpenAI(model_name = 'gpt-4-1106-preview', temperature=0) # switch to 'gpt-4' or 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4-0614', 'gpt-4-1106-preview'

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

# db_chain.run("How many rows is in the Words_Ayas table of this db?")
# db_chain.run("What is the most recurring aya in the Quran and how many times it repeated uniquely")
# db_chain.run("how many ayas have 114 letters in length in FirstScript, with unique ayas")
# db_chain.run("how many times the word محمد was mentioned ?")
# db_chain.run("how many letters are there in first script, between the start of aya number 19 of sura number 4 to the end of aya number 38 of sura number 4 ?")
# db_chain.run("how many times an aya containing treasure was mentioned in the Words_Ayas table , in unique aya's text")
# db_chain.run("how many times an aya containing treasure was mentioned in the Words_Ayas table the aya_text_modern field in unique instance of each aya, and list the ayas")
# db_chain.run("what is the aya text in sura 19 aya 19 ?")

# db_chain.run("how many times an aya containing مُحَمَّد was mentioned in unique aya word tashkeel text")

# db_chain.run("how many times an aya containing treasure was mentioned in unique aya word tashkeel text, LIMIT results to 100, and list the unique ayas")

# db_chain.run("كم قصة وردت في سورة الكهف")

# db_chain.run("كم مرّة ذكرت كلمة ءادم  بالقرآن، مع ذكر جميع مواقع الآيات الفريدة ورقم السورة والآية في كل القرآن")
# db_chain.run("كم مرّة ذكرت الآيات التي تحتوي جزئيا الكلمات مثل (بسم الله الرحمن الرحيم) كجزء من آيات القرآن بشكل فريد في النص، ما هي هذه الآيات وكم عدد الكلمات بين أول كلمة من أول آية إلى أول كلمة من آخر آية فيها بإستعمال (ترتيب الكلمة من بداية القرآن)، وكم حرف Baa_2 ذكرت بينهما")
# db_chain.run("كم مرّة ذكرت الآيات التي تحتوي جزئيا الكلمات مثل (بسم الله الرحمن الرحيم) كجزء من آيات القرآن بشكل فريد في النص، ما هي هذه الآيات وكم عدد الحروف بالرسم الأول بين أول مرّة وآخر مرّة ذكرت بإستعمال (ترتيب الحرف بالرسم الأول من بداية القرآن)")
# db_chain.run("""
# ما هو مجموع الجمّل الكبير للآية
# بالرسم الأول لهذه الأرقام للآيات الفريدة برقم الآية من بداية القرآن  بترتيب الآية من بداية القرءان
# 1111و 2121و3131و4141و5151و6161
# """)

# db_chain.run("""
# ما هو الفرق بالجمّل الكبير للآيتان بسورة الفاتحة وسورة النمل
# اللتان تحتويان بشكل جزئي (بسم الله الرحمن الرحيم)
# """)

# db_chain.run("""
# ما هي الأيات الفريدة التي تحتوي كلمات (من ما)
# """)

# db_chain.run("""
# ما هو مجموع عدد الكلمات بالآيات الفريدة التي ترتيب الآية من بداية السورة 20 وكم عددها ؟
# """)

# db_chain.run("what are the top 25 unique ayas in the Quran that are related to inheritance with word root ورث")
# db_chain.run("if a husband dies and leaves $1000000 how much does each of his two sons and daughter and wife inherit ?")


