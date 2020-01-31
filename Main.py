import regex
import calculo
import re
import matplotlib
import matplotlib.pyplot as plt
from prettytable.prettytable import PrettyTable
import numpy as np



###gráficos e afins





##ler o arquivo


files = open("C:/Users/Computador/Documents/GitHub/Projeto-ZAP/1.txt", "r", encoding="UTF-8")
f = files.readlines()
files.close()


##tratar o arquivo
calculo.organizarTxt(f)
dict_nomes = calculo.popularDictNomes(f)
grupo_variaveis = {}


##loop principal para popular as variáveis quantidade de mensagens,
##quantidade de palavras, média e quantidade de imagens
for idx, nome in enumerate(dict_nomes, 1):
    nomeTratado = regex.nomePuro(nome)
    grupo_variaveis["qtd_msg%d" % idx] = 0
    grupo_variaveis["qtd_plv%d" % idx] = 0
    grupo_variaveis["qtd_img%d" % idx] = 0
    for linha in f:
        if nomeTratado in linha:
            grupo_variaveis["qtd_msg%d" % idx] += 1
            msgPura = regex.msgPura(linha).strip()
            grupo_variaveis["qtd_plv%d" % idx] += regex.contarPalavras(msgPura)
            grupo_variaveis["qtd_img%d" % idx] += calculo.quantasImg(msgPura)
    media = round(calculo.calcularMedia(grupo_variaveis["qtd_msg%d" % idx], grupo_variaveis["qtd_plv%d" % idx] ), 2)
    grupo_variaveis["qtd_media%d" % idx] = media


##criação da tabela de output 1
zc = PrettyTable()
zc.field_names = ["Nome","Qtd Mensagens","Qtd Palavras", "Média", "Qtd imagens"]

for idx, nome in enumerate(dict_nomes, 1):
    zc.add_row([
        nome, 
        format(grupo_variaveis["qtd_msg%d" % idx], ",d"), 
        format(grupo_variaveis["qtd_plv%d" % idx], ",d"),
        grupo_variaveis["qtd_media%d" % idx], 
        format(grupo_variaveis["qtd_img%d" % idx], ",d")
        ])

print(zc)


##criação da tabela de output 2
listas = [[] for i in dict_nomes]

zx = PrettyTable()
zx.field_names = ["Msg por Hora","0", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]


for idx,nome in enumerate(dict_nomes):
    grupo_tempo = calculo.popularDictHoras(f, nome)
    for hora in grupo_tempo:
        listas[idx].append(grupo_tempo[hora])
    zx.add_row([
        nome,
        grupo_tempo["0"],
        grupo_tempo["1"],
        grupo_tempo["2"],
        grupo_tempo["3"],
        grupo_tempo["4"],
        grupo_tempo["5"],
        grupo_tempo["6"],
        grupo_tempo["7"],
        grupo_tempo["8"],
        grupo_tempo["9"],
        grupo_tempo["10"],
        grupo_tempo["11"],
        grupo_tempo["12"],
        grupo_tempo["13"],
        grupo_tempo["14"],
        grupo_tempo["15"],
        grupo_tempo["16"],
        grupo_tempo["17"],
        grupo_tempo["18"],
        grupo_tempo["19"],
        grupo_tempo["20"],
        grupo_tempo["21"],
        grupo_tempo["22"],
        grupo_tempo["23"],
    ])

print(zx)


##criação da tabela de output 3
chat = calculo.popularDictDias(f)
chat = calculo.organizarDictValor(chat)

zv = PrettyTable()
zv.field_names = ["Qtd Mensagens/Dias", "Valores"]

for idx,key in enumerate(chat):
   if (idx !=10):
       tratada = regex.diaPuro(str([key]))
       zv.add_row([tratada,chat[key]])
   else:
       break

print(zv)


##criação da tabela de output 4
dias_semana = calculo.popularDictDiasConversaSemana(f)
dias_semana = calculo.organizarDictValor(dias_semana)

zb = PrettyTable()
zb.field_names = ["Dias com mais mensagens", "Valores"]

for idx,key in enumerate(dias_semana):
    tratada = regex.diaPuroSemana(str([key]))
    zb.add_row([tratada,dias_semana[key]])

print(zb)


##criação da tabela de output 5
dias_mes = calculo.popularDictDiasConversaMes(f)
dias_mes = calculo.organizarDictValor(dias_mes)

zn = PrettyTable()
zn.field_names = ["Mês com mais mensagens", "Valores"]

for idx,key in enumerate(dias_mes):
    tratada = regex.diaPuroSemana(str([key]))
    zn.add_row([tratada,dias_mes[key]])

print(zn)


##criação da tabela de output 6
palavras_mais_usadas = calculo.popularDictPalavrasMaisUsadas(f)
palavras_mais_usadas = calculo.organizarDictValor(palavras_mais_usadas)

zm = PrettyTable()
zm.field_names = ["Palavras mais usadas", "Valores"]

for idx,key in enumerate(palavras_mais_usadas):
   if (idx != 50):
      if (key != "<Media" and key != "Omitted>"):
         tratada = regex.diaPuroSemana(str([key]))
         zm.add_row([tratada,palavras_mais_usadas[key]])
   else:
      break


print(zm)

"""
labels = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
men_means = [20, 34, 30, 35, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27]
women_means = [25, 32, 34, 20, 25, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
   
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
=======

>>>>>>> d5abd46732b3fb778f17d9febbeec6e371dee215





"""
