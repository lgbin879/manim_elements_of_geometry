#!/usr/bin/env python3

"""
Author: Guibin Li
Email: guibinli@gmail.com
Github: lgbin879
Description: 
"""

from manim import *

class Definitions01(Scene):
    """
    chapter01 Definitions:


    08. 平面角是一个平面上两条线之间的倾斜，它们相交且不在一条直线上
    A Plane Angle is the inclination to one another of two lines
    in a plane which meet one another and do not lie in a straight line

    09. 且当夹这个角的线是直线时，这个角叫作直线角
    And when the lines containing the angle are straight, the
    angle is called Rectilineal

    10. 当一条直线与另一条直线交成的邻角彼此相等时，这些等角中的每一个都是直角，
    且称这条直线垂直于另一条直线
    When a straight line set up on a straight line makes the
    adjacent angles equal to one another, each of the equal
    angles is right, and the straight line standing on the other
    is called a Perpendicular to that on which it stands

    11. 钝角是大于直角的角
    An Obtuse Angle is an angle greater than a right angle

    12. 锐角是小于直角的角
    An Acute Angle is an angle less than a right angle

    13. 边界是某个东西的端
    A Boundary is that which is an extremity of anything

    14. 形是某一边界或若干边界所围成的东西
    A figure is that which is contained by any boundary or boundaries

    15. 圆是由一条线所围成的平面形，其内有一点与这条线上的点连成的所有线段都相等
    A Cicle is a plane figure contained by one line such that
    all the straight lines falling upon it from one point among
    those lying within the figure are equal to one another

    16. 且这个点叫作圆心
    And the point is called the Center of the circle

    17. 圆的直径是任意一条过圆心作出且沿两个方向被圆周截得的直线，且该直线把圆二等分
    A Diameter of the circle is any straight line drawn through
    the centre and terminated in both directions by the
    circumference of the circle, and such a straight line also
    bisects the circle

    18. 半圆是由直径和它截得的圆周所围成的图形。且半圆的心和圆心相同
    A Semicircle is the figure contained by the diameter and the
    circumference cut off by it. And the centre of the semicircle
    is the same as that of the circle

    19.  直线是由直线围成的形， 三边形是由三条直线围成的形， 
    四边形是由四条直线围成的形，多边形是由四条以上直线围成的形
    Rectilineal Figures are those which are contained by straight
    lines, Trilateral Figures being those contained by three,
    Quadrilateral those contained by four, and Multilateral those
    contained by more than four straight lines

    20. 在三边形中，三边均相等的叫作等边三角形，只有两边相等的叫作等腰三角形，
    三边各不相等的叫作不等边三角形
    Of trilateral figures, an Equilateral Triangle is that which
    has its three sides equal, an Isosceles Triangle that which
    has two of its sides alone equal, and a Scalene Triangle that
    which has its three sides unequal

    21. 此外，在三边形中，有一个直角的叫作直角三角形，有一个钝角的
    叫作钝角三角形，三个角均为锐角的叫作锐角三角形
    Further, of trilateral figures, a Right-Angle Triangle
    that which has a right angle, an Obtuse-Angle Triangle
    which has an obtuse angle, and an Acute-Angle Triangle
    which has its three angles acute

    22. 在四边形中，等边且均为直角的叫作正方形，均为直角但不等边的
    叫作长方形，等边但非直角的叫作菱形，对角对边相等但不等边
    且非直角的叫作长菱形，其他四边形叫作不规则四边形
    Of quadrilateral figures, a Square is that which is both
    equilateral and right-angled; an oblong that which is right-
    angled but not equilateral; a rhombus that which is
    equilateral but not right-angled; and a rhomboid that which
    has its opposite sides and angles equal to one another but is
    neither equilateral nor right-angled. And let quadrilaterals
    other than these be called trapezia

    23. 平行直线是同一平面上沿两个方向无定限延长、不论沿哪个方向都不相交的直线
    Parallel Straight lines are straight lines which, being in
    the same plane and being produced indefinitely in both
    directions, do not meet one another in either direction
    """
    def construct(self):
        """
        01. 点是没有部分的东西
        A point is that which has no part
        """
        def_cn = Tex('01. 点是没有部分的东西', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_cn.set_color(BLUE)
        def_cn.to_edge(UP)
        
        def_en = Tex('A point is that which has no part', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_en.set_color(GREEN)
        def_en.next_to(def_cn, DOWN)

        self.add(def_cn)
        self.play(FadeIn(def_cn))
        self.wait(2)
        self.add(def_en)
        self.play(FadeIn(def_en))
        self.wait(2)
        
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*2.)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=10, rate_func=linear))
        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=6, rate_func=linear))


