#!/usr/bin/python3

class Egg:
    def __init__(self, kind='fried'):
        self.kind = kind
    
    def getKind(self):
        return self.kind

def main():
    egg = Egg()
    print(egg.getKind())

if __name__ == '__main__': main()
