Data Encryption/Decryption Tool
Introduction
The Data Encryption/Decryption Tool is a user-friendly application designed to secure text data using symmetric encryption with the Fernet algorithm from the cryptography library. Built with Python and Tkinter, this tool provides a graphical interface to generate encryption keys, encrypt messages, and decrypt them. It is an excellent resource for learning about cryptography and comparing the efficiency of encryption/decryption processes. Ideal for cybersecurity students and enthusiasts, it supports secure data handling and key management.
How to Run
Installation Process

Install Python: Download and install Python 3.x from python.org. During installation, check "Add Python to PATH" and verify with python --version or python3 --version.
Install Cryptography Library:
Open a terminal (e.g., Command Prompt, Terminal, or VS Code terminal).
Navigate to your project directory (e.g., cd C:\encryption decryption).
Run the following command to install the required cryptography library:pip install cryptography


If pip fails, try pip3 install cryptography or python -m pip install cryptography. Wait for the installation to complete and verify with pip show cryptography.


Save the Code: Copy the data_encryption_decryption_tool.py code into a file named data_encryption_decryption_tool.py in your project folder.
Run the Script: Open VS Code, go to Terminal > New Terminal, navigate to the project folder, and type python data_encryption_decryption_tool.py or python3 data_encryption_decryption_tool.py, then press Enter. A GUI window will appear.

Usage

Encrypt: Enter text in the "Enter Text" box, generate a key with "Generate Key" or input an existing key, then click "Encrypt" to see the encrypted result and time taken.
Decrypt: See detailed instructions below.

How to Decrypt
Decryption requires the same key used for encryption. Follow these steps:

Prepare Encrypted Text: Paste the encrypted text (e.g., gAAAAABlQ...) into the "Enter Text" box. This is the output from a previous encryption.
Enter the Key: Input the exact key used for encryption into the "Key" field. 
If you generated a key earlier with "Generate Key," copy that key (e.g., u7xM...=) from the field. This is a base64-encoded string unique to each encryption.
Important: The key must match the one used for encryption. Save it after generating, as the tool doesn’t store it automatically.


Decrypt: Click the "Decrypt" button. The decrypted text and decryption time (e.g., "Decrypted Text: Hello, World!\nDecryption Time: 0.0015 seconds") will appear in the result area.
Error Handling: If the key is incorrect or the text is invalid, an error message like "Decryption failed: Invalid key or padding" will display. Ensure the encrypted text and key are correctly copied.

Example:

Encrypted Text: gAAAAABlQ...
Key: u7xM...=
After clicking "Decrypt," you might see: "Decrypted Text: Hello, World!\nDecryption Time: 0.0012 seconds".

Conclusion
This Data Encryption/Decryption Tool offers a practical introduction to symmetric encryption, providing a secure way to protect text data. Its ability to measure execution time aids in efficiency analysis, making it a valuable learning tool. Future enhancements could include support for multiple algorithms or file encryption. This project lays a strong foundation for exploring advanced cryptographic techniques.
Contact: pawankumar73380@gmail.comLinkedIn: pavankumar022  
ThankYou
