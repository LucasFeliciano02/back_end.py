"""

Plural = conjunto de arquivos
singular = 1 arquivo em especificos

EX: for arquivo in arquivos:
    print(arquivo)

"""

import os


caminho_procura = input(r'Digite um caminho: ')
termo_procura = input('Digite um termo: ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'p'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')


conta = 0
for raiz, diretorio, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                tamanho = os.path.getsize(caminho_procura)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho))
            except PermissionError as ex:
                print('Sem permisões.')
            except FileNotFoundError as ex:
                print('Arquivo não encontrado.')
            except Exception as ex:
                print('Erro desconhecido', ex)

print()
print(f'{conta} arquivo(s) encontrado(s)')
