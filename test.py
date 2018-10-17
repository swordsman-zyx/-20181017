import random
from parking_lot import pl_carrefour,pl_tesco
from parking_record import pr1
from car import car_baoma,car_benchi
from order_form import OrderForm
import datetime
while True:    
    a = random.randint(1,2)
    if a == 1:
        parking_lot = pl_carrefour
    else:
        parking_lot = pl_tesco
    if parking_lot.pl_free_carport>=1:
        print('剩余停车位数：'+str(parking_lot.pl_free_carport))
        input('输入任意字符，表示进入停车场：')
        parking_lot.countFreeCarportenter()
        print('汽车已经进入')
        #停车记录获取信息
        car_random = random.randint(1,2)
        # print(car_random)
        if car_random == 1:
            car = car_baoma
        else:
            car = car_benchi

        pr1.pr_car_number = car.car_number
        pr1.pr_car_id = pr1.createCarId()
        pr1.pr_entertime_record = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#进入车场记录

        # input('输入任意字符，表示已停到车位上：')
        print('已停到车位上')
        pr1.pr_starttime_record = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#停到车位记录


        # input('输入任意字符，表示已离开车位上：')
        print('已离开车位上')

        pr1.pr_endtime_record = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#离开车位记录

        # input('输入任意字符，表示生成订单：')    
        or_create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            

        of1 = OrderForm(OrderForm.ofNumber(),OrderForm.payMoney(),or_create_time,'选择支付方式','未支付')
        print('---------------')
        print(of1.getorder())
        print('---------------')

        of1.of_mode_pay = input('输入支付方式：')
        print('---------------')
        print(of1.getorder())
        print('---------------')
        of1.of_pay_state = '已支付'
        print('---------------')
        print(of1.getorder())
        print('---------------')

        input('输入任意字符，表示已离开停车场：')
        print('已离开停车场')
            
        pr1.pr_leavetime_record = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#离开车位记录

        print('---------------')
        print(pr1.getRecord())
        print('---------------')
        print(parking_lot.pl_name)
        print(car.car_carowner.owner_name)
        parking_lot.countFreeCarportleave()
        if input() == '1':
            break
    else:
        print('车位已满')