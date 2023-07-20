from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import scrolledtext
from tkinter import filedialog as fd

# Importanto View
from view import *

################# tkcalendar ###############
from tkcalendar import Calendar, DateEntry
from datetime import date

#cores
Co0 = "#2e2d2b"
Co1 = "#feffff"
Co2 = "#4fa882"
Co3 = "#38576b"
Co4 = "#403d3d"
Co5 = "#e06636"
Co6 = "#038cfc"
Co7 = "#3fbfb9"
Co8 = "#263238"
Co9 = "#e9edf5"

#Criando janela

janela = Tk()
janela.title('')
janela.geometry('1043x453')
janela.configure(background=Co9)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")


################# Frames ####################
frameHeader = Frame(janela, width=1043, height=50, bg=Co1, relief="flat")
frameHeader.grid(row=0, column=0)

frameBody = Frame(janela, width=1043, height=303, bg=Co1, pady=20, relief="flat")
frameBody.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameDireita = Frame(janela,width=143, height=300, bg=Co1, relief="flat")
frameDireita.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

global tree

# funcao inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local= e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome,local,descricao,model,data,valor,serie,imagem]
    
    for i in lista_inserir:
        if i== '':
            messagebox.showerror('Erro','Preencha todos os campos')
            return
        
    inserir_form(lista_inserir)
  
    messagebox.showinfo('Sucesso','Os dados foram  inseridos com sucesso')

    e_nome.delete(0,'end')
    e_local.delete(0,'end')
    e_descricao.delete(0,'end')
    e_model.delete(0,'end')
    e_cal.delete(0,'end')
    e_valor.delete(0,'end')
    e_serial.delete(0,'end')

    mostrar()

# função para carregar a imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem 

    imagem = fd.askopenfilename()
    imagem_string = imagem

    #Abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem= Label(frameBody, image=imagem,bg=Co1, fg=Co4)
    l_imagem.place(x=700, y=10)

# função para ver a imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    item = ver_item(valor)

    imagem = item[0][8]

    #Abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameBody, image=imagem,bg=Co1, fg=Co4)
    l_imagem.place(x=700, y=10)

