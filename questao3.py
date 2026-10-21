from abc import ABC, abstractmethod
class Entrega(ABC) :
    def __init__(self,codigo):
        self.codigo = codigo
    @abstractmethod
    def informar_prazo(self) :
        pass

    def mostrar_codigo(self):
        print(f'codigo :{self.codigo}')

            
class EntregaComum(Entrega):
    def informar_prazo(self):
        print('Prazo: 5 dias')

class EntregaExpressa(Entrega):
    def informar_prazo(self):
        print ('Prazo: 2 dias')

# Bloco principal
entrega1 = EntregaComum("E001")
entrega2 = EntregaExpressa("002")
entrega1.mostrar_codigo()
entrega1.informar_prazo()
entrega2.mostrar_codigo()
entrega2.informar_prazo()
                                


  