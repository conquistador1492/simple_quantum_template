#!/usr/bin/env python3

from tools import set_parameters
from launcher import Launcher

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

parameters = set_parameters()
# parameters['backend_name'] = 'qasm_simulator'
# parameters['shots'] = 100
launcher = Launcher(**{item: parameters[item] for item in ['backend_name', 'shots']})

qr, cr = QuantumRegister(5), ClassicalRegister(5)
circuit = QuantumCircuit(qr, cr)

circuit.u3(0, 0, 0, qr[0])
circuit.h(qr[0])
circuit.cx(qr[0], qr[1])

#...........................................
# Third algorithm's step realisation


# Decomposition of conditioned rotation:
  
def ConditionedRotation(angle, controllingQbit, subjectedQbit, circuit, quantReg):
  
    circuit.u3(angle, 0, 0, quantReg[subjectedQbit])
    circuit.z(quantReg[subjectedQbit])
    circuit.cx(quantReg[controllingQbit], quantReg[subjectedQbit])
    circuit.u3( ( - angle ), 0, 0, quantReg[subjectedQbit])
    circuit.z(quantReg[subjectedQbit])
    
    return


#Execution in main coode:

pi = 3.1416

ConditionedRotation(pi/4, 1, 0, circuit, qr)
ConditionedRotation(pi/8, 2, 0, circuit, qr)


#...........................................





# meas_qubits - кубиты, использующиеся для томографии. Порядок важен (для [0, 1] и [1, 0] ответ будет разным)
print(launcher.run([circuit], meas_qubits=[0]))
