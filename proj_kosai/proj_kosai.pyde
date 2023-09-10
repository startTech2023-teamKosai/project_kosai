add_library("minim") # 音声を扱うライブラリ

scene = 1 #画面条件分岐用のフラグ
bg_count = 0 #iのグローバル宣言

orbit_list = []

remain_count = 6 # キャッチできる回数

game_flag = False # ゲームフラグ
end_rect_density = 0

music_call1 = True # drawの中で１回だけ関数を呼ぶためのフラグ
music_call2 = True
music_call3 = True
    
def setup():
    global orbit_list, earth, img_seed, img_water, img_life, img_start
    size(1500,1000)
    textSize(100)
    textAlign(CENTER, CENTER)
    
    global sercle_lenge, object, img_bg, img_st
    
    # イメージのロード　グローバルで保存しとく
    img_bg = loadImage("img/haikei.jpg")
    img_st = loadImage("img/start.jpg")
    
    img_start = loadImage("img/start.png")
    img_seed = loadImage("img/seed.png")
    img_water = loadImage("img/water.png")
    img_life = loadImage("img/life.png")
    
    global seed_lv1_img, seed_lv2_img, seed_lv3_img
    seed_lv1_img = loadImage("img/seed_lv1.PNG")
    seed_lv2_img = loadImage("img/seed_lv2.PNG")
    seed_lv3_img = loadImage("img/seed_lv3.PNG")
    
    global water_lv1_img, water_lv2_img, water_lv3_img
    water_lv1_img = loadImage("img/water_lv1.png")
    water_lv2_img = loadImage("img/water_lv2.png")
    water_lv3_img = loadImage("img/water_lv3.png")
    
    global life_lv1_img, life_lv2_img, life_lv3_img
    life_lv1_img = loadImage("img/life_lv1.PNG")
    life_lv2_img = loadImage("img/life_lv2.PNG")
    life_lv3_img = loadImage("img/life_lv3.PNG")
    
    global water_end_img, seed_end_img, life_end_img, faild_end_img
    water_end_img = loadImage("img/end_water.png")
    seed_end_img = loadImage("img/end_seed.png")
    life_end_img = loadImage("img/end_life.png")
    faild_end_img = loadImage("img/end_faild.png") 
    
    # earth オブジェクト　インスタンス
    earth = Earth()
    
    # 軌道上のオブジェクト　インスタンス
    orbit_Coordinate = [i for i in range(300,600,30)]
    orbit_list = [Orbit_object(orbit_Coordinate[i], random(0.03,0.05)) for i in range(9)]
    
    noStroke()
    
    # フォント設定
    font = createFont(u"Meiryo", 50);
    textFont(font);
    
    global back_music
    global music_call1, music_call2, music_call3
    # 音　インスタンス
    back_music = Minim(this)

