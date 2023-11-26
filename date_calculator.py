month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
months={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
total_days_year=0


for i in month_days:
    total_days_year+=i
    
print('Month:Total days')

for i in months:
    
    print(i,':',month_days[months.get(i)-1])    
    
open=True
while open:
    


    counter=0
    days_passed_year1=0
    days_passed_year2=0
    try:
        
        choose=input('Type "E" to close the program or Type "C" to continue:')
        if choose.upper()=='E':
            print('Have a nice day')
            open=False
        elif choose.upper()=='C':
            
         print('From:')
         date_1=input('Month_name Day_number Year(example:june 12 2023):').split(' ') 

         if len(date_1)!=3:
            print('The date must have three arguments!')

         elif date_1[0].lower() not in months :
    
            print('The month name is incorrect!')
            
         elif int(date_1[1])<=0  :
             
            print('Invalid value for day!')
         elif int(date_1[2])<=0:
            print('Invalid value for year!')   
         else:
                
          for i in date_1:
            if months.get(i.lower())==1:
                if int(date_1[1])>31:
                    print('Invalid value')
                    break
            elif months.get(i.lower())==2:
                if int(date_1[1])>28:
                    print('Invalid value')
                    break

            elif months.get(i.lower())==3:
                if int(date_1[1])>31:
                    print('Invalid value')
                    break  




            elif months.get(i.lower())==4:
                if int(date_1[1])>30:
                    print('Invalid value')
                    break  







            elif months.get(i.lower())==5:
                if int(date_1[1])>31:
                    print('Invalid value')
                    break  




            elif months.get(i.lower())==6:
                if int(date_1[1])>30:
                    print('Invalid value')
                    break  



            elif months.get(i.lower())==7:
                if int(date_1[1])>31:
                    print('Invalid value')
                    break  



            elif months.get(i.lower())==8:
                if int(date_1[1])>31:
                    print('Invalid value')
                    break


            elif months.get(i.lower())==9:
                if int(date_1[1])>30:
                    print('Invalid value')
                    break  






            elif months.get(i.lower())==10:
                if int(date_1[1])>31:
                    print('Invalid value')
                    break  




            elif months.get(i.lower())==11:
                if int(date_1[1])>30:
                    print('Invalid value')
                    break
                


            elif months.get(i.lower())==12:
                if int(date_1[1])>31:
                    print('Invalid value')
                    break  



                
                    
          else:
            while True:
                try:
                    
                
                    print('To:')
                    date_2=input('Month_name Day_number Year(example:march 23 2020):').split(' ')
                    if len(date_2)!=3:
                        print('The date must have three arguments!')
                    elif date_2[0].lower() not in months :
    
                        print('The month name is incorrect!')
            
                    elif int(date_2[1])<=0 :
                        print('Invalid value for day!')
                    elif int(date_2[2])<=0:
                        print('Invalid value for year!')    
                    else:
                            
                     for i in date_2:
                        if months.get(i.lower())==1:
                            
                            
                            if int(date_2[1])>31:
                                
                                print('Invalid value')
                                break
                        elif months.get(i.lower())==2:
                            if int(date_2[1])>28:
                                print('Invalid value')
                                break

                        elif months.get(i.lower())==3:
                            if int(date_2[1])>31:
                                print('Invalid value')
                                break  




                        elif months.get(i.lower())==4:
                            if int(date_2[1])>30:
                                print('Invalid value')
                                break  







                        elif months.get(i.lower())==5:
                            if int(date_2[1])>31:
                                print('Invalid value')
                                break  




                        elif months.get(i.lower())==6:
                            if int(date_2[1])>30:
                                print('Invalid value')
                                break  



                        elif months.get(i.lower())==7:
                            if int(date_2[1])>31:
                                print('Invalid value')
                                break  



                        elif months.get(i.lower())==8:
                            if int(date_2[1])>31:
                                print('Invalid value')
                                break


                        elif months.get(i.lower())==9:
                            if int(date_2[1])>30:
                                print('Invalid value')
                                break  






                        elif months.get(i.lower())==10:
                            if int(date_2[1])>31:
                                print('Invalid value')
                                break  




                        elif months.get(i.lower())==11:
                            if int(date_2[1])>30:
                                print('Invalid value')
                                break
                


                        elif months.get(i.lower())==12:
                            if int(date_2[1])>31:
                                print('Invalid value')
                                break  

                        
                                    
                        
                        

                                                

                     else:
                        for i in month_days:
                            counter+=1
                            if counter<months.get(date_1[0].lower()):
                                days_passed_year1+=i
                            if counter<months.get(date_2[0].lower()):
                                days_passed_year2+=i
                            
                            
                        total_days_passed_1=(int(date_1[2])*total_days_year)+(days_passed_year1+int(date_1[1]))
                        total_days_passed_2=(int(date_2[2])*total_days_year)+(days_passed_year2+int(date_2[1]))
                        days_between_dates_passed=abs(total_days_passed_1-total_days_passed_2)
                        print(f'Difference(days)={days_between_dates_passed}')
                        if abs(int(date_1[2])-int(date_2[2]))>=1:
                            print(f'Difference(years)={abs(int(date_1[2])-int(date_2[2]))}')
                            print(f'Difference(months)={(abs(months.get(date_1[0].lower())-months.get(date_2[0].lower())))+((abs(int(date_1[2])-int(date_2[2])))*12)}')
                        else:
                            print(f'Difference(months)={abs(months.get(date_1[0].lower())-months.get(date_2[0].lower()))}')
                        break
                        



                        
                except ValueError:
                    print('The value of the day and year must be integers!')


        else:
            print('Wrong command!')

            
    except ValueError:
        print('The value of the day and year must be integers!')