import os

caminho_procura = 'D:\Clips'
termo_procura = 'clip'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    # vai na raiz e passa verificando o diretorio atras do arquivo
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print("Encontrei o arquivo:", arquivo)
                print("Caminho:", caminho_completo)
                print("Nome:", nome_arquivo)
                print("Extensão:", ext_arquivo)
                print("Tamanho:", tamanho)
            except PermissionError as e:
                print("Acesso não autorizado.")

            except FileNotFoundError as e:
                print("Arquivo não encontrado. ")

            except Exception as e:
                print("Erro desconhecido", e)
