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


# def connect_to_db():
conn_string = "host=" + config.PGHOST + " port=" + config.GPPORT + " dbname=" + \
                   config.PGDATABASE + " user=" + config.PGUSER + " password=" + config.PGPASSWORD
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


def load_all_data(table_name: str) -> ():
    """

    :param1 table_name: name of table in your database
    :return: SELECT * FROM table;
    """
    sql_command = f"SELECT * FROM {table_name} ORDER BY quantity ASC LIMIT 10;"
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

    sql_command = f"SELECT * FROM {table_name} WHERE "
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

    sql_command = f"SELECT * FROM {table_name} WHERE ozm = {ozm_number}"
    data = pd.read_sql(sql_command, conn)
    return data


class GUIForDatabase(tk.Tk):
    def __int__(self, title_gui: str = config.NAME_GUI, width: int = config.WIDTH,
                height: int = config.HEIGHT,
                offsetx: int = config.OFFSETX, offsety: int = config.OFFSETY,
                png_ico_filepath: str = config.PNG_ICO_PATH, maxsizex: int = config.MAXSIZEX,
                maxsizey: int = config.MAXSIZEY, minsizex: int = config.MINSIZEX,
                minsizey: int = config.MINSIZEY,
                resizablexy: bool = config.RESIZE, bg_gui: str = config.BGCOLOR):
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

    def search(self):
        if self.search_entry.get() == '':
            text = 'Вы не ввели данные! Попробуйте снова :)'
            self.label1.config(text=text)
            return
        if self.ozm_search.get() and self.search_entry.get() != '':
            text = str(load_one_item_by_ozm_from_db(table_name=config.PGTABLE,
                                                    ozm_number=int(self.search_entry.get())))
            self.label1.config(text=text)
            print(text)
        elif not self.ozm_search.get() and self.search_entry.get() != '':
            text = str(load_one_item_by_name_from_db(table_name=config.PGTABLE,
                                                     selected_name=self.search_entry.get()))
            self.label1.config(text=text)
            print(text)

    def package_widgets_on_screen_application(self):
        self.wrapper.grid(row=0, column=0)
        self.search_entry.grid(row=0, column=0, columnspan=2)
        self.search_ozm.grid(row=1, column=0)
        self.search_name.grid(row=1, column=1)
        self.search_button.grid(row=0, column=1)
        self.label1.grid(row=1, column=0)

    def enter_parametrs(self):
        self.ozm_search = tk.BooleanVar()

    def app_create_widgets(self):
        """

        Create a widgets on application
        """
        self.wrapper = ttk.Frame(self, borderwidth=2, width=100, height=100)
        self.search_entry = tk.Entry(self.wrapper, takefocus=True)
        self.search_ozm = tk.Radiobutton(self.wrapper, value=True, variable=self.ozm_search, text='Поиск по ОЗМ')
        self.search_name = tk.Radiobutton(self.wrapper, value=False, variable=self.ozm_search, text='Поиск по имени')
        self.search_button = tk.Button(self.wrapper, text='Поиск', background='blue', foreground='white',
                                       command=self.search)
        self.label1 = tk.Label(self, width=50, height=10)

        self.package_widgets_on_screen_application()

    def start_app(self):
        """

        This function for start application:
            - init
            - configure
            - create widgets
        """
        self.__int__()
        self.config_gui()
        self.enter_parametrs()
        self.app_create_widgets()

        self.mainloop()


if __name__ == '__main__':
    # table = 'items'
    # name = '6ES'
    # ozm = 707801
    # new_val = []

    # data = WorkWithDatabase()
    # data.update_data_in_db(table, new_value=new_val, field='')

    print(load_all_data('Items'))
    app = GUIForDatabase()
    app.start_app()

    # print(load_one_item_by_name_from_db(table, name))

# Time of watchdog resolve work time
    work_time = time.time() - start
    print(f'Work time of program = {work_time}')
