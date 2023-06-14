import pandas as pd

def convert_to_excel(data_string, path):
 
    data_lines = data_string.strip().split('\n')
    data = []
    current_floor = ''
    current_subgroup = ''

    for line in data_lines:
        if line.startswith('Floor:'):
            current_floor = line.split()[1]
        elif line.startswith('Group'):
            current_subgroup = line.strip(':')
        elif line.strip().startswith('{'):
            group_data = line.split('  ')
            group_values = group_data[0].replace('{', '').replace('}', '').split(', ')
            group_dict = {}
            for item in group_values:
                key, value = item.split(': ')
                group_dict[key] = int(value)
            if len(group_data) > 1:
                leftover = int(group_data[1].split(': ')[1])
            else:
                leftover = 1
            data.append((current_floor, current_subgroup, group_dict, leftover))

    df = pd.DataFrame(data, columns=['Floor', 'Subgroup', 'Group', 'Leftover'])
    df.to_excel(path, index=False)