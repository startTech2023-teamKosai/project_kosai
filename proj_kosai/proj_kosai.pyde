def setup():
    
    global sercle_lenge, object
    size(1000,800)
    
    
    sercle_lenge = 300 # 周る円の大きさ
    speed = 0.05 # 円を周る時のスピード　低いほど遅い
    object = Orbit_object(sercle_lenge, speed)
    
    noStroke()

def draw():
    background(0)
    global m,n,sercle_lenge,object
    translate(width//2,height//2)
    
    object.update()
    
    
class Orbit_object():
    def __init__(self, sercle_lenge, d_speed):
        self.sercle_lenge = sercle_lenge
        self.d_speed = d_speed
        self.speed = 0
        self.x = 0
        self.y = 0
        
    def update(self):
        self.speed += self.d_speed
        if self.speed > 360:
            self.speed = self.d_speed
        self.x = self.sercle_lenge * cos(self.speed)
        self.y = self.sercle_lenge * sin(self.speed)
        ellipse(self.x,self.y,30,30)
        print(self.x,self.y)
        
    
        
