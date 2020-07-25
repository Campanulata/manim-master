from numpy.core.defchararray import center
from manimlib.imports import *
import numpy as np



class LinearMotion(Scene):
    def construct(self):
        axes_shift=np.array([-2,-2,0])
        axes=Axes(center_point=axes_shift,x_min=-5,x_max=9,y_min=-2,y_max=6)
        #
        text_y=Text("velocity")
        text_x=Text("time")
        text_function=Text("v=f(t)函数图像")
        text_CD=Text("在t正半轴任取一段函数")
        text_O=TextMobject("O")
        text_v0_pre=Text("初速度")
        text_v0=TextMobject("$v_0$")
        text_vt_pre=Text("末速度")
        text_vt=TextMobject("$v_t$")
        text_t_pre=Text("初末时间差")
        text_t=TextMobject("$t$")
        text_a_pre=Text("加速度")
        text_a=TextMobject("$a$")
        text_trapezoid=Text("直角梯形")
        text_at=TextMobject("$at$")
        #
        point_O=axes_shift
        point_A=np.array([-5-1/3,-2,0])+axes_shift
        point_B=np.array([5+1/3,6,0])+axes_shift
        point_C=np.array([0,2,0])+axes_shift
        point_D=np.array([4,5,0])+axes_shift
        point_E=np.array([0,5,0])+axes_shift
        point_F=np.array([4,0,0])+axes_shift
        #
        line_function=Line(start=point_A,end=point_B)
        line_CD=Line(start=point_C,end=point_D).set_color(BLUE)
        line_DE=DashedLine(start=point_D,end=point_E)
        line_DF=DashedLine(start=point_D,end=point_F)
        #
        trapezoid =VGroup(
            Line(start=point_O,end=point_F).set_color(YELLOW),
            Line(start=point_D,end=point_F).set_color(ORANGE),
            line_CD.copy(),
            Line(start=point_O,end=point_C).set_color(RED)
        )
        #
        self.play(ShowCreation(axes))
        self.play(ApplyMethod(text_y.shift,(np.array([1,5.5,0])+axes_shift)))
        self.play(ApplyMethod(text_x.shift,(np.array([8.5,-0.5,0])+axes_shift)))
        self.play(FadeInFromLarge(text_O.copy().next_to(point_O,DOWN+ LEFT)))
        self.play(FadeInFromLarge(text_function))
        self.wait(0.5)
        self.play(Transform(text_function,line_function.copy()))
        #
        self.play(FadeInFromLarge(text_CD))
        self.wait(0.5)
        self.play(Transform(text_CD,line_CD.copy()))
        self.play(ShowCreation(VGroup(line_DE,line_DF)))
        #
        self.play(FadeInFromLarge(text_v0_pre))
        self.wait(0.5)
        self.play(Transform(text_v0_pre,text_v0.copy().move_to(LEFT*2.5)))
        #
        self.play(FadeInFromLarge(text_vt_pre))
        self.wait(0.5)
        self.play(Transform(text_vt_pre,text_vt.copy().move_to(LEFT*2.5+UP*3)))
        #
        self.play(FadeInFromLarge(text_t_pre))
        self.wait(0.5)
        self.play(Transform(text_t_pre,text_t.copy().move_to(RIGHT*2+DOWN*2.5)))
        #
        self.play(FadeInFromLarge(text_a_pre))
        self.wait(0.5)
        t_a=text_a.copy().move_to(UP*2)
        self.play(Transform(text_a_pre,t_a))
        #
        self.play(FadeInFromLarge(text_trapezoid))
        self.wait(0.5)
        self.play(Transform(text_trapezoid,trapezoid.copy()))
        #
        self.wait(0.5)
        t_v0=text_v0.copy().set_color(RED).move_to(LEFT*2.5+DOWN)
        t_vt=text_vt.copy().set_color(ORANGE).next_to(line_DF,RIGHT)
        t_t=text_t.copy().set_color(YELLOW).move_to(DOWN*2.5)
        self.play(Transform(trapezoid.copy(),VGroup(t_v0,t_vt,t_t)))
        #
        self.wait(0.5)
        t_at=text_at.copy().set_color(PINK).move_to(LEFT*2.5+UP*1.5)
        line_CE=Line(start=point_C,end=point_E).set_color(PINK)
        self.play(Transform(VGroup(t_t.copy(),t_a.copy()),VGroup(t_at,line_CE)))
        #
        self.wait(0.5)
        t_x=TextMobject("$x$").set_color(PURPLE).scale(2)
        square=Polygon(point_O,point_F,point_D,point_C,fill_color=PURPLE,fill_opacity=0.5,buff=0)
        self.play(Transform(square.copy(),t_x))
        self.play(Transform(t_x.copy(),VGroup(square.copy(),trapezoid.copy()) ))
        self.wait()
        t_fun1=TextMobject("$v_t=v_0+at$").set_color(ORANGE).shift(np.array([-3,5,0])+axes_shift)
        self.play(Transform(VGroup(t_vt.copy(),t_v0.copy(),t_a.copy(),t_t.copy()),t_fun1))
        self.wait()
        t_fun2=TextMobject("$x=\\frac{v_0+v_t}{2}t$").set_color(PURPLE).shift(np.array([-3,4,0])+axes_shift)
        self.play(Transform(VGroup(t_x.copy(),t_v0.copy(),t_t.copy(),t_vt.copy()),t_fun2))
        self.wait(5)

