import psycopg2
# import sqlalchemy
import pandas as pd
import variables as config
import time
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning

# Time for watchdog how long time working program
start = time.time()


class WorkWithDatabase:
    def __int__(self):
        self.conn_string = "host=" + config.PGHOST + " port=" + config.GPPORT + " dbname=" + \
                           config.PGDATABASE + " user=" + config.PGUSER + " password=" + config.PGPASSWORD
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


class GUIForDatabase(tk.Tk):
    def __int__(self, title_gui: str = 'Tk', width: int = 400, height: int = 400,
                offsetx: int = 100, offsety: int = 100, png_ico_filepath: str = '',
                maxsizex: int = 500, maxsizey: int = 500, minsizex: int = 100, minsizey: int = 100,
                resizablexy: bool = True, bg_gui: str = 'gray'):
        """

        :param1 title_gui: name of application
        :param2 width: width of application
        :param3 height: height of application
        :param4 offsetx: to offset the left top application angle for 'x'
        :param5 offsety: to offset the left top application angle for 'y'
        :param6 png_ico_filepath: path to png file for make ico for application
        :param7 maxsizex: maximum size of application for 'x'
        :param8 maxsizey: maximum size of application for 'y'
        :param9 minsizex: minimum size of application for 'x'
        :param10 minsizey: minimum size of application for 'x'
        :param11 resizablexy: resizable for horizontal and vertical of application
        :param12 bg_gui: background of application
        """
        super()
        self.title(title_gui)
        self.width = width
        self.height = height
        self.offsetx = offsetx
        self.offsety = offsety
        self.ico_filepath = png_ico_filepath
        self.maxsizex = maxsizex
        self.maxsizey = maxsizey
        self.minsizex = minsizex
        self.minsizey = minsizey
        self.resizablex = resizablexy
        self.resizabley = resizablexy
        self.bg = bg_gui

    def config_gui(self):
        """

        Configurate your application:
            - size
            - maxsize
            - minsize
            - position on screen
            - resizable application
            - ico in title string
        """
        self.geometry(f"{self.width}x{self.height}+{self.offsetx}+{self.offsety}")
        self.maxsize(self.maxsizex, self.maxsizey)
        self.minsize(self.minsizex, self.minsizey)
        self.resizable(self.resizablex, self.resizabley)
        if self.ico_filepath:
            self.iconphoto(False, tk.PhotoImage(file=self.ico_filepath))
        self.config(bg=self.bg)

    def create_menu(self):
        """

        """
        pass

    def app_create_widgets(self):
        """

        Create a widgets on application
        """
        pass

    def start_app(self):
        """

        This function for start application:
            - init
            - configure
            - create widgets
        """
        self.__int__()
        self.config_gui()
        self.app_create_widgets()

        self.mainloop()


if __name__ == '__main__':
    # table = 'items'
    # name = '6ES'
    # ozm = 707801
    # new_val = []

    # data = WorkWithDatabase()
    # data.update_data_in_db(table, new_value=new_val, field='')

    app = GUIForDatabase()
    app.start_app()

    # print(load_one_item_by_name_from_db(table, name))

# Time of watchdog resolve work time
    work_time = time.time() - start
    print(f'Work time of program = {work_time}')
