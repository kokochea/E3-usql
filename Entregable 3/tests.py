import unittest
from ESP_ENG import parser, lexer

class TestParser(unittest.TestCase):
    def setUp(self):
        self.lexer = lexer
        self.parser = parser

    def test_select_query(self):
        result = self.parser.parse("TRAEME TODO DE LA TABLA usuarios DONDE edad > 18")
        self.assertEqual(result, "SELECT * FROM usuarios WHERE edad > 18")

    def test_insert_query(self):
        result = self.parser.parse("METE EN usuarios (nombre, edad) LOS VALORES ('Alice', 30)")
        self.assertEqual(result, "INSERT INTO usuarios (nombre, edad) VALUES ('Alice', 30)")

    def test_update_query(self):
        result = self.parser.parse("ACTUALIZA usuarios SETEA edad = 35 DONDE nombre = 'Alice'")
        self.assertEqual(result, "UPDATE usuarios SET edad = 35 WHERE nombre = 'Alice'")

    def test_delete_query(self):
        result = self.parser.parse("BORRA DE LA usuarios DONDE edad > 18")
        self.assertEqual(result, "DELETE FROM usuarios WHERE edad > 18")

    def test_alter_add_column_query(self):
        result = self.parser.parse("CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO")
        self.assertEqual(result, "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL")

    def test_invalid_query(self):
        with self.assertRaises(SyntaxError):
            self.parser.parse("INVALID COMMAND")

if __name__ == '__main__':
    unittest.main()