class SumDifferenceProduct(GraphScene):
    CONFIG={
        "graph_origin":np.array([0,0,0]),
        "x_min": -2,
        "x_max": 2,
        "x_axis_width": 12,
        "y_min": -1,
        "y_max": 1,
        "y_axis_height": 6,
    }
    def construct(self):
        self.setup_axes(animate=True)
        self.play(ShowCreation(Circle(radius=3).set_color(DARK_GREY)))
        point_A=np.array([1.5,1.5*np.sqrt(3),0])
        point_B=np.array([1.5,0,0])
        point_C=np.array([1.5,-1.5,0])
        point_D=np.array([0,-1.5,0])
        point_E=np.array([-1.5*np.sqrt(3),-1.5,0])
        point_O=np.array([0,0,0])
        line_AB=Line(start=point_A,end=point_B).set_color(RED)
        line_BC=Line(start=point_B,end=point_C).set_color(YELLOW)
        line_CD=Line(start=point_C,end=point_D).set_color(BLUE)
        line_DE=Line(start=point_D,end=point_E).set_color(PINK)
        line_EA=Line(start=point_E,end=point_A).set_color(GREEN)
        #
        line_OA=Line(start=point_O,end=point_A)
        line_OE=Line(start=point_O,end=point_E)
        alpha=60*DEGREES
        beta=30*DEGREES
        theta=(alpha-beta)/2
        arc_alpha=Arc(radius=0.3,angle=alpha,arc_center=point_O)
        arc_beta=Arc(radius=0.5,angle=beta,arc_center=point_E)
        text_alpha=TextMobject("$\\alpha$").shift(np.array([0.5,0.2,0]))
        text_beta=TextMobject("$\\beta$").shift(np.array([-1.7,-1.3,0]))
        arc_theta_up=Arc(radius=1,angle=theta,arc_center=point_A,start_angle=theta+beta+180*DEGREES).set_color(GREEN)
        arc_theta_down=Arc(radius=1,angle=theta,arc_center=point_E,start_angle=beta).set_color(GREEN)
        text_theta_up=TextMobject("$\\theta$").shift(np.array([0.7,1.5,0])).set_color(GREEN)
        text_theta_down=TextMobject("$\\theta$").shift(np.array([-1.45,-0.6,0])).set_color(GREEN)
        bg=VGroup(
            line_AB.copy(),
            line_BC.copy(),
            line_CD.copy(),
            line_DE.copy(),
            line_EA.copy()
        )
        self.play(ShowCreation(VGroup(line_OA.copy(),arc_alpha.copy(),text_alpha.copy())))
        self.play(ShowCreation(VGroup(line_OE.copy())))
        self.play(ShowCreation(bg))
        self.play(ShowCreation(VGroup(arc_beta.copy(),text_beta.copy())))
        self.play(Transform(VGroup(line_OA.copy(),line_OE.copy()),VGroup(arc_theta_up.copy(),arc_theta_down.copy(),text_theta_up.copy(),text_theta_down.copy())))
        self.wait()
        self.play(ApplyMethod(bg.copy().scale(0.2).shift,np.array([-5,2,0])))
        text_1=TextMobject("$2\\theta+\\beta+\\frac{\\pi}{2}-\\alpha=\\frac{\\pi}{2}$").shift(np.array([-3.8,1.5,0]))
        self.play(Transform(bg.copy(),text_1.copy()))
        text_2=TextMobject("$2\\theta+\\beta-\\alpha=0$").shift(np.array([-4.1,1,0]))
        self.play(Transform(text_1.copy(),text_2.copy()))
        text_3=TextMobject("$\\theta=\\frac{\\alpha-\\beta}{2}$").shift(np.array([-4.5,0.5,0])).set_color(GREEN)
        self.play(Transform(text_2.copy(),text_3.copy()))
        #
        self.wait()
        line_OB=Line(start=point_O,end=point_B)
        line_OD=Line(start=point_O,end=point_D)
        text_sin_a=TextMobject("$\\sin\\alpha$").rotate(90*DEGREES).next_to(line_AB,RIGHT).set_color(RED)
        text_sin_b=TextMobject("$\\sin\\beta$").rotate(90*DEGREES).next_to(line_BC,RIGHT).set_color(YELLOW)
        text_cos_a=TextMobject("$\\cos\\alpha$").next_to(line_CD,DOWN).set_color(BLUE)
        text_cos_b=TextMobject("$\\cos\\beta$").next_to(line_DE,DOWN).set_color(PINK)
        #
        self.wait()
        self.play(Transform(VGroup(line_OA,arc_alpha).copy(),text_sin_a.copy()))
        self.play(Transform(VGroup(line_OA,arc_alpha).copy(),text_cos_a.copy()))
        self.play(Transform(VGroup(line_OE,arc_beta).copy(),text_cos_b.copy()))
        self.play(Transform(VGroup(line_OE,arc_beta).copy(),text_sin_b.copy()))
        #
        self.wait()
        point_M=(point_A+point_E)/2
        line_OM=DashedLine(start=point_O,end=point_M)
        self.play(ShowCreation(line_OM))
        #
        self.wait()
        text_cos_t=TextMobject("$\\cos\\frac{\\alpha-\\beta}{2}$").rotate(45*DEGREES).set_color(GREEN)
        text_cos_t_up=text_cos_t.copy().shift(np.array([0,1.7,0]))
        text_cos_t_down=text_cos_t.copy().shift(np.array([-2,-0.3,0]))
        self.play(ReplacementTransform(VGroup(line_OA.copy(),arc_theta_up.copy()),text_cos_t_up))
        self.play(ReplacementTransform(VGroup(line_OE.copy(),arc_theta_down.copy()),text_cos_t_down))
        #
        self.wait()
        text_2cos_diff=TextMobject("2$\\cos\\frac{\\alpha-\\beta}{2}$").rotate(45*DEGREES).set_color(GREEN).shift(np.array([-1,1,0]))
        self.play(Transform(VGroup(text_cos_t_up,text_cos_t_down),text_2cos_diff))
        #
        self.wait()
        arc_orange=Arc(radius=1.7,angle=beta+theta,arc_center=point_E).set_color(ORANGE)
        text_orange=TextMobject("$\\frac{\\alpha+\\beta}{2}$").set_color(ORANGE).shift(np.array([-0.5,-1,0]))
        self.play(ShowCreation(VGroup(text_orange,arc_orange)))
        #
        t_plus=TextMobject("$+$")
        t_equal=TextMobject("$=$")
        #
        self.wait()
        t_sin_a=TextMobject("$\\sin\\alpha$").set_color(RED).shift(np.array([-5.5,-2.5,0]))
        t_1=t_plus.copy().next_to(t_sin_a,RIGHT)
        t_sin_b=TextMobject("$\\sin\\beta$").set_color(YELLOW).next_to(t_1,RIGHT)
        t_2=t_equal.copy().next_to(t_sin_b)
        t_2cos_diff=TextMobject("$2\\cos\\frac{\\alpha-\\beta}{2}$").set_color(GREEN).next_to(t_2,RIGHT)
        t_2sin_sum=TextMobject("$\\sin\\frac{\\alpha+\\beta}{2}$").set_color(ORANGE).next_to(t_2cos_diff,RIGHT)
        self.play(Transform(text_sin_a.copy(),t_sin_a))
        self.play(ShowCreation(t_1))
        self.play(Transform(text_sin_b.copy(),t_sin_b))
        self.play(ShowCreation(t_2))
        self.play(Transform(VGroup(text_2cos_diff.copy(),arc_orange.copy()),VGroup(t_2cos_diff.copy(),t_2sin_sum.copy())))
        #
        self.wait()
        t_cos_a=TextMobject("$\\cos\\alpha$").set_color(BLUE).shift(np.array([-5.5,-3.5,0]))
        t_3=t_plus.copy().next_to(t_cos_a,RIGHT)
        t_cos_b=TextMobject("$\\cos\\beta$").set_color(PINK).next_to(t_3,RIGHT)
        t_4=t_equal.copy().next_to(t_cos_b)
        t_2cos_diff_c=TextMobject("$2\\cos\\frac{\\alpha-\\beta}{2}$").set_color(GREEN).next_to(t_4,RIGHT)
        t_2cos_sum=TextMobject("$\\cos\\frac{\\alpha+\\beta}{2}$").set_color(ORANGE).next_to(t_2cos_diff_c,RIGHT)
        self.play(Transform(text_cos_a.copy(),t_cos_a))
        self.play(ShowCreation(t_3))
        self.play(Transform(text_cos_b.copy(),t_cos_b))
        self.play(ShowCreation(t_4))
        self.play(Transform(VGroup(text_2cos_diff.copy(),arc_orange.copy()),VGroup(t_2cos_diff_c.copy(),t_2cos_sum.copy())))
        self.wait(5)

