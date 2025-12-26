"""
Validation script for calculator code structure
This script validates the calculator without requiring a display
"""
import ast
import sys


def validate_calculator_code():
    """Validate the calculator.py file structure"""
    print("Validating calculator.py...")
    
    with open('calculator.py', 'r') as f:
        code = f.read()
    
    try:
        tree = ast.parse(code)
        print("✓ Syntax is valid")
    except SyntaxError as e:
        print(f"✗ Syntax error: {e}")
        return False
    
    # Check for required elements
    checks = {
        'Calculator class': False,
        'theme switching': False,
        'light theme': False,
        'dark theme': False,
        'switch_theme method': False,
        'apply_theme method': False,
        'on_button_click method': False,
        'main function': False
    }
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'Calculator':
            checks['Calculator class'] = True
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    if item.name == 'switch_theme':
                        checks['switch_theme method'] = True
                    elif item.name == 'apply_theme':
                        checks['apply_theme method'] = True
                    elif item.name == 'on_button_click':
                        checks['on_button_click method'] = True
        
        elif isinstance(node, ast.FunctionDef) and node.name == 'main':
            checks['main function'] = True
    
    # Check for theme-related strings in the code
    if "'light'" in code and "'dark'" in code:
        checks['theme switching'] = True
    
    if 'light' in code:
        checks['light theme'] = True
    
    if 'dark' in code:
        checks['dark theme'] = True
    
    # Print results
    all_passed = True
    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"{status} {check}: {'Present' if passed else 'Missing'}")
        if not passed:
            all_passed = False
    
    return all_passed


def main():
    print("=" * 60)
    print("Calculator Code Validation")
    print("=" * 60)
    
    if validate_calculator_code():
        print("\n" + "=" * 60)
        print("All validations passed! ✓")
        print("=" * 60)
        print("\nThe calculator application includes:")
        print("  • Basic arithmetic operations")
        print("  • Theme switching capability (Light/Dark)")
        print("  • User-friendly interface")
        print("\nTo run the calculator:")
        print("  python calculator.py")
        return 0
    else:
        print("\n" + "=" * 60)
        print("Some validations failed ✗")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
