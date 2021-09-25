def append_text(files):
    dictionary = dict()
    for doc in files:
        with open(doc) as file:
            text = file.read().splitlines()
            quantity = len(text)
            dictionary[doc] = (quantity, text)
    return dictionary


def write_data(file_name, mode):
    for i in sorted(append_text(['1.txt', '2.txt', '3.txt']).items(), key=lambda para: para[1]):
        with open(file_name, f'{mode}') as file:
            text = '\n'.join(i[1][1])
            file.write(f'{i[0]}\n{i[1][0]}\n{text}\n')


write_data('4.txt', 'a')