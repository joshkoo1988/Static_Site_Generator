def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("# "):
            title_text = line[1:].strip()
            return title_text
    raise Exception ("no h1 found")