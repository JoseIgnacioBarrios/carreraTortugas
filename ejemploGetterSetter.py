class ClassconGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    def setPropiedadPrivada(self,valor):
        self.__propiedad_privada=valor
        
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    
    def propiedadPrivada(self,valor=None):
        if valor ==None:
            #Actua Como Getter
            return self.__propiedad_privada
        else:
            #Actua Como Setter
            self.__propiedad_privada=valor
        
    def __str__(self):
        return "ClassconGetterySetter con propiedad pirvada->{} ".format(self.__propiedad_privada)
        
if __name__=='__main__':
    c=ClassconGetterySetter()