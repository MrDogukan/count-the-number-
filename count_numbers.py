# -*- coding: utf-8 -*-
"""ilkders.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1925Q_omSxBMhzOcM1KdiWWbuh68rEd3A
"""

from collections import Counter
a= input("Bir cümle giriniz:")
b = list(a)
c = Counter(b)
d = dict(c)
print(d)