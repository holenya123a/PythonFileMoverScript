def print_options():
    print('\n   ---------OPTIONS----------')
    print('\n   1. DELETE DUPLICATES')
    print('\n   2. MOVE DUPLICATES')
    print('\n   3. EXIT')


def print_duplicates(files_info: dict):
    value: str = ''
    print('\n   -----DUPLICATED FILES-----')
    for key in files_info:
        for name in files_info[key]:
            value += f'{name}, '
            value = value[:-2]
            print(f'\n   {value}')
            value = ''
    print('\n   --------------------------')
