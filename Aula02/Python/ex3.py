def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F

Q = ['q0', 'q1', 'q2', 'q3']
Sigma = ['a', 'b']
delta = {('q0', 'a') : 'q1', ('q0', 'b') : 'q2', ('q1', 'a') : 'q0', ('q1', 'b') : 'q3', 
         ('q2', 'a') : 'q3', ('q2', 'b') : 'q0', ('q3', 'a') : 'q2', ('q3', 'b') : 'q1'}
q0 = 'q0'
F = ['q0', 'q3']

print(AFD((Q, Sigma, delta, q0, F), 'bba')) # False
print(AFD((Q, Sigma, delta, q0, F), 'baaaaba')) # False
print(AFD((Q, Sigma, delta, q0, F), 'bbab')) # True
print(AFD((Q, Sigma, delta, q0, F), 'baaaab')) # True
print(AFD((Q, Sigma, delta, q0, F), 'ba')) # True