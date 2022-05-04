#!/usr/bin/env python3

"""
Author: Guibin Li
Email: guibinli@gmail.com
Github: lgbin879
Description: 
"""

from manim import *


class Opening(Scene):
    """Show all at the Ending"""
    def construct(self):

        ## Make objects
        title = Tex('欧几里得几何五大公设',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=50).set_color(BLUE)
        str1 = Tex('公设1. 平面上从任一点到任一点可作一条直线',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=30).set_color(YELLOW)
        str2 = Tex('公设2. 一条有限直线可沿直线继续延长',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=30).set_color(YELLOW)
        str3 = Tex('公设3. 以任一点为心和任意距离可以作圆',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=30).set_color(YELLOW)
        str4 = Tex('公设4. 所有直角都彼此相等',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=30).set_color(YELLOW)
        str5 = Tex('公设5. 过直线外一点有且只有一条直线与已知直线平行',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=30).set_color(YELLOW)
        
        groups = VGroup(str1, str2, str3, str4, str5)

        ## Set positions
        groups.arrange(DOWN, center=True, aligned_edge=LEFT)
        title.next_to(groups, UP, buff=1, aligned_edge=LEFT)
        self.add(title)
        self.play(FadeIn(title), run_time=1)
        self.add(groups)
        self.play(FadeIn(groups), run_time=2)
        self.wait(3)

        ## Show objects


def add_front_title(self, cn, en):
    """
    add front title for every scene
    """
    title_cn = Tex(cn,
                tex_template=TexTemplateLibrary.ctex, 
                font_size=40)
    title_cn.set_color(BLUE)
    
    title_en = Tex(en,
                tex_template=TexTemplateLibrary.ctex, 
                font_size=40)
    title_en.set_color(GREEN)
    title_en.next_to(title_cn, DOWN)

    self.add(title_cn)
    self.play(FadeIn(title_cn))
    self.wait(2)
    self.add(title_en)
    self.play(FadeIn(title_en))
    self.wait(1)
    self.add_foreground_mobjects(title_cn, title_en)
    self.play(VGroup(title_cn, title_en).animate.to_edge(UP))
    self.wait(1)


class Postulates01(Scene):
    """
    1. 从任一点到任一点可作一条直线
    To draw a straight line from any point to any point
    """
    def construct(self):
        add_front_title(self, 
        '公设1. 平面上从任一点到任一点可作一条直线', 
        'To draw a straight line from any point to any point', 
        )

        dots_up, dots_down = VGroup(), VGroup()
        dots_up.add(Dot(UL), Dot(UR))
        dots_down.add(Dot(DL), Dot(DR))

        self.add(dots_up, dots_down)
        self.play(FadeIn(dots_down), FadeIn(dots_up))
        self.wait(1)

        scale_size = 2
        for down in dots_down:
            for up in dots_up:
                line = Line(down, up, color=ORANGE).scale(scale_size)
                #  line.save_state()
                self.add(line)
                self.play(Create(line))
                #  self.play(ScaleInPlace(line, 3), run_time=3)
                #  self.play(Restore(line))

        line01 = Line(dots_up[0], dots_up[1], color=ORANGE).scale(scale_size)
        self.add(line01)
        self.play(Create(line01))
        line02 = Line(dots_down[0], dots_down[1], color=ORANGE).scale(scale_size)
        self.add(line02)
        self.play(Create(line02))
        self.wait(1)


class Postulates02(Scene):
    """
    2. 一条有限直线可沿直线继续延长
    To produce a finite straight line continuously in a straight line
    """
    def construct(self):
        add_front_title(self, 
        '公设2. 一条有限直线可沿直线继续延长', 
        'To produce a finite straight line continuously in a straight line', 
        )

        dot01, dot02 = Dot(DL*1), Dot(UR*1)
        self.add(dot01, dot02)
        self.play(FadeIn(dot01))
        self.play(FadeIn(dot02))
        line = Line(dot01, dot02).scale(1.2)
        self.play(Create(line))
        self.play(ScaleInPlace(line, 3), run_time=3)
        self.wait(2)


