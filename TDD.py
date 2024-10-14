import unittest

# Definición de la clase
class MaquinaArtesMarciales:
    def __init__(self):
        self.dificultad = 1
        self.total_golpes = 0
        self.precision = 0

    def aumentar_dificultad(self, desempeño):
        if desempeño > 80 and self.dificultad < 10:
            self.dificultad += 1
        elif desempeño < 50 and self.dificultad > 1:
            self.dificultad -= 1

    def contar_golpes(self, golpes):
        self.total_golpes += len(golpes)
        fuerza_promedio = sum(golpe['fuerza'] for golpe in golpes) / len(golpes)
        return fuerza_promedio

    def evaluar_precision(self, golpes_exitosos, golpes_totales):
        if golpes_totales == 0:
            return 0
        self.precision = (golpes_exitosos / golpes_totales) * 100
        return self.precision

    def __str__(self):
        return (f"Estado de la Máquina:\n"
                f" - Dificultad: {self.dificultad}/10\n"
                f" - Total de golpes: {self.total_golpes}\n"
                f" - Precisión actual: {self.precision:.2f}%\n")

# Definición de las pruebas unitarias
class TestMaquinaArtesMarciales(unittest.TestCase):

    def test_inicializacion(self):
        maquina = MaquinaArtesMarciales()
        self.assertEqual(maquina.dificultad, 1)
        self.assertEqual(maquina.total_golpes, 0)
        self.assertEqual(maquina.precision, 0)

    def test_aumentar_dificultad(self):
        maquina = MaquinaArtesMarciales()
        maquina.aumentar_dificultad(85)
        self.assertEqual(maquina.dificultad, 2)

        maquina.aumentar_dificultad(45)
        self.assertEqual(maquina.dificultad, 1)

    def test_contar_golpes(self):
        maquina = MaquinaArtesMarciales()
        golpes = [{'fuerza': 50}, {'fuerza': 60}, {'fuerza': 70}]
        fuerza_promedio = maquina.contar_golpes(golpes)
        self.assertEqual(maquina.total_golpes, 3)
        self.assertAlmostEqual(fuerza_promedio, 60)

    def test_evaluar_precision(self):
        maquina = MaquinaArtesMarciales()
        precision = maquina.evaluar_precision(8, 10)
        self.assertAlmostEqual(precision, 80.0)

    def test_str_method(self):
        maquina = MaquinaArtesMarciales()
        maquina.contar_golpes([{'fuerza': 50}, {'fuerza': 60}, {'fuerza': 70}])
        maquina.evaluar_precision(8, 10)
        maquina.aumentar_dificultad(85)
        estado = str(maquina)
        self.assertIn("Dificultad: 2/10", estado)
        self.assertIn("Total de golpes: 3", estado)
        self.assertIn("Precisión actual: 80.00%", estado)

# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main()

