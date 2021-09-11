from __future__ import print_function  # allow it to run on python2 and python3
import numpy as np
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dwave.cloud import Client
import os
import sys
qubomatrix = np.loadtxt(os.path.join(sys.path[0], 'qubomatrix.txt'))/100
print('Loaded matrix:\n', qubomatrix, '\n')
# convert into QUBO
qubo = {(i,i):0.0 for i in range(len(qubomatrix))}
print(type(qubo[(0,0)]))
# necessary to keep the order of the sample columns consistent
for index,value in np.ndenumerate(qubomatrix):
    if value != 0:
        qubo[index] = value
print('Converted matrix into QUBO for D-Wave:\n', qubo, '\n')
# embed and run on the D-Wave with 7500 reads
#Token hier einfügen
response = EmbeddingComposite(DWaveSampler(token='Hier das Token einfügen')).sample_qubo(qubo, num_reads=7500)
print('Response from the D-Wave:\n', response,response.data, '\n')
# save results in results.txt
with open(os.path.join(sys.path[0], 'results.txt'),'a') as file:
    file.write(str(qubo)+'\n'+str(response)+'\n\n')
print(sample[0]+"\n")
print(sample[len(sample)-1])
