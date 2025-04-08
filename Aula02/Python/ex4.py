def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F

Q = ['q0', 'q1', 'q2', 'q3', 'q4']
Sigma = ['a', 'b']
delta = {('q0', 'a') : 'q1', ('q0', 'b') : 'q3', ('q1', 'a') : 'q0', ('q1', 'b') : 'q2', 
         ('q2', 'a') : 'q4', ('q2', 'b') : 'q3', ('q3', 'a') : 'q4', ('q3', 'b') : 'q2',
         ('q4', 'a') : 'q4', ('q4', 'b') : 'q4'}
q0 = 'q0'
F = ['q0', 'q2']

print(AFD((Q, Sigma, delta, q0, F), 'aaabb')) # False
print(AFD((Q, Sigma, delta, q0, F), 'aaabbb')) # True
print(AFD((Q, Sigma, delta, q0, F), 'abab')) # False
print(AFD((Q, Sigma, delta, q0, F), 'aaaaabbb')) # True
print(AFD((Q, Sigma, delta, q0, F), 'ba')) # False