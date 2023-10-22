class LogicaPorDefecto:
    def __init__(self):
        self.creencias = {"Los p�jaros vuelan"}
        self.excepciones = set()

    def agregar_creencia(self, creencia):
        self.creencias.add(creencia)

    def agregar_excepcion(self, excepcion):
        self.excepciones.add(excepcion)

    def verificar(self, creencia):
        if creencia in self.excepciones:
            return False
        return creencia in self.creencias
# Crear una instancia de l�gica por defecto
sistema = LogicaPorDefecto()
# Verificar la creencia por defecto
print("�Los p�jaros vuelan? (Por defecto):", sistema.verificar("Los p�jaros vuelan"))
# Agregar una excepci�n: los ping�inos no vuelan
sistema.agregar_excepcion("Los ping�inos no vuelan")
# Verificar la creencia nuevamente
print("�Los p�jaros vuelan? (Despu�s de agregar excepci�n):", sistema.verificar("Los p�jaros vuelan"))
print("�Los ping�inos vuelan? (Despu�s de agregar excepci�n):", sistema.verificar("Los ping�inos vuelan"))
# Agregar una nueva creencia: evidencia de que los avestruces no vuelan
sistema.agregar_creencia("Los avestruces no vuelan")
# Verificar nuevamente la creencia por defecto
print("�Los p�jaros vuelan? (Despu�s de agregar creencia):", sistema.verificar("Los p�jaros vuelan"))
