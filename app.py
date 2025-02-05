from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        print("❤️POST 방식으로 전송된 데이터" )
        
        str_amount=request.form.get("amount")
        amount= int(str_amount)

        print("받은금액 : ", amount)


        str_price=request.form.get("price")
        price=int(str_price)
        
        print(f"상품가격: , {price}")
        
        change= amount-price
        print("거스름돈: ", change)

        if change < 0:
            return render_template("index.html")
        
        WON_50000 = 50000
        WON_10000 = 10000   
        WON_5000 = 5000   
        WON_1000 = 1000 
        WON_500 = 500 
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10
        
        won_list = [WON_50000, WON_10000, WON_5000, WON_1000, WON_500,
                       WON_100, WON_50, WON_10]
        
    
        for won in won_list:
            print(won)

       
        won50000 = change // won_list[0] 
        won50000_nmg = change % won_list[0]
        won10000 = won50000_nmg // won_list[1] 
        won10000_nmg = won50000_nmg % won_list[1]
        won5000 = won10000_nmg // won_list[2] 
        won5000_nmg = won10000_nmg % won_list[2]
        won1000 = won5000_nmg // won_list[3] 
        won1000_nmg = won5000_nmg % won_list[3]
        won500 = won1000_nmg // won_list[4] 
        won500_nmg = won1000_nmg % won_list[4]
        won100 = won500_nmg // won_list[5]
        won100_nmg = won500_nmg % won_list[5] 
        won50 = won100_nmg // won_list[6]
        won50_nmg = won100_nmg % won_list[6]
        won10 = won50_nmg // won_list[7]

        
        for won in won_list:
            
            mok = change // won
            nmg = change % won
            change = nmg

            
            print(f"{won}원: {mok}개")
    
       
        
    
        return render_template("index.html",won50000 = won50000, won10000 = won10000,
                                won5000 = won5000, won1000 = won1000, amount = amount, won500=won500,
                                  won100=won100,won50=won50, won10=won10, price=price, change=change)
       
        
    else:
        print("😒GET 방식으로 전송된 데이터")
        return render_template("index.html")
    
    
if __name__ == '__main__':
     
   app.run('0.0.0.0',port=5000,debug=True)

   app.config['TEMPLATES_AUTO_RELOAD'] = True