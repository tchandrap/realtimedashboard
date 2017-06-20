import paho.mqtt.publish as publish
from itertools import cycle
import time
import random

import json


#json ="{\"device_addr\":\"AS:DS:AD:EW:QW:RE\", \"rssi_dbm\":-32, \"node_id\":\"abam\", \"time_epoch\":tim}"

mq_topic = "pub"
mq_host = "167.205.24.77"


device_addr = ["AS:DS:AD:EW:QW:RE","AS:DS:AD:EW:QW:12","AS:AW:AD:EW:QW:9E"]
node_id = "B"
while(True):
	rssi_dbm = random.gauss(5, 4) 
	time_epoch = time.time()
	msgs = [{'topic': mq_topic, 'payload': rssi_dbm}, {'topic': mq_topic, 'payload': rssi_dbm }]
	publish.multiple(msgs, hostname="localhost")
	print "sending.."
	time.sleep(2)
	#publish.single("com.stream/track/wifi", json, hostname="localhost")


