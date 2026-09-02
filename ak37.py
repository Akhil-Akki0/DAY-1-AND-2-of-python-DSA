#simple cart filter also know as the GST + filter ing the product above 100
p = [250 , 999 , 45 , 1500 , 60]
a_100 = [p for p in p if p > 100]
print("items above 100rs:",a_100)
with_gst  = [round(p*1.18,2) for p in p]
print("items with GST:",with_gst)
#end of the python code
