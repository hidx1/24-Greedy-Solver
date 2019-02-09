from random import randint, sample

def symbol_switch(arg):
    listSym = ["H","C","D","S"]
    return listSym[arg-1]

class Cards:
    def __init__(self, num, sym):
        self.num = num
        self.sym = sym

class BackEnd():
    def __init__(self, deck, scoreList):
        self.scoreList = {'+':5, '-':4, '*':3, '/':2}
        self.deck = []

    def getNums(self):
        availableIndex = sorted(list(sample(range(0,len(self.deck)),4)),reverse=True)
        nums = [self.deck[idx] for idx in availableIndex]
        for idx in availableIndex:
            del self.deck[idx]
        return nums

    def reset(self):
        self.deck = [None] * 52
        self.reset_deck()

    def reset_deck(self):
        sym_num = 0
        for i in range(52):
            if (i % 13 == 0):
                sym_num += 1
            self.deck[i] = Cards(((i % 13) + 1), symbol_switch(sym_num))

    def solution(self,listNum):
        listNum.sort()
        expr = str(listNum.pop(0))
        for num in listNum:
            maxPoint = -50
            for key, val in self.scoreList.items():
                cExpr = expr + key + str(num)
                if self.calcPoint(cExpr) > maxPoint:
                    maxPoint = self.calcPoint(cExpr)
                    choice = cExpr
            expr = choice
        expr = expr + ' = ' + str(eval(expr))
        return expr, maxPoint
        
    def calcPoint(self,expr):
        result = eval(expr)
        score = -abs(result-24)
        for key, val in self.scoreList.items():
            score += expr.count(key)*val
        return score

