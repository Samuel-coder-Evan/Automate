import random
import requests
import json
import cv2
myimage = ''
def takesnapshot():
    picture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = picture.read()
        cv2.imwrite('photo.jpg',frame)
        result = False
    picture.release()
    myimage = frame
    cv2.destroyAllWindows()

def uploadfile():
    myrand = random.randint(0,100)
    headers = {"Authorization": "Bearer ya29.a0ARrdaM8xd5Pb-86aiL9CkOzFrNYdwTdHOy8TbW1u4dvLTE-gtRMwv_d1VFwSJEDkLD-E54x3RzxRX2biEWoZ9b5apjLnbyDl0xnG_p7sSpo8yUQiYSrGB1M8y0K2Y4nHr5Tpa3UwJ_G2Vh-1cBpJVCIlbg4s"} #put ur access token after the word 'Bearer '
    para = {
        "name": "Hello" + str(myrand), #file name to be uploaded
        "parents": ["13CKR6aHHmkRcz47UPglQeXbYiMton3i7"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': ('image/jpg',open('photo.jpg', "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)
takesnapshot()
uploadfile()