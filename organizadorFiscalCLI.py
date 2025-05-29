from organizadorreceitabx import OrganizadorReceitaBX 
from tkinter import filedialog

caminho = filedialog.askdirectory()

print("Informe quais diretórios deverão ser criados:")
esocial = True if input("E-SOCIAL [y/n]: ").strip().lower()[0] == "y" else False
ecd = True if input("SPED ECD [y/n]: ").strip().lower()[0] == "y" else False
contribuicoes = True if input("SPED CONTRIBUIÇÕES [y/n]: ").strip().lower()[0] == "y" else False
ecf = True if input("SPED ECF [y/n]: ").strip().lower()[0] == "y" else False
efd = True if input("SPED EFD [y/n]: ").strip().lower()[0] == "y" else False
quais_diretorios_criar = [esocial, ecd, contribuicoes, ecf, efd]


org = OrganizadorReceitaBX(caminho)
dir_esocial = esocial
dir_ecd = ecd
dir_contribuicoes = contribuicoes
dir_ecf = ecf
dir_efd = efd

dir = (dir_esocial, dir_ecd, dir_contribuicoes, dir_ecf, dir_efd)

try:
    categorizar = org.categorizar_arquivos()
    checagem_diretorios = org.checar_diretorios()
    criacao_diretorios = org.criar_diretorios(*dir, *checagem_diretorios) 
    org.organizar_arquivos()
    registro_erros = org.registrar_erros()
    print("Organização finalizada!")
except Exception as e:
    print(e)