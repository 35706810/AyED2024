import unittest
from datetime import datetime
from modules.Arbol_AVL import Arbol_AVL  
from modules.Temperaturas_DB import TemperaturasDB 

class TestTemperaturasDB(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.db = TemperaturasDB()

    def test_guardar_y_devolver_temperatura(self):
        """Prueba guardar y devolver temperatura."""
        self.db.guardar_temperatura(23.5, "01/01/2023")
        temperatura = self.db.devolver_temperatura("01/01/2023")
        self.assertEqual(temperatura, 23.5)

    def test_max_temp_rango(self):
        """Prueba para obtener la temperatura máxima en un rango."""
        self.db.guardar_temperatura(20.0, "01/01/2023")
        self.db.guardar_temperatura(25.5, "02/01/2023")
        self.db.guardar_temperatura(22.3, "03/01/2023")
        max_temp = self.db.max_temp_rango("01/01/2023", "03/01/2023")
        self.assertEqual(max_temp, 25.5)

    def test_min_temp_rango(self):
        """Prueba para obtener la temperatura mínima en un rango."""
        self.db.guardar_temperatura(20.0, "01/01/2023")
        self.db.guardar_temperatura(25.5, "02/01/2023")
        self.db.guardar_temperatura(22.3, "03/01/2023")
        min_temp = self.db.min_temp_rango("01/01/2023", "03/01/2023")
        self.assertEqual(min_temp, 20.0)

    def test_temp_extremos_rango(self):
        """Prueba para obtener temperaturas extremas en un rango."""
        self.db.guardar_temperatura(20.0, "01/01/2023")
        self.db.guardar_temperatura(25.5, "02/01/2023")
        self.db.guardar_temperatura(22.3, "03/01/2023")
        min_temp, max_temp = self.db.temp_extremos_rango("01/01/2023", "03/01/2023")
        self.assertEqual(min_temp, 20.0)
        self.assertEqual(max_temp, 25.5)

    def test_borrar_temperatura(self):
        """Prueba para borrar una temperatura y asegurarse que no está disponible."""
        self.db.guardar_temperatura(23.5, "01/01/2023")
        self.db.borrar_temperatura("01/01/2023")
        temperatura = self.db.devolver_temperatura("01/01/2023")
        self.assertIsNone(temperatura)

    def test_devolver_temperaturas(self):
        """Prueba para devolver todas las temperaturas en un rango específico."""
        self.db.guardar_temperatura(20.0, "01/01/2023")
        self.db.guardar_temperatura(25.5, "02/01/2023")
        self.db.guardar_temperatura(22.3, "03/01/2023")
        temperaturas = self.db.devolver_temperaturas("01/01/2023", "03/01/2023")
        self.assertIn("01/01/2023: 20.0 ºC", temperaturas)
        self.assertIn("02/01/2023: 25.5 ºC", temperaturas)
        self.assertIn("03/01/2023: 22.3 ºC", temperaturas)

    def test_cantidad_muestras(self):
        """Prueba para verificar la cantidad de muestras guardadas."""
        self.db.guardar_temperatura(23.5, "01/01/2023")
        self.db.guardar_temperatura(20.0, "02/01/2023")
        self.assertEqual(self.db.cantidad_muestras(), 2)

if __name__ == "__main__":
    unittest.main()
