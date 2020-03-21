from pyspark.sql import Row
data = [(1,1,'M','all',1000),(1,1,'M','superactive',300),(1,1,'M','frequent',200),(1,1,'M','dormant',100),(1,1,'M','non-active',400), \
(2,1,'M','all',1000),(2,1,'M','superactive',200),(2,1,'M','frequent',300),(2,1,'M','dormant',200),(2,1,'M','non-active',300),\
(3,1,'M','all',1000),(3,1,'M','superactive',150),(3,1,'M','frequent',250),(3,1,'M','dormant',100),(3,1,'M','non-active',500),\
(4,1,'M','all',1000),(4,1,'M','superactive',100),(4,1,'M','frequent',200),(4,1,'M','dormant',50),(4,1,'M','non-active',650),\
(5,1,'M','all',1000),(5,1,'M','superactive',50),(5,1,'M','frequent',150),(5,1,'M','dormant',10),(5,1,'M','non-active',790),\
(1,1,'F','all',1000),(1,1,'F','superactive',300),(1,1,'F','frequent',200),(1,1,'F','dormant',100),(1,1,'F','non-active',400), \
(2,1,'F','all',1000),(2,1,'F','superactive',200),(2,1,'F','frequent',300),(2,1,'F','dormant',200),(2,1,'F','non-active',300),\
(3,1,'F','all',1000),(3,1,'F','superactive',150),(3,1,'F','frequent',250),(3,1,'F','dormant',100),(3,1,'F','non-active',500),\
(4,1,'F','all',1000),(4,1,'F','superactive',100),(4,1,'F','frequent',200),(4,1,'F','dormant',50),(4,1,'F','non-active',650),\
(5,1,'F','all',1000),(5,1,'F','superactive',50),(5,1,'F','frequent',150),(5,1,'F','dormant',10),(5,1,'F','non-active',790),\
(1,2,'M','all',1000),(1,2,'M','superactive',600),(1,2,'M','frequent',300),(1,2,'M','dormant',100),(1,2,'M','non-active',0),\
(2,2,'M','all',1000),(2,2,'M','superactive',300),(2,2,'M','frequent',500),(2,2,'M','dormant',50),(2,2,'M','non-active',150),\
(3,2,'M','all',1000),(3,2,'M','superactive',550),(3,2,'M','frequent',250),(3,2,'M','dormant',100),(3,2,'M','non-active',100),\
(4,2,'M','all',1000),(4,2,'M','superactive',400),(4,2,'M','frequent',200),(4,2,'M','dormant',150),(4,2,'M','non-active',250),\
(5,2,'M','all',1000),(5,2,'M','superactive',200),(5,2,'M','frequent',300),(5,2,'M','dormant',200),(5,2,'M','non-active',300),\
(1,2,'F','all',1000),(1,2,'F','superactive',800),(1,2,'F','frequent',100),(1,2,'F','dormant',50),(1,2,'F','non-active',50), \
(2,2,'F','all',1000),(2,2,'F','superactive',700),(2,2,'F','frequent',200),(2,2,'F','dormant',50),(2,2,'F','non-active',50),\
(3,2,'F','all',1000),(3,2,'F','superactive',600),(3,2,'F','frequent',250),(3,2,'F','dormant',70),(3,2,'F','non-active',80),\
(4,2,'F','all',1000),(4,2,'F','superactive',500),(4,2,'F','frequent',250),(4,2,'F','dormant',100),(4,2,'F','non-active',150),\
(5,2,'F','all',1000),(5,2,'F','superactive',400),(5,2,'F','frequent',100),(5,2,'F','dormant',300),(5,2,'F','non-active',200),\
(1,3,'M','all',1000),(1,3,'M','superactive',200),(1,3,'M','frequent',300),(1,3,'M','dormant',200),(1,3,'M','non-active',300),\
(2,3,'M','all',1000),(2,3,'M','superactive',200),(2,3,'M','frequent',300),(2,3,'M','dormant',200),(2,3,'M','non-active',300),\
(3,3,'M','all',1000),(3,3,'M','superactive',150),(3,3,'M','frequent',250),(3,3,'M','dormant',100),(3,3,'M','non-active',500),\
(4,3,'M','all',1000),(4,3,'M','superactive',100),(4,3,'M','frequent',200),(4,3,'M','dormant',50),(4,3,'M','non-active',650),\
(5,3,'M','all',1000),(5,3,'M','superactive',50),(5,3,'M','frequent',150),(5,3,'M','dormant',10),(5,3,'M','non-active',790),\
(1,3,'F','all',1000),(1,3,'F','superactive',300),(1,3,'F','frequent',200),(1,3,'F','dormant',100),(1,3,'F','non-active',400), \
(2,3,'F','all',1000),(2,3,'F','superactive',200),(2,3,'F','frequent',300),(2,3,'F','dormant',200),(2,3,'F','non-active',300),\
(3,3,'F','all',1000),(3,3,'F','superactive',150),(3,3,'F','frequent',250),(3,3,'F','dormant',100),(3,3,'F','non-active',500),\
(4,3,'F','all',1000),(4,3,'F','superactive',100),(4,3,'F','frequent',200),(4,3,'F','dormant',50),(4,3,'F','non-active',650),\
(5,3,'F','all',1000),(5,3,'F','superactive',50),(5,3,'F','frequent',150),(5,3,'F','dormant',10),(5,3,'F','non-active',790),\
]
rdd = sc.parallelize(data)
data = rdd.map(lambda x: Row(time_period=x[0], age=int(x[1]), gender=x[2], type=x[3], count=int(x[4])))
data = sqlContext.createDataFrame(data)