class Postulates03(Scene):
    """
    3. 以任一点为心和任意距离可以作圆
    To describe a circle with any center and distance
    """
    def construct(self):
        add_front_title(self, 
        '公设3. 以任一点为心和任意距离可以作圆', 
        'To describe a circle with any center and distance', 
        )

        dot01, dot02, dot03 = Dot(), Dot(RIGHT), Dot(2*UP)
        self.add(dot01)
        self.play(FadeIn(dot01))

        arrow02 = Arrow(dot01, dot02, buff=0, stroke_width=1, tip_length=0.2)
        self.play(FadeIn(arrow02))
        circle02 = Circle(radius=1)
        self.play(Create(circle02), 
                Rotate(arrow02, about_point=ORIGIN, angle=2*PI, rate_func=linear), 
                run_time=2)
        self.wait(2)
        self.play(FadeOut(VGroup(arrow02, circle02)))
        self.wait(1)

        arrow03 = Arrow(dot01, dot03, buff=0, stroke_width=1, tip_length=0.2)
        self.play(FadeIn(arrow03))
        circle03 = Circle(radius=2).rotate(90*DEGREES)
        self.play(Create(circle03), 
                Rotate(arrow03, about_point=ORIGIN, angle=2*PI, rate_func=linear), 
                run_time=3)
        self.wait(2)


class Postulates04(Scene):
    """
    4. 所有直角都彼此相等
    That all right angles are equal to one another
    """
    def construct(self):
        add_front_title(self, 
        '公设4. 所有直角都彼此相等', 
        'That all right angles are equal to one another',
        )
        line1 = Line(LEFT, RIGHT)
        line2 = Line(DOWN, UP)
        rightangles = [
            RightAngle(line1, line2, length=0.5, quadrant=(1,1), color=BLUE),
            RightAngle(line1, line2, length=0.5, quadrant=(1,-1), color=TEAL),
            RightAngle(line1, line2, length=0.5, quadrant=(-1,1), color=GREEN),
            RightAngle(line1, line2, length=0.5, quadrant=(-1,-1), color=PURPLE),
        ]

        plots = VGroup()
        for rightangle in rightangles:
            lable = MathTex(r"90^{\circ}").move_to(
                    rightangle.point_from_proportion(0.5)*2
                    )
            plot=VGroup(line1.copy(),line2.copy(), rightangle, lable)
            plots.add(plot)
            plots.arrange(buff=1.5)
            self.add(plots)

        self.play(Create(plots), run_time=8)
        self.wait(1)

        equal_mark = Text("=").scale(1.1)
        equal_left = equal_mark.copy().move_to(4*LEFT)
        equal_right = equal_mark.copy().move_to(4*RIGHT)
        equals = VGroup(equal_mark, equal_left, equal_right)
        self.add(equals)
        self.play(FadeIn(equals))
        self.wait(1)
        #  self.play(
        #          Circumscribe(equal_mark, fade_out=True),
        #          Circumscribe(equal_left, fade_out=True),
        #          Circumscribe(equal_right, fade_out=True),
        #          )
        #  self.wait(1)
        self.play(
                Indicate(equals[0]),
                Indicate(equals[1]),
                Indicate(equals[2]),
                )
        self.wait(1)


class Postulates05(Scene):
    """
    5. 同平面内一直线和两条直线相交，若直线同侧的两内角和小于两直角和，
    则这两条直线经无线延长后，在这一侧相交
    if a straight line falling on two straight lines make the 
    interior angles on the same side less than two right angles,
    the two straight lines, if produced indefinitely, meet one
    that side on which are the angles less than the two right angles
    """
    def construct(self):
        add_front_title(self, 
        '公设5. 平行线公设', 
        '过直线外一点有且只有一条直线与已知直线平行'
        )

        dot = Dot(color=RED)
        line1 = Line(LEFT, RIGHT).scale(4).set_color(YELLOW)
        line2 = Line(LEFT, RIGHT).scale(4).shift(DOWN)
        line3 = Line(LEFT, RIGHT).scale(4).set_color(RED).rotate(5*DEGREES)
        line4 = Line(LEFT, RIGHT).scale(4).set_color(RED).rotate(-5*DEGREES)

        yes_str = Tex('平行',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=30).set_color(YELLOW)
        no_str = Tex('不平行',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=30).set_color(RED)

        self.add(line2)
        self.play(FadeIn(line2))
        self.wait(1)
        self.add(dot)
        self.play(FadeIn(dot))
        self.wait(1)
        self.add(line1)
        self.play(Create(line1), run_time=2)
        yes_str.next_to(line1.get_end(), RIGHT, buff=1.)
        self.play(FadeIn(yes_str))
        self.wait(1)

        # not parallel
        self.add(line3)
        self.play(Create(line3), run_time=2)
        self.wait(1)
        no_str.next_to(line3.get_end(), UR, buff=1)
        self.play(FadeIn(no_str))
        self.add(line4)
        self.play(Create(line4), run_time=2)
        self.wait(1)
        no_str1 = no_str.copy()
        no_str1.next_to(line4.get_end(), DR, buff=1)
        self.play(FadeIn(no_str1))
        self.wait(2)


