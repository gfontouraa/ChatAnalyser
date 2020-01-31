import regex
import re
from datetime import datetime, date

dict_dias = ["","Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
dict_mes = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def calcularMedia(msg,plv):
    media = plv/msg
    return media


def quantasImg(msg):
     mediaTeste = "<Media omitted>"
     if (msg == mediaTeste):
           return 1
     else:
          return 0


##organizar dict por valor
def organizarDictValor(dict):
    dict_organizado = {k: v for k, v in sorted(dict.items(),reverse=True, key=lambda x: x[1])}
    return dict_organizado

##retirar a primeira mensagem de criptografia
def organizarTxt(f):
    teste = "Messages to this chat and calls are now secured with end-to-end encryption."
    if teste in f[0]:
        f.remove(f[0])
    ##testar se há quebra de linha, se há adicionar o timestamp da mensagem de cima    
    for idx,x in enumerate(f):
        y = regex.dataHoraNome(x)
        z = regex.msgPura(x)
        if y is None:
            linha = f[idx-1]
            y = regex.dataHoraNome(linha)
            c = y.group() + z
            f.remove(f[idx])
            f.insert(idx, c)
    return f


##métodos de tratar data
def organizarData(data):
    if (data is not None):
        data = datetime.strptime(data, "%m/%d/%y")
        data = datetime.strftime(data, "%d/%m/%y")
        return data


def organizarDataSemana(data):
    if (data is not None):
        data = datetime.strptime(data, "%m/%d/%y")
        dia = data.isoweekday()  
        return dict_dias[dia]


def organizarDataMes(data):
    if (data is not None):
        data = datetime.strptime(data, "%m/%d/%y")
        data = datetime.strftime(data, "%m")
        return dict_mes[int(data)]


##métodos para popular dict
def popularDictHoras(f, nome):
    grupo_tempo = {}
    for i in range(24):
        grupo_tempo[str(i)] = 0
    for x in f:
        y = regex.horaPura(x)
        if nome in x:
            hora_atual = int(y.split(":")[0])   
            hora_atual = str(hora_atual)
            grupo_tempo[hora_atual] += 1
    return grupo_tempo


def popularDictDias(f):
    dias = {}
    for x in f:
        y = regex.diaPuro(x)
        y = organizarData(y)
        if y not in dias:
            dias[y] = 0
        dias[y] += 1
    return dias


def popularDictDiasConversaSemana(f):
    dias_semana = {}
    for x in f:
        y = regex.diaPuro(x)
        y = organizarDataSemana(y)
        if y not in dias_semana:
            dias_semana[y] = 0
        dias_semana[y] += 1
    return dias_semana


def popularDictDiasConversaMes(f):
    dias_mes = {}
    for x in f:
        y = regex.diaPuro(x)
        y = organizarDataMes(y)
        if y not in dias_mes:
            dias_mes[y] = 0
        dias_mes[y] += 1
    return dias_mes


def popularDictNomes(f):
    grupo_nome = {}
    for x in f:
        y = regex.nomesConversa(x)
        if y not in grupo_nome:
            grupo_nome[y] = 0
        grupo_nome[y] += 1    
    return grupo_nome


def popularDictPalavrasMaisUsadas(f):
    palavras_mais_usadas = {}
    for x in f:
        y = regex.msgPura(x)
        y = regex.palavrasSeparadas(y)
        for z in y:    
            z = z.title()
            if len(z) >= 4:    
                if z not in palavras_mais_usadas:
                    palavras_mais_usadas[z] = 1
                else:
                    palavras_mais_usadas[z] += 1
    return palavras_mais_usadas
