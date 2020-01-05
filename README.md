# Prueba Tecnica

prueba tecnica

clonar el repositorio:

```
git clone https://github.com/Mexarm/prueba_tecnica.git
```
# ejercicio 1

el codigo de la funcion solicitada se encuentra en el archivo ejercicio1/script.py

```
def get_greatest(str_val, length):
    lst = []
    for i in range(len(str_val)-length+1):
        lst.append(int(str_val[i:i+length]))
    return max(lst)
```

para realizar las pruebas unitarias ejecutar

```
cd ejercicio1/
python3.6 test.py
```

se obtiene lo siguiente:

```
$ python3.6 test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

correr los ejemplos:

```
$ python3.6 example.py
```

se obtiene lo siguiente:

```
get_gratest('283910',2) => 91
get_gratest('1234567890',5) => 67890
```

# ejercicio 2

aplicacion web para obtener las siguientes series de datos:

- Valor de UDIS
- Tipo de cambio Pesos por dólar E.U.A.
- TIIE a 28 días
- TIIE a 91 días
- TIIE a 182 días

el codigo de la aplicacion se encuentra disponible en el directorio [ejercicio2/](https://github.com/Mexarm/prueba_tecnica/tree/master/ejercicio2)

se puede usar la aplicacion aqui

http://prueba.herzudigital.com

o bien:

http://45.79.46.89

uso:

- Seleccionar la serie que se quiere visualizar
- seleccionar la fecha inicial
- seleccional la fecha final
- click en el boton "Consultar"

para ejecutar localmente la aplicacion debe contar con python 3.6 o 3.7 y pipenv y realizar lo siguiente:

```
$cd ejercicio2/
$pipenv install
$pipenv run python manage.py migrate
$pipenv run python manage.py runserver
```