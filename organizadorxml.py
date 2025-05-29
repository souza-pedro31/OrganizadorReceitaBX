import os
from shutil import move


class OrganizadorXML():
    def __init__(self, caminho) -> None:
        self.__caminho = caminho
        self.__periodos_existentes = set()
        self.__contador = 0
        return None

    def categorizar_xml(self) -> set:
        for root, dirs, files in os.walk(self.__caminho):
            for file in files:
                if file[-4:] == '.xml':
                    periodo = file[2:6]
                    self.__contador += 1
                    self.__periodos_existentes.add(periodo)
        return self.__periodos_existentes, self.__contador


    def criar_diretorios(self) -> str:
        for periodo in self.__periodos_existentes:
            ano = periodo[0:2]
            mes = periodo[2:4]
            caminho_diretorios = os.path.join(self.__caminho, f'20{ano}', mes)
            os.makedirs(caminho_diretorios, exist_ok=True)
        return 'Diretórios criados com sucesso!'
    

    def organizar_xml(self):
        for root, dirs, files in os.walk(self.__caminho):
            for file in files:
                mes = file[4:6]
                ano = file[2:4]
                antigo_caminho = os.path.join(root, file)

                if f'20{ano}' in dirs and file[-4:] == '.xml':
                    novo_caminho = os.path.join(root,f'20{ano}', mes)
                    move(antigo_caminho, novo_caminho)


if __name__ == '__main__':
    org = OrganizadorXML('C:\\Users\\DRG 133 06\\Desktop\\xml')
    org.categorizar_xml()
    org.criar_diretorios()
    org.organizar_xml()