from markdown_blocks import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    if not os.path.exists(from_path):
        raise ValueError("from path dosent exist")
    if not os.path.exists(template_path):
        raise ValueError("temple path dosent exist")

    os.makedirs(os.path.dirname(dest_path),exist_ok=True)

    with open(from_path, 'r') as md_file:
        md_content = md_file.read()
    
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
    
    div_parent_node = markdown_to_html_node(md_content)
    html_string = div_parent_node.to_html()
    title = extract_title(md_content)

    updated_content = template_content.replace("{{ Title }}",title).replace("{{ Content }}",html_string)

    with open(dest_path,'w') as content:
        content.write(updated_content)