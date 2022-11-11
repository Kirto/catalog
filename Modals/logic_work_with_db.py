"""

This block for working with postgres database.

Author: Kirto
version: zero
"""

import variables as config
import pandas as pd
# import sqlalchemy
import psycopg2


conn_string = "host=" + config.PGHOST + " port=" + config.GPPORT + " dbname=" + \
                   config.PGDATABASE + " user=" + config.PGUSER + " password=" + config.PGPASSWORD
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


def load_limit_data(table_name: str, lim: int = 10) -> ():
    """

    :param1 table_name: name of table in your database
    :param2 lim: limit row in query selection from database
    :return: SELECT * FROM table;
    """
    sql_command = f"SELECT name, ozm, description, quantity FROM {table_name} " \
                  f"ORDER BY quantity ASC LIMIT {lim};"
    data = pd.read_sql(sql=sql_command, con=conn)
    return data


def update_data_in_db(table_name: str, new_value: list, field: str) -> ():
    """

    :param1 table_name: name table in database
    :param2 new_value: new values which need insert into table
    :param3 field: old values
    :return: None
    """
    pass


def load_one_item_by_name_from_db(table_name: str, selected_name: str) -> ():
    """

    :param1 table_name:  name table of database
    :param2 selected_name: piece of name in database
    :return: table of select with piece search phrase by name device
    """

    sql_command = f"SELECT name FROM {table_name};"
    colum_name = pd.read_sql(sql_command, conn)
    ar = []
    for _ in colum_name.values:
        if f'{selected_name}'.lower() in _[0].lower():
            ar.append([_[0]])
    data = pd.DataFrame(ar, columns=['name'])

    sql_command = f"SELECT name, ozm, description, quantity FROM {table_name} WHERE "
    for _ in range(len(data['name']) - 1):
        sql_command += f"(name = '{data['name'][_]}') OR "
    sql_command += f"(name = '{data['name'][len(data['name']) - 1]}');"
    data = pd.read_sql_query(sql_command, conn)
    return data


def load_one_item_by_ozm_from_db(table_name: str, ozm_number: int) -> ():
    """

    :param1 table_name:  name table of database
    :param2 ozm_number:  search by ozm
    :return:  table of search by ozm device
    """

    sql_command = f"SELECT name, ozm, description, quantity FROM {table_name} WHERE ozm = {ozm_number}"
    data = pd.read_sql(sql_command, conn)
    return data


if __name__ == "__main__":
    print(load_one_item_by_ozm_from_db('Items', 707801))    # ozm = 707801  for tests