class TrigonometricFunOfSpecial(GraphScene):
    CONFIG={
        "graph_origin":np.array([0,0,0]),
        "x_min": -2,
        "x_max": 2,
        "x_axis_width": 12,
        "y_min": -1,
        "y_max": 1,
        "y_axis_height": 6,
    }
    def construct(self):
        self.setup_axes(animate=True)
        self.play(ShowCreation(Circle(radius=3)))
        self.play(ShowCreation(Line(start=np.array([0,0,0]),end=np.array([3,0,0])).rotate_about_origin(15*PI/180)))
        self.play(ShowCreation(Arc(radius=0.7,angle=15*PI/180)))
        text_15=TextMobject("$15^o$").scale(0.5).shift(np.array([1,0.1,0]))
        self.play(ShowCreation(text_15))
        self.play(ShowCreation(Polygon(np.array([0,0,0]),np.array([(np.sqrt(6)+np.sqrt(2))*0.75,0,0]),np.array([(np.sqrt(6)+np.sqrt(2))*0.75,(np.sqrt(6)+np.sqrt(2))*0.75,0]))))
        text45=TextMobject("$45^o$").scale(0.5).set_color(BLUE).shift(np.array([2.7,2.5,0]))
        self.add(VGroup(Square(side_length=0.2).set_color(BLUE).shift(np.array([(np.sqrt(6)+np.sqrt(2))*0.75-0.1,0.1,0])),TextMobject("$90^o$").scale(0.5).set_color(BLUE).shift(np.array([2.5,0.1,0])),text45,Arc(radius=0.2,arc_center=np.array([(np.sqrt(6)+np.sqrt(2))*0.75,(np.sqrt(6)+np.sqrt(2))*0.75,0]),start_angle=225*DEGREES,angle=45*DEGREES).set_color(BLUE)))
        # graph = self.get_graph(self.x_2,color = GREEN,x_min = 2,x_max = 4)
        # self.play(ShowCreation(graph),run_time = 2)
        self.play(ShowCreation(Line(start=np.array([(np.sqrt(6)+np.sqrt(2))*0.75,(np.sqrt(6)-np.sqrt(2))*0.75,0]),end=np.array([np.sqrt(6)*0.75,np.sqrt(6)*0.75,0]))))
        text30=TextMobject("$30^o$").scale(0.5).shift(np.array([0.7,0.35,0]))
        self.add(VGroup(Square(side_length=0.2).rotate(45*DEGREES).shift(np.array([np.sqrt(6)*0.75,np.sqrt(6)*0.75-0.1*np.sqrt(2),0])),Arc(radius=0.5,start_angle=15*DEGREES,angle=30*DEGREES),TextMobject("$90^o$").scale(0.5).shift(np.array([1.9,1.4,0])),text30))
        self.wait()
        text1=TextMobject("1").shift(np.array([2,0.5,0]))
        self.play(FadeInFromLarge(text1))
        text_1_2=TextMobject("$\\frac{1}{2}$").shift(np.array([2.3,1.5,0]))
        text_3_2=TextMobject("$\\frac{\\sqrt{3}}{2}$").shift(np.array([0.8,1.3,0]))
        self.play(Transform(VGroup(text30.copy(),text1.copy()),VGroup(text_1_2,text_3_2) ))
        self.wait()
        text_1_2_up=TextMobject("$\\frac{1}{2}$").shift(np.array([2.3,2.9,0]))
        self.play(Transform(VGroup(text_1_2.copy(),text45.copy()),text_1_2_up))
        self.wait()
        text_down=TextMobject("$\\frac{\\sqrt{6}+\\sqrt{2}}{2}$").shift(np.array([1.5,-0.5,0]))
        text_right=TextMobject("$\\frac{\\sqrt{6}+\\sqrt{2}}{2}$").shift(np.array([4,1.5,0]))
        self.play(Transform(VGroup(text_1_2_up.copy(),text_3_2.copy(),text45.copy()),VGroup(text_down,text_right)))
        self.wait()
        line_up=Line(
            start=np.array([(np.sqrt(6)+np.sqrt(2))*0.75,(np.sqrt(6)+np.sqrt(2))*0.75,0]),
            end=np.array([(np.sqrt(6)+np.sqrt(2))*0.75,(np.sqrt(6)-np.sqrt(2))*0.75,0])
            ).set_color(YELLOW)
        v_up=VGroup(
            TextMobject("$\\frac{\\sqrt{2}}{2}$").set_color(YELLOW).next_to(line_up,buff=0),
            line_up
        )
        self.play(Transform(VGroup(text_1_2_up.copy(),text45.copy()),v_up))
        line_down=Line(
            start=np.array([(np.sqrt(6)+np.sqrt(2))*0.75,(np.sqrt(6)-np.sqrt(2))*0.75,0]),
            end=np.array([(np.sqrt(6)+np.sqrt(2))*0.75,0,0])
        ).set_color(PINK)
        text_p1=TextMobject("$\\frac{\\sqrt{6}+\\sqrt{2}}{2}-\\frac{\\sqrt{2}}{2}$").set_color(PINK).shift(np.array([4.5,0.5,0]))
        text_p2=TextMobject("$\\frac{\\sqrt{6}-\\sqrt{2}}{2}$").set_color(PINK).shift(np.array([3.7,0.5,0]))
        self.play(ShowCreation(line_down))
        self.play(FadeInFromLarge(text_p1))
        self.wait()
        self.play(Transform(text_p1,text_p2))
        text_cos=TextMobject("$\\cos15^o=\\sin75^o=\\frac{\\sqrt{6}+\\sqrt{2}}{2}$").shift(np.array([-3,1,0]))
        text_sin=TextMobject("$\\sin15^o=\\cos75^o=\\frac{\\sqrt{6}-\\sqrt{2}}{2}$").shift(np.array([-3,-1,0]))
        self.wait()
        self.play(Transform(VGroup(text_15.copy(),text_down.copy()),text_cos))
        self.wait()
        self.play(Transform(VGroup(text_15.copy(),text_p2.copy()),text_sin))
        self.wait()


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
