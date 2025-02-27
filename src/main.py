from textnode import TextNode, TextType
import os
import shutil
from html_helpers import generate_pages_recursively

def main():
    source = "/home/hunter/workspace/github.com/Edecxo/static-site-generator/static"
    destination = "/home/hunter/workspace/github.com/Edecxo/static-site-generator/public"
    copy_files(source, destination)
    generate_pages_recursively("/home/hunter/workspace/github.com/Edecxo/static-site-generator/content", "/home/hunter/workspace/github.com/Edecxo/static-site-generator/template.html", "/home/hunter/workspace/github.com/Edecxo/static-site-generator/public")

def copy_files(source, destination):
    if not os.path.exists(source) or os.path.isfile(source):
        raise Exception("source folder does not exist")
    if not os.path.exists(destination) or os.path.isfile(destination):
        raise Exception("destination folder does not exist")
    if os.listdir == []:
        return

    shutil.rmtree(destination)
    os.mkdir(destination)
    for file in os.listdir(source):
        file_path = os.path.join(source, file)
        if os.path.isfile(file_path):
            shutil.copy(os.path.join(source, file), destination)
        elif os.path.exists(file_path) and not os.path.isfile(file_path):
            os.mkdir(os.path.join(destination, file))
            copy_files(file_path, os.path.join(destination, file))

main()
