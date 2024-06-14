# Secrets Manager

This project is a simple application built using Python and Tkinter for encrypting and decrypting secret messages. The application allows users to save their secrets securely with encryption and decrypt them when needed.

## Features

- Encrypt secret messages with a master key.
- Save encrypted messages to a file.
- Decrypt messages using the master key.
- Simple and user-friendly GUI.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. This project was developed with Python 3.8.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/secrets-manager.git
    cd secrets-manager
    ```

2. Install required packages (Tkinter is usually included with Python):
    ```bash
    pip install tkinter
    ```

### Running the Application

1. Navigate to the project directory.
2. Run the `main.py` file:
    ```bash
    python main.py
    ```

## Usage

1. **Enter your title:** Provide a title for your secret.
2. **Enter your secrets:** Type your secret message.
3. **Enter your master key:** Provide a master key for encryption.
4. **Encrypt & Save:** Click this button to encrypt and save your message.
5. **Decrypt:** To decrypt a message, paste the encrypted text into the text area, provide the master key, and click this button.

## GUI Overview

![GUI](https://github.com/YusufCelebii/SecretNotes/assets/95516451/0ee53f99-6430-4b48-b0d6-79df879086a7)

The GUI consists of the following components:

- **Title Entry (`title1`):** A text entry field where you enter the title for your secret.
- **Secrets Textbox (`text1`):** A text box where you enter the secret message that you want to encrypt or decrypt.
- **Master Key Entry (`master_key`):** A text entry field where you enter the master key used for encryption and decryption.
- **Encrypt & Save Button (`save_button`):** A button that, when clicked, encrypts the entered secret using the master key and saves it to the file `My Secrets.txt`.
- **Decrypt Button (`decrypte_button`):** A button that, when clicked, decrypts the entered encrypted message using the master key and displays the decrypted message in the secrets textbox.


## Files

- `main.py`: The main script containing the application code.
- `My Secrets.txt`: The file where encrypted secrets are stored.

## Code Explanation

The application uses the Tkinter library to create a GUI and the base64 module for encoding and decoding the messages.

### Encryption Function
```python
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
