import requests
import pandas as pd
from bs4 import BeautifulSoup

#Descargar la página web
url='https://ingdanielbs.github.io/Datos/'
response=requests.get(url)

#Analizar la pagina con BeutifulSoup
soup=BeautifulSoup(response.content,"html.parser")

#Encontrar la tabla en el html
tabla=soup.find("table")

if tabla is not None:
    rows=tabla.find_all("tr")
    data=[]
    for row in rows:
        cols=row.find_all("td")
        cols=[col.text.strip() for col in cols]
        data.append(cols)
    
    #Convertir los datos en dataframe de panda
    df=pd.DataFrame(data, columns=["Documento", "Nombre", "Apellidos", "Dirección", "Teléfono", "Edad", "Estatura"])

    #Escribir el dataframe en un archivo de excel
    df.to_excel("Datossena.xlsx", index=False)

else:
    print("La tabla no fue encontrada")