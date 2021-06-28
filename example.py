from datetime import datetime
timelive = '2021-06-28 13:50:59'

timelive = datetime.strptime(timelive,"%d/%m/%Y %H:%M:%S")

print(timelive)