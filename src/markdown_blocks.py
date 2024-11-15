block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    stripped_markdown = []
    for line in split_markdown:
        stripped_line = line.strip()
        if stripped_line:
            stripped_markdown.append(stripped_line)
    return stripped_markdown
    

def block_to_block_type(block):
    # heading block
    if block[0] == "#":
        hash_count = 0
        for char in block:
            if char == "#":
                hash_count += 1
            else:
                break
        if hash_count <= 6 and block[hash_count] == " ":
            return block_type_heading
        
    # code block 
    if block.startswith("```"):
        split_block = block.split("\n")
        if len(split_block) > 1 and split_block[0].startswith("```")and split_block[-1].startswith("```"):
            return block_type_code
    
    # quote block
    if block[0] == ">":
        split_block = block.split("\n")
        for line in split_block:
            if not line.startswith(">"):
                break
        else:
            return block_type_quote
    
    #unordered list
    if block[0] == "*" or block[0] == "-":
        split_block = block.split("\n")
        for line in split_block:
            if not (line.startswith("* ") or line.startswith("- ")):
                break
        else:
            return block_type_ulist
    
    #ordered list
    if block.startswith("1."):
        split_block = block.split("\n")
        counter = 1
        for line in split_block:
            if line.startswith(f"{counter}. "):
                counter += 1
            else:
                break
        else:
            return block_type_olist
    
    #if none of the above return paragraph
    else:
        return block_type_paragraph