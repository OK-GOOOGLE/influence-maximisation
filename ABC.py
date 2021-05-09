import json
from random import randint

# usuwanie duplikatów z listy pszczół
def unique(seq, idfun=None):
    # order preserving
    if idfun is None:
        def idfun(x): return x.userName
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

# usuwanie duplikatów z listy
def unique2(seq, idfun=None):
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result



with open('usersjson2.txt', 'r') as f:
    users = json.load(f)

for key in users:
    users[key]["RetweetedFrom"] = []

for key in users:
    users[key]["RetweetedBy"] = unique2(users[key]["RetweetedBy"])

for key in users:
    for key2 in users[key]["RetweetedBy"]:
        if key not in users[key2]["RetweetedFrom"]:
            users[key2]["RetweetedFrom"].append(key)


class empBee:
    def __init__(self, userName, fitness):
        self.userName = userName    # położenie
        self.fitness = fitness     
        self.evaluated = False


class scoutBee:
    def __init__(self, userName, fitness):
        self.userName = userName
        self.fitness = fitness


class lookBee:
    def __init__(self, userName, empBee):
        self.userName = userName
        self.empBee = empBee


def calcFitness(employee, users, onlookers):
    localOnlookers = []
    i = 0
    for u1 in users[employee.userName]["RetweetedBy"]:
        localOnlookers.append(lookBee(u1, employee))
        # for u2 in users[u1]["RetweetedBy"]:
        #     i+=1
        #     if i % 2 == 0:
        #         localOnlookers.append(lookBee(u2, employee))
            # for u3 in users[u2]["RetweetedBy"]:
            #     localOnlookers.append(lookBee(u3, employee))
    localOnlookers = unique(localOnlookers) # unikanie powtorzen dla fitness function
    onlookers.extend(localOnlookers)
    return len(localOnlookers)


def findTopKNodes():
    topUsers = {}

    for name in users:
        topUsers[name] = users[name]["rep"]

    sortedUsers = dict(sorted(topUsers.items(), key=lambda kv: kv[1], reverse=True))
    i = 1
    topUsers = {}
    for user in sortedUsers:
        topUsers[user] = sortedUsers[user]
        if i > k:
            break
        else:
            i = i + 1
    return topUsers


def initEmployerBees():
    topK = findTopKNodes()
    empBees = []
    for name in topK:
        empBees.append(empBee(name, 0))
    return empBees


def evaluateEmpBees(empBees, users, onlookers):
    for employee in empBees:
        if not employee.evaluated:
            employee.fitness = calcFitness(employee, users, onlookers)
            employee.evaluated = True

def evaluateScoutBees(scoutBees, users, onlookers):
    for scout in scoutBees:
        scout.fitness = calcFitness(scout, users, onlookers)


def randomNeighbour(name):
    count = 0
    for user in users[name]["RetweetedBy"]:
        if users[user]["retweets"] > 0:
            count += 1
    if count == 0:
        return name

    index = randint(0, count)
    i = 0
    for user in users[name]["RetweetedBy"]:
        if i < index and users[user]["retweets"] > 0:
            i += 1
        if i == index and users[user]["retweets"] > 0:
            return user


def randomNeighbour2(name):
    count = 0
    for user in users[name]["RetweetedBy"]:
        if users[user]["retweets"] > 0:
            count += 1
    if count == 0:
        return name

    index = randint(0, count)
    i = 0
    for user in users[name]["RetweetedBy"]:
        if i < index and users[user]["retweets"] > 0:
            i += 1
        if i == index and users[user]["retweets"] > 0:
            return randomNeighbour(user)


def initScoutBees(empBees):
    scoutBees = []
    for emp in empBees:
        scoutBees.append(scoutBee(randomNeighbour(emp.userName), 0))
        # scoutBees.append(scoutBee(randomNeighbour(emp.userName), 0))
        # scoutBees.append(scoutBee(randomNeighbour(emp.userName), 0))
    return scoutBees


def updateScoutBees(empBees):
    scoutBees = []
    for emp in empBees:
        scoutBees.append(scoutBee(randomNeighbour2(emp.userName), 0))
        # scoutBees.append(scoutBee(randomNeighbour2(emp.userName), 0))
        # scoutBees.append(scoutBee(randomNeighbour2(emp.userName), 0))
    return scoutBees


