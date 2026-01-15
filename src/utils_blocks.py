def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split('\n\n')
    list_of_blocks = [x.strip() for x in list_of_blocks if x != '']


    return list_of_blocks