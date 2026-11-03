# 객체로 구성된 게임 월드
# world = [] 

# 객층적 구조를 갖는 게임 월드
world = [[], []]

# 객체를 담든 함수
# 앞에 잔디 그다음 캐릭터 그리고 잔디 이렇게 구성을 하여서 소년이 잔디밭 사이에 있게끔 해야 하는데
def add_object(o, depth=0): # depth 0(배경) 1(캐릭터)
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

# 게임 로직
def update():
   for layer in world:
       for o in layer:
           o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()
          
