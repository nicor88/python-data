file_path = 'data/table.txt'


with open(file_path) as f:
    content = f.readlines()

# it removes the empty lines
clean_content = [l for l in content if l != '\n']

# remove the line terminator for each line
lines = [l.replace('\n', '') for l in clean_content]

dict_attrs = lines[0].split()

interfaces = [dict(zip(dict_attrs, l.split())) for l in lines[1:]]

interfaces_up = [i for i in interfaces if i['State'] == 'Up']
