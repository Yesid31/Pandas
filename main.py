import pandas as pd


def llenarDataF():
    print ('Creando un Data Frame De Pandas')

    datosEstu={
        'identificacion':[123,124,125],
        'nombre':['Diego','German','Santiago'],
        'edad':[19,25,21]
    }

    df=pd.DataFrame(datosEstu)
    print(df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    llenarDataF()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