def minFit(employers):
    minFit = employers[0].fitness
    index = 0
    for i in range(len(employers)):
        if minFit > employers[i].fitness:
            minFit = employers[i].fitness
            index = i
    return minFit, index


def updateOnlookers(empBees, onlookers):
    removeList = []
    for onlooker in onlookers:
        ok = False
        for employee in empBees:
            if onlooker.empBee.userName == employee.userName:
                ok = True
                break
        if not ok:
            removeList.append(onlooker)
    for onlooker in removeList:
        onlookers.remove(onlooker)

def calcFitnessName(userName, users):
    localOnlookers = []
    print(userName, "dist 1 retweets: ", len(users[userName]["RetweetedBy"]))
    for u1 in users[userName]["RetweetedBy"]:
        localOnlookers.append(u1)
        for u2 in users[u1]["RetweetedBy"]:
            localOnlookers.append(u2)
            # for u3 in users[u2]["RetweetedBy"]:
            #     localOnlookers.append(u3)

    result = []
    for i in localOnlookers:
        if i not in result:
            result.append(i) # unikanie powtorzen dla fitness function
    return len(result)

################################################################################
################################################################################
k = 20  # colony size
file = open("pop15it100.txt", "a+")
globAvgUsr = []
globAvgGlob = []
for run in range(0, 20):
    onlookers = []
    empBees = initEmployerBees()  # employer bees with nodes with top k ranks as the initial solution.
    evaluateEmpBees(empBees, users, onlookers)
    scouts = initScoutBees(empBees) # po jednym losowym sasiedzie dla kazdego employeeBee


    def isIn(scout, empBees):
        return any(scout.userName == elem.userName for elem in empBees)


    it = 0
    N_iter = 100
    while it < N_iter:
        scouts = unique(scouts)
        evaluateScoutBees(scouts, users, onlookers)
        scouts.sort(key=lambda x: x.fitness, reverse=True)
        for sBee in scouts:
            evaluateEmpBees(empBees, users, onlookers)
            minFitness, minIndex = minFit(empBees)
            sLocFit = sBee.fitness  # scoutLocalFitness
            if sLocFit > minFitness and not isIn(sBee, empBees):
                empBees.pop(minIndex)
                employee = empBee(sBee.userName, sLocFit)
                employee.evaluated = True
                empBees.append(employee)
        onlookers = unique(onlookers)
        updateOnlookers(empBees, onlookers) # usuwanie onlookerow bez przyporzadkowanych employee
        # print(it, len(onlookers))
        scouts = []
        scouts = updateScoutBees(empBees) # scout w odleglosci 2 od employee
        it += 1

    updateOnlookers(empBees, onlookers)

    for bee in empBees:
        print(bee.userName , "; " , bee.fitness)
        file.write(str(bee.userName)+";"+str(bee.fitness)+"\n")

    sortedBees = sorted(empBees, key=lambda x: x.fitness, reverse=True)
    sortedBees = sortedBees[0:20]
    copyOnlookers = [i for i in onlookers]
    updateOnlookers(sortedBees, copyOnlookers)

    avgList = [i.fitness for i in sortedBees]
    summ = sum(avgList)
    avg = summ / len(avgList)
    globAvgUsr.append(avg)
    globAvgGlob.append(len(copyOnlookers))
    print(run, ": Glob fit: ", len(onlookers), "\n aver: ", avg)
    print()
    file.write(str(run) + ": Glob fit: " + str(len(onlookers)) + "\n")

    # print("flynn::: ", calcFitnessName("mflynnJR", users))
    # print("beeee::: ", calcFitnessName("BeeSaysPolitics", users))
    # print(users['mflynnJR'])  # mflynnJR BeeSaysPolitics
    # print(users['BeeSaysPolitics'])
    #
    # print("beeee::: ", calcFitnessName("h0n3y_73", users))
    # print(users['h0n3y_73'])
    # print(users['amandapolitic'])

file.close()
print("GLOBAL AVG_USR: ", sum(globAvgUsr) / len(globAvgUsr))
print("GLOBAL AVG_GLOB: ", sum(globAvgGlob) / len(globAvgGlob))


################################################################################
################################################################################

