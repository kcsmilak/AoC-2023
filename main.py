

import p01, p05, p12, p17, p18, p19, p20, p21, p23, p24

INPUTS = ["ex", "in"]

def bf(puzzle, input):
    return f"p{puzzle:02}.{INPUTS[input]}.txt"

#p05.run('p05.in.txt')
#p12.run('p12.in.txt')

#p17.run('p17.ex.txt')

puzzle, part, input = 18, 1, 0
expected = p18.P1E
result = p18.run(bf(puzzle,input),part)

print(f"puzzle=[{puzzle}] part=[{part}] input=[{input}] -> {result} expected {expected}") 

assert(result == expected)


print("-=-")
