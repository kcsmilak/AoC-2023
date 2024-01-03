# P1: 19114 - 446935
# P2: ? - ?

DEBUG = True

def main():
    #print(f"Ex p1: {run('test.txt')}")
    print(f"Ex p1: {run('example.txt')}")
    print(f"In p1: {run('input.txt')}")
    print(f"Ex p2: {run('example.txt', 2)}")
    #print(f"In p1: {run('input.txt')}")
    print(f"In p2: {run('input.txt', 2)}")
    print("__")

def run(filename, puzzlePart = 1):

    result = 0

    inputLines = open(filename).read().splitlines()
    i = 0
    workflows = {}
    while True:
        if len(inputLines[i]) == 0:
            i += 1
            break

        key = inputLines[i].split("{")[0]
        instructions = inputLines[i].split("{")[1][:-1].split(",")
        
        
        workflows[key] = instructions
        i += 1

    #print(workflows)
    
    ratings = []
    while i < len(inputLines):
        ratingBits = inputLines[i][1:-1].split(",")
        rating = {}
        for ratingBit in ratingBits:
            rating[ratingBit.split("=")[0]] = int(ratingBit.split("=")[1])

            
        ratings.append(rating)
        i += 1

    #print(ratings)

    # here is where the work starts

    if puzzlePart == 1:
        
        for rating in ratings:
    
            workflowKey = "in"
    
            #print(f"on workflow={workflowKey}")
            
            accept = False
            while True:
    
                
                if "A" == workflowKey:
                    #print("Accept")
                    accept = True
                    break
                elif "R" == workflowKey:
                    #print("REJECT")
                    break
    
                workflow = workflows[workflowKey]
                
                for test in workflow:
                
                    if ":" in test:
                        # comparison test
                        #print(f"compare {test}")
                        subtest = test.split(":")[0]
                        destination = test.split(":")[1]
                        if "<" in subtest:
                            part = subtest.split("<")[0]
                            value = int(subtest.split("<")[1])
        
                            if rating[part] < value:
                                #print(f"  test {test} passed")
                                workflowKey = destination
                                break
                            else:
                                #print(f"  test {test} failed")
                                pass
             
                        
                        elif ">" in subtest:
                            part = subtest.split(">")[0]
                            value = int(subtest.split(">")[1])
        
                            if rating[part] > value:
                                #print(f"  test {test} passed")
                                workflowKey = destination
                                break
                            else:
                                #print(f"  test {test} failed")
                                pass
                        else:
                            throw("invalid test")
                        
                    else:
                        # move or finish test
                        #print(f"move {test}")
                        workflowKey = test
                        break
    
            
            if accept:
                result += rating["x"] + rating["m"] + rating["a"] + rating["s"]

    else:

        acceptNodes = []

        tree = {}
        for key in workflows:
            for test in workflows[key]:
                destination = test if not ":" in test else test.split(":")[1]
                if destination not in tree:
                    tree[destination] = []
                tree[destination].append(key)
        tree["in"] = "ROOT"

        print(tree)
        for key in workflows:
            for test in workflows[key]:

                if test[-1] == 'A':
                    print(f"Starting from key={key} test={test}")
                    #walk up the tree from key
                    previous = None
                    while True:

                        # get each of the left parts, then move up
                        
                        potentialTests = []
                        if previous != None:
                            for potentialTest in workflows[key]:
                                # see if previous matches start, if so, add to potentialTests
                                if not potentialTest.endswith(previous):
                                    potentialTests.append(potentialTest)
                                else:
                                    potentialTests.append(potentialTest)
                                    break
                        else:
                            potentialTests.append(test)
                            
                            

                        
                        print(f" {key:5} {' , '.join(potentialTests):40}", end="")
                        if key == "in":
                            print(f"-> DONE")
                            break
                        
                        parent = tree[key][0]
                        print(f"-> {parent}")
                        previous = key
                        key = parent
 
        
        result = None


    
    return result

main()
