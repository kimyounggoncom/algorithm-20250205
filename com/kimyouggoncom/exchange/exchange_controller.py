
from com.kimyouggoncom.exchange.exchange_model import ExchangeModel
from com.kimyouggoncom.exchange.exchange_service import ExchangeService


class ExchangeController:
    def __init__(self,**kwargs):
        self.amount = kwargs.get('amount')
        self.currency = kwargs.get("currency")
        
        
    
    def getResult(self)-> ExchangeModel:
        service = ExchangeService()
        exchange = ExchangeModel()
        exchange.amount = self.amount
        exchange.currency = self.currency
        return service.execute(exchange)
           
