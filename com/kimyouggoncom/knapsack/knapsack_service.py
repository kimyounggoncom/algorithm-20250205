
from com.kimyouggoncom.knapsack.knapsack_model import KnapsackModel


class KnapsackService:
    def __init__(self):
        pass

    def execute(self, knapsack: KnapsackModel) -> KnapsackModel:
        max_capacity = knapsack.max_capacity
        profit1 = knapsack.profit1
        weight1 = knapsack.weight1
        profit2 = knapsack.profit2
        weight2 = knapsack.weight2
        profit3 = knapsack.profit3
        weight3 = knapsack.weight3
        profit4 = knapsack.profit4
        weight4 = knapsack.weight4


        # weight4 = knapsack.weight4 #property getter
        # knapsack.weight4 = weight4 #property setter
        # weight4 = knapsack.get("weight4")# attribute getter
        # weight4 = knapsack["weight4"] #attribute getter
        # knapsack["weight4" ] = weight4 #attribute setter

        # itm1 = ItemModel()
        # itm1.name = "item1"
        # itm1.profit = profit1
        # itm1.weight = weight1
        # itm1.profit_per_weight = profit_per_weight[0]

        item1 = {"profit":profit1, "weight":weight1}
        item2 = {"profit":profit2, "weight":weight2}
        item3 = {"profit":profit3, "weight":weight3}
        item4 = {"profit":profit4, "weight":weight4}
        
        items = [item1, item2, item3, item4]

        for i in range(4):
            items[i]["name"] = f"item{i+1}"
            items[i]["profit_per_weight"] = items[i].get("profit") / items[i].get("weight")
            
        print("item")

        # for i in items:
        #     i["name"] = f"item{i+1}"

        # temp = []
        # for i in range(4):
        #     temp.append(profit_list[i] / weight_list[i])
        # print("😒temp:", temp)
        # temp = [4, 2, 3, 5]
        # profit_per_weight = [temp[0], temp[1], temp[2], temp[3]]

        for i in range(4):
           for j in range(i+1, 4):
              if items[i].get("profit_per_weight") < items[j].get("profit_per_weight"):
                 items[i], items[j] = items[j], items[i]

        for i in items:
           print("😒💰", i.get("name"))

        remain_weight = max_capacity
        total_profit = 0

        for i in range(4):
            # 3, 4, 4, 2 -> 10, 7, 3, 0
            if items[i].get("weight") <= remain_weight:
                remain_weight -= items[i].get("weight")
                total_profit += items[i].get("profit")
                continue
            else:   
                fraction = remain_weight / items[i].get("weight")  
                total_profit += items[i].get("profit") * fraction  
                remain_weight = 0  # 배낭이 꽉 차므로 종료
                break
                
        print('😒😒',total_profit)
        
        knapsack.total_profit = total_profit

        
        return knapsack        

           
           
               

        

        

        
        
