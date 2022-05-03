#!/usr/bin/env python3

"""
Author: Guibin Li
Email: guibinli@gmail.com
Github: lgbin879
Description: 
"""

from manim import *

class Postulates01(Scene):
    """
    1. 从任一点到任一点可作一条直线
    To draw a straight line from any point to any point



    4. 所有直角都彼此相等
    That all right angles are equal to one another

    5. 同平面内一直线和两条直线相交，若直线同侧的两内角和小于两直角和，
    则这两条直线经无线延长后，在这一侧相交
    if a straight line falling on two straight lines make the 
    interior angles on the same side less than two right angles,
    the two straight lines, if produced indefinitely, meet one
    that side on which are the angles less than the two right angles
    """
    def construct(self):
        title_cn = Tex('公设1. 从任一点到任一点可作一条直线', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        title_cn.set_color(BLUE)
        title_cn.to_edge(UP)
        
        title_en = Tex('To draw a straight line from any point to any point', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        title_en.set_color(GREEN)
        title_en.next_to(title_cn, DOWN)

        self.add(title_cn)
        self.play(FadeIn(title_cn))
        self.wait(2)
        self.add(title_en)
        self.play(FadeIn(title_en))
        self.wait(2)
        self.add_foreground_mobjects(title_cn, title_en)

        dots_up, dots_down = VGroup(), VGroup()
        dots_up.add(Dot(UL), Dot(UR))
        dots_down.add(Dot(DL), Dot(DR))

        self.add(dots_up, dots_down)
        self.play(FadeIn(dots_down), FadeIn(dots_up))
        self.wait(1)

        for down in dots_down:
            for up in dots_up:
                line = Line(down, up, color=ORANGE).scale(1.5)
                #  line.save_state()
                self.add(line)
                self.play(Create(line))
                #  self.play(ScaleInPlace(line, 3), run_time=3)
                #  self.play(Restore(line))

        line01 = Line(dots_up[0], dots_up[1], color=ORANGE).scale(1.5)
        self.add(line01)
        self.play(Create(line01))
        line02 = Line(dots_down[0], dots_down[1], color=ORANGE).scale(1.5)
        self.add(line02)
        self.play(Create(line02))
        self.wait(1)


class Postulates02(Scene):
    """
    2. 一条有限直线可沿直线继续延长
    To produce a finite straight line continuously in a straight line
    """
    def construct(self):
        title_cn = Tex('公设2. 一条有限直线可沿直线继续延长', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        title_cn.set_color(BLUE)
        title_cn.to_edge(UP)
        
        title_en = Tex('To produce a finite straight line continuously in a straight line', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        title_en.set_color(GREEN)
        title_en.next_to(title_cn, DOWN)

        self.add(title_cn)
        self.play(FadeIn(title_cn))
        self.wait(2)
        self.add(title_en)
        self.play(FadeIn(title_en))
        self.wait(2)
        self.add_foreground_mobjects(title_cn, title_en)

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
        title_cn = Tex('公设3. 以任一点为心和任意距离可以作圆', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        title_cn.set_color(BLUE)
        title_cn.to_edge(UP)
        
        title_en = Tex('To describe a circle with any center and distance', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        title_en.set_color(GREEN)
        title_en.next_to(title_cn, DOWN)

        self.add(title_cn)
        self.play(FadeIn(title_cn))
        self.wait(2)
        self.add(title_en)
        self.play(FadeIn(title_en))
        self.wait(2)
        self.add_foreground_mobjects(title_cn, title_en)

        dot01, dot02, dot03 = Dot(DL*1), Dot(), Dot(UP)
        self.add(dot01)
        self.play(FadeIn(dot01))
        arrow02 = Arrow(dot01, dot02, buff=0)
        self.play(FadeIn(arrow02))
        #  circle02 = Circle(dot01, radius=arrow02.get_length())
        #  self.play(Create(circle02))
        self.wait(1)


