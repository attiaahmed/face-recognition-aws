
import time
import os
import boto3
import eel
import os 
import time

import time
import RPi.GPIO as GPIO
from picamera import PiCamera


            

def recog():
    directory = '/home/pi' #folder name on your raspberry pi

    collectionId='mycollection' #collection name

    rek_client=boto3.client('rekognition',
                        aws_access_key_id='AKIAYXMBY32MAU7LRJP6',# add the aws access key
                        aws_secret_access_key='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',# add the aws secret access key
                        region_name='eu-central-1',)# add the region here

    if _name_ == "_main_":

        milli = int(round(time.time() * 1000))
        
        image = '{}/image_{}.jpg'.format(directory,milli)
	P.capture(image) #capture an image
        print('captured '+image)

        with open(image, 'rb') as image:
            try:  # match the captured imges against the indexed faces
                match_response = rek_client.search_faces_by_image(CollectionId=collectionId,
                                                                  Image={'Bytes': image.read()}, MaxFaces=1,
                                                                  FaceMatchThreshold=85)

                if match_response['FaceMatches']:
                    os.system("xset -display :0.0 dpms force on")

                    print('Hello, ', match_response['FaceMatches'][0]['Face']['ExternalImageId'])
                    x=match_response['FaceMatches'][0]['Face']['ExternalImageId']
                    if(x=="ahmed"):
                        eel.addtext("a1")
                        eel.sleep(4)
                    if (x == "salim"):
                        eel.addtext("a2")
                        eel.sleep(4)
                    if (x == "mahmoud"):
                        eel.addtext("a3")
                        eel.sleep(4)
                        
                    

                else:
                     os.system("xset -display :0.0 dpms force on")

                     print("facee")
                     eel.addtext("a4")
                     eel.sleep(4)


            except:
                os.system("xset -display :0.0 dpms force off")

                print("no one")
                time.sleep(4)


@eel.expose
def hello():
    print("Hello from ")
eel.init("faces")
eel.start("index.html", block=False,port=8080,cmdline_args=['chrome-app --start-fullscreen'])
eel.addtext("a4")
eel.sleep(4)

while True:
    recog()
    eel.sleep(7)
