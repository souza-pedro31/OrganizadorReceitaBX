import PySimpleGUI as sg
from organizadorreceitabx import OrganizadorReceitaBX 
from pathlib import Path

sg.theme('Default')
fonte = 'Roboto'
imgs = Path(__file__).parent

layout = [
    [sg.Text(text=f'{' '*50}Organizador ReceitaNetBX', font='Roboto 12 bold', pad=7)],
    [sg.Text('Pasta c/ arquivos: ', font='Roboto 10'), sg.Input(key='-FOLDER-', enable_events=True), sg.FolderBrowse(f'Buscar', font=f'{fonte} 10', size=(14,1))
    ,sg.Image(f'{imgs}\\img.png', pad=((0,0),(0,0)))],
    [],
    [sg.Text(text=f'{' '*65}Diretórios', font='Roboto 12 bold', pad=7)],
    [sg.Text(text='ESOCIAL'), sg.Checkbox(text='', key='-ESOCIAL-', default=True), sg.Text(text='SPED ECD'), sg.Checkbox(text='', key='-SPEDECD-', default=True),
    sg.Text(text='SPED Contribuições'), sg.Checkbox(text='', key='-SPEDCONTRIBUICOES-', default=True), sg.Text(text='SPED ECF'), sg.Checkbox(text='', key='-SPEDECF-', default=True),
    sg.Text(text='SPED EFD'), sg.Checkbox(text='', key='-SPEDEFD-', default=True)],
    [sg.Text(text=f'Versão 1.0{' '*142}Github: souza-pedro31', font=f'{fonte} 8 bold')]
    ]

sg.popup_ok('Os seguintes diretórios serão criados:\n\n- ESOCIAL\n- SPED ECD\n- SPED Contribuições\n- SPED ECF\n- SPED EFD\n\n( Desmarque os que você não precisa )', title='Popup início', font=(f'{fonte} 12'))
window = sg.Window('Organizador', layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == '-FOLDER-':
        caminho = value['-FOLDER-']
        org = OrganizadorReceitaBX(caminho)
        dir_esocial = value['-ESOCIAL-']
        dir_ecd = value['-SPEDECD-']
        dir_contribuicoes = value['-SPEDCONTRIBUICOES-']
        dir_ecf = value['-SPEDECF-']
        dir_efd = value['-SPEDEFD-']

        dir = (dir_esocial, dir_ecd, dir_contribuicoes, dir_ecf, dir_efd)
        
        try:
            categorizar = org.categorizar_arquivos()
            checagem_diretorios = org.checar_diretorios()
            criacao_diretorios = org.criar_diretorios(*dir, *checagem_diretorios) 
            org.organizar_arquivos()
            registro_erros = org.registrar_erros()
            sg.popup_auto_close(f'Organização completa!\n\n{categorizar[6]} arquivos foram ordenados!', title='Popup êxito', auto_close_duration=15, font=(f'{fonte} 12'))
        except Exception as e:
            sg.popup_ok('Erro: ', e, title='Popup erro', font=(f'{fonte} 12'))
        window['-FOLDER-'].update('')
        break
        
        