# funcao atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:          
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serial.delete(0, 'end')

        id = int(treev_lista[0])  
 
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serial.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]
        # print(treev_lista)
      

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serial.get()
            imagem = imagem_string                
            
            if imagem == '':
                    imagem = e_serial.insert(0, treev_lista[7])

            lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem, str(id)]

            for i in lista_atualizar:
              if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return 
              
            atualizar_(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serial.delete(0, 'end')

            b_confirmar.destroy()
            mostrar()

        b_confirmar = Button(frameBody, command=update, width=13, text='Confirmar'.upper(), overrelief=RIDGE, font=('ivy 8 bold'),bg=Co2, fg=Co1 )
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

      




# funcao deletar
def deletar():
    try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']

            valor = treev_lista[0]

            deletar_form([valor])       

            mostrar()   

            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            for widget in frameDireita.winfo_children():
                    widget.destroy()
            mostrar()
    
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


# funcao para mostrar
def mostrar():

    # creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome','Tipo','Descrição','Modelo','Data','Valor','Número de série']

    lista_itens = ver_form()

    global tree

    tree = ttk.Treeview(frameDireita,selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center","center"]
    h=[40,150,100,160,130,100,100,100]

    n=0

    for col in tabela_head:tree.heading(col, text=col.title(), anchor=CENTER)

    # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])

    n+=1

    for item in lista_itens:tree.insert('', 'end', values=item)

    quantidade = []

    for iten in lista_itens:quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens



#Abrindo imagem
app_img = Image.open('inventorio.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameHeader, image=app_img, text=' Inventário ', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=Co1, fg=Co4)
app_logo.place(x=0, y=0)

#campos de entrada
l_nome = Label(frameBody, text="Nome", height=1, anchor=NW, font=('Ivy 10 bold'), bg=Co1, fg=Co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameBody, width=30, justify='left',relief="solid")
e_nome.place(x=130, y=11)

l_local = Label(frameBody, text="Sala/Área", height=1,anchor=NW, font=('Ivy 10 bold'), bg=Co1, fg=Co4)
l_local.place(x=10, y=40)
e_local = Entry(frameBody, width=30, justify='left',relief="solid")
e_local.place(x=130, y=41)

l_descricao = Label(frameBody, text="Decrição", height=1, anchor=NW, font=('Ivy 10 bold'), bg=Co1, fg=Co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameBody, width=30,justify='left',relief="solid")
e_descricao.place(x=130, y=71)

l_model = Label(frameBody, text="Marca/Modelo", height=1,anchor=NW, font=('Ivy 10 bold'), bg=Co1, fg=Co4)
l_model.place(x=10, y=100)
e_model = Entry(frameBody, width=30, justify='left',relief="solid")
e_model.place(x=130, y=101)

l_cal = Label(frameBody, text="Data da compra", height=1,anchor=NW, font=('Ivy 10 bold'), bg=Co1, fg=Co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameBody, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
e_cal.place(x=130, y=131)


l_valor = Label(frameBody, text="Valor da compra", height=1,anchor=NW, font=('Ivy 10 bold'), bg=Co1,fg=Co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameBody, width=30, justify='left',relief="solid")
e_valor.place(x=130, y=161)

l_serial = Label(frameBody, text="Número de série", height=1, anchor=NW, font=('Ivy 10 bold'), bg=Co1, fg=Co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameBody, width=30, justify='left', relief = 'solid')
e_serial.place(x=130, y=191)


#carregar imagem
l_carregar = Label(frameBody, text="Imagem do iten", height=1,anchor=NW, font=('Ivy 10 bold'),
bg=Co1, fg=Co4)
l_carregar.place(x=10, y=220)
botao_carregar = Button(frameBody,command=escolher_imagem, compound=CENTER, anchor=CENTER, text="carregar".upper(),
width=30, overrelief=RIDGE, font=('ivy 8'),bg=Co1, fg=Co0 )
botao_carregar.place(x=130, y=221)


# Botao Inserir
img_add = Image.open('add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)
botao_inserir = Button(frameBody, image=img_add,command=inserir, compound=LEFT, anchor=NW, text="Adicionar".upper(), width=95, overrelief=RIDGE, font=('ivy 8'),bg=Co1, fg=Co0 )
botao_inserir.place(x=330, y=10)

# Botaop Atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)
botao_atualizar = Button(frameBody, command=atualizar, image=img_update, compound=LEFT, anchor=NW, text="Atualizar".upper(), width=95, overrelief=RIDGE, font=('ivy 8'),bg=Co1, fg=Co0 )
botao_atualizar.place(x=330, y=50)

# Botao Deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frameBody, command=deletar, image=img_delete, compound=LEFT, anchor=NW, text="Deletar".upper(), width=95, overrelief=RIDGE, font=('ivy 8'),bg=Co1, fg=Co0 )
botao_deletar.place(x=330, y=90)

# Botao ver Item
img_item = Image.open('item.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)
botao_ver = Button(frameBody,command=ver_imagem, image=img_item, compound=LEFT, anchor=NW, text=" Ver item".upper(), width=95, overrelief=RIDGE, font=('ivy 8'),bg=Co1, fg=Co0 )
botao_ver.place(x=330, y=221)



# Labels Quantidade total e Valores
l_total = Label(frameBody, width=14, height=2,anchor=CENTER, font=('Ivy 17 bold'), bg=Co7, fg=Co1,
relief=FLAT)
l_total.place(x=450, y=17)
l_valor_total = Label(frameBody, text=' Valor Total de todos os itens ' ,anchor=NW, font=('Ivy 10 bold'),
bg=Co7, fg=Co1)
l_valor_total.place(x=450, y=12)
l_qtd = Label(frameBody, width=10, height=2,anchor=CENTER, font=('Ivy 25 bold'), bg=Co7, fg=Co1,
relief=FLAT)
l_qtd.place(x=450, y=90)
l_qtd_itens = Label(frameBody, text='Quantidade total de itens' ,anchor=NW, font=('Ivy 10 bold'), bg=Co7,
fg=Co1)
l_qtd_itens.place(x=460, y=92)

mostrar()

janela.mainloop()