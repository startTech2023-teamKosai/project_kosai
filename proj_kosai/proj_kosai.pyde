orbit_list = []
def setup():
    global orbit_list, earth
    size(1500,1000)
    
    earth = Earth()
    
    orbit_Coordinate = [i for i in range(300,600,30)]
    orbit_list = [Orbit_object(orbit_Coordinate[i], random(0.005,0.01)) for i in range(9)]
    # orbit_list = [Orbit_object(orbit_Coordinate[i], random(0.005,0.01)) for i in range(1)]

def draw():
    global orbit_list,earth
    background(255)
    translate(width//2,height//2)
    # print(mouseX,mouseY)
    
    fill(127,255,212)
    noStroke()
    ellipse(0,0,300,300)
    
    for i,object in enumerate(orbit_list):
        object.update()
        # つかむ判定
        object_x, object_y = object.get_position()
        earth_x, earth_y = earth.get_arm_position()
        earth_flag = earth.get_is_catch()
        
        
        if earth_flag:
            if earth_x-5 < object_x < earth_x+55:
                if earth_y-5 < object_y < earth_y+55:
                    print(object.get_number())
                    orbit_list.pop(i)

        # print(earth_x, earth_y, earth_flag)
        # print(object_x,object_y)

    
    earth.update()
    
    if keyPressed:
        if key == "a":
            earth.arm_update_plus()
        elif key == "d":
            earth.arm_update_minus()
        
        if key == ENTER:
            earth.catch_arm()
    
    # object.update()
    
    
    
class Orbit_object():
    count = 0
    def __init__(self, sercle_lenge, d_speed):
        
        self.sercle_lenge = sercle_lenge
        self.d_speed = d_speed
        self.speed = 0
        self.x = 0
        self.y = 0
        self.orbit_num = Orbit_object.count
        Orbit_object.count += 1
        if random(0,100)<=50:
            self.sign = 1
        else:
            self.sign = -1
            
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
        if 0<= self.orbit_num <=2:
            fill(139,69,19)
        elif 3<= self.orbit_num <=5:
            fill(0,191,255)
        if 6<= self.orbit_num <=8:
            fill(255,250,205)

            
        ellipse(self.x,self.y,60,60)
        
        
        fill(0)
        text(str(self.orbit_num),self.x,self.y)
        # print(self.x,self.y)
        
    def get_position(self):
        return self.x, self.y
    
    def get_number(self):
        return self.orbit_num

class Earth():
    def __init__(self):
        self.arm_size = 100
        self.arm_img_open = loadImage("img/open_arm.PNG")
        self.arm_img_catch = loadImage("img/catch_arm.PNG")
        self.arm_img = self.arm_img_open
        self.is_catch = False
        self.is_catch_now = False
     
    def update(self):
        fill(127,255,212)
        noStroke()
        ellipse(0,0,300,300)
        
        if self.is_catch_now:
            self.arm_img = self.arm_img_catch
            self.is_catch = False
            if frameCount % 2 == 0:
                 self.arm_size -= 10
                 if self.arm_size < 100:
                     self.arm_size = 100
                     self.is_catch = False
                     self.is_catch_now = False
        else:
            self.arm_img = self.arm_img_open    
            
        fill(255)
        ellipse(-50,0,30,60)            
        image(self.arm_img, -self.arm_size-50, -50,self.arm_size,100)
        
        fill(0)
        ellipse(0,0,10,10)
        
    # アームの動き
    def arm_update_plus(self):
        if self.is_catch_now == False:
            self.arm_size += 10
            if self.arm_size > 600:
                 self.arm_size = 600
            fill(255)
            ellipse(-50,0,30,60)
            image(self.arm_img, -self.arm_size-50,-50,self.arm_size,100)
    def arm_update_minus(self):
        if self.is_catch_now == False:
            self.arm_size -= 10
            if self.arm_size < 100:
                self.arm_size = 100
            fill(255)
            ellipse(-50,0,30,60)
            image(self.arm_img, -self.arm_size-50,-50,self.arm_size,100)
    def catch_arm(self):
        self.is_catch_now = True
        self.is_catch = True
    
    # 変数を返す    
    def get_arm_position(self):
        return -self.arm_size-50, -50
    
    def get_is_catch(self):
        return self.is_catch
        
# -------------------追加-------------------------
# 取ったオブジェクトの数に応じて星を成長させるクラス        
class Grow():
    def __init__(self, count_seed, count_water, count_creature, count_clock):
        self.count_seed = count_seed  # 種をとった数
        self.count_water = count_water  # 水をとった数
        self.count_creature = count_creature  # 生き物をとった数
        self.count_clock = count_clock  # 時計をとった数
        
        self.lv_seed = 0  # 種のレベル
        self.lv_water = 0  # 水のレベル
        self.lv_creature = 0  # 生き物のレベル
        
    def judge_level(self):
        
        # 100の位: 種のレベル, 10の位: 水のレベル, 1の位: 生き物のレベル
        look_up_table = [[[0, 1, 1, 1, 1],
                          [10, 11, 12, 12, 12], 
                          [20, 21, 22, 22, 22], 
                          [30, 31, 32, 32, 32], 
                          [40, 41, 42, 42, 42]],
        
                        [[100, 101, 101, 101, 101],
                         [110, 111, 113, 113, 113], 
                         [120, 121, 123, 123, 123], 
                         [130, 131, 133, 133, 133], 
                         [140, 141, 143, 143, 143]],
                        
                        [[200, 201, 201, 201, 201],
                         [210, 211, 313, 313, 313], 
                         [220, 221, 323, 324, 324], 
                         [230, 231, 333, 334, 334], 
                         [240, 241, 343, 344, 344]], 
                        
                        [[200, 201, 201, 201, 201],
                         [310, 311, 313, 313, 313], 
                         [420, 421, 423, 424, 424], 
                         [430, 431, 433, 434, 434], 
                         [440, 441, 443, 444, 444]], 
                        
                        [[200, 201, 201, 201, 201],
                         [310, 311, 313, 313, 313], 
                         [420, 421, 423, 424, 424], 
                         [430, 431, 433, 434, 434], 
                         [440, 441, 443, 444, 444]]]
        
        for s in range(len(look_up_table)):
            for w in range(len(look_up_table[0])):
                for c in range(len(look_up_table[0][0])):
                    try:
                        lv_obj = look_up_table[self.count_seed][self.count_water][self.count_creature]
                        
                    except IndexError:
                        if self.count_seed > 4:
                            lv_obj = 500
                        elif self.count_water > 4:
                            lv_obj = 50
                        elif self.count_creature > 4:
                            lv_obj = 5
        
        # レベル判定
        self.lv_seed = lv_obj // 100 + self.count_clock
        self.lv_water = (lv_obj // 10) % 10 + self.count_clock
        self.lv_creature = lv_obj % 10 + self.count_clock
            
        return (self.lv_seed, self.lv_water, self.lv_creature)
    
     
    
    
