"""

This block created GUI for view information from postgres database.

Author: Kirto
version: zero
"""

import tkinter as tk
import variables as config


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
        pass

    def package_widgets_on_screen_application(self):
        self.wrapper.grid(row=0, column=0)
        self.search_entry.grid(row=0, column=0, columnspan=2)
        self.search_ozm.grid(row=1, column=0)
        self.search_name.grid(row=1, column=1)
        self.search_button.grid(row=0, column=1)
        # self.label1.grid(row=1, column=0)
        self.list_of_items.grid(row=2, column=0, padx=2, pady=2)

    def enter_parametrs(self):
        self.ozm_search = tk.BooleanVar()

    def get_combobox_items(self):
        s = load_limit_data(config.PGTABLE, config.LIMIT_IN_LIST_HOME_PAGE)\
            .get(['name', 'ozm', 'quantity'])
        print(s)
        print(type(s))

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
        self.list_of_items = ttk.Combobox(self.wrapper, values=self.get_combobox_items(), height=20, width=50)

        tk.Listbox(self.wrapper, )
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


def configuration_gui(root):
    """
        
        This function configurate main window 
    """
    root.title(config.NAME_GUI)

    root.geometry(f"{config.WIDTH}x{config.HEIGHT}+"
                  f"{root.winfo_screenwidth() // 2 - config.WIDTH // 2}+"
                  f"{root.winfo_screenheight() // 2 - config.HEIGHT // 2}")
    root.maxsize(config.MAXSIZEX, config.MAXSIZEY)
    root.minsize(config.MINSIZEX, config.MINSIZEY)

    root.config(background=config.BGCOLOR, width=root.winfo_screenwidth() // 2 - config.WIDTH,
                height=root.winfo_screenheight() // 2 - config.HEIGHT)
    root.resizable(config.RESIZE, config.RESIZE)
    if config.PNG_ICO_PATH:
        root.iconphoto(False, tk.PhotoImage(file=config.PNG_ICO_PATH))


def create_widgets(root):
    def added_widgets_on_application():
        wrapper.grid(row=0, column=0)
        list_items.grid(row=1, column=0)
        arr = {
            'id': 'ID',
            'name': 'Name',
            'description': 'Description',
            'quantity': 'Quantity'
        }
        text = '|' + f"{arr['id']}".center(20) + '|' + f'{arr["name"]}'.center(30) + '|' + \
               f'{arr["description"]}'.center(30) + '|' + f'{arr["quantity"]}'.center(30) + '|'
        tk.Label(wrapper, text=text).grid(row=0, column=0)

    wrapper = tk.Frame(root, borderwidth=2, background='silver', relief='raised')
    list_items = tk.Listbox(wrapper, bg=config.BGCOLOR, selectforeground=config.LSTFGCOLOR,
                            selectbackground=config.LSTBGCOLOR, justify='center', width=50)

    # for testing list item
    a = []
    for i in range(50):
        a.append(i // 10)
        list_items.insert(0, i)
    list_items.insert(0, a)

    added_widgets_on_application()


def main_gui_start():
    window = tk.Tk()
    configuration_gui(window)
    create_widgets(window)

    window.mainloop()



if __name__ == '__main__':
    main_gui_start()


