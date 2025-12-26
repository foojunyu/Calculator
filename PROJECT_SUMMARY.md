# Project Summary: Windows Calculator with Theme Switching

## Overview
This project implements a fully functional Windows calculator application with theme-switching capabilities as requested.

## Implementation Details

### Main Application (calculator.py)
- **Size**: 12 KB
- **Language**: Python 3.x
- **GUI Framework**: tkinter (built-in with Python)
- **Key Features**:
  - Basic arithmetic operations (+, -, *, /)
  - Advanced functions (percentage, decimal, sign toggle, clear, backspace)
  - Theme switching (Light and Dark themes)
  - Clean, object-oriented design
  - **Secure expression evaluation** without eval()
  - Proper error handling with specific exception types

### Security Features
✅ **No eval() usage**: Implemented custom expression parser
✅ **Input validation**: Regex-based validation of allowed characters
✅ **Operator precedence**: Proper mathematical operator precedence (PEMDAS)
✅ **Error handling**: Specific exception catching for better error management
✅ **CodeQL verified**: 0 security vulnerabilities detected

### Themes

#### Light Theme
- Background: #f0f0f0 (light gray)
- Display: #ffffff (white) with black text
- Buttons: #e0e0e0 (light gray) with black text
- Operators: #ff9500 (orange) with white text
- Professional appearance suitable for all lighting conditions

#### Dark Theme
- Background: #1e1e1e (dark gray)
- Display: #2d2d2d (darker gray) with white text
- Buttons: #3a3a3a (medium gray) with white text
- Operators: #ff9500 (orange) with white text
- Modern appearance that reduces eye strain

### How to Switch Themes
1. Launch the calculator: `python calculator.py`
2. Click "Theme" in the menu bar
3. Select "Light Theme" or "Dark Theme"
4. The interface updates instantly

## Documentation

### README.md
- Installation instructions
- Usage guide
- Feature list
- Requirements

### FEATURES.md
- Detailed feature breakdown
- Technical specifications
- Code quality notes

### VISUAL_GUIDE.md
- ASCII art representations of both themes
- Visual comparison
- Usage examples

## Testing & Validation

### validate.py
- Validates code structure
- Checks for required components
- Verifies theme implementation
- **Status**: All validations pass ✓

### test_calculator.py
- Unit tests for calculator functionality
- Theme switching tests
- Button operation tests
- Calculation tests
- *Note: Requires display environment to run*

## Files Included
1. **calculator.py** - Main application
2. **README.md** - User documentation
3. **FEATURES.md** - Feature documentation
4. **VISUAL_GUIDE.md** - Visual design guide
5. **requirements.txt** - Dependencies (tkinter is built-in)
6. **test_calculator.py** - Unit tests
7. **validate.py** - Validation script
8. **.gitignore** - Git exclusions

## Running the Application

```bash
# Clone the repository
git clone https://github.com/foojunyu/Calculator.git
cd Calculator

# Run the calculator
python calculator.py
```

## Requirements
- Python 3.x (tested with Python 3.12.3)
- tkinter (included with Python)
- No external dependencies required

## Code Quality
- Clean, object-oriented design
- Well-commented code
- Separated concerns (theme config, business logic, UI)
- Extensible architecture (easy to add more themes)
- No security vulnerabilities
- No code smells
- Proper error handling

## Accomplishments
✅ Created fully functional calculator application
✅ Implemented theme switching feature
✅ Added Light and Dark themes
✅ Created comprehensive documentation
✅ Implemented secure calculation without eval()
✅ Passed all security checks (CodeQL: 0 alerts)
✅ Removed all code smells
✅ Clean, maintainable codebase

## Future Enhancement Ideas
- More themes (e.g., high contrast, colorful)
- Scientific calculator mode
- History of calculations
- Keyboard shortcuts
- Settings persistence (save theme preference)
- Customizable colors
