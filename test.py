from manimlib.imports import *


class LinearMotionPart3(Scene):
	def construct(self):
		axes_shift = np.array([-2, -2, 0])
		axes = Axes(center_point=axes_shift, x_min=-5, x_max=9, y_min=-2, y_max=6)
		#
		text_y = Text("velocity")
		text_x = Text("time")
		text_function = Text("v=f(t)函数图像")
		text_CD = Text("在t正半轴任取一段函数")
		text_O = TextMobject("O")
		text_v0_pre = Text("初速度")
		text_v0 = TextMobject("$v_0$")
		text_vt_pre = Text("末速度")
		text_vt = TextMobject("$v_t$")
		text_t_pre = Text("初末时间差")
		text_t = TextMobject("$t$")
		text_a_pre = Text("加速度")
		text_a = TextMobject("$a$")
		text_trapezoid = Text("直角梯形")
		text_at = TextMobject("$at$")
		#
		point_O = axes_shift
		point_A = np.array([-5 - 1 / 3, -2, 0]) + axes_shift
		point_B = np.array([5 + 1 / 3, 6, 0]) + axes_shift
		point_C = np.array([0, 2, 0]) + axes_shift
		point_D = np.array([4, 5, 0]) + axes_shift
		point_E = np.array([0, 5, 0]) + axes_shift
		point_F = np.array([4, 0, 0]) + axes_shift
		point_G = np.array([4, 2, 0]) + axes_shift
		point_H = np.array([-8 / 3, 0, 0]) + axes_shift
		#
		line_function = Line(start=point_A, end=point_B)
		line_CD = Line(start=point_C, end=point_D).set_color(BLUE)
		line_DE = DashedLine(start=point_D, end=point_E)
		line_DF = DashedLine(start=point_D, end=point_F)
		#
		trapezoid = VGroup(
			Line(start=point_O, end=point_F),
			Line(start=point_D, end=point_F).set_color(ORANGE),
			line_CD.copy(),
			Line(start=point_O, end=point_C).set_color(RED)
		)
		#
		self.play(ShowCreation(axes))
		self.play(ApplyMethod(text_y.shift, (np.array([1, 5.5, 0]) + axes_shift)))
		self.play(ApplyMethod(text_x.shift, (np.array([8.5, -0.5, 0]) + axes_shift)))
		self.play(FadeInFromLarge(text_O.copy().next_to(point_O, DOWN + LEFT)))
		self.play(FadeInFromLarge(text_function))
		self.wait(0.5)
		self.play(Transform(text_function, line_function.copy()))
		#
		self.play(FadeInFromLarge(text_CD))
		self.wait(0.5)
		self.play(Transform(text_CD, line_CD.copy()))
		self.play(ShowCreation(VGroup(line_DE, line_DF)))
		#
		self.play(FadeInFromLarge(text_v0_pre))
		self.wait(0.5)
		self.play(Transform(text_v0_pre, text_v0.copy().move_to(LEFT * 2.5)))
		#
		self.play(FadeInFromLarge(text_vt_pre))
		self.wait(0.5)
		self.play(Transform(text_vt_pre, text_vt.copy().move_to(LEFT * 2.5 + UP * 3)))
		#
		self.play(FadeInFromLarge(text_t_pre))
		self.wait(0.5)
		self.play(Transform(text_t_pre, text_t.copy().move_to(RIGHT * 2 + DOWN * 2.5)))
		#
		self.play(FadeInFromLarge(text_a_pre))
		self.wait(0.5)
		t_a = text_a.copy().move_to(UP * 2)
		self.play(Transform(text_a_pre, t_a))
		#
		self.play(FadeInFromLarge(text_trapezoid))
		self.wait(0.5)
		self.play(Transform(text_trapezoid, trapezoid.copy()))
		#
		self.wait(0.5)
		t_v0 = text_v0.copy().set_color(RED).move_to(LEFT * 2.5 + DOWN)
		t_vt = text_vt.copy().set_color(ORANGE).next_to(line_DF, RIGHT)
		self.play(Transform(trapezoid.copy(), VGroup(t_v0, t_vt)))
		#
		self.wait(0.5)
		#
		self.wait(0.5)
		t_x = TextMobject("$x$").set_color(PURPLE).scale(2)
		square = Polygon(point_O, point_F, point_D, point_C, fill_color=PURPLE, fill_opacity=0.5, buff=0)
		self.play(ReplacementTransform(square.copy(), t_x))
		xxx = VGroup(square.copy(), trapezoid.copy())
		xxx_c = xxx.copy().scale(0.15).to_corner(UL)
		self.play(ReplacementTransform(t_x.copy(), xxx))
		self.play(ReplacementTransform(xxx, xxx_c))
		t1 = Text("=").next_to(xxx_c)
		self.play(Write(t1))
		angle_l = Polygon(point_H, point_F, point_D, fill_color=ORANGE, fill_opacity=0.5, buff=0)
		angle_s = Polygon(point_H, point_O, point_C, fill_color=RED, fill_opacity=0.5, buff=0)
		angle_l_c = angle_l.copy().scale(0.15).next_to(t1)
		t2 = Text("-").next_to(angle_l_c)
		angle_s_c = angle_s.copy().scale(0.2).next_to(t2)
		self.play(ShowCreation(angle_l))
		self.play(ReplacementTransform(angle_l, angle_l_c))
		self.play(Write(t2))
		self.play(ShowCreation(angle_s))
		self.play(ReplacementTransform(angle_s, angle_s_c))
		line_HF=Line(start=point_H,end=point_F,color=ORANGE)
		self.play(ShowCreation(line_HF))
		text_HF=TextMobject("$\\frac{v_t}{a}$",color=ORANGE).next_to(line_HF,DOWN)
		self.play(Write(text_HF))
		line_HO=Line(start=point_H,end=point_O,color=RED)
		self.play(ShowCreation(line_HO))
		self.play(ApplyMethod(line_HO.shift,DOWN*0.08))
		text_HO=TextMobject("$\\frac{v_0}{a}$",color=RED).next_to(line_HO,DOWN)
		self.play(Write(text_HO))
		t3=TexMobject("x","=","\\frac{1}{2}\\frac{v_t}{a}v_t","-","\\frac{1}{2}\\frac{v_0}{a}v_0", stroke_width=2).next_to(angle_l_c,DOWN)
		t3[0].set_color(PURPLE)
		t3[2].set_color(ORANGE)
		t3[4].set_color(RED)
		self.play(ReplacementTransform(t_x,t3[0]))
		self.play(Write(t3[1]))
		self.play(ReplacementTransform(angle_l.copy(),t3[2]))
		self.play(Write(t3[3]))
		self.play(ReplacementTransform(angle_s.copy(),t3[4]))
		t4=TexMobject("2ax=v_t^2-v_0^2", stroke_width=2).next_to(t3,DOWN)
		self.play(ReplacementTransform(t3.copy(),t4))
		self.wait(5)

# class Campanulata(Scene):
# 	def construct(self):
# 		circle = Circle(radius=3)
# 		self.play(ShowCreation(circle))
# 		vg = VGroup()
# 		for i in range(12):
# 			k = i + 1
# 			vg.add(Dot(np.array(
# 				[3 * np.sin(15 * DEGREES + 30 * DEGREES * (k - 1)), 3 * np.cos(15 * DEGREES + 30 * DEGREES * (k - 1)),
# 				 0])))
# 		vg.add(vg[0].copy(), vg[1].copy())
# 		for i in range(12):
# 			self.play(ShowCreation(Line(vg[i], vg[i + 2], path_arc=2)))
