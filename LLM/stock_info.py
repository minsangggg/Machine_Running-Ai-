import pandas as pd
import yfinance as yf

class StockInfo():
    def __init__(self,symbol):
        self.symbol=symbol
        self.ticker=yf.Ticker(symbol)
        
    
    
    def get_basic_info(self):
        basic_info=pd.DataFrame.from_dict(
        self.ticker.info, orient='index', columns=['Value']
        )
        
        return basic_info.loc[['longName', 
                               'industry', 
                               'sector', 
                               'marketCap', 
                               'sharesOutstanding']].to_markdown()
    
            
    def get_financial_statement(self):
        pass
    
    
if __name__=="__main__":
    stock=StockInfo("MSFT")
    print(stock.get_basic_info())
