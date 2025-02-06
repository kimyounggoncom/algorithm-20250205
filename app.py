from flask import Flask, render_template, request

app = Flask(__name__)

def get_unit_count(change, unit_list): 
    money = change
    unit_dict = {}

    for unit in unit_list:
        unit_dict[unit] = money // unit
        money %= unit
    return unit_dict


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/exchange_won', methods = ["POST", "GET"])
def exchange_won():
    
    # amount = None
    # price = None
    
    if request.method == "POST":

        print("❤️POST 방식으로 전송된 데이터" )
        
        amount=request.form.get("amount")
        print("받은금액 : ", amount)
        price=request.form.get("price")
        amount, price = int(amount), int(price)
        
        print(f"상품가격:  {price}")
        
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
        
        unit_list = [WON_50000, WON_10000, WON_5000, WON_1000, WON_500,
                       WON_100, WON_50, WON_10]
    
        unit_dict = get_unit_count(change, unit_list)

        for won, count in unit_dict.items():
            print(f"{won}원: {count}개")
        
        render_html = '<h2>결과보기</h2>'
        for won, count in unit_dict.items():
            render_html += f"{won}원: {count}개<br/>" # 줄바꿔라 

        return render_template("exchange_won.html", render_html = render_html)
        
    else:
        print("😒GET 방식으로 전송된 데이터")
        return render_template("exchange_won.html")

    
@app.route('/exchange_dollar', methods = ["POST", "GET"])
def exchange_dollar():
    
    
    
    if request.method == "POST":

        print("❤️POST 방식으로 전송된 데이터" )
        
        amount=request.form.get("amount")
        

        print("받은금액 : ", amount)


        price=request.form.get("price")
        
        amount, price = int(amount), int(price)
        
        print(f"상품가격: {price}")
        
        change= amount-price
        print("거스름돈: ", change)

        if change < 0:
            return render_template("index.html")
        
        unit_list = [100, 50, 10, 5, 1]
    
        unit_dict = get_unit_count(change, unit_list)

        
        dollar_html = '<h2>결과보기</h2>'
        for dollar, count in unit_dict.items():
            dollar_html += f"{dollar}달러: {count}개<br/>" # 줄바꿔라 

        return render_template("exchange_dollar.html", dollar_html = dollar_html)
        
    else:
        print("😒GET 방식으로 전송된 데이터")
        return render_template("exchange_dollar.html")
    

if __name__ == '__main__':
     
   app.run('0.0.0.0',port=5000,debug=True)

   app.config['TEMPLATES_AUTO_RELOAD'] = True