def draw():
    global back_music,back_music_player
    
    global orbit_list,earth, remain_count
    
    global m,n,sercle_lenge,object, bg_count, scene
    global img_bg, img_st
    
    global end_rect_density, game_flag
    
    global music_call1, music_call2, music_call3
    

    translate(width//2,height//2)
    
    if game_flag == False:
        image(img_bg,-width//2,bg_count,width,height) #背景画像の貼り付け1枚目
        image(img_bg,-width//2,bg_count-height,width,height) #背景画像の貼り付け2枚目
        bg_count+=1 #背景画像のｙ座標の値を徐々に大きくする
        if bg_count>=height/2: 
            bg_count=-height//2

        for i,object in enumerate(orbit_list):
            object.update()
            # つかむ判定
            object_x, object_y = object.get_position()
            earth_x, earth_y = earth.get_arm_position()
            earth_flag = earth.get_is_catch()
            
            if earth_flag:
                if earth_x-5 < object_x < earth_x+55:
                    if earth_y-5 < object_y < earth_y+55:
                        # つかんだらlistからpop、つかんだ物をearthに渡す
                        earth.set_Level(object.get_number())
                        orbit_list.pop(i)
                        
        # earth の更新
        earth.update()
        
        # 残り回数表示
        fill(255)
        text(u"残り"+str(remain_count)+u"回",0,-350)
    
        # 画面切り替え
        if scene == 1:
            image(img_st,-width//2,-height//2,1500,1000)
            #sceneが1の時スタート画面を表示
            if mousePressed:
                if mousePressed and (276<=mouseX<=1215) and (621<=mouseY<=879):
                    # if music_call1:
                    #     bg_music("music/8-bit_Aggressive1.mp3")
                    #     music_call1 = False
                    #startの枠の中でマウスが押されたらsceneを0にする
                    scene = 2
        if scene == 2:
            image(img_start,-width//2,-height//2,width,height)
            fill(255)
            text("[ ENTER ]",0,400)
            #sceneが2の時スタート画面を表示
            if keyPressed:

                if key == ENTER:
                    scene = 0
        
        #残り回数が０になったらゲームを終了
        # if remain_count <= 0:
        #         game_flag = True    

    # リザルト処理
    if game_flag == True:
        if frameCount % 2 == 0:
            # 暗転　だんだん暗くする
            end_rect_density += 0.5
            
            fill(0,0,0,end_rect_density)
            rect(-width/2, -height/2, width, height)

            # print(end_rect_density)
            
            if end_rect_density > 30:
                end_rect_density = 30
                
                # 星の状態の結果(list)を所得
                result = earth.get_earth_lv()
                
                # 結果表示
                
                if result[2] >= 3:
                    # if music_call3:
                    #     bg_music("music/life_end.mp3")
                    #     music_call3 = False
                    image(life_end_img,-width//2,-height//2,1500,1000)
                    
                elif result[0] >= 3:
                    # if music_call3:
                    #     bg_music("music/Day_Dream_Down.mp3")
                    #     music_call3 = False
                    image(water_end_img,-width//2,-height//2,1500,1000)
                    
                elif result[1] >= 3:
                    # if music_call3:
                    #     bg_music("music/seed.mp3")
                    #     music_call3 = False
                    image(seed_end_img,-width//2,-height//2,1500,1000)
                    
                else:
                    # if music_call3:
                    #     bg_music("music/bad_end.mp3")
                    #     music_call3 = False
                    image(faild_end_img,-width//2,-height//2,1500,1000)
                    
def keyPressed():
    global remain_count, game_flag
    if scene == 0:
        if key == "a":
            earth.arm_update_plus()
        elif key == "d":
            earth.arm_update_minus()
        if key == ENTER:
            if remain_count > 0:
                remain_count -= 1 
                earth.catch_arm()
                
def bg_music(file):
    """
    音声を流すための関数
    引数：ファイル名
    """
    global back_music,back_music_player
    back_music.stop()
    
    back_music_player = back_music.loadFile(file)
    back_music_player.setGain(0)
    back_music_player.loop()
                    
class Orbit_object():
    """
    軌道上を回るオブジェクトのクラス
    updateメソッド：呼ばれるたびに画像を更新する
    get_positionメソッド：オブジェクトの位置を返す
    get_numberメソッド：オブジェクトの番号を返す
    
    """
    global img_seed, img_water, img_life, test
    count = 0
    
    def __init__(self, sercle_lenge, d_speed):
        self.sercle_lenge = sercle_lenge
        self.d_speed = d_speed
        self.speed = 0
        self.x = 0
        self.y = 0
        self.img = None
        self.orbit_num = Orbit_object.count
        Orbit_object.count += 1
        
        # 1/2で時計回りor反時計回り
        if random(0,100)<=50:
            self.sign = 1
        else:
            self.sign = -1

        # 軌道の色の設定（ランダム）        
        self.sercle_colour_R = int(random(128,255))
        self.sercle_colour_G = int(random(50,128))
        self.sercle_colour_B = int(random(128,255))
        self.sercle_colour_D = 50

    def update(self):
        noFill()
        strokeWeight(5)
        stroke(self.sercle_colour_R, self.sercle_colour_G, self.sercle_colour_B, self.sercle_colour_D)
        ellipse(0,0,self.sercle_lenge*2,self.sercle_lenge*2)
        
        self.speed += self.d_speed
        if self.speed > 360:
            self.speed = self.d_speed

        if self.sign == -1:
            self.x = self.sercle_lenge * cos(-self.speed)
            self.y = self.sercle_lenge * sin(-self.speed)
        else:
            self.x = self.sercle_lenge * cos(self.speed)
            self.y = self.sercle_lenge * sin(self.speed)
            
        noStroke()
        
        # 番号で種、水、生命を設定
        if 0<= self.orbit_num <=2:
            fill(222,184,135)
            self.img = img_seed
        elif 3<= self.orbit_num <=5:
            fill(135,206,250)
            self.img = img_water
        if 6<= self.orbit_num <=8:
            fill(255,250,205)
            self.img = img_life
                
        ellipse(self.x,self.y,60,60)
        image(self.img, self.x-30, self.y-30, 60, 60)
        
        
    def get_position(self):
        """
        オブジェクトの座標(x,y)を返す
        """
        return self.x, self.y
    
    def get_number(self):
        """
        オブジェクトの番号を返す
        """
        return self.orbit_num

class Earth():
    """
    星のオブジェクトのクラス
    update メソッド：呼ばれるたびに画像を更新する
    set_Level メソッド：取ったものを判断し星のレベルを上げる
    
    arm_update_plus メソッド：アームを伸ばす処理
    arm_update_minus メソッド：アームを縮める処理
    catch_arm メソッド：アームが閉じる処理
    
    get_arm_position メソッド：アームについている口の位置を返す
    get_is_catch メソッド：アームの口の開閉状態を真偽で返す
    get_earth_lv メソッド：星のレベルを返す
    
    """
    
    def __init__(self):
        self.arm_size = 100
        self.arm_img_open = loadImage("img/open_arm.PNG")
        self.arm_img_catch = loadImage("img/catch_arm.PNG")
        self._env_img = loadImage("img/earth.png")
        self.arm_img = self.arm_img_open
        self.is_catch = False # アームの開閉状態
        self.is_catch_now = False # アームの運動状態
        
        # 種、水、生命の画像、レベル
        self.seed_lv = 0
        self.seed_lv_img = loadImage("img/None.png")
        self.water_lv = 0
        self.water_lv_img = loadImage("img/None.png")
        self.life_lv = 0
        self.life_lv_img = loadImage("img/None.png")
        
        # 音声について
        self.music = Minim(this)
        self.music_player = self.music.loadFile("music/catch.mp3")
        self.music_player.setGain(300)
     
    def update(self):
        fill(127,255,212)
        noStroke()
        ellipse(0,0,300,300)
        
        image(self._env_img, -300, -300, 600, 600)
        
        # 水の表示
        if self.water_lv_img:
            if self.water_lv == 1:
                self.water_lv_img = water_lv1_img
            elif self.water_lv == 2:
                self.water_lv_img = water_lv2_img
            elif self.water_lv == 3:
                self.water_lv_img = water_lv3_img
            image(self.water_lv_img, -300, -300, 600, 600)
        
        # 種の表示
        if self.seed_lv_img:
            if self.seed_lv == 1:
                self.seed_lv_img = seed_lv1_img
            elif self.seed_lv == 2:
                self.seed_lv_img = seed_lv2_img
            elif self.seed_lv == 3:
                self.seed_lv_img = seed_lv3_img
            image(self.seed_lv_img, -300, -300, 600, 600)

        # 生命の表示
        if self.life_lv_img:
            if self.life_lv == 1:
                self.life_lv_img = life_lv1_img
            elif self.life_lv == 2:
                self.life_lv_img = life_lv2_img
            elif self.life_lv == 3:
                self.life_lv_img = life_lv3_img
            image(self.life_lv_img, -300, -300, 600, 600)
        
        if self.is_catch_now:
            self.arm_img = self.arm_img_catch
            self.is_catch = False
            if frameCount % 1 == 0:
                 self.arm_size -= 10
                 if self.arm_size < 100:
                     self.arm_size = 100
                     self.is_catch = False
                     self.is_catch_now = False
                     self.music_player.close()
                     self.music.stop()
                     if remain_count <= 0:
                        global game_flag
                        game_flag = True  
        else:
            self.arm_img = self.arm_img_open    
            
        fill(255)
        ellipse(-50,-2,15,30)            
        image(self.arm_img, -self.arm_size-50, -50,self.arm_size,100)
        
    def set_Level(self, orbit_number):        
        if 0 <= orbit_number <= 2:
            self.music_player = self.music.loadFile("music/catch.mp3")
            self.music_player.play()
            self.seed_lv += 1
        elif 3 <= orbit_number <= 5:
            self.music_player = self.music.loadFile("music/catch.mp3")
            self.music_player.play()
            self.water_lv += 1
        elif 6 <= orbit_number <= 8:
            self.music_player = self.music.loadFile("music/catch.mp3")
            self.music_player.play()
            self.life_lv += 1
        
    # アームの動き
    def arm_update_plus(self):
        """
        アームを徐々に伸ばす処理
        """
        if self.is_catch_now == False:
            self.arm_size += 10
            if self.arm_size > 600:
                 self.arm_size = 600
            fill(255)
            ellipse(-50,-2,15,30)
            image(self.arm_img, -self.arm_size-50,-50,self.arm_size,100)
    def arm_update_minus(self):
        """
        アームを徐々に縮める処理
        """
        if self.is_catch_now == False:
            self.arm_size -= 10
            if self.arm_size < 100:
                self.arm_size = 100
            fill(255)
            ellipse(-50,-2,15,30)
            image(self.arm_img, -self.arm_size-50,-50,self.arm_size,100)
            
    def catch_arm(self):
        self.is_catch_now = True
        self.is_catch = True
    
    # 変数を返す    
    def get_arm_position(self):
        return -self.arm_size-50, -50
    def get_is_catch(self):
        return self.is_catch
    def get_earth_lv(self):
        return self.water_lv, self.seed_lv, self.life_lv  
