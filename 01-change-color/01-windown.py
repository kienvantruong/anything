from tkinter import *
from define import *
import os

roof = Tk()
def setup_window():
    roof.geometry("{}x{}+{}+{}".format(WINDOWN_WIDTH, WINDONW_HEIGHT, WINDOWN_POSITION_RIGHT, WINDOWN_POSITION_DOWN))

    # title
    roof.title("Change Color")
    # website-optimization-icon_icon-icons.com_55720.ico = path_image+\website-optimization-icon_icon-icons.com_55720.ico
    directory_path = os.path.dirname(os.path.abspath(__file__))
    print("directory_path" + directory_path)
    path_image = os.path.join(directory_path, 'image')
    print("mooon ngu\n"+path_image+"/seo1.png")

    iconhinh = path_image+"/seo1.png"

    if os.path.exists(iconhinh):
        # roof.iconbitmap(iconhinh)
        roof.iconphoto(False, PhotoImage(file=iconhinh))

    roof['background'] = COLOR_BACKGROUND
    roof.resizable(False, False)
setup_window()
roof.mainloop()
