import cmath
import uuid
import random

from hypothesis import given
from hypothesis.strategies import 

class Backend:
    def __init__(self, X, Y, Z, H, T, CNOT):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.H = H
        self.T = T
        self.CNOT = CNOT

class qubit:
    def __init__(self):
        self.state = (complex(1,0),complex(0,0))
        self.uuid = uuid.uuid4() 

    def X(self):
        new_state = (self.state[1], self.state[0])
        self.state = new_state

    def Y(self):
        new_state = (complex(0,1) * self.state[1], - complex(0,1) * self.state[0])
        self.state = new_state

    def Z(self):
        new_state = (self.state[0], -self.state[0])
        self.state = new_state

    def __str__(self):
        return f"""Qubit: {self.uuid}; State: {self.state[0]}|0> + {self.state[1]}|1>"""
        
class QRoutines:
    def __init__(self, backend):
        self.X = backend.X
        self.Y = backend.Y
        self.Z = backend.Z
        self.H = backend.H
        self.T = backend.T
        self.CNOT = backend.CNOT


    def qotp(self, block):
        key = []
        for q in block:
            r = random.randint(0,3)
            if r == 0: pass
            if r == 1: self.X(q)
            if r == 2: self.Z(q)
            if r == 3: self.Y(q)
            key.append(r)
        return key

# Define backend
b = Backend(
    lambda q: q.X(),
    lambda q: q.Y(),
    lambda q: q.Z(),
    lambda q: q.H(),
    lambda q: q.T(),
    lambda q: q.CNOT())

# Instantiating QRoutines library
qr = QRoutines(b)

# Run example with 2 qubit qotp encoding, returns key used
q1 = qubit()
q2 = qubit(); q2.X()
block = [q1,q2]

print('Clear block')
for q in block: print(q)

print('Applying QOTP') 
key = qr.qotp(block)

print('Encrypted block') 
for q in block: print(q)
print('Used key', key)

