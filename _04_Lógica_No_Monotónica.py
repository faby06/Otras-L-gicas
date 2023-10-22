
class LogicaNoMonotona:
    def __init__(self):
        self.creencias = set()
        self.excepciones = set()

    def agregar_creencia(self, creencia):
        self.creencias.add(creencia)

    def agregar_excepcion(self, excepcion):
        self.excepciones.add(excepcion)

    def verificar(self, creencia):
        if creencia in self.excepciones:
            return False
        return creencia in self.creencias

# Crear una instancia de l�gica no mon�tona
sistema = LogicaNoMonotona()

# Inicialmente, creemos que "los p�jaros vuelan"
sistema.agregar_creencia("Los p�jaros vuelan")

# Verificar la creencia
print("�Los p�jaros vuelan? (Creencia inicial):", sistema.verificar("Los p�jaros vuelan"))

# Agregar una excepci�n: los ping�inos no vuelan
sistema.agregar_excepcion("Los ping�inos no vuelan")

# Verificar la creencia nuevamente
print("�Los p�jaros vuelan? (Despu�s de agregar excepci�n):", sistema.verificar("Los p�jaros vuelan"))
print("�Los ping�inos vuelan? (Despu�s de agregar excepci�n):", sistema.verificar("Los ping�inos vuelan"))