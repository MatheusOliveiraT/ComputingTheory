def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F

Q = ['q0', 'q1', 'q2']
Sigma = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
delta = {('q0', '0') : 'q1', ('q0', '1') : 'q2', ('q0', '2') : 'q2', ('q0', '3') : 'q2', 
         ('q0', '4') : 'q2', ('q0', '5') : 'q1', ('q0', '6') : 'q2', ('q0', '7') : 'q2', 
         ('q0', '8') : 'q2', ('q0', '9') : 'q2', ('q1', '0') : 'q1', ('q1', '1') : 'q2', 
         ('q1', '2') : 'q2', ('q1', '3') : 'q2', ('q1', '4') : 'q2', ('q1', '5') : 'q1', 
         ('q1', '6') : 'q2', ('q1', '7') : 'q2', ('q1', '8') : 'q2', ('q1', '9') : 'q2', 
         ('q2', '0') : 'q1', ('q2', '1') : 'q2', ('q2', '2') : 'q2', ('q2', '3') : 'q2', 
         ('q2', '4') : 'q2', ('q2', '5') : 'q1', ('q2', '6') : 'q2', ('q2', '7') : 'q2', 
         ('q2', '8') : 'q2', ('q2', '9') : 'q2'}
q0 = 'q0'
F = ['q1']

print(AFD((Q, Sigma, delta, q0, F), '103')) # False
print(AFD((Q, Sigma, delta, q0, F), '500')) # True
print(AFD((Q, Sigma, delta, q0, F), '503')) # False
print(AFD((Q, Sigma, delta, q0, F), '5')) # True
print(AFD((Q, Sigma, delta, q0, F), '9')) # False