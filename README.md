# Práctica 1 - Tipologia y ciclo de vida de los datos (Web Scrapping)
El objetivo que persigue la práctica es generar un dataset a partir de un sitio web. En el proyecto han participado:
- Rafael Jimenez Sarmentero
- Jorge Marchán Gutiérrez

## Estructura del proyecto
El fichero principal que tendremos que lanzar con el CLI es `main.py`, el resto del codigo de la aplicación lo podemos encontrar dentro del directorio `src`, en este directorio encontramos dos subdirectorios, `scrappers` y `utils`, el primero de ellos contiene los diferentes *scrappers*, el de la búsqueda y el del detalle del alojamiento. Y en el directorio de `utils` encontramos un fichero que contiene la funcion para pasar de una lista de diccionarios a csv.

## DOI.z del fichero generado
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6408120.svg)](https://doi.org/10.5281/zenodo.6408120)

## Memoría de la práctica
La memoría de la práctica la podéis encontrar en el fichero `PRA1.pdf`

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
