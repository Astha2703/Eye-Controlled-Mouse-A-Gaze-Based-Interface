import cv2
import mediapipe
import pyautogui
cam=cv2.VideoCapture(0)
screen_w,screen_h=pyautogui.size()
face_mesh_landmarks=mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True:
    _,image=cam.read()
    image=cv2.flip(image,1)
    window_h,window_w,_= image.shape
    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    processed_image=face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points=processed_image.multi_face_landmarks
    
    if all_face_landmark_points:
        one_face_landmark_points=all_face_landmark_points[0].landmark
        for id,landmark_points in enumerate(one_face_landmark_points[474:478]):
            x=int(landmark_points.x*window_w)
            y=int(landmark_points.y*window_h)
            #print(x,y)
            if id==1:
                mouse_x=int(screen_w/window_w*x)
                mouse_y=int(screen_h/window_w*y)
                pyautogui.moveTo(mouse_x,mouse_y)

            cv2.circle(image,(x,y),3,(0,0,255))
        
            
        left_eye=[one_face_landmark_points[145],one_face_landmark_points[159]]
        for landmark_points in left_eye:
            x=int(landmark_points.x*window_w)
            y=int(landmark_points.y*window_h)
            #print(x,y)
            cv2.circle(image,(x,y),3,(0,0,255))
            
        if(left_eye[0].y-left_eye[1].y<0.01):
            pyautogui.click()
            pyautogui.sleep(2)
            print("mouse clicked")
    cv2.imshow("Eye controlled mouse", image)
    key=cv2.waitKey(100)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()