import cv2
import winsound
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

CONSECUTIVE_FRAMES = 15
FRAME_COUNTER = 0
ALARM_ON = False

script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, "alarm.wav")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        FRAME_COUNTER = 0
        if ALARM_ON:
            ALARM_ON = False
            winsound.PlaySound(None, winsound.SND_PURGE)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
        
        print(f"Detected Eyes Count: {len(eyes)} | Frame Counter: {FRAME_COUNTER}")
        
        if len(eyes) == 0:
            FRAME_COUNTER += 1
            if FRAME_COUNTER >= CONSECUTIVE_FRAMES:
                if not ALARM_ON:
                    print("--- ALARM TRIGGERED! ---")
                    ALARM_ON = True
                    if os.path.exists(audio_path):
                        try:
                            winsound.PlaySound(audio_path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
                        except Exception as e:
                            print(f"Audio Playback Error: {e}")
                    else:
                        print(f"Error: '{audio_path}' not found! Playing default alert.")
                        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            FRAME_COUNTER = 0
            if ALARM_ON:
                print("--- ALARM STOPPED ---")
                ALARM_ON = False
                winsound.PlaySound(None, winsound.SND_PURGE)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
