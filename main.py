
e = box(pos=vec(0, 0, 0), size=vec(10, 0.2, 10), color=color.white) 
p = sphere(pos=vec(0, 5, 0), radius=0.5, color=color.orange)

p.v = vec(0, 0, 0)      

_gravity =  vec (0,-9.8,0)  
_time = 0.02               
speed = 0.05

while p.pos.y >= (0.5+0.2):   
    rate(100)    
    p.v = p.v + _gravity * _time 
    p.pos = p.pos + p.v * _time   
