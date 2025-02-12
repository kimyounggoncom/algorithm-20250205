
from com.kimyouggoncom.exchange.exchange_model import ExchangeModel


class ExchangeService:
    def __init__(self):
        pass

    def execute(self, exchange: ExchangeModel) -> ExchangeModel:
        currency_list= []
        currency_unit= ""
        page = ''
        print("😒", exchange.currency)
        if exchange.currency == 'USD':
            currency_list = self.get_dollar_list()
            currency_unit = "달러"
            page = "exchange_dollar.html"
        elif exchange.currency =='WON':
            currency_list = self.get_won_list()
            currency_unit = '원'
            page = "exchange_won.html"
        else:
            print("잘못된 화폐단위입니다.")
        
        exchange.page = page
        currency_dict = self.get_currency_dict(exchange.amount, currency_list)
        self.print_currency_dict(currency_dict, currency_unit)
        exchange.result = self.format_currency_counts(currency_dict, currency_unit)
        return exchange 
    
    def get_currency_dict(self, amount, currency_list):
        money = amount
        currency_dict ={}
        for currency in currency_list:
            currency_dict[currency] = money // currency
            money %= currency 
        return currency_dict
    
    def print_currency_dict(self, currency_dict, currency_unit):
        print("----------거스름돈-----------" )
        for currency, count in currency_dict.items():
            print(f"{currency}{currency_unit}: {count}개")
        print("-------끝-------")

    def get_won_list(self):
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
                       
        return won_list
    
    def get_dollar_list(self):
        DOLLAR_100 = 100
        DOLLAR_50 = 50
        DOLLAR_20 = 20
        DOLLAR_10 = 10
        DOLLAR_5 = 5
        DOLLAR_2 = 2
        DOLLAR_1 = 1
        
        dollar_list = [DOLLAR_100, DOLLAR_50, DOLLAR_20, 
                       DOLLAR_10, DOLLAR_5, DOLLAR_2, DOLLAR_1]
                    
        return dollar_list

    def format_currency_counts(self, currency_dict, currency_unit):
        temp = ""
        for currency, count in currency_dict.items():
            print("💰",currency)
            temp += f"{currency}{currency_unit}: {count}개<br/>"
        return temp
       

