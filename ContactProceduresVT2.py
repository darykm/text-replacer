

#file_name = input('Enter file: ')
fhandle = open('contact_procedures.txt', 'r')

# variables
# time_of_day = 'Day' #could be improved with additional functionality to determine if morning or afternoon or evening
caregiver = input('What is CGs name? : ')  #would be nice to be able to pull this data directly from service-now
ticketnumber = input('What is ticket #? : ') #would be nice to be able to pull this data directly from service-now
#myname = input('What is my name? : ')  #can be hardcoded per tech
#myphone = input('What is my phone #? : ') #can be hardcoded per tech
#myhours = input('When do I work?: ')
myhours = 'M-F, 7:00am to 4:00pm PST'
myname = 'Daryk McCoy'
myphone = '503-922-6024'
issue = input('What is the issue regarding? : ') #would be nice to be able to pull this data directly from service-now

list = []

for line in fhandle:
    line = line.rstrip()
    #print(line)
    #line = line.replace('TIMEOFDAY', time_of_day)
    line = line.replace('TICKETNUMBER', ticketnumber)
    line = line.replace('CAREGIVER', caregiver)
    line = line.replace('MYNAME', myname)
    line = line.replace('MYPHONE', myphone)
    line = line.replace('MYHOURS', myhours)
    line = line.replace('ISSUE', issue)
    print(line)
    #list.append(line)

# print(list)  
# Next improvement needs to be creating a new file and writing to it what is printing out for "line".  Attempted code below but it wasn't formatted correcty 
# newfile = open('new_contactprocedures.txt', 'a')
# newfile.write(str(list))
# newfile.close()

    
