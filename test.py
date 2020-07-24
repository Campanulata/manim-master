from manimlib.imports import *
import numpy as np
class SquareDifference(Scene):
    def construct(self):
        def AddSide(DoubleArrow):
            line_l=Line(np.array([0,0,0]),np.array([0,0.5,0])).next_to(DoubleArrow,LEFT, buff=0)
            line_r=Line(np.array([0,0,0]),np.array([0,0.5,0])).next_to(DoubleArrow,RIGHT, buff=0)
            return VGroup(DoubleArrow,line_l,line_r)
        
        self.play(FadeIn(TextMobject("$(a-b)^2=a^2+b^2-2ab$").shift(np.array([0,3.5,0]))))
        #
        line_a=Line(LEFT*2,RIGHT*2,stroke_width=10).set_color(BLUE)
        double_arrow_a=AddSide(DoubleArrow(LEFT*2.2,RIGHT*2.2)).shift(np.array([0,-0.5,0]))
        double_arrow_a =VGroup( double_arrow_a,TextMobject("a").shift(np.array([0,-1,0])))
        self.play(ShowCreation(line_a))
        self.play(ShowCreation(double_arrow_a))
        self.play(ApplyMethod(VGroup(line_a,double_arrow_a).shift,np.array([0,-2,0])))
        #
        line_b=Line(LEFT*0.5,RIGHT*0.5,stroke_width=5).set_color(RED)
        double_arrow_b=AddSide(DoubleArrow(LEFT*0.7,RIGHT*0.7).next_to(line_b,UP))
        double_arrow_b =VGroup( double_arrow_b,TextMobject("b").next_to(double_arrow_b,UP, buff=0))
        self.play(ShowCreation(line_b))
        self.play(ShowCreation(double_arrow_b))
        self.play(ApplyMethod(VGroup(line_b,double_arrow_b).shift,DOWN*2+RIGHT*1.5))
        #vgroup
        bg=VGroup(
            Square(side_length=4,stroke_width=10).set_color(BLUE),
            Square(side_length=1,stroke_width=5).set_color(RED).shift(np.array([1.5,1.5,0])),
            Line(np.array([1,1,0]),np.array([1,-2,0])).set_color(YELLOW),
            Line(np.array([1,1,0]),np.array([-2,1,0])).set_color(YELLOW),
            #a
            AddSide(DoubleArrow(LEFT*2.2,RIGHT*2.2)).shift(np.array([0,-2.5,0])),
            AddSide(DoubleArrow(LEFT*2.2,RIGHT*2.2)).rotate(PI/2).shift(np.array([-2.5,0,0])),
            TextMobject("a").shift(np.array([0,-3,0])).set_color(BLUE),
            TextMobject("a").shift(np.array([-3,0,0])).set_color(BLUE),
            #b
            AddSide(DoubleArrow(LEFT*0.7,RIGHT*0.7)).shift(np.array([1.5,2.5,0])),
            AddSide(DoubleArrow(LEFT*0.7,RIGHT*0.7)).rotate(PI/2).shift(np.array([2.5,1.5,0])),
            TextMobject("b").shift(np.array([1.5,3,0])).set_color(RED),
            TextMobject("b").shift(np.array([3,1.5,0])).set_color(RED)
        )
        self.play(Transform(VGroup(line_a,double_arrow_a,line_b,double_arrow_b),bg))
        #tex
        square_a_b=Square(side_length=3,fill=True,fill_color=YELLOW,fill_opacity=0.5).shift(np.array([-0.5,-0.5,0]))
        text_a_b=TextMobject("$(a-b)^2$").next_to(square_a_b,IN).set_color(YELLOW)
        #
        square_a2=Square(side_length=4,fill=True,fill_color=YELLOW,fill_opacity=0.5)
        square_b2=Square(side_length=1,fill=True,fill_color=YELLOW,fill_opacity=0.5).shift(np.array([1.5,1.5,0]))
        square_2ab_up=Polygon(np.array([2,1,0]),np.array([2,2,0]),np.array([-2,2,0]),np.array([-2,1,0]),fill_color=YELLOW,fill_opacity=0.5)
        square_2ab_right=Polygon(np.array([1,2,0]),np.array([2,2,0]),np.array([2,-2,0]),np.array([1,-2,0]),fill_color=YELLOW,fill_opacity=0.5)
        self.play(ShowCreation(text_a_b))
        self.play(Transform(square_a_b.copy(),TextMobject("$(a-b)^2$").shift(np.array([-1.8,3.5,0])).set_color(YELLOW)))
        self.wait(1)
        self.add(square_b2)
        self.play(Transform(square_b2.copy(),TextMobject("$b^2$").shift(np.array([1.02,3.55,0])).set_color(YELLOW)))
        self.wait(1)
        self.remove(square_b2)
        self.add(square_2ab_up,square_2ab_right,square_a_b)
        self.play(Transform(square_a2,TextMobject("$a^2$").shift(np.array([-0.05,3.55,0])).set_color(YELLOW)))
        self.wait(1)
        self.play(Transform(square_2ab_up,TextMobject("$ab$").shift(np.array([2.37,3.54,0])).set_color(YELLOW)))
        self.wait(1)
        self.play(Transform(square_2ab_right,TextMobject("$2ab$").shift(np.array([2.25,3.54,0])).set_color(YELLOW)))
        self.play(FadeInFromLarge(TextMobject("$=$").shift(np.array([-0.6,3.5,0])).set_color(YELLOW)))
        self.wait(3)

