import os
import shutil

from copystatic import copy_static_to_public,delete_public_dir
from page_generator import generate_pages_recursive

def main():
    path_to_public = "./public"
    path_to_static = "./static"
    from_path = "./content"
    template_path = "./template.html"

    delete_public_dir()
    copy_static_to_public(path_to_static,path_to_public)

    generate_pages_recursive(from_path,template_path,path_to_public)



    
main()

