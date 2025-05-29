import os
from shutil import move
class OrganizadorReceitaBX:
    def __init__(self, caminho: str) -> None:
        self.__caminho = caminho
        self.__arquivos = os.listdir(caminho)
        self.__sped_EFD = []
        self.__sped_PisCofins = []
        self.__sped_ECF = []
        self.__sped_ECD = []
        self.__esocial = []
        self.__lista_erros = []
        return
    

    def categorizar_arquivos(self) -> None:
        for arquivo in self.__arquivos:
            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
            if arquivo[:9] == 'PISCOFINS':
                self.__sped_PisCofins.append(arquivo)
            elif arquivo[:7] == 'SPEDECF':
                self.__sped_ECF.append(arquivo)
            elif arquivo[-12:] == 'SPED-EFD.txt':
                self.__sped_EFD.append(arquivo)
            elif arquivo[-12:] == 'SPED-ECD.txt':
                self.__sped_ECD.append(arquivo)
            elif extensao_arquivo == '.zip':
                self.__esocial.append(arquivo)
            else:
                self.__lista_erros.append(arquivo)
        qtd_arquivos = len(self.__arquivos)
        return (self.__sped_EFD, self.__sped_PisCofins, self.__sped_ECF, self.__sped_ECD, self.__esocial, self.__lista_erros, qtd_arquivos)
    

    def registrar_erros(self) -> None:
        if len(self.__lista_erros) > 1:
            with open('Erros.txt','a') as registro:
                for o in self.__lista_erros:
                    registro.write(f'{o}\n')
        return


    def checar_diretorios(self) -> tuple:
        checagem_sped_contabil = os.path.exists(os.path.join(self.__caminho, 'SPED Contábil'))
        checagem_sped_contribuicoes = os.path.exists(os.path.join(self.__caminho, 'SPED Contribuições'))
        checagem_sped_ecf = os.path.exists(os.path.join(self.__caminho, 'SPED ECF'))
        checagem_sped_fiscal = os.path.exists(os.path.join(self.__caminho, 'SPED Fiscal'))
        checagem_esocial = os.path.exists(os.path.join(self.__caminho, 'ESOCIAL'))

        return (checagem_sped_contabil, checagem_sped_contribuicoes, checagem_sped_ecf,
                checagem_sped_fiscal, checagem_esocial)
    

    def criar_diretorios(self, dir_esocial: bool,
                    dir_ecd: bool, dir_contribuicoes: bool,dir_ecf: bool, dir_efd: bool, 
                    checagem_sped_contabil: bool = True, checagem_sped_contribuicoes: bool = True,
                    checagem_sped_ecf: bool = True, checagem_sped_fiscal: bool = True,
                    checagem_esocial: bool = True) -> None:
    
        if not checagem_sped_contabil and dir_ecd:
            os.mkdir(os.path.join(self.__caminho, 'SPED Contábil'))
            # os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED Contábil')}"')
        if not checagem_sped_contribuicoes and dir_contribuicoes:
            os.mkdir(os.path.join(self.__caminho, 'SPED Contribuições'))
            # os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED Contribuições')}"')
        if not checagem_sped_ecf and dir_ecf:
            os.mkdir(os.path.join(self.__caminho, 'SPED ECF'))
            # os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED ECF')}"')
        if not checagem_sped_fiscal and dir_efd:
            os.mkdir(os.path.join(self.__caminho, 'SPED Fiscal'))
            # os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED Fiscal')}"')
        if not checagem_esocial and dir_esocial:
            os.mkdir(os.path.join(self.__caminho, 'ESOCIAL'))
            # os.system(f'mkdir "{os.path.join(self.__caminho, 'ESOCIAL')}"')  
        return
    

    def organizar_arquivos(self) -> None:
        for arquivoEFD in self.__sped_EFD:
            caminho_antigo = os.path.join(self.__caminho, arquivoEFD)
            caminho_novo = os.path.join(self.__caminho, 'SPED Fiscal')
            move(caminho_antigo, caminho_novo)
            # os.system(f'move "{os.path.join(self.__caminho, arquivoEFD)}" "{os.path.join(self.__caminho, 'SPED Fiscal')}"')
        for arquivoPisCofins in self.__sped_PisCofins:
            caminho_antigo = os.path.join(self.__caminho, arquivoPisCofins)
            caminho_novo = os.path.join(self.__caminho, 'SPED Contribuições')
            move(caminho_antigo, caminho_novo)
            # os.system(f'move "{os.path.join(self.__caminho, arquivoPisCofins)}" "{os.path.join(self.__caminho, 'SPED Contribuições')}"')
        for arquivoECF in self.__sped_ECF:
            caminho_antigo = os.path.join(self.__caminho, arquivoECF)
            caminho_novo = os.path.join(self.__caminho, 'SPED ECF')
            move(caminho_antigo, caminho_novo)            
            # os.system(f'move "{os.path.join(self.__caminho, arquivoECF)}" "{os.path.join(self.__caminho, 'SPED ECF')}"')
        for arquivoECD in self.__sped_ECD:
            caminho_antigo = os.path.join(self.__caminho, arquivoECD)
            caminho_novo = os.path.join(self.__caminho, 'SPED Contábil')
            move(caminho_antigo, caminho_novo)
            # os.system(f'move "{os.path.join(self.__caminho, arquivoECD)}" "{os.path.join(self.__caminho, 'SPED Contábil')}"')
        for arquivoEsocial in self.__esocial:
            caminho_antigo = os.path.join(self.__caminho, arquivoEsocial)
            caminho_novo = os.path.join(self.__caminho, 'ESOCIAL')
            move(caminho_antigo, caminho_novo)
            # os.system(f'move "{os.path.join(self.__caminho, arquivoEsocial)}" "{os.path.join(self.__caminho, 'ESOCIAL')}"')
        return
    
    @property
    def lista_arquivos(self):
        return self.__arquivos


if __name__ == '__main__':
    caminho = str(input('Insira o caminho completo da pasta dos seus arquivos: '))
    org = OrganizadorReceitaBX(caminho)
    categorizar = org.categorizar_arquivos()
    checagem_diretorios = org.checar_diretorios()
    criacao_diretorios = org.criar_diretorios(*checagem_diretorios) 
    org.organizar_arquivos()
    registro_erros = org.registrar_erros() 