import math
# COLUMN LİSTS:
x1=[]
x2=[]
y=[]
gColumn=[]
hColumn=[]
IColumn=[]
jColumn=[]
kColumn=[]
lColumn=[]
#egitim
Ytahmin=[]
Ytahmin_Yort=[]
Ytahmin_Yort_2=[]
#test
testYtahmin=[]
YtestVeri_Ytahmin=[]
YtestVeri_Ytahmin_2=[]
# EĞİTİM VERİLERİ
egitim_verileri_x1 = [10.26,985.69,1445.56,1188.19,574.51,568.95,471.81,537.35,514.07,174.09,
                      1720.81,611.48,251.19,97.97,406.81,265.4,1323.29,196.65,1326.6,1380.69,
                      792.35,957.12,1789.66,656.14,613.7]
egitim_verileri_x2 = [43,28,35,33,44,19,20,22,21,40,32,20,24,38,24,25,35,36,27,33,33,28,30,34,49]
egitim_verileri_y = [330,120,360,270,220,170,70,210,200,300,290,70,150,190,
                     240,100,250,210,280,230,210,230,320,210,230]
# TEST VERİLERİ
test_verileri_x1 = [313.36,336.51,1544.9,68.95,785.69]
test_verileri_x2 = [40,20,42,35,8]
test_verileri_y = [250,60,330,150,150]

# ORTALAMA DEĞERLERİ
x1_ortalama = sum(egitim_verileri_x1)/len(egitim_verileri_x1)
x2_ortalama = sum(egitim_verileri_x2)/len(egitim_verileri_x2)
y_ortalama = sum(egitim_verileri_y)/len(egitim_verileri_y)
y_test_ortalama=sum(test_verileri_y)/len(test_verileri_y)

# ---------------------- COLUMN HESAPLAMALAR ----------------------
# X1-X1ort = x1 ...
for i in range(0,25,1):
    example_value0 = egitim_verileri_x1[i] - x1_ortalama
    example_value1 = egitim_verileri_x2[i] - x2_ortalama
    example_value2 = egitim_verileri_y[i] - y_ortalama
    x1.append(example_value0)
    x2.append(example_value1)
    y.append(example_value2)
# x1*x2 ...
for i in range(0,25,1):
    example_value0 = y[i]  * x1[i]
    example_value1 = y[i]  * x2[i]
    example_value2 = x1[i] * x2[i]
    gColumn.append(example_value0)
    IColumn.append(example_value1)
    jColumn.append(example_value2)
# x1^2 ...
for i in range(0,25,1):
    example_value0 = x1[i]  * x1[i]
    example_value1 = x2[i]  * x2[i]
    example_value2 = y[i]   * y[i]
    kColumn.append(example_value0)
    hColumn.append(example_value1)
    lColumn.append(example_value2)
# ---------------------- COLUMN HESAPLAMALAR ----------------------

# b1 sonuç :
b1 = ((sum(gColumn)*sum(hColumn))-(sum(IColumn)*sum(jColumn)))/((sum(kColumn)*sum(hColumn))-(sum(jColumn)*sum(jColumn)))
# b2 sonuç :
b2 = ((sum(IColumn)*sum(kColumn))-(sum(gColumn)*sum(jColumn)))/((sum(kColumn)*sum(hColumn))-(sum(jColumn)*sum(jColumn)))
# b0 sonuç :
b0 = (y_ortalama-b1*x1_ortalama-b2*x2_ortalama)

# ---------------------- EĞİTİM VERİ SETİ TAHMİN DEĞERLERİ ----------------------
# Ytahmin ...
for i in range(0,25,1):
    example_value0 = (b0+b1*egitim_verileri_x1[i]+b2*egitim_verileri_x2[i])
    Ytahmin.append(example_value0)
# Ytahmin-Yort ...
for i in range(0,25,1):
    example_value0 = (Ytahmin[i]-y_ortalama)
    Ytahmin_Yort.append(example_value0)
# (Ytahmin-Yort)^2 ...
for i in range(0,25,1):
    example_value0 = Ytahmin_Yort[i]**2
    Ytahmin_Yort_2.append(example_value0)
# ---------------------- EĞİTİM VERİ SETİ TAHMİN DEĞERLERİ ----------------------

# ---------------------- TEST VERİ SETİ TAHMİN DEĞERLERİ ----------------------
# Ytahmin TEST ...
for i in range(0,5,1):
    example_value0 = (b0+b1*test_verileri_x1[i]+b2*test_verileri_x2[i])
    testYtahmin.append(example_value0)
# YtestVeri-Ytahmin ...
for i in range(0,5,1):
    example_value0 = (test_verileri_y[i]-testYtahmin[i])
    YtestVeri_Ytahmin.append(example_value0)
# (YtestVeri-Ytahmin)^2 ...
for i in range(0,5,1):
    example_value0 = YtestVeri_Ytahmin[i]**2
    YtestVeri_Ytahmin_2.append(example_value0)
# ---------------------- TEST VERİ SETİ TAHMİN DEĞERLERİ ----------------------

# R^2 ve adjR'2 değerleri :
r2= (sum(gColumn)*b1+sum(IColumn)*b2)/sum(lColumn)
adjR2= 1-(1-r2)*24/22
# MSE ve RMSE değerleri :
mse = sum(YtestVeri_Ytahmin_2)/len(testYtahmin)
rmse = math.sqrt(mse)

print("b0 :",b0)
print("b1 :",b1)
print("b2 :",b2)
print("*************************")
print("R^2 :",r2)
print("adjR^2 :",adjR2)
print("*************************")
print("MSE :",mse)
print("RMSE :",rmse)
print("*************************")
i=1
while(i<6):
    print("{}. Test tahmin verisi : {}".format(i,testYtahmin[i-1]))
    i+=1

























