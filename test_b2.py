class Singer:
    ''' 가수를 표현하는 클래스 '''
    def __init__(self, name, debut):
        self.name = name
        self.debut = debut 
        
    def intruduce(self):
        print('안녕하세요 가수 %s입니다'%self.name)        

    def age(self):
        print('데뷰한지 %d 년이 되었어요'%(2020 -  self.debut + 1)) 
        

iyou = Singer('아이유', 2008)        
iyou.intruduce()
iyou.age()
        
        
                