class PythagoreanTransformation(Scene):
    def construct(self):
        tri1 = VGroup(
            Line(ORIGIN, 2*RIGHT, color = BLUE),
            Line(2*RIGHT, 3*UP, color = YELLOW),
            Line(3*UP, ORIGIN, color = MAROON_B),
        )
        tri1.shift(2.5*(DOWN+LEFT))
        tri2, tri3, tri4 = copies = [
            tri1.copy().rotate(-i*np.pi/2)
            for i in range(1, 4)
        ]
        a = TexMobject("a").next_to(tri1[0], DOWN, buff = MED_SMALL_BUFF)
        b = TexMobject("b").next_to(tri1[2], LEFT, buff = MED_SMALL_BUFF)
        c = TexMobject("c").next_to(tri1[1].get_center(), UP+RIGHT)

        c_square = Polygon(*[
            tri[1].get_end()
            for tri in [tri1] + copies
        ])
        c_square.set_stroke(width = 0)
        c_square.set_fill(color = YELLOW, opacity = 0.5)
        c_square_tex = TexMobject("c^2")
        big_square = Polygon(*[
            tri[0].get_start()
            for tri in [tri1] + copies
        ])
        big_square.set_color(WHITE)
        a_square = Square(side_length = 2)
        a_square.shift(1.5*(LEFT+UP))
        a_square.set_stroke(width = 0)
        a_square.set_fill(color = BLUE, opacity = 0.5)
        a_square_tex = TexMobject("a^2")
        a_square_tex.move_to(a_square)
        b_square = Square(side_length = 3)
        b_square.move_to(
            a_square.get_corner(DOWN+RIGHT),
            aligned_edge = UP+LEFT
        )
        b_square.set_stroke(width = 0)
        b_square.set_fill(color = MAROON_B, opacity = 0.5)
        b_square_tex = TexMobject("b^2")
        b_square_tex.move_to(b_square)

        self.play(ShowCreation(tri1, run_time = 2))
        self.play(*list(map(Write, [a, b, c])))
        self.wait()
        self.play(
            FadeIn(c_square),
            Animation(c)
        )
        self.play(Transform(c, c_square_tex))
        self.wait(2)
        mover = tri1.copy()
        for copy in copies:
            self.play(Transform(
                mover, copy,
                path_arc = -np.pi/2
            ))
            self.add(copy)
        self.remove(mover)
        self.add(big_square, *[tri1]+copies)
        self.wait(2)
        self.play(*list(map(FadeOut, [a, b, c, c_square])))
        self.play(
            tri3.shift,
            tri1.get_corner(UP+LEFT) -\
            tri3.get_corner(UP+LEFT)
        )
        self.play(tri2.shift, 2*RIGHT)
        self.play(tri4.shift, 3*UP)
        self.wait()
        self.play(FadeIn(a_square))
        self.play(FadeIn(b_square))
        self.play(Write(a_square_tex))
        self.play(Write(b_square_tex))
        self.wait(2)

