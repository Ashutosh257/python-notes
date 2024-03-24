
# python3 abstract_classes.py  

from abc import ABC, abstractmethod

class Processor(ABC):

    @abstractmethod
    def get_balance():
        pass

    @abstractmethod
    def get_rate_of_interest():
        pass

class HDFC(Processor):

    def __init__(self) -> None:
        self.interest = 10.5
        self.balance = 4000
    
    def get_balance(self):
        return self.balance

    def get_rate_of_interest(self):
        return self.interest
    

class ICICI(Processor):
    def __init__(self) -> None:
        self.interest = 13.5
        self.balance = 9000
    
    def get_balance(self):
        return self.balance

    def get_rate_of_interest(self):
        return self.interest

def main():
    hdfc = HDFC()
    print(hdfc.get_rate_of_interest())

if __name__ == "__main__":
    main()