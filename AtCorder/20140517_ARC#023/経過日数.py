year=int(raw_input())
month=int(raw_input())
day=int(raw_input())
if(month==1 or month==2):
	month = month+12
	year = year-1
print(735369-(365*year+year/4-year/100+year/400+306*(month+1)/10+day-429))