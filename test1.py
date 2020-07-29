# -*- coding: UTF-8 -*-
from numpy.core.defchararray import center
from manimlib.imports import *
import numpy as np
import random
import pymunk
import pymunk.pygame_util

# pymunk初始化
space = pymunk.Space()        # 空间
space.gravity = (0.0, -900.0) # 设置重力

balls = []  # 所有的球
ticks_to_next_ball = 10  # 多少帧后出现下一个球
# #.创建静态物体
# 静态实体即固定不动的实体，一般不可被穿过。比如地面和墙。
# pymunk.Segment 是静态物体类，我们通过它实例化物体。

# 注意：pymunk中(0, 0)坐标在左下角，pygame中在左上角

# 下面的代码将创建两个静态物体。
static_body = space.static_body
static_lines = [
	pymunk.Segment(static_body, (111.0, 280.0), (407.0, 246.0), 0.0),
	pymunk.Segment(static_body, (407.0, 246.0), (407.0, 343.0), 0.0)
]
for line in static_lines:
    line.elasticity = 0.95  # 弹性系数 0-1
    line.friction = 0.9     # 摩擦系数 0-1
space.add(static_lines)

# 4.创建物体
# pymunk.Body 是物体类
# pymunk.Circle是圆类（其父类是Shape 形状类）
# 下面我们写个函数来创建小球
def create_ball():
    mass = 10   # 质量
    radius = 25 # 半径
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(115, 350)
    body.position = x, 400
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0.9
    space.add(body, shape)
    balls.append(shape)

# 从世界中删除物体
# space.remove(Shape, Body)

# 下面这个函数是创建或删除小球
def update_balls():
	global ticks_to_next_ball
    ticks_to_next_ball -= 1
    if ticks_to_next_ball <= 0:
        create_ball()
        ticks_to_next_ball = 100
    # 移除低于100的球
    balls_to_remove = [ball for ball in balls if ball.body.position.y < 100]
    for ball in balls_to_remove:
        space.remove(ball, ball.body)
        balls.remove(ball)