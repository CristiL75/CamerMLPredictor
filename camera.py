import cv2 as cv
#constructorul
class Camera:
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():#daca camera nu e deschisa, atunci ridicam o eroare
            raise ValueError("Nu s-a putut deschide camera")
        
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
    
    def __del__(self):
        if self.camera.isOpened():#atunci cand nu mai avem nevoie de camera, o inchidem
            self.camera.release()
    
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))#Aici vrem sa transformam imaginea din una formata din 3 culori gri,rosu albastru in una rgb
            else:
                return (ret,None)
        else:
            return None