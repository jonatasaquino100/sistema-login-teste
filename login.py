import PySimpleGUI as sg


users = {
    "user1": "password123",
    "admin": "adminpass",
    "guest": "guest123"
}


sg.theme("DarkBlue3")
font = ("Helvetica", 16)
button_font = ("Helvetica", 14)


layout = [
    [sg.Text("Nome de Usuário", font=font)],
    [sg.Input(key="-USERNAME-", size=(30, 1), font=font)],
    [sg.Text("Senha", font=font)],
    [sg.Input(key="-PASSWORD-", password_char="*", size=(30, 1), font=font)],
    [sg.Button("Login", font=button_font), sg.Button("Cancelar", font=button_font)]
]


window = sg.Window("Sistema de Login", layout, element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancelar":
        break
    
    username = values["-USERNAME-"]
    password = values["-PASSWORD-"]


    if username in users and users[username] == password:
        sg.popup("Login bem-sucedido!", title="Sucesso", font=font)
        break
    else:
        sg.popup("Nome de usuário ou senha incorretos.", title="Erro", font=font)

window.close()
