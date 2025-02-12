from flask import Flask, render_template, request
from com.kimyouggoncom.exchange.exchange_controller import ExchangeController
from com.kimyouggoncom.exchange.exchange_model import ExchangeModel

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

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True