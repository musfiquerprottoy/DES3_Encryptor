# DES3 Encryptor/Decryptor

A simple GUI application for encrypting and decrypting text using Triple DES (3DES) algorithm. Built with CustomTkinter and PyCryptodome.

## ⚠️ Security Warning
3DES is deprecated and not recommended for production use. Use AES-256 instead for secure encryption.

## Features
- Encrypt plaintext to hex ciphertext
- Decrypt hex ciphertext back to plaintext
- Display session key and IV
- Copy to clipboard functionality
- Social links to developer profiles

## Installation

### Option 1: Run from Source (Recommended)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/des3-encryptor.git
   cd des3-encryptor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python DES3.py
   ```

### Option 2: Download Pre-built Executable (Linux Only)
- Download the latest release from the [Releases](https://github.com/yourusername/des3-encryptor/releases) page.
- Make it executable: `chmod +x DES3`
- Run: `./DES3`

## Usage
1. Enter plaintext in the encryption input.
2. Click "ENCRYPT" to get hex ciphertext.
3. Copy the ciphertext and paste into decryption input.
4. Click "DECRYPT" to get back the plaintext.
5. Use "Show Key & IV" to view the session credentials.

## Dependencies
- Python 3.7+
- customtkinter
- pycryptodome
- darkdetect

## License
All rights reserved.

## Made by
Musfique Prottoy

## Social Links
- [Facebook](https://facebook.com/musfiqueprottoy.1)
- [GitHub](https://github.com/yourusername)