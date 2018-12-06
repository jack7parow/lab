import csv
import math
def mean(numbers):
    return sum(numbers)/len(numbers)
def stdev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2) for x in numbers])/(len(numbers)-1)
    return math.sqrt(variance)
def summarize(dataset):
    summaries=[(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries
def calcprob(summary,item):
    prob=1
    for i in range(len(summary)):
        x=item[i]
        mean,stdev=summary[i]
        exponent=math.exp(-pow(x-mean,2)/(2*stdev**2))
        final=exponent/(math.sqrt(2*math.pi)*stdev)
        prob*=final
    return prob
file=open('pima-indians-diabetes.csv','r')
data=list(csv.reader(file))
for i in range(len(data)):
    data[i]=[float(x) for x in data[i]]
split=int(0.90*len(data))
train=data[:split]
test=data[split:]
yes=[]
no=[]
for i in range(len(train)):
    if data[i][-1]==0:
        no.append(data[i])
    else:
        yes.append(data[i])
yes=summarize(yes)
no=summarize(no)
predictions=[]
for item in test:
    yesprob=calcprob(yes,item)
    noprob=calcprob(no,item)
    predictions.append(1 if(yesprob>noprob) else 0)
correct=0
for i in range(len(test)):
    if (test[i][-1]==predictions[i]):
        correct+=1
print('\n actual values\n')
for i in range(len(test)):
    print(test[i][-1],end=" ")
print('\npredicted values')
for i in range(len(predictions)):
    print(predictions[i],end=" ")
print('\naccuracy is:%.1f%%'%((correct/len(test))*100))
