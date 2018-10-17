from car import car_baoma
class ParkingRecord():  #停车记录
    result = 0    #（停车记录编号）汽车ID
    def __init__(self,pr_car_id,pr_car_number,
                pr_entertime_record,pr_starttime_record,
                pr_endtime_record,pr_leavetime_record):  
        self.pr_car_id = pr_car_id
        self.pr_car_number = pr_car_number
        self.pr_entertime_record = pr_entertime_record
        self.pr_starttime_record = pr_starttime_record
        self.pr_endtime_record = pr_endtime_record
        self.pr_leavetime_record = pr_leavetime_record
    
    @classmethod
    def createCarId(self):
        ParkingRecord.result +=1
        return ParkingRecord.result
    def getRecord(self):
        return  '''车编号：\t'''+str(pr1.pr_car_id)+'''
                \n车牌号码：\t'''+str(pr1.pr_car_number)+'''
                \n进入时间：\t'''+pr1.pr_entertime_record+'''
                \n开始时间：\t'''+pr1.pr_starttime_record+'''
                \n结束时间：\t'''+pr1.pr_endtime_record+'''
                \n离开时间：\t'''+pr1.pr_leavetime_record
                
# pr1 = ParkingRecord(car_baoma.car_id,car_baoma.car_number,
#                     '无记录','无记录','无记录','无记录')
pr1 = ParkingRecord(1,1,'无记录','无记录','无记录','无记录')
