import time
import operator
import sys

fileN = sys.argv[1]
f = open(fileN, "r")


SEQ_INFO = 3
SEQ_ID = 0
SEQ_TYPE = 2
SEQ_START = 3
SEQ_END = 4
SEQ_VALUE = 5
SEQ_DIRECTION = 6
POS_DIRECTION = 1
NEG_DIRECTION = 0
SEQ_STOP = 8
TMP = []

#pripraveni sekvence na vypis
def makeString(lMAX):
    string = ""
    for x in lMAX:
        string += str(x[SEQ_ID]) + "	" + str(x[1]) + "	" + str(x[SEQ_TYPE]) + "	" + str(x[SEQ_START]) + "	" + str(x[SEQ_END]) + "	" + str(x[SEQ_VALUE]) + "	" + str(x[SEQ_DIRECTION]) + "	" + str(x[7])
    return string[:-1]

def sortStart(elem):
    return elem[3]

def findMaximum(array, index):
    max = 0
    ix = 0
    for i in range(len(array)):
        tmpMax = array[i]
        if tmpMax >= max:
            max = tmpMax
            ix = index[i]
    return max, ix

#nalezeni nejvetsi, neprekryvajici se sekvence
def findMAX(arr):
    length = len(arr)
    MAX = {}

    for i in range(length):
        end = arr[i][SEQ_END]
        MAX[i] = i

        for j in range(i+1, length):
            if end <= arr[j][SEQ_START]:
                max = {}
                max[j] = len(arr[j:])
                MAX[i] = max
                break

    dict = {}
    prevFR = []
    save = {}

    for i in range(len(MAX)):
        reverse = len(MAX) -1 -i
        if MAX[reverse] == reverse:
            MAX[reverse] = arr[reverse][SEQ_VALUE]
        else:
            fr = next(iter(MAX[reverse]))
            to = MAX[reverse][fr]
            tmp =[]
            index = []
            current = arr[reverse][SEQ_VALUE]

            if fr in prevFR:
                MAX[reverse] = current + save[fr][0]
                dict[reverse] = save[fr][1]
            else:
                prevFR.append(fr)
                for j in range(fr, fr+to):
                    tmp.append(MAX[j])
                    index.append(j)

                inMAX = [0.0, 0]
                inMAX = findMaximum(tmp, index)
                save[fr] = inMAX
                MAX[reverse] = current + inMAX[0]
                dict[reverse] = inMAX[1]

    biggest = []
    indexes = []
    length = len(MAX)

    for i in range(length):
        indexes.append(i)
        biggest.append(MAX[i])

    finMAX = findMaximum(biggest, indexes)
    first = finMAX[1]
    final = []

    while first in dict:
        final.append(arr[first])
        first = dict[first]

    if len(arr) != 0:
        final.append(arr[first])
        print(makeString(final))

#optimalizacni funkce spociva ve vytvareni mensich bloku sekvenci, na kterych se hleda vysledek 
#prochazi pole arr a drzi si nejvetsi hodnotu SEQ_END, pokud je tato hodnota mensi nez SEQ_START, muzeme ukoncit
#nacitani lokalniho bloku a provest nalezeni nejdelsi maximalni neprekryvajici se sekvence
def subProblems(arr):
	S = []
	maximum = arr[0][SEQ_END]
	for i in arr:

		if i[SEQ_START] >= maximum:
			findMAX(S)
			S.clear()
			S.append(i)
		else:
			S.append(i)
		if maximum <= i[SEQ_END]:
				maximum = i[SEQ_END]
	findMAX(S)

def main():         
    G = {}

    for line in f:
        #vyporadani se s komentari v souboru
        if '##' in line:
            print(line[:-1])
        else:
            lists = line.split("	")
            tmp = ["", "", "", 0, 0, 0, "", ""]

            #naplneni pomocneho pole
            for i in range(SEQ_INFO):
                tmp[i] = lists[i]

            tmp[SEQ_START] = int(lists[SEQ_START])
            tmp[SEQ_END] = int(lists[SEQ_END])
            tmp[SEQ_VALUE] = float(lists[SEQ_VALUE])

            for i in range(SEQ_DIRECTION, SEQ_STOP):
                tmp[i] = lists[i]

            #vytvoreni zaznamu ve slovniku, pokud se zmenil kontext
            if tmp[SEQ_ID] not in G:
                X = {}
                Y = {}
                X['pos'] = []
                Y['neg'] = []
                G[tmp[SEQ_ID]] = []
                G[tmp[SEQ_ID]].append(X['pos'])
                G[tmp[SEQ_ID]].append(Y['neg'])

            #ulozeni na spravne misto do slovniku
            if tmp[SEQ_DIRECTION] == '+':
                G[tmp[SEQ_ID]][0].append(tmp)
            else:
                G[tmp[SEQ_ID]][1].append(tmp)
    
    #prochazeni slovniku a zpracovani vsech zaznamu v nem
    for i in G:
        if(len(G[i][1]) != 0):
            G[i][1].sort(key=sortStart)
            subProblems(G[i][1])
        if(len(G[i][0]) != 0):
            G[i][0].sort(key=sortStart)
            subProblems(G[i][0])
            
main()

