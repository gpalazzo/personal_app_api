from typing import Dict, List, Any
import psycopg2
from pathlib import Path
from env_var_handler.env_var_loader import load_credentials, load_config
import os
import pandas as pd


queries_dir = Path(__file__).resolve().parents[1]

# load credentials and configs as env variables
load_credentials(), load_config()


class DBClient:
    """Class to connect to the database and define db methods'.
    """

    def __init__(self, db_name: str):
        """Creates connection and cursor to the database.
        Args:
            db_name: database name
        """
        self.cnn = psycopg2.connect(
                                    user=os.getenv("db_username"),
                                    password=os.getenv("db_password"),
                                    database=db_name,
                                    host=os.getenv("db_host")
                                   )
        self.cursor = self.cnn.cursor()

    def execute_sql_statement(self, 
                              sql_file_name: str,
                              api_post_json: Dict[str, str]):
        """Execute and commit statements to the database. Statement is usually represented by a SQL query as string.
        Args:
            str_query: SQL query as string to be executed
        """
        sql_query = self._read_sql_file_text(sql_file_name=sql_file_name,
                                            query_params=api_post_json)

        if sql_query is None:
            assert False, f"""sql query is empty when parsing `{sql_file_name}.sql`, 
            provide a valid query to be executed and/or check the dictionary
            unpacking in `self._read_sql_file_text` method"""
       
        df = pd.read_sql(sql=sql_query, con=self.cnn)
        return df

    @staticmethod
    def _read_sql_file_text(sql_file_name: str,
                            query_params: Dict[str, str]):
        
        try:
            sql_file_content = Path(f"{queries_dir}/queries/{sql_file_name}.sql").read_text()
            sql_file_content_unpacked = sql_file_content.format(**query_params)
            return sql_file_content_unpacked
        
        except KeyError:
            pass

        except IOError:
            assert False, f"file with name {sql_file_name} does not exist at directory: {local_project_root_dir}/queries"

        except Exception as e:
            assert False, f"the following error occured with args: {e.args}"

