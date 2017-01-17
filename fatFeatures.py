# those classes use pandas
import pandas as pd
import time
__author__ = 'FanGhost'
__date__ = '2017/1/17'
class fatFeatures(object):
    def __init__(self,fileName = 'data.csv'):
        self.data = pd.read_csv(fileName)

    def changeVal(self,col = ['month','day']):
        for i in col:
            ser = self.data[i]
            s= ser.unique()
            s.sort()
            m = dict(zip(s,range(1,len(s)+1)))
            #self.data[i] = ser.replace(s,range(1,len(s)+1))
            self.data[i] = self.data[i].map(m)
        return m
    def oneHot(self,col = ['month','day'], drop = True):
        #df = self.data[col]
        flag = []
        flag.append(self.data)
        for i in col:
            df = self.data[i]
            flag.append(pd.get_dummies(df,prefix=i))
        if drop:
            self.data.drop(col,axis=1,inplace=True)
                #self.data[nd.columns] = nd
        self.data = pd.concat(flag, axis=1)



if __name__ ==  '__main__':
    f = fatFeatures(fileName ='forestfires.csv')
    start = time.clock()
    f.changeVal()
    end = time.clock()

    print "time: %f s" % (end - start)
    #print f.data
    print('------------------')
    start = time.clock()
    f.oneHot()
    end = time.clock()
    print f.data
    print "time: %f s" % (end - start)


