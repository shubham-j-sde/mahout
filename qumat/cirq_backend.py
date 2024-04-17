#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cirq

def initialize_backend(backend_config):
   # Assuming 'simulator_type' specifies the type of simulator in Cirq
    simulator_type = backend_config.get('backend_options', {}).get('simulator_type', 'default')
    if simulator_type != 'default':
        print(f"Simulator type '{simulator_type}' is not supported in Cirq. Ignoring this argument")

    return cirq.Simulator()


def create_empty_circuit(num_qubits):
    return cirq.Circuit()

def apply_not_gate(circuit, qubit_index):
    qubit = cirq.LineQubit(qubit_index)
    circuit.append(cirq.X(qubit))

def apply_hadamard_gate(circuit, qubit_index):
    qubit = cirq.LineQubit(qubit_index)
    circuit.append(cirq.H(qubit))

def apply_cnot_gate(circuit, control_qubit_index, target_qubit_index):
    control_qubit = cirq.LineQubit(control_qubit_index)
    target_qubit = cirq.LineQubit(target_qubit_index)
    circuit.append(cirq.CNOT(control_qubit, target_qubit))

def apply_toffoli_gate(circuit, control_qubit_index1, control_qubit_index2, target_qubit_index):
    control_qubit1 = cirq.LineQubit(control_qubit_index1)
    control_qubit2 = cirq.LineQubit(control_qubit_index2)
    target_qubit = cirq.LineQubit(target_qubit_index)
    circuit.append(cirq.CCX(control_qubit1, control_qubit2, target_qubit))

def apply_swap_gate(circuit, qubit_index1, qubit_index2):
    qubit1 = cirq.LineQubit(qubit_index1)
    qubit2 = cirq.LineQubit(qubit_index2)
    circuit.append(cirq.SWAP(qubit1, qubit2))

def apply_pauli_x_gate(circuit, qubit_index):
    qubit = cirq.LineQubit(qubit_index)
    circuit.append(cirq.X(qubit))

def apply_pauli_y_gate(circuit, qubit_index):
    qubit = cirq.LineQubit(qubit_index)
    circuit.append(cirq.Y(qubit))

def apply_pauli_z_gate(circuit, qubit_index):
    qubit = cirq.LineQubit(qubit_index)
    circuit.append(cirq.Z(qubit))

def execute_circuit(circuit, backend, backend_config):
    # This is a simplified example. You'll need to adjust this based on how you're handling backend configuration.
    circuit.append(cirq.MeasurementGate(key=f'result',
                                        num_qubits=len(circuit.all_qubits())).on(circuit.all_qubits()))
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=backend_config['backend_options'].get('shots', 1))
    return result.histogram(key='result')

