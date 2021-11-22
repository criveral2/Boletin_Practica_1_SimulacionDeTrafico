#!/usr/bin/env python
# coding: utf-8

# ## Tarea simulacion 03 - Generador tausworthe

# #### Nombre: Christian Rivera

# In[19]:


"""
Una implementación de Python del generador tausworthe (TG)

Tausworthe Generator (TG) es una especie de generador recursivo multiplicativo
que produce bits aleatorios

"""

import numpy as np

class TG(object):
    def __init__(self, length: int = 1, debug: bool = False) -> None:
        """
        Parámetros
        ----------
        longitud: int
                longitud de la matriz PRN generada
        """
        self.r = self.q = self.chunk_len = 0
        self.debug = debug
        if length <= 0:
            raise ValueError("¡La longitud debe ser un número entero positivo!")
        self.length = length

    def get_bits(self) -> np.ndarray:
        """
        Obtener bits en bruto

        """
        return self.B

    def seed(self, r: int = 3, q: int = 5, chunk_len: int = 4):
        """
        Definir una semilla para el generador PRN
        Las semillas se definen por r, q y l

        Parámetros
        ----------
        r: int
                como se define en
                B [i] = (B [i − r] + B [i − q]) mod 2 = B [i − r] XOR B [i − q] (0 <r <q)
        q: int
                como se define en
                B [i] = (B [i − r] + B [i − q]) mod 2 = B [i − r] XOR B [i − q] (0 <r <q)
        l: int
                longitudes de bits en base 2
                Use (l-bits en base 2) / 2 ^ ly convierta a base 10
        """
        self.r = r
        self.q = q
        self.chunk_len = chunk_len

    def convert(self, bits: np.ndarray) -> np.ndarray:
        """
        Convertir bits en decimales

        Parámetros
        ----------
        bits: numpy.ndarray
                bits para convertir
        """
        res = 0
        for index, bit in enumerate(bits):
            res += bit * np.power(2, (len(bits) - index - 1))
        return res

    def random(self, n_decimal: int = 3) -> np.ndarray:
        """
        Genere números aleatorios usando el método Tauwort
        """

        # check whether seed was initialized
        if self.r == 0 or self.q == 0 or self.chunk_len == 0:
            self.seed()

        # length is the number of bits we need
        self.length_bit = self.length * self.chunk_len
        self.verbose(f"self.length_bit = {self.length_bit}")

        # initialize the array B
        self.B = np.ones(self.length_bit)

        # extend array B
        for i in range(self.q, self.length_bit):
            new_bit = 1 if self.B[i - self.r] != self.B[i - self.q] else 0
            self.B[i] = new_bit

        self.verbose(f"Before splitting, self.B is {self.B}")

        self.B = np.array_split(self.B, self.length)

        self.verbose(f"After splitting, self.B is {self.B}")

        self.decimal = np.array(
            [
                round(self.convert(seg) / np.power(2, self.chunk_len), n_decimal)
                for seg in self.B
            ]
        )

        if 0 in self.decimal:
            print(f"Warning: zero found in index {np.where(self.decimal == 0.0)}")
            print(f"r = {self.r}; q = {self.q}; l = {self.chunk_len}")

        return self.decimal

    def get_cycle(self) -> int:
        """
        Calcular la duración de un ciclo en matrices TG actuales
        """
        try:
            idx = np.where(self.decimal == self.decimal[0])[1]
            return idx
        except IndexError:
            print(f"Cycle larger than {len(self.decimal)}.")
            return 0

    def verbose(self, *args, **kwargs) -> None:
        """
        Función de impresión personalizada para depuración
        """
        if self.debug:
            print(*args, **kwargs)


def main() -> None:
    tg = TG(length=20)
    tg.seed(r=5, q=17, chunk_len=19)
    res = tg.random()
    print(res.tolist())

if __name__ == "__main__":
    main()


# In[ ]:




