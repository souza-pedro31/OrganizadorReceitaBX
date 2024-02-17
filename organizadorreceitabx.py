import os

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
            os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED Contábil')}"')
        if not checagem_sped_contribuicoes and dir_contribuicoes:
            os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED Contribuições')}"')
        if not checagem_sped_ecf and dir_ecf:
            os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED ECF')}"')
        if not checagem_sped_fiscal and dir_efd:
            os.system(f'mkdir "{os.path.join(self.__caminho, 'SPED Fiscal')}"')
        if not checagem_esocial and dir_esocial:
            os.system(f'mkdir "{os.path.join(self.__caminho, 'ESOCIAL')}"')  
        return
    

    def organizar_arquivos(self) -> None:
        for arquivoEFD in self.__sped_EFD:
            os.system(f'move "{os.path.join(self.__caminho, arquivoEFD)}" "{os.path.join(self.__caminho, 'SPED Fiscal')}"')
        for arquivoPisCofins in self.__sped_PisCofins:
            os.system(f'move "{os.path.join(self.__caminho, arquivoPisCofins)}" "{os.path.join(self.__caminho, 'SPED Contribuições')}"')
        for arquivoECF in self.__sped_ECF:
            os.system(f'move "{os.path.join(self.__caminho, arquivoECF)}" "{os.path.join(self.__caminho, 'SPED ECF')}"')
        for arquivoECD in self.__sped_ECD:
            os.system(f'move "{os.path.join(self.__caminho, arquivoECD)}" "{os.path.join(self.__caminho, 'SPED Contábil')}"')
        for arquivoEsocial in self.__esocial:
            os.system(f'move "{os.path.join(self.__caminho, arquivoEsocial)}" "{os.path.join(self.__caminho, 'ESOCIAL')}"')
        return
    
    @property
    def lista_arquivos(self):
        return self.__arquivos


if __name__ == '__main__':
    pass