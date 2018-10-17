import random
from parking_space import ps001

class OrderForm():
    result = 0
    def __init__(self,of_number,of_pay_money,
                of_create_time,of_mode_pay,of_pay_state):
        self.of_number = of_number
        self.of_pay_money = of_pay_money
        self.of_create_time = of_create_time
        self.of_mode_pay = of_mode_pay
        self.of_pay_state = of_pay_state
    
    @classmethod
    def payMoney(self):
        A = random.randint(1,10)*ps001.ps_price
        return A

    @classmethod
    def ofNumber(self):
        OrderForm.result += 1
        return OrderForm.result
    
    def getorder(self):
        return '''订单编号：\t'''+str(OrderForm.result)+'''
                \n付款金额：\t'''+str(self.of_pay_money)+'''
                \n生成时间：\t'''+str(self.of_create_time)+'''
                \n支付方式：\t'''+self.of_mode_pay+'''
                \n支付状态：\t'''+self.of_pay_state
                
    
