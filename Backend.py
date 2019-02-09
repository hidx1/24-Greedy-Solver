from random import randint

def symbol_switch(arg):
    if (arg == 1):
        return "H"
    elif (arg == 2):
        return "C"
    elif (arg == 3):
        return "D"
    else:
        return "S"

class Cards:
    def __init__(self, num, sym):
        self.num = num
        self.sym = sym

class BackEnd():
    def __init__(self, deck, scoreList):
        self.scoreList = {'+':5, '-':4, '*':3, '/':2}
        self.deck = []
    def getNums(self):
        nums = []
        for _ in range(4):
            cards_remaining = len(self.deck)
            idx = randint(0,cards_remaining-1)
            nums.append(self.deck[idx])
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
        for i in range (0,len(listNum)):
            max = -50
            for key, val in self.scoreList.items():
                cExpr = expr
                cExpr += key
                cExpr += str(listNum[i])
                if self.calcPoint(cExpr) > max:
                    max = self.calcPoint(cExpr)
                    choice = cExpr
            expr = choice
        points = self.calcPoint(expr)
        expr = expr + ' = ' + str(eval(expr))
        return expr, points
        
    def calcPoint(self,expr):
        result = eval(expr)
        score = 0
        for key, val in self.scoreList.items():
            score += expr.count(key)*val
        score -= abs(result-24)
        return score

