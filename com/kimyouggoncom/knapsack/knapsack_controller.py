
from com.kimyouggoncom.knapsack.knapsack_model import KnapsackModel
from com.kimyouggoncom.knapsack.knapsack_service import KnapsackService


class KnapsackController:
    def __init__(self,**kwargs):
        self.max_capacity = kwargs.get("max_capacity")
        self.profit1 = kwargs.get("profit1")
        self.weight1 = kwargs.get("weight1")
        self.profit2 = kwargs.get("profit2")
        self.weight2 = kwargs.get("weight2")
        self.profit3 = kwargs.get("profit3")
        self.weight3 = kwargs.get("weight3")
        self.profit4 = kwargs.get("profit4")
        self.weight4 = kwargs.get("weight4")
    
    def getResult(self) -> KnapsackModel:
        service = KnapsackService()
        knapsack = KnapsackModel()
        knapsack.max_capacity =  self.max_capacity
        knapsack.profit1 =  self.profit1
        knapsack.weight1 =  self.weight1
        knapsack.profit2 =  self.profit2
        knapsack.weight2 =  self.weight2
        knapsack.profit3 =  self.profit3
        knapsack.weight3 =  self.weight3
        knapsack.profit4 =  self.profit4
        knapsack.weight4 =  self.weight4
        
        return service.execute(knapsack)
        
        