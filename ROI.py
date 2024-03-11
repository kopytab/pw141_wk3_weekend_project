class ROI_calc():

    def __init__(self, tmi, tme, total_investment):
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
        self.cc_roi_calc
        print(f'Your Cash on Cash Return on Investment is {self.cc_roi}%')
        return self.cc_roi


duplex = ROI_calc(2000, 1610, 50000)

duplex.run()