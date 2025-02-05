from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        print("❤️POST 방식으로 전송된 데이터" )
        
        str_amount=request.form.get("amount")
        amount= int(str_amount)

        print("받은금액 : ", amount)


        str_price=request.form.get("price")
        price=int(str_price)
        
        print(f"상품가격: ", price)
        
        change= amount-price
        print("거스름돈: ", change)
        if change <0:
            return render_template("index.html")
            


        COIN_500=500 # 상수는 대문자_ 형식으로 보통 선언함
        coin500=change//COIN_500 # 몫 구하는 연산자 //
        coin500_nmg=change%COIN_500 # 나머지 구하는 연산자 %
        
        
        COIN_100=100
        coin100=coin500_nmg//COIN_100
        coin100_nmg=coin500_nmg%COIN_100

        COIN_50=50
        coin50=coin100_nmg//COIN_50
        coin50_nmg=coin100_nmg%COIN_50

        COIN_10=10
        coin10=coin50_nmg//COIN_10
        coin10_nmg=coin50_nmg%COIN_10

        

        
        
        
        
        return render_template("index.html",amount=amount, coin500=coin500, coin100=coin100,coin50=coin50, coin10=coin10, price=price, change=change)
       
        print("500원: ", )
    else:
        print("😒GET 방식으로 전송된 데이터")
        return render_template("index.html")
    
    

    

    



if __name__ == '__main__':
     
   app.run('0.0.0.0',port=5000,debug=True)

   app.config['TEMPLATES_AUTO_RELOAD'] = True