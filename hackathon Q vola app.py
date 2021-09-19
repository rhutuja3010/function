print("WELCOME TO VOLA TRAVELS")
current_location=["palghar","pune","relway", "station","mumbai","boriwali","virar","andheri"]
dropping_point=["palghar bus stand","katraj","pune","khed shiivapur"]

driver1st = [driver_name==["ram"],car_colour==["white"],driver_current_location==["lonavala"],time==["1 hour"],
mobile_number==["9045231462"],feedback==["good,frindly","responcible driving","good service"],rate==["300"]]

driver2nd = [driver_name==["om"],car_colour==["gray"],driver_current_location==["shivajinagar"],time==["2 hour"],
mobile_number==["7012367858"],feedback==["responcible driving"],rate==["350"]]

driver3rd=[driver_name==["yash"],car_colour==["blue"],driver_current_location==["pune city"],time==["3 hour"],
mobile_number==["7089453623"],feedback==["nice","good service"],rate==["400"]










current_location1=input("enter the current location")
i=0
while i<len(current_location):
    if current_location1 in current_location[i]:
        print("available")
    else:
        print("not available")
    i+=1
        
    
# dropping_point(input("enter the dropping point"))
# driver_name=
