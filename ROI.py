class ROI_calc():
    
    def __init__(self):
        tmi = int(input('What is your total montly income? '))
        tme = int(input('What is your total montly expenses? '))
        total_investment = int(input('What is your total investment in the property? '))
        self.tmi = tmi
        self.tme = tme
        self.cash_flow = tmi - tme
        self.acf = self.cash_flow * 12
        self.total_investment = total_investment
        self.roi = self.acf / self.total_investment
        self.cc_roi = self.roi * 100
    

    
    def cc_roi_calc(self):
        self.roi = self.acf / self.total_investment
        self.cc_roi = self.roi * 100
        
        return self.roi
    
    def run(self):
        self.tmi
        self.tme
        self.total_investment
        self.cc_roi_calc
        print(f'Your Cash on Cash Return on Investment is {self.cc_roi}%')
        return self.cc_roi


duplex = ROI_calc()

duplex.run()