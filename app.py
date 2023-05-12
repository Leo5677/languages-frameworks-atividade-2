from tkinter import *

# CLASSE PARA RECEBER O OBJETO TKINTER
class AplicacaoTkInter:
  # CONSTRUCT DA APLICAÇÃO
  def __init__(self, master=None):
    # CONTAINER PARA O TÍTULO
    self.container_titulo = Frame(master)
    self.container_titulo["pady"] = 10
    self.container_titulo.pack()
    
    # TÍTULO
    self.titulo = Label(self.container_titulo, text="IMC", font=("Arial", "12", "bold"))
    self.titulo.pack()

    # CONTAINER PARA ALTURA
    self.container_altura = Frame(master)
    self.container_altura["pady"] = 10
    self.container_altura.pack()
    
    # LABEL/INPUT PARA ALTURA
    self.label_altura = Label(self.container_altura, text="Altura")
    self.label_altura.pack(side=TOP)
    self.input_altura = Entry(self.container_altura, width=20)
    self.input_altura.pack()
    
    # CONTAINER PARA PESO
    self.container_peso = Frame(master)
    self.container_peso["pady"] = 10
    self.container_peso.pack()
    
    # LABEL/INPUT PARA PESO
    self.label_peso = Label(self.container_peso, text="Peso")
    self.label_peso.pack(side=TOP)
    self.input_peso = Entry(self.container_peso, width=20)
    self.input_peso.pack()
    
    # CONTAINER PARA O BOTÃO
    self.container_botao = Frame(master)
    self.container_botao["pady"] = 10
    self.container_botao.pack()
    
    # BOTÃO PARA CALCULAR IMC
    self.botao_calcular = Button(
      self.container_botao, 
      text="Calcular", 
      borderwidth=1, 
      width=10,
      command=self.calcularIMC
    )
    self.botao_calcular.pack() 
    
    # CONTAINER PARA APRESENTAR O RESULTADO DO IMC
    self.container_mensagem = Frame(master)
    self.container_mensagem["pady"] = 10
    self.container_mensagem.pack()
    
    # RESULTADO DO IMC
    self.mensagem = Label(self.container_mensagem, text="")
    self.mensagem.pack(side=TOP)

  # VERIFICA SE O VALOR DIGITADO NÃO É UMA STRING
  def verificarValor(self):
    try:  
      float(self.input_altura.get().replace(",", "."))
      float(self.input_peso.get().replace(",", "."))
      return True
    except ValueError:
      return False
                
  # REALIZA O CÁLCULO DO IMC
  def calcularIMC(self):
    # VERIFICA O VALOR DIGITADO
    if self.verificarValor(): 
      altura = float(self.input_altura.get().replace(",", "."))
      peso = float(self.input_peso.get().replace(",", "."))
      imc = float("{:.2f}".format(peso / (altura ** 2)))
      
      # CATEGORIZA O IMC
      if(imc < 18.5): 
        imc_categoria = "Magreza"
      elif (imc >= 18.5 and imc <= 24.9): 
        imc_categoria = "Normal"
      elif (imc >= 24.9 and imc <= 30):
        imc_categoria = "Sobrepeso"
      else :
        imc_categoria = "Obesidade"
        
      # APRESENTA A MENSAGEM
      self.mensagem["text"] = f'{imc_categoria} -> Seu IMC é de: {imc}'
    else:
      self.mensagem["text"] = "Por favor, digite uma altura e/ou peso válido(s)."
    
# INICIA A APLICAÇÃO
aplicacao = Tk()
AplicacaoTkInter(aplicacao)

# MANTÉM A APLICAÇÃO EM LOOP
aplicacao.mainloop()
