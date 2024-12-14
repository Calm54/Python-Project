'''
PYTHON PROJECT:

*Appointment Scheduling System*: Create a system for scheduling and managing appointments.
Include features for booking,rescheduling, and canceling appointments, as well as viewing schedules.

1. Create user login
2. Login User
3. User chooses schedule

'''

#USER LOGIN:
PatientID = []
User = input('Enter your four Patient ID: ' ).upper()
PatientID.append(User)

print(' ')

def Task():
    import calendar
    import datetime
    PID = PatientID
    print('Welcome', PatientID, 'how can we help you today')
    print(' ')

    print('1. Book Appointment')
    print('2. Reschedule Appointment')
    print('3. Cancel Appointment')
    print('4. Exit')
    print(' ')

    while True:
        
        task = int(input('Select an Option: '))
        
        if task == 1:
            cur_datetime = datetime.datetime.now()
            year = cur_datetime.year
            month = cur_datetime.month
            print(calendar.month(year,month))
            DesiredDate = int(input('Enter desired Date: '))
            print('Your Appointment has been Confirmed for: ', DesiredDate, 'Aug. 2024')
            print(' ')
            print('Would you like to do something else?')
            print('1. Yes')
            print('2. No')

            something_else = int(input('Choice: '))


            if something_else == 1:
                Task()
            elif something_else == 2:
                print('GoodBye!')
                break
        
        elif task == 2:
            print('Are you sure you want to reschedule?, previous date would be lost')
            print(' ')
            print('1. Yes, proceed')
            print('2. No, do not proceed')
            choice = int(input('Choice: '))
            

            if choice == 1:
                print(' ')
                print('Choose New Date')
                print(' ')
                cur_datetime = datetime.datetime.now()
                year = cur_datetime.year
                month = cur_datetime.month
                print(calendar.month(year,month))
                DesiredDate = int(input('Enter desired Date: '))
                print('Your Appointment has been Confirmed for: ', DesiredDate, 'Aug. 2024')
                print(' ')
                break
            elif choice == 2:
                print('Thanks for confirming!')
            break

        elif task == 3:
            print('Your Appointmrnt will be cacelled')
            print(' ')
            print('1. Yes, proceed')
            print('2. No, do not proceed')
            print(' ')
            confirm = int(input('Choice: '))
           

            if confirm == 1:
                print('Your Appointment has now been Canceled, Thanks!')
                break
            elif confirm == 2:
                break
            
        elif task == 4:
            print('See you later, GoodBye!')
            break
        
                         
           
            
Task()
