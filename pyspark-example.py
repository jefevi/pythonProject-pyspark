from pyspark import SparkConf, SparkContext
import sys

#HOW TO CALL
#bigdata@bigdata:~/spark/bin$ spark-submit /home/bigdata/PycharmProjects/pythonProject-pyspark/pyspark-example.py

conf = SparkConf().setMaster("local").setAppName("My App") #Cluster URL namely local + Application name
sc = SparkContext(conf = conf)

lines = sc.textFile("/spark/README.md")
pythonlines = lines.filter(lambda line: "Python" in line)
print(pythonlines.first())

sys.exit()