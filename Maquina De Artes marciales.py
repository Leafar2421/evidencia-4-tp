class MaquinaArtesMarciales:
    def __init__(self):
        self.dificultad = 1  # Nivel de dificultad inicial
        self.total_golpes = 0  # Contador de golpes
        self.precision = 0  # Precisión inicial

    # Método para aumentar o disminuir la dificultad en base al desempeño
    def aumentar_dificultad(self, desempeño):
        if desempeño > 80 and self.dificultad < 10:  # Si el desempeño es alto, sube la dificultad
            self.dificultad += 1
        elif desempeño < 50 and self.dificultad > 1:  # Si el desempeño es bajo, baja la dificultad
            self.dificultad -= 1

    # Método para contar golpes y calcular la fuerza promedio
    def contar_golpes(self, golpes):
        self.total_golpes += len(golpes)
        fuerza_promedio = sum(golpe['fuerza'] for golpe in golpes) / len(golpes)
        return fuerza_promedio

    # Método para evaluar la precisión del usuario
    def evaluar_precision(self, golpes_exitosos, golpes_totales):
        if golpes_totales == 0:
            return 0  # Evita la división entre 0
        self.precision = (golpes_exitosos / golpes_totales) * 100
        return self.precision

    # Método especial __str__ para mostrar el estado actual de la máquina
    def __str__(self):
        return (f"Estado de la Máquina:\n"
                f" - Dificultad: {self.dificultad}/10\n"
                f" - Total de golpes: {self.total_golpes}\n"
                f" - Precisión actual: {self.precision:.2f}%\n")

maquina = MaquinaArtesMarciales()


maquina.contar_golpes([{'fuerza': 50}, {'fuerza': 60}, {'fuerza': 70}])
maquina.evaluar_precision(8, 10)
maquina.aumentar_dificultad(85)

print(maquina)