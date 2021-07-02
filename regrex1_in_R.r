mydata = read.csv("regrex1.csv")
mydata
xval = mydata$x
yval = mydata$y

plot(xval, yval, main="Scatterplot in R")
png('r_orig.png')

linearmodel <- lm(yval ~ xval, data=mydata) 
print(linearmodel)

predict(linearmodel, mydata)

plot(xval, yval ,col = "blue",main = "Linear Regression in R",abline(linearmodel), cex = 1.3,pch = 16,xlab = "x",ylab = "y")
png('r_Im.png')



print("here")


