import pandas as pd
import win32com.client as win32
import PySimpleGUI as sg

layout = [
    [sg.Text('0', size=(18,1), font=('Helvetica', 30), text_color='black', key='tela')],
    [sg.Button('1', size=(10, 2), pad=(5, 5), key='1',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('2', size=(10, 2), pad=(5, 5), key='2',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('3', size=(10, 2), pad=(5, 5), key='3',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('-', size=(10, 2), pad=(5, 5), key='-',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True)],
    [sg.Button('4', size=(10, 2), pad=(5, 5), key='4',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('5', size=(10, 2), pad=(5, 5), key='5',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('6', size=(10, 2), pad=(5, 5), key='6',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('/', size=(10, 2), pad=(5, 5), key='/',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True)],
    [sg.Button('7', size=(10, 2), pad=(5, 5), key='7',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('8', size=(10, 2), pad=(5, 5), key='8',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('9', size=(10, 2), pad=(5, 5), key='9',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('*', size=(10, 2), pad=(5, 5), key='*',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True)],
    [sg.Button('+', size=(10, 2), pad=(5, 5), key='+',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('0', size=(10, 2), pad=(5, 5), key='0',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('.', size=(10, 2), pad=(5, 5), key='.',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True), sg.Button('=', size=(10, 2), pad=(5, 5), key='=',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True)],
    [sg.Button('Limpar', size=(10, 2), pad=(5, 5), key='Limpar',  font=('Helvetica', 12), button_color=('white', 'grey'), border_width=2, focus=True)],
    [sg.Text('',key='mensagem')],
]

janela = sg.Window('Calculadora',layout = layout)

resultado = ''
while True:
    evento, valores = janela.read()
    
    if evento in '0123456789+-*/.':
        resultado += evento
        janela['tela'].update(resultado)
        
    if evento == '=':
        resultado = str(eval(resultado))
        janela['tela'].update(resultado)
        
    if evento == 'Limpar':
        resultado = ''
        janela['tela'].update(resultado)
        
    if evento == sg.WINDOW_CLOSED:
        break

janela.close()

