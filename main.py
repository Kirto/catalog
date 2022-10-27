import psycopg2
# import sqlalchemy
import pandas as pd
import variables as creds
import time
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning

# Time for watchdog how long time working program
start = time.time()


class WorkWithDatabase:
    def __int__(self):
        self.conn_string = "host=" + creds.PGHOST + " port=" + creds.GPPORT + " dbname=" + \
                           creds.PGDATABASE + " user=" + creds.PGUSER + " password=" + creds.PGPASSWORD
        self.conn = psycopg2.connect(self.conn_string)
        self.cursor = self.conn.cursor()

    def load_all_data(self, table_name: str) -> ():
        """

        :param1 table_name: name of table in your database
        :return: SELECT * FROM table;
        """
        sql_command = f"SELECT * FROM {table_name};"
        data = pd.read_sql(sql=sql_command, con=self.conn)
        return data

    def update_data_in_db(self, table_name: str, new_value: list, field: str) -> ():
        """

        :param1 table_name: name table in database
        :param2 new_value: new values which need insert into table
        :param3 field: old values
        :return: None
        """
        pass

    def load_one_item_by_name_from_db(self, table_name: str, selected_name: str) -> ():
        """

        :param1 table_name:  name table of database
        :param2 selected_name: piece of name in database
        :return: table of select with piece search phrase by name device
        """

        sql_command = f"SELECT name FROM {table_name};"
        colum_name = pd.read_sql(sql_command, self.conn)
        ar = []
        for _ in colum_name.values:
            if f'{selected_name}' in _[0]:
                ar.append([_[0]])
        data = pd.DataFrame(ar, columns=['name'])

        sql_command = f"SELECT * FROM {table_name} WHERE "
        for _ in range(len(data['name']) - 1):
            sql_command += f"(name = '{data['name'][_]}') OR "
        sql_command += f"(name = '{data['name'][len(data['name']) - 1]}');"
        data = pd.read_sql(sql_command, self.conn)
        return data

    def load_one_item_by_ozm_from_db(self, table_name: str, ozm_number: int) -> ():
        """

        :param1 table_name:  name table of database
        :param2 ozm_number:  search by ozm
        :return:  table of search by ozm device
        """

        sql_command = f"SELECT * FROM {table_name} WHERE ozm = {ozm_number}"
        data = pd.read_sql(sql_command, self.conn)
        return data


class GUIForDatabase:
    def __int__(self):
        self.gui = tk.Tk()

    def open_gui(self):
        pass

    def gui_mainloop(self):
        self.gui.mainloop()


if __name__ == '__main__':
    table = 'items'
    name = '6ES'
    ozm = 707801
    new_val = []

    data = WorkWithDatabase()
    data.update_data_in_db(table, new_value=new_val, field='')

    app = GUIForDatabase()
    app.open_gui()

    # print(load_one_item_by_name_from_db(table, name))

# Time of watchdog resolve work time
    work_time = time.time() - start
    print(f'Work time of program = {work_time}')
