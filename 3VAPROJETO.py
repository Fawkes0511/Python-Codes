#Importando as bibliotecas
import requests
from tkinter import *
#Definindo a função principal
def buscar_moedas():
    #Requisitando o site das cotações
    requisicoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicoes_dic = requisicoes.json()

    cot_dolar = requisicoes_dic['USDBRL']['bid']
    cot_euro = requisicoes_dic['EURBRL']['bid']
    cot_bitcoin = requisicoes_dic['BTCBRL']['bid']

    linhas = f'''
    Dólar: {cot_dolar}
    Euro: {cot_euro}
    BTC: {cot_bitcoin}'''

    textobot["text"] = linhas
#Criando a janela de exibição
janela = Tk()
janela.title('Cotações de Moedas')
janela.configure(background="black")
janela.geometry("370x195")

infos = Label(janela, text='Clique no botão abaixo para exibir as cotações atuais',background="black",foreground="yellow",font="Calibri")
infos.grid(column=0, row=0,padx=10, pady=10)

botao = Button(janela, text='Clique Aqui',background="black",foreground="yellow",command=buscar_moedas,font="Calibri")
botao.grid(column=0, row=1,padx=10,pady=10)

textobot = Label(janela, text='',background="black",foreground="yellow",font="Calibri")
textobot.grid(column=0, row=2)


janela.mainloop()