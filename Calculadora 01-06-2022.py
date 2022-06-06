from tkinter import * 
#salvar os valores inseridos para calculalos
def entrada(valor):
    in0_fr2['text'] += valor 
def resultado():
    if (in0_fr2['text'][-1:]) == '+' or (in0_fr2['text'][-1:]) == '.' or (in0_fr2['text'][-1:]) == '-' or (in0_fr2['text'][-1:]) == '/' or (in0_fr2['text'][-1:]) == '*':
        lb0_fr1['text']=in0_fr2['text']
        in0_fr2['text'] = 'Calculo Inválido'
    else:
        x=in0_fr2['text']
        in0_fr2['text'].replace('+','|',1).replace('-','|',1).replace('/','|',1).replace('*','|',1)
        in0_fr2['text'].split('|')
        
        
       #TERMINANDO ESTA PARTE 
        for i in range(len(in0_fr2['text'])):
            if not (in0_fr2['text'][i]):
                in0_fr2['text']='Calculo Inválido'
                break
        lb0_fr1['text']=in0_fr2['text']
        x=round(eval(in0_fr2['text']),2)
        in0_fr2['text']=str(x)
    

def limpar():
    in0_fr2['text'] = ''
    lb0_fr1['text']='HISTORICO'  
#front-end
root = Tk()
#Frame
fr1 = Frame(root)
fr2 = Frame(root)
#Configuração Janela
root.title('Calculadora')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
#Configuração Frame
fr1.grid_rowconfigure(0, weight=1)
fr1.grid_columnconfigure(0, weight=1)
#Configuração Dentro do Frame
fr2.grid_rowconfigure(0, weight=1)
fr2.grid_rowconfigure(1, weight=1)
fr2.grid_rowconfigure(2, weight=1)
fr2.grid_rowconfigure(3, weight=1)
fr2.grid_rowconfigure(4, weight=1)
fr2.grid_rowconfigure(5, weight=1)
fr2.grid_rowconfigure(6, weight=1)
fr2.grid_columnconfigure(0, weight=1)
fr2.grid_columnconfigure(1, weight=1)
fr2.grid_columnconfigure(2, weight=1)
fr2.grid_columnconfigure(3, weight=1)
root.geometry('320x500')
#Label and Name
in0_fr2 = Label (fr2, text='', font='Arial 25')
in0_fr2.grid(row=1, column=0, columnspan=4, sticky=NSEW)
lb0_fr1 = Label (fr1, text='HISTÓRICO', font='Arial 25', fg='green')
lb0_fr1.grid(row=0, column=0, columnspan=4, sticky=NSEW)
lb0_fr1.config(bg='black')
#widgets numéricos
bt0_fr2 = Button (fr2, text='0', font= 'Arial 25', command=lambda: entrada('0'))
bt1_fr2 = Button (fr2, text='1', font= 'Arial 25', command=lambda: entrada('1'))
bt2_fr2 = Button (fr2, text='2', font= 'Arial 25', command=lambda: entrada('2'))
bt3_fr2 = Button (fr2, text='3', font= 'Arial 25', command=lambda: entrada('3'))
bt4_fr2 = Button (fr2, text='4', font= 'Arial 25', command=lambda: entrada('4'))
bt5_fr2 = Button (fr2, text='5', font= 'Arial 25', command=lambda: entrada('5'))
bt6_fr2 = Button (fr2, text='6', font= 'Arial 25', command=lambda: entrada('6'))
bt7_fr2 = Button (fr2, text='7', font= 'Arial 25', command=lambda: entrada('7'))
bt8_fr2 = Button (fr2, text='8', font= 'Arial 25', command=lambda: entrada('8'))
bt9_fr2 = Button (fr2, text='9', font= 'Arial 25', command=lambda: entrada('9'))
#widgets simbolos
bt10_fr2 = Button (fr2, text='.', font= 'Arial 25', command=lambda: entrada('.'))
bt11_fr2 = Button (fr2, text='=', font= 'Arial 25', command=lambda: resultado())
bt12_fr2 = Button (fr2, text='+', font= 'Arial 25', command=lambda: entrada('+'))
bt13_fr2 = Button (fr2, text='-', font= 'Arial 25', command=lambda: entrada('-'))
bt14_fr2 = Button (fr2, text='x', font= 'Arial 25', command=lambda: entrada('*'))
bt15_fr2 = Button (fr2, text='/', font= 'Arial 25', command=lambda: entrada('/'))
bt16_fr2 = Button (fr2, text='√', font= 'Arial 25', command=lambda: entrada('√'))
bt17_fr2 = Button (fr2, text='x²', font= 'Arial 25', command=lambda: entrada('x²'))
bt18_fr2 = Button (fr2, text='%', font= 'Arial 25', command=lambda: entrada('%'))
bt19_fr2 = Button (fr2, text='⌫', font= 'Arial 25', command=lambda: limpar())
bt20_fr2 = Button (fr2, text='C', font= 'Arial 25', command=lambda: limpar())
#interação com o teclado
root.bind('.', lambda event: entrada('.'))
root.bind('<Return>', lambda event: resultado())
root.bind('+', lambda event: entrada('+'))
root.bind('-', lambda event: entrada('-'))
root.bind('*', lambda event: entrada('*'))
root.bind('/', lambda event: entrada('/'))
#root.bind('16', lambda event: entrada())
root.bind('^^', lambda event: entrada('**'))
root.bind('%', lambda event: entrada('/100'))
#root.bind('', lambda event: limpar())
root.bind('c', lambda event: limpar())
root.bind('C', lambda event: limpar())
#vincular as teclas do teclado
root.bind('0', lambda event: entrada('0'))
root.bind('1', lambda event: entrada('1'))
root.bind('2', lambda event: entrada('2'))
root.bind('3', lambda event: entrada('3'))
root.bind('4', lambda event: entrada('4'))
root.bind('5', lambda event: entrada('5'))
root.bind('6', lambda event: entrada('6'))
root.bind('7', lambda event: entrada('7'))
root.bind('8', lambda event: entrada('8'))
root.bind('9', lambda event: entrada('9'))
#Pack
fr1.grid(row=0, column=0, sticky=NSEW)
fr2.grid(row=1, column=0, sticky=NSEW)
#Números
bt0_fr2.grid(row=7, column=0, columnspan=2, sticky=NSEW)
bt1_fr2.grid(row=6, column=0, sticky=NSEW)
bt2_fr2.grid(row=6, column=1, sticky=NSEW)
bt3_fr2.grid(row=6, column=2, sticky=NSEW)
bt4_fr2.grid(row=5, column=0, sticky=NSEW)
bt5_fr2.grid(row=5, column=1, sticky=NSEW)
bt6_fr2.grid(row=5, column=2, sticky=NSEW)
bt7_fr2.grid(row=4, column=0, sticky=NSEW)
bt8_fr2.grid(row=4, column=1, sticky=NSEW)
bt9_fr2.grid(row=4, column=2, sticky=NSEW)
#Simbolos
bt10_fr2.grid(row=7, column=2, sticky=NSEW)
bt11_fr2.grid(row=7, column=3, sticky=NSEW)
bt12_fr2.grid(row=6, column=3, sticky=NSEW)
bt13_fr2.grid(row=5, column=3, sticky=NSEW)
bt14_fr2.grid(row=4, column=3, sticky=NSEW)
bt15_fr2.grid(row=3, column=3, sticky=NSEW)
bt16_fr2.grid(row=3, column=2, sticky=NSEW)
bt17_fr2.grid(row=3, column=1, sticky=NSEW)
bt18_fr2.grid(row=3, column=0, sticky=NSEW)
bt19_fr2.grid(row=2, column=2, columnspan=2, sticky=NSEW)
bt20_fr2.grid(row=2, column=0, columnspan=2, sticky=NSEW)
#run #Função expecífica para manter a janela aparecendo.
root.mainloop()