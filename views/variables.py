# GUI variables
NAME_GUI = 'Catalog'
WIDTH_MAIN = 1075
HEIGHT_MAIN = 767
BGCOLOR_MAIN = 'gray'
FGCOLOR_MAIN = 'white'
BTNBGCOLOR_MAIN = 'black'
BTNFGCOLOR_MAIN = 'white'
LSTBGCOLOR_MAIN = 'black'
LSTFGCOLOR_MAIN = 'white'

NAME_GUI_CONNECT = 'Connect to data base'
WIDTH_CONNECT = 647
HEIGHT_CONNECT = 289

NAME_GUI_CHANGE_ITEM = 'Change parameters item in data base'
WIDTH_CHANGE = 918
HEIGHT_CHANGE = 469

RESIZE = True
PNG_ICO_PATH = 'ico_gui.png'  # path to file *.png for creating ico application
LIMIT_IN_LIST_HOME_PAGE = 10 # limit in sql query in listbox or labels or combobox on home page\
MAX_VALUES_FOR_ITEMS = 9999 # this value for maximum quantity of item on warehouse
MAX_VALUES_FOR_ROW = 10
MAX_VALUES_FOR_SHELF = 10
TEMPLATE_ITEM_IN_LIST_BOX = 'ID: {:^6} | NAME: {:^60} | OZM: {:^10} | DESCR: {:^100} | COUNT: {:^6}'
FAIL_MESSAGE_TO_LIST_BOX = (-1, 'No into data base item with this ozm number!', -1, '-----------------', -1)