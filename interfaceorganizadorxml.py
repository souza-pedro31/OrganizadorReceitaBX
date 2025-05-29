import FreeSimpleGUI as sg
from organizadorxml import OrganizadorXML

class InterfaceOrganizadorXML:
    def __init__(self) -> None:
        return
    

    def interface(self) -> None:
        sg.theme('Default')
        fonte = 'Roboto'

        layout = [
            [sg.Text(text=f'{' '*52}Organizador de XMLs', font='Roboto 12 bold', pad=7)],
            [sg.Text('Pasta c/ arquivos: ', font='Roboto 10'), sg.Input(key='-FOLDER-', enable_events=True), sg.FolderBrowse(f'Buscar', font=f'{fonte} 10', size=(14,1))
            ,sg.Image(r'.\\.images\\img2.png', pad=((0,0),(0,0)))],
            [sg.Text(text=f'Versão 1.0{' '*142}Github: souza-pedro31', font=f'{fonte} 8 bold')]
        ]

        sg.popup_ok('Os arquivos serão organizados\nde acordo com ano e mês\n\nExemplo:\nPasta ano 2000 que contém\nmês 01 e 02', title='Popup início', font=(f'{fonte} 12'))
        window = sg.Window('Organizador', layout)

        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == '-FOLDER-':
                caminho = value['-FOLDER-']
            try:
                org = OrganizadorXML(caminho)
                _, contador = org.categorizar_xml()
                org.criar_diretorios()
                org.organizar_xml()
                sg.popup_auto_close(f'Organização completa!\n\n{contador} arquivos foram ordenados!', title='Popup êxito', auto_close_duration=15, font=(f'{fonte} 12'))
            except Exception as e:
                sg.popup_ok('Erro: ', e, title='Popup erro', font=(f'{fonte} 12'))
                continue
            break
        return
    

if __name__ == "__main__":
    interface = InterfaceOrganizadorXML()
    interface.interface()