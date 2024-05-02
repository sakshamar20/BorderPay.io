from celery import Celery, shared_task
from .models import Contract_Requests
from .models import Employee
import time

@shared_task(bind= True)
def print_hey(self):
  while True:
    # start = time.time()
  
      
      contracts = Contract_Requests.objects.all()
      
      for contract in contracts:
        
        try:
             employee = Employee.objects.get(username = contract.username_ee)
        except Employee.DoesNotExist:
            continue
        
        contract.timer-=1
        
        if contract.timer==0:
          contract.timer = contract.interval
          employee.worked_amount += contract.salary
        
          if employee.worked_amount - employee.given_amount > 0:
        
            if contract.type == 'regular':
              pass
            #   make transaction
        
            else:
              employee.withdraw_amount += contract.salary
              employee.given_amount += contract.salary
        
        contract.save()
        employee.save()


    

    
