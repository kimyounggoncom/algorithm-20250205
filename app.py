from flask import Flask, render_template, request

app = Flask(__name__)

def get_unit_count(amount, won_list): 
    money = amount 
    won_dict = {}
    for won in won_list:
        won_dict[won] = money // won
        money %= won
    return won_dict
    
@app.route('/', methods=["GET","POST"])
def index():

    amount = None
    price = None
    mok = None
    nmg = None
    result = None

    if request.method == "POST":

        print("❤️POST 방식으로 전송된 데이터" )
        
        amount=int(request.form.get("amount"))
        

        print("받은금액 : ", amount)


        price=int(request.form.get("price"))
        
        
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
        
        won_list = [WON_50000, WON_10000, WON_5000, WON_1000, WON_500,
                       WON_100, WON_50, WON_10]
    
        won_dict = get_unit_count(amount, won_list)

        for won, count in won_dict.items():
            print(f"{won}원: {count}개")
        
        render_html = '<h2>결과보기</h2>'
        for won, count in won_dict.items():
            render_html += f"{won}원: {count}개<br/>" # 줄바꿔라 

        return render_template("index.html", render_html = render_html)
    
                                
        
    else:
        print("😒GET 방식으로 전송된 데이터")
        return render_template("index.html")
    
    
if __name__ == '__main__':
     
   app.run('0.0.0.0',port=5000,debug=True)

   app.config['TEMPLATES_AUTO_RELOAD'] = True