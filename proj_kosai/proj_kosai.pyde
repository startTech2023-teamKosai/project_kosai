img_bg = None #背景画像のグローバル宣言
img_st = None #スタート画像のグローバル宣言
scene = 1 #画面条件分岐用のフラグ
i = 0 #iのグローバル宣言

def setup():
    
    global sercle_lenge, object, img_bg, img_st
    size(1500,1000)
    img_bg = loadImage("img/haikei.jpg") #背景画像をロードする
    img_st = loadImage("img/start.jpg") #スタート画像をロードする
    
    sercle_lenge = 300 # 周る円の大きさ
    speed = 14 # 円を周る時のスピード　低いほど遅い
    object = Orbit_object(sercle_lenge, speed)
    
    noStroke()

def draw():
    background(0)
    global m,n,sercle_lenge,object, i, scene
    image(img_bg,0,i,1500,1000) #背景画像の貼り付け1枚目
    image(img_bg,0,i-1000,1500,1000) #背景画像の貼り付け2枚目
    i+=1 #背景画像のｙ座標の値を徐々に大きくする
    if i>=1000: #iの値がy座標の最大値(1000)を超えたらiを0にする
        i=0
    translate(width//2,height//2)
    
    object.update()
    if scene == 1:
        image(img_st,-width//2,-height//2,1500,900)
        #sceneが1の時スタート画面を表示
    # if mousePressed:
        # print(mouseX,mouseY)
    if mousePressed and (276<=mouseX<=1216) and (558<=mouseY<=788):
        #startの枠の中でマウスが押されたらsceneを0にする
        scene = 0
        
    
    
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
        # print(self.x,self.y)
        
        
    
        
