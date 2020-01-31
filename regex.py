import re

def contarPalavras(x):
    c = re.split(r"\s",x)
    return(len(c))

def palavrasSeparadas(x):
    c = re.split(r"\s",x)
    return c

def nomesConversa(x):
    c = re.search(r"(?=-).+?(?=:)",x)
    if c is not None:
        z = re.sub(r"(?:-)\s","", c.group())
        return z

def dataHoraNome(x):
    c = re.search(r"(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\w+)(\s)(-)(\s\w+)*(\s?\W?\d?)(:)(\s)",x)
    return c

def msgPura(x):
    y = re.sub(r"(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\w+)(\s)(-)(\s\w+)*(\s?\W?\d?)(:)(\s)", "",x)
    return y

def horaPura(x):
    y = re.search(r"(\d){2}:(\d){2}\s-\s", x)
    #se não for uma mensagem com quebra de linha
    if (y is not None):
        z = re.search(r"(\d){2}:(\d){2}", y.group())
        return z.group()
    else:
        pass

def diaPuro(x):
    y = re.search(r"(\d)?(\d)/(\d)?(\d)/(\d)?(\d)",x)
    #se não for uma mensagem com quebra de linha
    if (y is not None):
        return y.group()
    else:
        pass

def diaPuroSemana(x):
    y = re.search(r"(\w)+",x)
    #se não for uma mensagem com quebra de linha
    if (y is not None):
        return y.group()
    else:
        pass

def nomePuro(dict_nome):
    y = re.search(r"(\w+)*(\s?\W?\d?)+",dict_nome)
    return y.group()

