"""
AstraLink
=========

Ponto de entrada do sistema quando executado pela pasta src.
A lógica principal está modularizada em dados.py, grafo.py, algoritmos.py e menu.py.
"""

try:
    from .menu import executar_sistema
except ImportError:
    from menu import executar_sistema


if __name__ == "__main__":
    executar_sistema()
