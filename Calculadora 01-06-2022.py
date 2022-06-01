from tkinter import * 
#back-end
#inserir os valores a serem calculados
def zero():
    in0['text'] = in0['text']+'0'
def um():
    in0['text'] = in0['text']+'1'
def dois():
    in0['text'] = in0['text']+'2'
def tres():
    in0['text'] = in0['text']+'3'
def quatro():
    in0['text'] = in0['text']+'4'
def cinco():
    in0['text'] = in0['text']+'5'
def seis():
    in0['text'] = in0['text']+'6'
def sete():
    in0['text'] = in0['text']+'7'
def oito():
    in0['text'] = in0['text']+'8'
def nove():
    in0['text'] = in0['text']+'9'
#salvar os valores inseridos para calculalos
def mais():
    global a
    a=in0['text']
    in0['text']=''
def igual():
    global a
    b=in0['text']
    x= a + b
    in0['text']=x
    
#front-end
root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
#Label and Name
in0 = Label (root, text='0', font='Arial 25')
in0.grid(row=1, column=0, columnspan=4, sticky=NSEW)
lb0 = Label (root, text='CALCULADORA', font='Arial 25', fg='green')
lb0.grid(row=0, column=0, columnspan=4, sticky=NSEW)
lb0.config(bg='black')
#widgets numéricos
bt0 = Button (root, text='0', font= 'Arial 25')
bt1 = Button (root, text='1', font= 'Arial 25')
bt2 = Button (root, text='2', font= 'Arial 25')
bt3 = Button (root, text='3', font= 'Arial 25')
bt4 = Button (root, text='4', font= 'Arial 25')
bt5 = Button (root, text='5', font= 'Arial 25')
bt6 = Button (root, text='6', font= 'Arial 25')
bt7 = Button (root, text='7', font= 'Arial 25')
bt8 = Button (root, text='8', font= 'Arial 25')
bt9 = Button (root, text='9', font= 'Arial 25')
#widgets simbolos
bt10 = Button (root, text='.', font= 'Arial 25')
bt11 = Button (root, text='=', font= 'Arial 25')
bt12 = Button (root, text='+', font= 'Arial 25')
bt13 = Button (root, text='-', font= 'Arial 25')
bt14 = Button (root, text='x', font= 'Arial 25')
bt15 = Button (root, text='/', font= 'Arial 25')
bt16 = Button (root, text='√', font= 'Arial 25')
bt17 = Button (root, text='x²', font= 'Arial 25')
bt18 = Button (root, text='%', font= 'Arial 25')
bt19 = Button (root, text='⌫', font= 'Arial 25')
bt20 = Button (root, text='C', font= 'Arial 25')

#root.bind('10', lambda event: ponto())
root.bind('=', lambda event: igual())
root.bind('+', lambda event: mais())
#root.bind('13', lambda event: menos())
#root.bind('14', lambda event: vezes())
#root.bind('15', lambda event: dividir())
#root.bind('16', lambda event: raiz())
#root.bind('17', lambda event: elevar())
#root.bind('18', lambda event: porcentagem())
#root.bind('19', lambda event: apagarTudo())
#root.bind('19', lambda event: apagar())

#Números
bt0.grid(row=7, column=0, columnspan=2, sticky=NSEW)
bt1.grid(row=6, column=0, sticky=NSEW)
bt2.grid(row=6, column=1, sticky=NSEW)
bt3.grid(row=6, column=2, sticky=NSEW)
bt4.grid(row=5, column=0, sticky=NSEW)
bt5.grid(row=5, column=1, sticky=NSEW)
bt6.grid(row=5, column=2, sticky=NSEW)
bt7.grid(row=4, column=0, sticky=NSEW)
bt8.grid(row=4, column=1, sticky=NSEW)
bt9.grid(row=4, column=2, sticky=NSEW)
#Simbolos
bt10.grid(row=7, column=2, sticky=NSEW)
bt11.grid(row=7, column=3, sticky=NSEW)
bt12.grid(row=6, column=3, sticky=NSEW)
bt13.grid(row=5, column=3, sticky=NSEW)
bt14.grid(row=4, column=3, sticky=NSEW)
bt15.grid(row=3, column=3, sticky=NSEW)
bt16.grid(row=3, column=2, sticky=NSEW)
bt17.grid(row=3, column=1, sticky=NSEW)
bt18.grid(row=3, column=0, sticky=NSEW)
bt19.grid(row=2, column=2, columnspan=2, sticky=NSEW)
bt20.grid(row=2, column=0, columnspan=2, sticky=NSEW)
#vincular as teclas do teclado
root.bind('0', lambda event: zero())
root.bind('1', lambda event: um())
root.bind('2', lambda event: dois())
root.bind('3', lambda event: tres())
root.bind('4', lambda event: quatro())
root.bind('5', lambda event: cinco())
root.bind('6', lambda event: seis())
root.bind('7', lambda event: sete())
root.bind('8', lambda event: oito())
root.bind('9', lambda event: nove())
#run #Função expecífica para manter a janela aparecendo.
root.mainloop()