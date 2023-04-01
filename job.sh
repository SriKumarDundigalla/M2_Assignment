#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /mapreduce/text1.txt  -output /mapreduce/output5


