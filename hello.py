#!/usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da ling configurada no ambiente, 
o programa exibe a mensagem correspondente.

Como usar:

    Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py

"""
#Meta dados

__version__ = "0.0.1"
__autor__   = "SL"
__license__ = "Unlicense"

import os

"""
if __name__ == "__main__":
    print("Hello, World!")
"""



current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
    
print(msg)


