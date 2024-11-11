def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    stripped_markdown = []
    for line in split_markdown:
        stripped_line = line.strip()
        if stripped_line:
            stripped_markdown.append(stripped_line)
    return stripped_markdown
    
