import numpy as np
#let have csv file and assign some of the data of csv to variable to perform functions on those

id, price, area, bedrooms = np.genfromtxt('datasets/zameencom-property-data-By-Kaggle-short.csv', delimiter= ';', usecols= (0, 4, 11, 13), unpack= True, dtype=None, skip_header=1)
print(id)
print(type(id))
print(price)
print(type(price))
print(area)
print(bedrooms)

#statistics operations on zameen.com data

print("Mean price from the whole data...", np.mean(price))
print("Average price from the whole data...",np.average(price))
print("Standard deviation of the price dataset...",np.std(price))
print("25th percentile of the bedrooms data...", np.percentile(bedrooms, 25))
print("75th percentile of the bedrooms data...",np.percentile(bedrooms, 75))
print("Minimum bedrooms...",np.min(bedrooms))
print("Maximumn bedrooms...",np.max(bedrooms))
print("Minimum price of plots/houses...",np.min(price))
print("Maximum price of plots/houses...",np.max(price))

#math operations on zameen.com data set

print("Square of the id column...", np.square(id))
print("Square root of price column...", np.sqrt(price))
print("Power of the bedrooms column...", np.power(bedrooms,bedrooms))
print("Absolute value of the area column...", np.abs(price))

#Arithmatic operation on dataset

addition = id + price
subtraction = id - price
multiplication = bedrooms * id
division = price / id

print("Addition of id and price = ", addition)
print("Subtraction of id and price = ", subtraction)
print("Multiplication of bedrooms and price = ", multiplication)
print("Division of price and id = ", division)

#by parameter method using numpy built in methods
print("Add price and id = ", np.add(price, id))
print("Subtract price and id = ", np.subtract(price, id))
print("Multiply bedrooms with id = ", np.multiply(bedrooms,id))
print("Divide price by id = ", np.divide(price,id))

#Applying Trigonometric Functions

print("Sin of id = ", np.sin(id))
print("Cos of bedrooms = ", np.cos(bedrooms))
print("Tangent of id = ", np.tan(id))

print("Exponential value of bedrooms = ", np.exp(bedrooms)) #where exp mean e**x

#Calculating the natural logirthm and base 10 log

log_array = np.log(bedrooms)
log_10_array = np.log10(bedrooms)

print("Natural log on bedroom array...",log_array)
print("Base 10 log values...", log_10_array)

#hyperbolic sinh, cosh, tanh

print("Hyperbolic sinh function on bedrooms...",np.sinh(bedrooms))
print("Hyperbolic cosh on bedroom array...",np.cosh(bedrooms))
print("Hyperbolic tanh on bedroom array...",np.tanh(bedrooms))

#inverse hyperbolic function

print("Inverse hyperbolic sin on bedroom column values...",np.arcsinh(bedrooms))
print("Inverse hyperbolic cos values for bedroom column are...",np.arccosh(bedrooms))
print("Inverse hyperbolic tan on bedroom column values...",np.arctan(bedrooms))

#two dimensional array

d2array = np.array([area, bedrooms])

print("Two dimensional array of area and bedrooms column is = ",d2array)

#Checking dimension of array

print("Dimension of d2array is = ",d2array.ndim)
