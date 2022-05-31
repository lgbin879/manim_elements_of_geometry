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
    一：如果n是自然数，那么，n+1=n'
    二：如果n和m都是自然数，那么n'+m=(n+m)'
    """
    def construct(self):

        ## Make objects
        title = Tex('皮亚诺公理',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=55).set_color(BLUE)
        str1 = Tex('公理1. 0是自然数',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=35).set_color(YELLOW)
        str2 = Tex("公理2. 每一个确定的自然数a，都有一个确定的后继数a' ，a' 也是自然数",
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=35).set_color(YELLOW)
        str3 = Tex('公理3. 0不是任何自然数的后继数',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=35).set_color(YELLOW)
        str4 = Tex('公理4. 对于每个自然数b、c，b=c当且仅当b的后继数=c的后继数',
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=35).set_color(YELLOW)
        str5 = Tex("公理5. 任意关于自然数的命题，如果证明：它对自然数0是真的，\\\\且假定它对自然数a为真时，可以证明对a' 也真。\\\\那么，命题对所有自然数都真",
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=35).set_color(YELLOW)
        
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
                font_size=35)
    title_cn.set_color(BLUE)
    
    title_en = Tex(en,
                tex_template=TexTemplateLibrary.ctex, 
                font_size=35)
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

