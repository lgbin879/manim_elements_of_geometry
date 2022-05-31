#!/usr/bin/env python3

"""
Author: Guibin Li
Email: guibinli@gmail.com
Github: lgbin879
Description: 
"""

from manim import *

class Opening(Scene):
    """


    公理3. 等量减等量，其差相等
    If equals be subtracted from equals, the remainders are equal

    公理4. 彼此重合的东西彼此相等
    Things which conincide with one another are equal to one another

    公理5. 整理大于部分
    The whole is greater than the part
    """
    def construct(self):

        ## Make objects
        title = Tex('欧几里得几何五大公理',
                    tex_template=TexTemplateLibrary.ctex,
                    font_size=50).set_color(BLUE)
        str1 = Tex('公理1. 等于同量的量相等',
                    tex_template=TexTemplateLibrary.ctex,
                    font_size=40).set_color(YELLOW)
        str2 = Tex('公理2. 等量加等量，其和相等',
                    tex_template=TexTemplateLibrary.ctex,
                    font_size=40).set_color(YELLOW)
        str3 = Tex('公理3. 等量减等量，其差相等',
                    tex_template=TexTemplateLibrary.ctex,
                    font_size=40).set_color(YELLOW)
        str4 = Tex('公理4. 彼此重合的东西彼此相等',
                    tex_template=TexTemplateLibrary.ctex,
                    font_size=40).set_color(YELLOW)
        str5 = Tex('公理5. 整理大于部分',
                    tex_template=TexTemplateLibrary.ctex,
                    font_size=40).set_color(YELLOW)

        groups = VGroup(str1, str2, str3, str4, str5)

        ## Show objects
        groups.arrange(DOWN, center=True, aligned_edge=LEFT)
        title.next_to(groups, UP, buff=1, aligned_edge=LEFT)
        self.add(title)
        self.play(FadeIn(title), run_time=1)
        self.add(groups)
        self.play(FadeIn(groups), run_time=2)
        self.wait(3)


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


class CommonNotion1(Scene):
    """
    公理1. 等于同量的量相等
    Things which are equal to the same thing are also equal to one another
    """
    def construct(self):
        add_front_title(self, 
        '公理1. 等于同量的量相等', 
        'Things which are equal to the same thing \\\\are also equal to one another', 
        )
        ## Make objects
        dot0 = Dot(color=RED).shift(DOWN)
        dot1 = dot0.copy().shift(2*LEFT).set_color(YELLOW)
        dot2 = dot0.copy().shift(2*UP).set_color(YELLOW)
        dot3 = dot0.copy().shift(2*RIGHT).set_color(YELLOW)

        line1 = Line(dot0, dot1)
        line2 = Line(dot0, dot2)
        line3 = Line(dot0, dot3)

        lable1 = Tex("b").next_to(line1, UP)
        lable2 = Tex("a").next_to(line2, RIGHT)
        lable3 = Tex("c").next_to(line3, UP)

        linedot1 = VGroup(line1, dot1, lable1)
        linedot2 = VGroup(line2, dot2, lable2)
        linedot3 = VGroup(line3, dot3, lable3)

        equation1 = Tex("a = b").next_to(line1, DOWN)
        equation2 = Tex("a = c").next_to(equation1, RIGHT, buff=1, aligned_edge=DOWN)
        equation3 = Tex("b = c").next_to(VGroup(equation1, equation2), DOWN, buff=1.5)

        arrow = Arrow(ORIGIN, DOWN, color=YELLOW).next_to(VGroup(equation1, equation2), 
                DOWN, buff=0.2).scale(2)

        ## Show objects
        self.add(dot0)
        self.play(FadeIn(dot0))
        self.add(dot1, dot2, dot3)
        self.play(FadeIn(dot1), FadeIn(dot2), FadeIn(dot3))
        self.add(line2)
        self.play(Create(line2))
        self.play(Create(line1))
        self.play(Create(line3))
        self.wait(1)

        self.play(FadeIn(lable1), FadeIn(lable2), FadeIn(lable3))
        self.play(Rotate(linedot2, about_point=dot0.get_center(), 
                angle=(90*DEGREES), rate_func=there_and_back), 
                run_time=3)
        self.wait(1)

        self.add(equation1)
        self.play(Create(equation1))
        self.wait(1)
        self.play(Rotate(linedot2, about_point=dot0.get_center(), 
                angle=(-90*DEGREES), rate_func=there_and_back), 
                run_time=3)

        self.add(equation2)
        self.play(Create(equation2))
        self.wait(1)
        self.add(arrow)
        self.play(Write(arrow))
        self.add(equation3)
        self.play(Create(equation3))
        self.wait(1)
        self.play(equation3.animate.scale(1.5))
        self.wait(1)
        self.play(Circumscribe(equation3))
        self.wait(2)
        

class CommonNotion2(Scene):
    """
    公理2. 等量加等量，其和相等
    If equals be added to equals, the wholes are equal
    """
    def construct(self):
        add_front_title(self, 
        '公理2. 等量加等量，其和相等', 
        'If equals be added to equals, the wholes are equal', 
        )
        ## Make objects
        triangle1 = Triangle(fill_color=BLUE, fill_opacity=1, stroke_color=WHITE).move_to(LEFT*4+UP)
        square1 = Square(fill_color=GREEN, fill_opacity=1).scale(0.8).move_to(UP)

        self.add(triangle1)
        self.play(FadeIn(triangle1))
        triangle2 = triangle1.copy()
        self.add(triangle2)
        self.play(triangle2.animate.move_to(LEFT*4+DOWN*2))
        self.wait(1)

        self.add(square1)
        self.play(FadeIn(square1))
        square2 = square1.copy()
        self.add(square2)
        self.play(square2.animate.move_to(DOWN*2))
        self.wait(1)

        plus_mark1 = Text("=").move_to(LEFT*2)
        plus_mark2 = Text("=").move_to(LEFT*2+DOWN*2)
        self.add(plus_mark1, plus_mark2)
        self.play(FadeIn(plus_mark1), FadeIn(plus_mark2))
        self.wait(1)
