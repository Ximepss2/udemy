#We want the tittle, the price, the suscribers
#reviews, percent of review,length
import csv 
import os #operative sistem

#udemy_csv = "./resources/web_starter.csv"
udemy_csv = os.path.join(".","resources","web_starter.csv")

#with open(udemy_csv,"r",encoding="UTF-8") as csvfile:
  #  csvreader = csv.reader(csvfile,delimiter=",")

 #   test=next(csvreader)

#print(test)

title =[]
price=[]
subscribers=[]
reviews=[]
reviews_percent=[]
length=[]

with open(udemy_csv,"r",encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        #add tittle
        title.append(row[1])
        #add price
        price.append(row[4])
        #add subscribers
        subscribers.append(row[5])
        #reviews
        reviews.append(row[6])
        #percent of reviews
        percent = round(int(row[6])/int(row[5]),2)
        reviews_percent.append(percent)
        #lenght
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

cleanCsv=zip(title,price,subscribers,reviews,reviews_percent,length)

outputFile=os.path.join("webFinal.csv")

with open(outputFile,"w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title","CoursePrice","Subscribers","Reviews","Percent of Reviews","Length of Course"])
    writer.writerows(cleanCsv)

#print(title)