class Definitions02(Scene):
    """
    02. 线是没有宽的长
    A line is breadthless length
    """
    def construct(self):
        def_cn = Tex('02. 线是没有宽的长', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_cn.set_color(BLUE)
        def_cn.to_edge(UP)
        
        def_en = Tex('A line is breadthless length', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_en.set_color(GREEN)
        def_en.next_to(def_cn, DOWN)

        self.add(def_cn)
        self.play(FadeIn(def_cn))
        self.wait(2)
        self.add(def_en)
        self.play(FadeIn(def_en))
        self.wait(2)

        dot11 = Dot(DL*1.)
        dot12 = Dot(UR*1.)
        l1= Line(dot11, dot12)
        self.add(l1)
        self.play(Create(l1), run_time=2)
        self.wait()
        
        dot21 = Dot(DL*2.)
        dot22 = Dot(UR*2.)
        l2= Line(dot21, dot22)
        self.play(Transform(l1, l2), run_time=2)
        self.wait()
        
        dot31 = Dot(DL*3.)
        dot32 = Dot(UR*3.)
        l3= Line(dot31, dot32)
        self.play(Transform(l2, l3), run_time=2)
        self.wait()
        

class Definitions03(Scene):
    """
    03. 线之端是点
    The extremities of a line are points
    """
    def construct(self):
        def_cn = Tex('03. 线之端是点', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_cn.set_color(BLUE)
        def_cn.to_edge(UP)
        
        def_en = Tex('The extremities of a line are points', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_en.set_color(GREEN)
        def_en.next_to(def_cn, DOWN)

        self.add(def_cn)
        self.play(FadeIn(def_cn))
        self.wait(2)
        self.add(def_en)
        self.play(FadeIn(def_en))
        self.wait(2)

        dot11 = Dot(LEFT*1.)
        dot12 = Dot(RIGHT*1.)
        l1= Line(dot11, dot12)
        self.add(l1)
        self.play(Create(l1), run_time=1)
        self.add(dot11, dot12)
        self.play(FadeIn(dot11), FadeIn(dot12))
        self.wait()
        self.play(FadeOut(dot11), FadeOut(dot12))
        self.wait()
        
        dot21 = Dot(LEFT*3.)
        dot22 = Dot(RIGHT*3.)
        l2= Line(dot21, dot22)
        self.play(Transform(l1, l2), run_time=1)
        self.add(dot21, dot22)
        self.play(FadeIn(dot21), FadeIn(dot22))
        self.wait()
        self.play(FadeOut(dot21), FadeOut(dot22))
        self.wait()
        
        dot31 = Dot(LEFT*6.)
        dot32 = Dot(RIGHT*6.)
        l3= Line(dot31, dot32)
        self.play(Transform(l2, l3), run_time=1)
        self.add(dot31, dot32)
        self.play(FadeIn(dot31), FadeIn(dot32))
        self.wait()
        self.play(FadeOut(dot31), FadeOut(dot32))
        self.wait()
        

class Definitions04(Scene):
    """
    04. 直线是其上均匀放置着点的线
    A Straight line is a line which lies evenly with the points
    """
    def construct(self):
        def_cn = Tex('04. 直线是其上均匀放置着点的线', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_cn.set_color(BLUE)
        def_cn.to_edge(UP)
        
        def_en = Tex('A Straight line is a line which lies evenly with the points', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_en.set_color(GREEN)
        def_en.next_to(def_cn, DOWN)

        self.add(def_cn)
        self.play(FadeIn(def_cn))
        self.wait(2)
        self.add(def_en)
        self.play(FadeIn(def_en))
        self.wait(2)

        dots = VGroup()
        dots.add(Dot())
        for i in range(1,8):
            dots.add(Dot(LEFT*i))
            dots.add(Dot(RIGHT*i))

        l1= Line(dots[-2], dots[-1])
        self.add(l1)
        self.play(Create(l1), run_time=2)
        self.add(dots[0])
        self.play(FadeIn(dots[0]))

        for i in range(1,8):
            self.add(dots[i*2-1], dots[i*2])
            self.play(FadeIn(dots[i*2-1]), FadeIn(dots[i*2]))
        

class Definitions05(Scene):
    """
    05. 面是只有长和宽的东西
    A Surface is that which has length and breadth only
    """
    def construct(self):
        def_cn = Tex('05. 面是只有长和宽的东西', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_cn.set_color(BLUE)
        def_cn.to_edge(UP)
        
        def_en = Tex('A Surface is that which has length and breadth only', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_en.set_color(GREEN)
        def_en.next_to(def_cn, DOWN)

        self.add(def_cn)
        self.play(FadeIn(def_cn))
        self.wait(2)
        self.add(def_en)
        self.play(FadeIn(def_en))
        self.wait(2)

        square = Square(side_length=4.0, fill_opacity=0.5, fill_color=ORANGE)
        square1 = Square(side_length=18.0, fill_opacity=0.5, fill_color=ORANGE)

        self.add(square)
        self.play(DrawBorderThenFill(square, run_time=2))
        self.play(Transform(square, square1), run_time=2)
        self.wait()


class Definitions06(Scene):
    """
    06. 面之端是线
    The extremities of a surface are lines
    """
    def construct(self):
        def_cn = Tex('06. 面之端是线', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_cn.set_color(BLUE)
        def_cn.to_edge(UP)
        
        def_en = Tex('The extremities of a surface are lines', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_en.set_color(GREEN)
        def_en.next_to(def_cn, DOWN)

        self.add(def_cn)
        self.play(FadeIn(def_cn))
        self.wait(2)
        self.add(def_en)
        self.play(FadeIn(def_en))
        self.wait(2)

        square = Square(side_length=4.0)
        rect = Rectangle(width=5.0, height=3.0)
        triangle = Triangle().scale(3).rotate(60*DEGREES)

        self.add(rect)
        self.play(FadeIn(rect), run_time=1)
        self.play(DrawBorderThenFill(rect.set_fill(opacity=1, color=ORANGE)), run_time=2)
        self.play(FadeOut(rect))
        self.wait()

        self.add(triangle)
        self.play(FadeIn(triangle), run_time=1)
        self.play(DrawBorderThenFill(triangle.set_fill(opacity=1, color=PINK)), run_time=2)
        self.play(FadeOut(triangle))
        self.wait()

        self.add(square)
        self.play(FadeIn(square), run_time=1)
        self.play(DrawBorderThenFill(square.set_fill(opacity=1, color=PURPLE)), run_time=2)
        self.play(FadeOut(square))
        self.wait()


class Definitions07(Scene):
    """
    07. 平面是其上均匀放置着直线的面
    A Plane surface is a surface which lies evenly with the
    straight lines on itself
    """
    def construct(self):
        def_cn = Tex('07. 平面是其上均匀放置着直线的面', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_cn.set_color(BLUE)
        def_cn.to_edge(UP)
        
        def_en = Tex('A Plane surface is a surface which lies\\\\' 
                    'evenly with the straight lines on itself', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        def_en.set_color(GREEN)
        def_en.next_to(def_cn, DOWN)

        self.add(def_cn)
        self.play(FadeIn(def_cn))
        self.wait(2)
        self.add(def_en)
        self.play(FadeIn(def_en))
        self.wait(2)

        square = Square(side_length=4.0)
        self.add(square.shift(DOWN))
        self.play(DrawBorderThenFill(square.set_fill(opacity=1, color=ORANGE)), run_time=2)
        self.wait()

        dots_h, dots_v = VGroup(), VGroup()
        for i in range(0,8):
            dots_h.add(Dot(UP*2 + LEFT*2 + RIGHT*(i*0.5)).shift(DOWN))
            dots_h.add(Dot(DOWN*2 + LEFT*2 + RIGHT*(i*0.5)).shift(DOWN))

        for i in range(1,8):
            line = Line(dots_h[i*2], dots_h[i*2+1])
            self.add(line)
            self.play(Create(line), run_time=0.5)

        for i in range(0,8):
            dots_v.add(Dot(LEFT*2 + UP + DOWN*(i*0.5)))
            dots_v.add(Dot(RIGHT*2 + UP + DOWN*(i*0.5)))

        for i in range(1,8):
            line = Line(dots_v[i*2], dots_v[i*2+1])
            self.add(line)
            self.play(Create(line), run_time=0.5)

        
