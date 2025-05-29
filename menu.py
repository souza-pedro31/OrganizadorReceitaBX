import FreeSimpleGUI as sg
from interfaceorganizadorreceitabx import InterfaceOrganizadorReceitaBX
from interfaceorganizadorxml import InterfaceOrganizadorXML


class MenuOrganizador:
    def __init__(self) -> None:
        return
    
    def interface(self):
        sg.theme('Default')
        fonte = 'Roboto'

        layout = [
            [sg.Text(f'{' '*32}Menu', font=f'{fonte} 12 bold', pad=7)],
            [sg.Text(f'{' '*21}Organizador Receita BX', font=f'{fonte} 10')],
            [sg.Image(r'.\\.images\\Org Receita BX menu.png',)],
            [sg.Button('Abrir', font=f'{fonte} 11', size=(33,1), key=('-ORGBX-'))],
            [sg.Text('')],
            [sg.Text(f'{' '*21}Organizador de XMLs', font=f'{fonte} 10')],
            [sg.Image(r'.\\.images\\Org XML menu.png', pad=3)],
            [sg.Button('Abrir', font=f'{fonte} 11', size=(33,1), key=('-ORGXML-'))],
            [sg.Text(text=f'Versão 1.1{' '*40}Github: souza-pedro31', font=f'{fonte} 8 bold')]
            ]

        window = sg.Window('Menu Organizador', layout)

        while True:
            event, value = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == '-ORGBX-':
                window.close()
                interface = InterfaceOrganizadorReceitaBX()
                interface.interface()

            if event == '-ORGXML-':
                window.close()
                interface = InterfaceOrganizadorXML()
                interface.interface()

if __name__ == '__main__':
    menu = MenuOrganizador()
    menu.interface()