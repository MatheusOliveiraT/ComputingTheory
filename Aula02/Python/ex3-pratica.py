def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F

Q = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
Sigma = ['a', 'b']
delta = {('q0', 'a') : 'q1', ('q0', 'b') : 'q2', ('q1', 'a') : 'q0', ('q1', 'b') : 'q3', 
         ('q2', 'a') : 'q3', ('q2', 'b') : 'q4', ('q3', 'a') : 'q2', ('q3', 'b') : 'q5',
         ('q4', 'a') : 'q5', ('q4', 'b') : 'q0', ('q5', 'a') : 'q4', ('q5', 'b') : 'q1'}
q0 = 'q0'
F = ['q1']

print(AFD((Q, Sigma, delta, q0, F), 'aaabb')) # False
print(AFD((Q, Sigma, delta, q0, F), 'aaabbb')) # True
print(AFD((Q, Sigma, delta, q0, F), 'abab')) # False
print(AFD((Q, Sigma, delta, q0, F), 'aaaaabbb')) # True
print(AFD((Q, Sigma, delta, q0, F), 'ba')) # False