import nltk


nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import regexp_tokenize
from nltk.stem import SnowballStemmer
import re

#Texto de entrada

texto = """
Este es un ejemplo de texto que contiene algunos caracteres especiales, números y palabras en mayúsculas. Queremos preprocesar este texto para que esté listo para el análisis de texto en un proyecto de Procesamiento de Lenguaje Natural (NLP).
"""

#Eliminación de caracteres especiales y números

texto_limpio=re.sub(r'[^a-zA-Z\s]', '', texto)

#minúsculas

texto_limpio=texto_limpio.lower()

#Tokenización se uso regexp_tokenize

tokens=regexp_tokenize(texto_limpio, pattern=r'\s+', gaps=True)

#Eliminación de stopwords

stop_words=set(stopwords.words('spanish'))
tokens_filtrados=[word for word in tokens if word not in stop_words]

#Stemming utilizando SnowballStemmer para español

stemmer=SnowballStemmer('spanish')
tokens_stemmed=[stemmer.stem(word) for word in tokens_filtrados]

print(tokens_stemmed)
