import os
import shutil

def delete_public_dir():
    path_to_public = "./public"
    if os.path.exists(path_to_public):
        shutil.rmtree(path_to_public)

def copy_static_to_public(source_path,destination_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    source_dir = os.listdir(source_path)
    for dir in source_dir:
        new_source = os.path.join(source_path,dir)
        new_destination = os.path.join(destination_path,dir)
        if os.path.isfile(new_source):
            shutil.copy(new_source,destination_path)
            print(f"Copied file: {new_source} to {destination_path}")
        else:
            if not os.path.exists(new_destination):
                copy_static_to_public(new_source,new_destination)
                print(f"Recursively copying directory: {new_source} to {new_destination}")