Web VPython 3.2
scene.autoscale = False
scene.userspin = False

end = sphere(pos=vec(14.5,6, 0), radius=0.3, color=color.yellow)
g  = box(pos=vec(5, -4.5, 0), size=vec(20.1, 10, 1.5), color=color.green)
sky = box(pos=vec(0,0,-1.2), size=vec(100,100,1), color=color.cyan)
boxes = []
for i in range(10) :
    if i % 2 :
        boxes.append(box(pos = vec(5.5+i,0.5,0),size=vec(1, i+1, 1)))


ball = sphere(pos=vec(0,10, 0), radius=0.5, color=color.orange)
ball.v = vec(0, -1, 0)      
gr =  vec(0,-9.8,0)  
dt = 0.01

    


while True:
    rate(50)
    scene.camera.follow(ball)
    k = keysdown()
    if 'd' in k:
        ball.pos.x += 0.1
    if 'a' in k:
        ball.pos.x -= 0.1
    if ' ' in k:
        ball.pos.y += 1.1
    if ball.pos.y > (1):
        rate(80)    
        ball.v = ball.v + gr * dt
        ball.pos = ball.pos + ball.v * dt
