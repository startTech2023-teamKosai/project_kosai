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
        
    # 取ったオブジェクトの数に対応した、オブジェクトのレベルを返すメソッド
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
                    lv_obj = look_up_table[self.count_seed][self.count_water][self.count_creature]
        
        # レベル判定
        self.lv_seed = lv_obj // 100 + self.count_clock
        self.lv_water = (lv_obj // 10) % 10 + self.count_clock
        self.lv_creature = lv_obj % 10 + self.count_clock
            
        return (self.lv_seed, self.lv_water, self.lv_creature)
    
        
