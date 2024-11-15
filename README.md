# Task3: Password Strength Checker

## Description
`task3.py` is a Python script that assesses the strength of a given password based on a variety of criteria, including length, uppercase and lowercase characters, digits, and special characters. The script includes a **Graphical User Interface (GUI)** built using **Tkinter**, making it easy and interactive for users to check the strength of their passwords. It also provides tips for creating stronger passwords.

## Features
- **Password Strength Evaluation**: Evaluates password strength based on the following criteria:
  - **Length**: At least 8 characters.
  - **Uppercase Letters**: At least one uppercase letter.
  - **Lowercase Letters**: At least one lowercase letter.
  - **Digits**: At least one digit.
  - **Special Characters**: At least one special character (e.g., `!@#$%^&*`).

- **Color-Coded Feedback**: Displays the password strength with color-coded labels:
  - **Very Strong** (Green): All criteria are met.
  - **Strong** (Blue): 4 out of 5 criteria are met.
  - **Moderately Strong** (Orange): 3 out of 5 criteria are met.
  - **Weak** (Red): Less than 3 criteria are met.

- **Password Tips**: Provides helpful tips for creating secure passwords.
- **User-Friendly GUI**: Built using **Tkinter**, ensuring an intuitive experience for users.

## Requirements
- **Python 3.x**: Ensure that Python 3 is installed on your machine.
- **Tkinter**: Tkinter is included with Python by default. If not installed, you can install it using:
  ```bash
  sudo apt-get install python3-tk    # For Linux
  ```
  Tkinter is bundled with Python on **Windows** and **macOS**.

## Installation
1. **Check if Python 3 is installed**:
   You can verify Python 3 installation by running:
   ```bash
   python3 --version
   ```
   This should show something like:
   ```
   Python 3.x.x
   ```

2. **Clone or Download the Repository**:
   Download or clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

3. **Install Dependencies** (if any):
   If there are any additional dependencies, you can install them by running:
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run the Script**:
   To run the script, simply execute:
   ```bash
   python3 task3.py
   ```

## Usage
1. **Enter Password**: Type the password you want to check in the input field.
2. **Check Strength**: Click the **Check Password Strength** button to see the strength of the password. The result will be displayed in the text box with color-coded feedback based on the password strength.
3. **View Tips**: Click the **Show Tips for Strong Password** button to view useful tips for creating strong passwords.

## Password Strength Criteria
The strength of the password is determined based on the following criteria:
1. **Length**: The password must be at least **8 characters** long.
2. **Uppercase Letters**: The password must contain at least **one uppercase letter**.
3. **Lowercase Letters**: The password must contain at least **one lowercase letter**.
4. **Digits**: The password must contain at least **one digit**.
5. **Special Characters**: The password must contain at least **one special character** (e.g., `!@#$%^&*`).

## GUI Layout

### Components:
- **Title**: "Password Strength Checker" label.
- **Password Input Field**: A field where the user can input their password.
- **Check Password Strength Button**: A button that evaluates the password.
- **Password Strength Result**: The strength of the password is displayed here, color-coded:
  - Green: Very Strong
  - Blue: Strong
  - Orange: Moderately Strong
  - Red: Weak
- **Show Tips Button**: A button that shows useful tips for creating a strong password.
- **Tips Display Area**: A text area where tips for password security are displayed in blue.

## Example Output
When you input a password and click "Check Password Strength", the application will evaluate the strength based on the criteria. The strength will be displayed as:
- **Very Strong (Green)**: All criteria met.
- **Strong (Blue)**: 4 out of 5 criteria met.
- **Moderately Strong (Orange)**: 3 out of 5 criteria met.
- **Weak (Red)**: Fewer than 3 criteria met.

## Tips for Strong Passwords
Here are some quick tips to create strong passwords:
- **Length**: Aim for at least 12 characters.
- **Character Variety**: Use a combination of uppercase and lowercase letters, digits, and special characters.
- **Avoid Common Words**: Don't use easily guessable passwords like "password" or "12345".
- **Avoid Personal Information**: Don't use names, birthdays, or personal information.
- **Use a Passphrase**: Consider using a passphrase made up of multiple random words.
- **Use a Password Manager**: For securely storing and generating passwords.

## License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, feel free to open an issue or contact the author:
- **Author**: 0xgh057r3c0n
