import os
import shutil


caminho = input("Digite um caminho: ")
arquivo = input("Digite o nome do arquivo: ")

# D:\Projeto_pv
# D:\Projeto_pv\projeto

try:
    if not os.path.exists(arquivo):
        os.makedirs(arquivo + caminho)


except FileExistsError as e:
    print(f'Pasta {arquivo} já existe')

for root, dirs, files in os.walk(caminho):
    for file in files:

        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(arquivo, file)

        shutil.move(old_file_path, new_file_path)

        print(f"Arquivo {file} movido com sucesso! ")


# directory = "TrainData/" +str(id)
# if not os.path.exists(directory):
#        os.makedirs(directory)
