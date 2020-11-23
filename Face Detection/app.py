import cv2
import numpy as np
from flask import Flask, render_template, request,redirect

app = Flask(__name__)
name=''

@app.route("/")
def start_page():
    return render_template('index.html')

@app.route("/home")
def home():
    return redirect("/")

@app.route('/submit', methods = ['POST'])
def submit_name():
    if request.method == 'POST':
        global name
        name += request.form["username"]
        faces = face_detect()
        if len(faces) == 0:
            faceDetected = False
        else:
            faceDetected = True

    return render_template('index.html', faceDetected=faceDetected, init=True)

def face_detect():
    #Initialising camera
    cap = cv2.VideoCapture(0)

    #FaceDetection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    skip = 0
    face_data = []
    while True:
        ret,frame = cap.read()
        
        if ret == False:
            continue
        
        faces = face_cascade.detectMultiScale(frame,1.3,5)
        
        ''' For multiple faces it sorts the images based in it's w and h value and by calculating the area and
            displays it in descending order i.e., largest face in the begining of the list. '''
        faces = sorted(faces,key=lambda f:f[2]*f[3])
        
        for face in faces[-1:]:
            x,y,w,h = face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            skip +=1
            if (skip%10 == 0):
                #Store every 10th face
                face_data.append(face)
            cv2.putText(frame,name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
                
        cv2.imshow("Video Frame",frame)
        
           
        
        KeyPressed = cv2.waitKey(1) & 0xFF
        if KeyPressed == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return face_data


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(debug=True)