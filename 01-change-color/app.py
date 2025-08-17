from define import *
import os
class APP:
    def __init__(self,window):
        window.geometry("{}x{}+{}+{}".format(WINDOWN_WIDTH, WINDONW_HEIGHT, WINDOWN_POSITION_RIGHT, WINDOWN_POSITION_DOWN))

        # title
        window.title("Change Color")
        # website-optimization-icon_icon-icons.com_55720.ico = path_image+\website-optimization-icon_icon-icons.com_55720.ico
        directory_path = os.path.dirname(os.path.abspath(__file__))
        print("directory_path" + directory_path)
        path_image = os.path.join(directory_path, 'image')
        print("mooon ngu\n"+path_image+"/seo1.png")

        iconhinh = path_image+"/seo1.png"

        if os.path.exists(iconhinh):
            # window.iconbitmap(iconhinh)
            pass
        window['background'] = COLOR_BACKGROUND
        window.resizable(False, False)