class SquareSum(Scene):
    def construct(self):
        #公式
        tex_ab=TexMobject("(a+b)^2").move_to(UP*3+LEFT*2)
        tex_equal=TexMobject("=").move_to((UP*3+LEFT*0.7))
        tex_ahat2=TexMobject("a^2").move_to((UP*3))
        tex_bhat2=TexMobject("+b^2").move_to((UP*3+RIGHT*0.9))
        tex_2ab=TexMobject("+2ab").move_to((UP*3+RIGHT*2))
        tex_origin=VGroup(tex_ab,tex_equal,tex_ahat2,tex_bhat2,tex_2ab)
        self.play(FadeIn(tex_origin))
        a=Line(np.array([-1.5,0,0]),np.array([1.5,0,0])).set_color(BLUE)
        text_a=TextMobject("a").set_color(BLUE)
        text_a.add_updater(lambda m: m.next_to(a,DOWN, buff=0.1))
        b=Line(np.array([-0.5,0,0]),np.array([0.5,0,0])).set_color(RED)
        text_b=TextMobject("b").set_color(RED)
        text_b.add_updater(lambda m: m.next_to(b,DOWN, buff=0.1))
        self.play(ShowCreation(a))        
        self.play(ShowCreation(text_a))
        self.play(a.move_to,DOWN*2+LEFT*0.5)
        self.play(ShowCreation(b)) 
        self.play(ShowCreation(text_b))
        self.play(b.move_to,DOWN*2+RIGHT*1.5)
        square_a = Square(side_length =3).set_color(BLUE)
        square_a.move_to(DOWN*0.5+LEFT*0.5)
        text_square_a=TexMobject("a^2").set_color(BLUE)
        text_square_a.add_updater(lambda m:m.next_to(square_a,IN, buff=0.1))
        square_b = Square(side_length =1).set_color(RED)
        square_b.move_to(DOWN*1.5+RIGHT*1.5)
        text_square_b=TexMobject("b^2").set_color(RED)
        text_square_b.add_updater(lambda m:m.next_to(square_b,IN, buff=0.1))
        self.play(ShowCreation(square_a))        
        self.play(ShowCreation(text_square_a))        
        self.play(ShowCreation(square_b))        
        self.play(ShowCreation(text_square_b))
        self.play(square_b.move_to,UP*1.5+RIGHT*1.5)
        #构造背景
        background_a4=Square(side_length =3).set_color(BLUE).move_to(DOWN*0.5+LEFT*0.5).set_depth(1)
        background_a1_right=Line(np.array([2,1,0]),np.array([2,-2,0])).set_color(BLUE)        
        background_a1_up=Line(np.array([-2,2,0]),np.array([1,2,0])).set_color(BLUE)
        background_b4=Square(side_length =1).set_color(RED).move_to(UP*1.5+RIGHT*1.5).set_depth(1)
        background_b1_left=Line(np.array([-2,1,0]),np.array([-2,2,0])).set_color(RED)
        background_all=VGroup(background_a4,background_a1_right,background_a1_up,background_b1_left,background_b4)
        self.play(FadeIn(background_all))

        #几何=>tex
        square_ab=Square(side_length=4).set_color(YELLOW).set_color(YELLOW)
        tex_ab_y=TexMobject("(a+b)^2").move_to(UP*3+LEFT*2).set_color(YELLOW)
        tex_equal_y=TexMobject("=").move_to((UP*3+LEFT*0.7)).set_color(YELLOW)
        tex_ahat2_y=TexMobject("a^2").move_to((UP*3)).set_color(BLUE)
        tex_2ab_y=TexMobject("+2ab").move_to((UP*3+RIGHT*2))
        self.play(ShowCreation(square_ab))
        self.play(Transform(square_ab,tex_ab_y))
        self.play(ShowCreation(square_a))
        self.play(Transform(square_a,tex_ahat2_y))
        self.play(ShowCreation(square_b))
        self.remove(text_square_b)
        self.play(Transform(square_b,TexMobject("+b^2").move_to((UP*3+RIGHT*0.9)).set_color(RED)))
        #2ab
        square_2ab_up=Rectangle(width=3, height=1).move_to(UP*1.5+LEFT*0.5)
        square_2ab_right=Rectangle(width=1, height=3).move_to(DOWN*0.5+RIGHT*1.5)
        double_square_ab=VGroup(square_2ab_up,square_2ab_right)
        self.play(ShowCreation(double_square_ab))
        self.play(Transform(double_square_ab,tex_2ab_y))
        tex_equal_y.scale(3)
        self.play(ShowCreation(tex_equal_y))
        self.play(Transform(tex_equal_y,tex_equal.set_color(YELLOW)))
