a = 2
b = 6
c = 3

operacaoAnd = a == b and c * a == b
print(operacaoAnd)
operacaoOr = a == b or c * a == b 
print(operacaoOr)

operacaoAnd = a == (c + b ) and b == c
print(operacaoAnd)
operacaoOr = a == (c + b ) or b == c
print(operacaoOr)

operacaoAnd = a > 5 and b > 3
print(operacaoAnd)
operacaoOr = a > 5 or b > 3
print(operacaoOr)

operacaoAnd = a < 5 and c >= 3
print(operacaoAnd)
operacaoOr = a < 5 or c >= 3
print(operacaoOr)

operacaoAnd = not b  == 6 and 3 * 2 == b
print(operacaoAnd)
operacaoOr = not b  == 6 or 3 * 2 == b
print(operacaoOr)

operacaoAnd = c < 5 and not b > 6
print(operacaoAnd)
operacaoOr = c < 5 or not b > 6
print(operacaoOr)