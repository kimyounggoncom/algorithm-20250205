from flask import Flask, render_template, request
from com.kimyouggoncom.exchange.exchange_controller import ExchangeController
from com.kimyouggoncom.exchange.exchange_model import ExchangeModel
from com.kimyouggoncom.knapsack.knapsack_controller import KnapsackController
from com.kimyouggoncom.knapsack.knapsack_model import KnapsackModel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dollar')
def exchange_dollar():
    return render_template("exchange_dollar.html")

@app.route('/won')
def exchange_won():
    return render_template("exchange_won.html")

@app.route('/yen')
def exchange_yen():
    return render_template("exchange_yen.html")

@app.route('/exchange', methods = ["POST", "GET"])
def exchange():
    if request.method == "POST":
        print("❤️POST 방식으로 전송된 데이터" )
        currency = request.form.get('currency') # USD, WON, JPY 상수
        amount=int(request.form.get("amount"))
        print("받은금액 : ", amount)

        controller = ExchangeController(amount=amount, currency=currency)

        resp: ExchangeModel = controller.getResult()

        render_html = '<h2>결과보기</h2>'
        render_html += resp.result
 
        return render_template(resp.page, render_html = render_html)
        
    else:
        print("😒GET 방식으로 전송된 데이터")
        return render_template("exchange_won.html")
    

@app.route('/knapsack', methods = ["POST", "GET"])
def knapsack():
    if request.method == "POST":
        print("❤️POST 방식으로 전송된 데이터" )
        max_capacity = int(request.form.get('max_capacity')) 
        profit1 = int(request.form.get('profit1')) 
        weight1 = int(request.form.get('weight1'))
        profit2 = int(request.form.get('profit2'))
        weight2 = int(request.form.get('weight2'))
        profit3 = int(request.form.get('profit3'))
        weight3 = int(request.form.get('weight3'))
        profit4 = int(request.form.get('profit4'))
        weight4 = int(request.form.get('weight4'))
        
        controller = KnapsackController(max_capacity=max_capacity,profit1=profit1,
                                        weight1=weight1, profit2=profit2, weight2=weight2, profit3=profit3, 
                                        weight3=weight3, profit4=profit4, weight4=weight4)

        resp: KnapsackModel = controller.getResult()

        render_html = '<h2>결과보기</h2>'
        render_html += f"{resp.total_profit}"
    
 
        return render_template("knapsack.html", render_html = render_html)
        
    else:
        print("😒GET 방식으로 전송된 데이터")
        return render_template("knapsack.html")


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True