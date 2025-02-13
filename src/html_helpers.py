import node_helpers
import html_helpers
import os
import shutil

def extract_title(markdown):
    title = ""
    for block in node_helpers.markdown_to_blocks(markdown):
        if block[0:2] == "# ":
            title = block[2:]
    return title

def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        raise Exception(f"from_path ({from_path}) does not exist")
    if not os.path.exists(template_path):
        raise Exception(f"template_path({template_path}) does not exist")
    if os.path.exists(dest_path):
        os.remove(dest_path)
    shutil.copy(template_path, dest_path)
    
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")
    with open(from_path) as f:
        markdown = f.read()

    title = html_helpers.extract_title(markdown)
    content = node_helpers.markdown_to_html_node(markdown).to_html()
    with open(dest_path) as f:
        target = f.read()

    target = target.replace("{{ Title }}", title)
    target = target.replace("{{ Content }}", content)

    with open(dest_path, "w") as f:
        f.write(target)

def generate_pages_recursively(from_dir, template_path, dest_dir):
    for file in os.listdir(from_dir):
        if os.path.isfile(os.path.join(from_dir, file)):
            from_path = os.path.join(from_dir, file)
            dest_path = os.path.join(dest_dir, file).split(".md")[0] + ".html"
            generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(os.path.join(from_dir, file)):
            next_from_dir = os.path.join(from_dir, file)
            next_dest_dir = os.path.join(dest_dir, file)
            os.mkdir(next_dest_dir)
            generate_pages_recursively(next_from_dir, template_path, next_dest_dir)
