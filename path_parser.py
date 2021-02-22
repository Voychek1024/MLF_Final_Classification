import os

my_path_normal = 'Data/test/NORMAL'
my_path_pneumonia = 'Data/test/PNEUMONIA'
filename = 'test_diagnose.txt'

if __name__ == '__main__':
    files_normal = [f for f in os.listdir(path=my_path_normal) if os.path.isfile(os.path.join(my_path_normal, f))]
    with open(filename, 'a', encoding='utf-8', newline='\n') as out_file:
        for item in files_normal:
            out_file.write(my_path_normal + '/' + item + '\t' + '0\n')
            continue

    files_pneumonia = [f for f in os.listdir(path=my_path_pneumonia) if os.path.isfile(os.path.join(my_path_pneumonia, f))]
    with open(filename, 'a', encoding='utf-8', newline='\n') as out_file:
        for item in files_pneumonia:
            if 'virus' in item:
                out_file.write(my_path_pneumonia + '/' + item + '\t' + '1\n')
            elif 'bacteria' in item:
                out_file.write(my_path_pneumonia + '/' + item + '\t' + '1\n')
