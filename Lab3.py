

import sys 

print "El rango del valor tiene que estar en el rango de 0 y 1"
x = str(raw_input("INGRESE VALOR:"))

pr = sys.stdout.write

class MachineTapeException(Exception):
    """ EXCEPCION DE MAQUINA DE TURING """
    def __init__(self,value):
            Exception.__init__(self)
            self.value = value
    def __str__(self):
            return self.value

class ErrorException(Exception):
    """ ERROR DE EXCEPCION DE MAQUINA DE TURING """ 
    def __str__(self):
            return "EL VALOR NO ESTA DENTRO DEL RENGO"

class AcceptException(Exception):
    "ACEPTACION DE EXCEPCION DE MAQUINA DE TURING"
    def __str__(self):
            return "VALORES CAMBIADOS TOTALMENTE"


# clase de la cinta
class MTape:
        def __init__(self, initialString=[], initialPos=0, blank= "_"):
            """ THE Tape uses a simple list. it could casily be changed into a string if need be """
            self.tape = []
            self.pos = initialPos
            self.blank = blank
            self.initialString = initialString
            if int(initialString) > 0:
                for ch in initialString:
                        self.tape.append(ch)
            else:
                self.tape.append(blank)

        def reinit(self):
                 self.__init__(self.initialString)

        def mover(self, check_char, changeto_char, direction):
                """ Solo se admiten direcciones R,L """

                if check_char != self.tape[self.pos]:
                        raise MachineTapeException (" Tapa head doesn't natch head character")

                self.tape[self.pos] = changeto_char

                if direction == "L":
                        self.mover_izquierda()
                elif direction == "R":
                        self.mover_derecha()
                else: raise MachineTapeException ("LA DIRECCION ES INVALIDAD")

        def leer(self):
            """ DEVOLVER LA CINTA SOBRE LA CABEZA DE LA MAQUINA """
            return self.tape[self.pos]

        def mover_izquierda(self):
                if self.pos <= 0:
                        self.tape.insert(-1, self.blank)
                        self.pos = 0
                else:
                        self.pos += -1

        def mover_derecha(self):
                self.pos += 1
                if self.pos >= len(self.tape): self.tape.append(self.blank)


        def show(self):
            """ IMPRIME LA CINTA """
            for ch in self.tape:
                pr(ch)
            pr("\n"); pr(" "*self.pos + "^"); pr("\n")



class MaquinaTuring:
        def __init__(self, initialString, finalStates=[], blank="_"):
                 self.blank = blank
                 self.tape = MTape(initialString)
                 self.fstates = finalStates
                 self.program = {}
                 self.initState = 0
                 self.state = self.initState
                 self.lenStr = len(initialString)

        def reinit(self):
                 self.state = selft.initState
                 self.tape.reinit()

        def addTransition(self, state, char_in, dest_state, char_out, movement):
                 if not self.program.has_key(state):
                        self.program[state] = {}

                 top = (dest_state, char_out, movement)
                 self.program[state][char_in] = top
    
        def pasos(self):
                 """ PASO 1 Y 3 """
                 if self.lenStr == 0 and self.state in self.fstates: raise AcceptException
                 if self.state in self.fstates: raise AcceptException
                 if self.state not in self.program.keys(): raise ErrorException

                 """ PASO 4 Y 5 """

                 head = self.tape.leer()
                 if head not in self.program[self.state].keys(): raise AcceptException


                 """ PASO 6 Y 7 """
                 # Ejecicion de transicion 
                 (dest_state, char_out, movement) = self.program[self.state][head]
                 self.state = dest_state
                 try:
                          """ PASO 8 """
                          self.tape.mover(head, char_out, movement)
                 except MachineTapeException, s:
                            print "Error1"

        def execute(self):
                 """ LA MAQUINA SEGUIRA CAMINANDO POR SIEMPRE HASTA QUE LA MAQUINA ACEPTE O RECHACE. ESTO PERMITE LOS BUCLE """ 
                
                 try:
                         while 1:
                                 x.tape.show()
                                 x.pasos()
                 except  (ErrorException, AcceptException), s:
                         print "Error2"


print "****************************************************"
print "* MAQUINA DE TURING, MODIFICA LOS VALORES DE 0 A 1 *"
print "****************************************************"
print ""

if __name__ == "__main__":
    x = MaquinaTuring(x, [1])

    x.addTransition(0,'1',0,'1','R')
    x.addTransition(0,'1',0,'1','R')
    x.addTransition(0,'_',1,'_','L')

    x.execute()


