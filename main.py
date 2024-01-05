############################################################

PUZZLES = [20]

PARTS = [1,2]

INPUTS = ["ex", "in"]

CATCH_EXCEPTIONS = False

############################################################

FINISHED_MISSING_PUZZLES = [1,2,3,4,6,7,8,9,10,11,14,15,16]

COMPLETED_PUZZLES = [13, 25]
WRONG_ANSWER_PUZZLES = [17, 18, 19, 21, 22, 24]
TOO_LONG_PUZZLES = [12, 20, 23]
BROKEN_PUZZLES = [5]

P1E, P1I, P2E, P2I = None, None, None, None

############################################################

import importlib
registry = {}
for i in PUZZLES:
    registry[i] = importlib.import_module(f"p{i:02}")

def expectedValue(registry, puzzle, part, input):
    if part == 1:
        if input == "ex":
            return registry[puzzle].P1E
        else:
            return registry[puzzle].P1I
    else:
        if input == "ex":
            return registry[puzzle].P2E
        else:
            return registry[puzzle].P2I

def bf(puzzle, input):
    return f"p{puzzle:02}.{input}.txt"

def main():
    for puzzle in PUZZLES:
        print(f"\n-[ Puzzle {puzzle} ]-------------\n")
        for part in PARTS:
            for input in INPUTS:
                filename = bf(puzzle, input)
    
                expected = expectedValue(registry, puzzle, part, input)
    
                try:
                    result = registry[puzzle].run(filename, part)
                    print(
                        f"puzzle=[{puzzle}] part=[{part}] input=[{input}] -> [{result}] expected [{expected}]"
                    )
                except Exception as e:
                    if not CATCH_EXCEPTIONS: raise e
                    print(f"p{puzzle:02}.{input}.{part} : {e}")
    
                #assert(result == expected)
    
main()