mydata = read.csv("regrex1.csv")
mydata
xval = mydata$x
yval = mydata$y

png("r_orig.png")
plot(xval, yval, main="Scatterplot in R")
dev.off()

linearmodel <- lm(yval ~ xval, data=mydata) 
print(linearmodel)

predict(linearmodel, mydata)

png('r_Im.png')
plot(xval, yval ,col = "blue",main = "Linear Regression in R",abline(linearmodel), cex = 1.3,pch = 16,xlab = "x",ylab = "y")
dev.off()

print("here")


