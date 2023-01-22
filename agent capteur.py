import paho.mqtt.client as mqttClient
import time
import random
 
def on_connect(client, userdata, flags, rc):

    print ("entered")
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address= "masteria-rfvf01v5x1kf.cedalo.cloud"
port = 1883
user = "ichrakhamdi"
password = "ichrakhamdi"
 
client = mqttClient.Client("Ichrak")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    while True:
        time.sleep(1)
        t = random.randint(10,45)
        value = str(t) + '°'
        print("New generated temperature = ", value)
        client.publish("MasterSSIA/Temperature",value)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()
