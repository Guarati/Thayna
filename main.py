# Integrantes: Aryela Freitas Souza, Anny Maria Almeida Galvão, Livia Gabrielle Ambrosio Dias e Thayná Guarati de Oliveira
# Turma: 2°A Informática matutino

from Acesso import logon, cadastro
from Classes import Empresa, Aluno

# Inicialização da lista DB com instâncias corretas
DB = [
    Empresa('LuminaEletro', 'iluminatudo', 'eletrotécnica', 'tarde', '3000'),
    Empresa('SublimeVolt', 'senhatop', 'eletrotécnica', 'manhã', '3500'),
    Empresa('BioQuimica', 'admin', 'química', 'tarde', '4000'),
    Empresa('QuímicaSolutions', 'senhasecreta', 'química', 'manhã', '4500'),
    Empresa('IfroPro', 'senhaetudo', 'informática', 'tarde', '5000'),
    Empresa('CiberSoluções', 'senha', 'informática', 'manhã', '5500'),
    Empresa('BuildArt', 'BuildArt', 'edificações', 'tarde', '6000'),
    Empresa('InnovaEdifica', 'EdificaInnova', 'edificações', 'manhã', '6500'),
    Aluno('Thayná', 'senhadathayna', 'informática', 'manhã', 'segunda'),
    Aluno('Anny', 'senhadaanny', 'química', 'tarde', 'terça'),
    Aluno('Lívia', 'senhadalivia', 'edificações', 'manhã', 'quarta'),
    Aluno('Aryela', 'senhadaaryela', 'eletrotécnica', 'tarde', 'quinta'),
]

while True:
    print('''1 - Cadastro
2 - Login
3 - Logout''')

    choice = input('O que você deseja fazer? ').strip()

    if '1' in choice or 'CADASTRO' in choice.upper():
        cadastro(DB)
    elif '2' in choice or 'LOGIN' in choice.upper():
        logon(DB)
    elif '3' in choice or 'LOGOUT' in choice.upper():
        print('Obrigado')
        break
    else:
        print("Escolha inválida, tente novamente.")