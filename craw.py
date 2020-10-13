import urllib.request
#"https://rj.olx.com.br/autos-e-pecas"

content=urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content=str(content)
find= '<input type="hidden" value='
posicao=int(content.index(find)+ len(find))
dolar=content[posicao:posicao + 4]

content=urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
content=str(content)
posicao=int(content.index(find)+ len(find))
euro=content[posicao:posicao + 4]


print("Dolar: " +dolar)
print("Euro:" +euro)