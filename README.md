# RSA

RSA, named after its inventors Ron Rivest, Adi Shamir, and Leonard Adleman, is a type of public-key cryptography, which is a method for securing data. It's especially important in computer science for secure data transmission.

Imagine you have a box with a special lock that has two keys: a public key, which everyone can see and use to lock the box, and a private key, which only you have and can use to unlock the box. RSA works similarly.

In RSA:

1. **Public Key**: This is like the lock everyone can see. It's used to encrypt (or lock) the data. Since it's public, anyone can use this key to encrypt a message.
1. **Private Key**: This is like the key only you have. It's used to decrypt (or unlock) the data. Since it's private, only the person with this key can read the message.

Here’s how RSA is typically used:

- When someone wants to send you a secure message, they encrypt it using your public key.
- Once a message is encrypted with this public key, it can only be decrypted with the corresponding private key, which only you have.
- When you receive the message, you use your private key to decrypt it and read it.

RSA is based on the mathematical difficulty of factoring the product of two large prime numbers. The security of RSA comes from the fact that while it's relatively easy to multiply two large primes together, it's extremely hard to do the reverse: to take a large number and figure out which two primes were multiplied to get it.

In summary, RSA is a way of sending encrypted messages that only the intended recipient can read, using a pair of keys, one public and one private, based on the mathematical principles of prime numbers. It's a foundational technology in secure communications over the internet.

## Overview

This repository includes files required to create a program that models the process in encrypting and decrypting data with the use of the RSA algorithm. This program utilizes the PyQt framework for creating a graphical user interface.

- Demo: This directory contains demonstration images / videos of the application.
- src: This directory contains source code for specific versions of the program.
    - Version 1.0.0: This directory contains source code for the first version of the program.
        - Images: This directory contains images that are used in the building of the application.
            - Icon.ico: Icon for a Windows application.
            - Icon.png: Icon for a MacOS application.
            - RSA.png: Image for the application.
        - Apple.spec: PyInstaller spec file for Apple platforms.
        - main.py: Main file where the other classes / functions are used to run the application.
        - Microsoft.spec: PyInstaller spec file for Microsoft platforms.
        - Modules.py: Python modules that were used in the application.
        - ToolSets.py: Functions that are used to perform RSA encryption / decryption.
        - Windows.py: PyQt window classes and functions that are used to build a GUI for the program.
- .gitignore: Git ignore file for specific files and directories.

## Releases

### Version 1.0.0

Version 1.0.0 of RSA was built with Python and the PyQt framework. This application is available for download as both a Windows .exe file and MacOS .app file. The files for this release can be found [here](https://github.com/QuantumCompiler/RSA/releases/tag/v1.0.0).

#### Version 1.0.0 Important Notes

When decoding a message in this application, one must only include the data that is encased with the brackets. Brackets must be included and no white space or other characters can be included before or after the brackets. Please see the graphics for this application (or the video in Demo/) for further assistance.

#### Version 1.0.0 Graphics

<p align = "center">
    <img src = "Demo/Main Screen Demo.png" width = "800">
    <img src = "Demo/Encode 1 Demo.png" width = "800">
    <img src = "Demo/Encode 2 Demo.png" width = "800">
    <img src = "Demo/Decode Demo.png" width = "800">
</p>