import os
import shutil

from copystatic import copy_static_to_public,delete_public_dir
from page_generator import generate_page

def main():
    path_to_public = "./public"
    path_to_static = "./static"
    from_path = "./content/index.md"
    template_path = "template.html"
    dest_path = "./public/index.html"

    delete_public_dir()
    copy_static_to_public(path_to_static,path_to_public)
    generate_page(from_path,template_path,dest_path)


    
main()

