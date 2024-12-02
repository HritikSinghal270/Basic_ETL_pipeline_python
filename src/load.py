from sqlalchemy import create_engine
import logging
from config import DB_CONNECTION_STRING
import psycopg2
from dotenv import load_dotenv
from psycopg2 import extras
import os
load_dotenv()

def load_to_db(dataframe, table_name="Alpha_vantage_ETL_pipeline"):
    """
    Load the transformed DataFrame into the database.
    """
    
    try:
        engine = create_engine(DB_CONNECTION_STRING)
        dataframe.to_sql(table_name, engine, if_exists="replace", index=False)
        logging.info(f"Data successfully loaded into table '{table_name}'.")
    except Exception as e:
        logging.error(f"Error during data loading: {e}")
        raise
    # try:
    #     connection = psycopg2.connect(
    #         dbname=os.getenv('DATABASE_NAME'),
    #         user=os.getenv('DATABASE_USER'),
    #         password=os.getenv('DATABASE_PASSWORD'),
    #         host=os.getenv('DATABASE_HOST'),
    #         port=os.getenv('DATABASE_PORT')
    #     )
    #     query = """
    #         INSERT INTO Alpha_vintage_ETL_pipleine (userid, groupid, filename, type) 
    #         VALUES %s
    #     """
   
