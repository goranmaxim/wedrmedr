import os
from subprocess import call

def set_wallpaper(image_file_path):
    filepath = os.path.abspath(image_file_path)

    call(['feh', '--bg-fill', '%s' % (filepath)])

    return True
