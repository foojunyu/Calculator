"""
Test script for calculator functionality
"""
import unittest
import tkinter as tk
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.root = tk.Tk()
        self.calc = Calculator(self.root)
    
    def tearDown(self):
        """Tear down test fixtures"""
        self.root.destroy()
    
    def test_calculator_initialization(self):
        """Test that calculator initializes correctly"""
        self.assertIsNotNone(self.calc)
        self.assertEqual(self.calc.current_theme, 'light')
        self.assertEqual(self.calc.display.get(), '0')
    
    def test_themes_exist(self):
        """Test that both themes are defined"""
        self.assertIn('light', self.calc.themes)
        self.assertIn('dark', self.calc.themes)
    
    def test_theme_switching(self):
        """Test theme switching functionality"""
        # Start with light theme
        self.assertEqual(self.calc.current_theme, 'light')
        
        # Switch to dark theme
        self.calc.switch_theme('dark')
        self.assertEqual(self.calc.current_theme, 'dark')
        
        # Switch back to light theme
        self.calc.switch_theme('light')
        self.assertEqual(self.calc.current_theme, 'light')
    
    def test_number_input(self):
        """Test number button clicks"""
        self.calc.on_button_click('1')
        self.assertEqual(self.calc.display.get(), '1')
        
        self.calc.on_button_click('2')
        self.assertEqual(self.calc.display.get(), '12')
        
        self.calc.on_button_click('3')
        self.assertEqual(self.calc.display.get(), '123')
    
    def test_clear_button(self):
        """Test clear functionality"""
        self.calc.on_button_click('1')
        self.calc.on_button_click('2')
        self.calc.on_button_click('3')
        self.calc.on_button_click('C')
        self.assertEqual(self.calc.display.get(), '0')
    
    def test_backspace(self):
        """Test backspace functionality"""
        self.calc.on_button_click('1')
        self.calc.on_button_click('2')
        self.calc.on_button_click('3')
        self.calc.on_button_click('⌫')
        self.assertEqual(self.calc.display.get(), '12')
    
    def test_sign_toggle(self):
        """Test sign toggle functionality"""
        self.calc.on_button_click('5')
        self.calc.on_button_click('±')
        self.assertEqual(self.calc.display.get(), '-5')
        
        self.calc.on_button_click('±')
        self.assertEqual(self.calc.display.get(), '5')
    
    def test_basic_addition(self):
        """Test addition calculation"""
        self.calc.on_button_click('2')
        self.calc.on_button_click('+')
        self.calc.on_button_click('3')
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.display.get(), '5')
    
    def test_basic_subtraction(self):
        """Test subtraction calculation"""
        self.calc.on_button_click('5')
        self.calc.on_button_click('-')
        self.calc.on_button_click('3')
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.display.get(), '2')
    
    def test_basic_multiplication(self):
        """Test multiplication calculation"""
        self.calc.on_button_click('4')
        self.calc.on_button_click('*')
        self.calc.on_button_click('3')
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.display.get(), '12')
    
    def test_basic_division(self):
        """Test division calculation"""
        self.calc.on_button_click('8')
        self.calc.on_button_click('/')
        self.calc.on_button_click('2')
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.display.get(), '4.0')
    
    def test_decimal_numbers(self):
        """Test decimal number input"""
        self.calc.on_button_click('3')
        self.calc.on_button_click('.')
        self.calc.on_button_click('1')
        self.calc.on_button_click('4')
        self.assertEqual(self.calc.display.get(), '3.14')
    
    def test_percentage(self):
        """Test percentage button"""
        self.calc.on_button_click('5')
        self.calc.on_button_click('0')
        self.calc.on_button_click('%')
        # Just verify it adds the % symbol
        self.assertIn('%', self.calc.display.get())


if __name__ == '__main__':
    unittest.main()
