import os
import shutil

# Nessa aula foi se usado o modulo shutil e tambem usado o modulo os para
# criar arquivos e mover os arquivos para outra pasta

caminho_original = 'D:\Clips\Python_teste'
caminho_novo = 'D:\Clips'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f"Pasta {caminho_novo} já existe")

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        shutil.move(old_file_path, new_file_path)

        print(f"Arquivo {file} movido com sucesso! ")
