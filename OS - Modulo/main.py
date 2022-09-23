import os

caminho_procura = 'D:\Clips'
termo_procura = '32'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    # vai na raiz e passa verificando o diretorio atras do arquivo
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)

        nome_arquivo, ext_arquivo = os.path.splitext(arquivo)

        print(nome_arquivo, ext_arquivo, sep='--')

        tamanho = os.path.getsize(caminho_completo)
        # pega o tamanho do arquivo
        print(tamanho)
