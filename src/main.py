import os
import shutil

from copystatic import copy_static_to_public,delete_public_dir

def main():
    path_to_public = "./public"
    path_to_static = "./static"
    delete_public_dir()
    copy_static_to_public(path_to_static,path_to_public)

    
main()

