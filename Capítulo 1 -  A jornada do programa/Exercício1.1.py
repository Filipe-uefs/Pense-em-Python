"""
1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?

2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?

3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?

4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?

5. O que acontece se você tiver dois valores sem nenhum operador entre eles?
"""

"""
1. Ao omitir um dos parênteses o interpretador Python retorna um SyntaxError com a seguinte mensagem
    'unexpected EOF while parsing', retornando também o local exato do erro, já ao omitir ambos os
    parênteses, o interpretador retorna SyntaxError com a mensagem 'invalid syntax'
"""

"""
2. Ao omitir uma das aspas o interpretador Python retorna um SyntaxError com a seguinte mensagem
    'EOL while scanning string literal', retornando também o local exato do erro, já ao omitir ambas as
    aspas, o interpretador retorna SyntaxError com a mensagem 'invalid syntax'
"""

"""
3. Ao usar a sintaxe +1, o python transforma essa expressão em um numero natural, nesse caso, 1.
    Já no caso 2++2, o Python faz o jogo de sinal, no caso + com + = +, portanto o resultado de 2++2 é 4
"""

"""
4. Ao tentar escrever um número na forma '02', o Python retorna um erro de SyntaxError, pois essa notação 
não é permitida
"""

"""
5. Ao tentar escrever dois valores sem um operador, o interpretador do Python retorna um SyntaxError
"""