# Práctica 1 - Tipologia y ciclo de vida de los datos (Web Scrapping)
El objetivo que persigue la práctica es generar un dataset a partir de un sitio web. En el proyecto han participado:
- Rafael Jimenez
- Jorge Marchán

## Requisitos
Primero necesitaremos instalar las dependencias de la aplicación
```python
pip install -r requirements.txt
```

Una parte del scrapper está desarrollado con Selenium, en el proyecto encontramos los ficheros `chromedriver` correspondientes para nuestros sistemas operativos, para otro caso habrá que descargar el fichero correspondiente de [aquí](https://chromedriver.chromium.org/downloads)

## Puesta en marcha
Se trata de una aplicación CLI que acepta varios parámetros, los más interesantes son el número de páginas de resultados a tratar y el término de búsqueda, el comando con el que se ha empezado a desarrollar es el siguiente:
```python
# Scrapper de las tres primeras páginas de la búsqueda sobre madrid (modo Headless)
python main.py -p 3 -s madrid -H
```
