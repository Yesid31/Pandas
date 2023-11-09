import pandas as pd
def llenarDic():
    Estudiantes ={
        'identifiacion':[123],
        'apellido':['Gil'],
        'Nombre':['Paco']
    }
    df= pd.DataFrame(Estudiantes)


def llenarDicModulos():
    pass

def CargarCsv():
    df=pd.read_csv('DatosEstudiantes.csv')
    #print(df)
    print(df.head(5))


if __name__ == '__main__':
    CargarCsv()


