

#

library(caret)
library(e1071)

data = read.csv('/Users/krista/Desktop/TOm/AI/LAB/ML/data/dataR2.csv')
data
length(data)

head(data)
data_part = createDataPartition(data[,10],p=.8,list=FALSE)
data_part 

trainX = data[data_part,1:9]
trainY = data[data_part,10]
trainX
trainY

testX <- data[-data_part,1:9]
testY <- data[-data_part,10]

model = train(x=trainX,y=trainY, method="knn")
predictions = predict(model,testX)
confusionMatrix(testY,predictions)