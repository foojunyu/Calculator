# Calculator Application - Features Overview

## Application Features

### 1. Basic Calculator Functionality
- **Numbers**: 0-9 buttons for input
- **Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Special Functions**:
  - Clear (C): Reset the calculator
  - Backspace (⌫): Delete last character
  - Sign Toggle (±): Switch between positive and negative
  - Decimal (.): Add decimal point
  - Percentage (%): Percentage calculations
  - Equals (=): Calculate result

### 2. Theme Switching Feature
The calculator supports two themes that can be switched via the Theme menu:

#### Light Theme
- Background: Light gray (#f0f0f0)
- Display: White background with black text
- Buttons: Light gray with black text
- Operators: Orange background with white text
- Clean, professional appearance suitable for daytime use

#### Dark Theme
- Background: Dark gray (#1e1e1e)
- Display: Dark background with white text
- Buttons: Medium gray with white text
- Operators: Orange background with white text
- Modern, sleek appearance that reduces eye strain

### 3. User Interface
- **Window Size**: 400x550 pixels
- **Menu Bar**: Contains Theme menu for switching themes
- **Display Area**: Large, clear display showing current input/result
- **Button Grid**: 5x4 grid of buttons with responsive layout
- **Professional Layout**: Clean, organized button arrangement

### 4. How to Switch Themes
1. Launch the calculator: `python calculator.py`
2. Click on "Theme" in the menu bar
3. Select either "Light Theme" or "Dark Theme"
4. The entire interface will instantly update to the selected theme

## Technical Details
- **Language**: Python 3.x
- **GUI Framework**: tkinter (built-in with Python)
- **Platform**: Windows (also works on macOS and Linux)
- **Dependencies**: None (tkinter included with Python)

## Code Quality
- Clean, object-oriented design
- Separated theme configuration
- Easy to extend with more themes
- Comprehensive button handling
- Error handling for invalid calculations
