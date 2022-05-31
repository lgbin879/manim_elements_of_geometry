#!/usr/bin/env python3

"""
Author: Guibin Li
Email: guibinli@gmail.com
Github: lgbin879
Description: 
"""

from manim import *

class chapter01Proposition01(Scene):
    """在一给定的有限直线上作一个等边三角形"""
    def construct(self):
        ## set default
        Dot.set_default(color=RED)
        Circle.set_default(color=WHITE)
        Text.set_default(font_size=30)
        Tex.set_default(font_size=25, tex_template=TexTemplateLibrary.ctex)
        Polygon.set_default(stroke_color=ORANGE)

        ## Make objects
        title = Tex('几何原本第一卷命题1',
                    font_size=50).set_color(BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait()

        dotA, dotB = Dot(LEFT), Dot(RIGHT)
        lableA, lableB = Text("A").next_to(dotA, LEFT), Text("B").next_to(dotB, RIGHT)
        lableD, lableE = Text("D").next_to(LEFT*3, LEFT), Text("E").next_to(RIGHT*3, RIGHT)
        circleA = Circle(radius=2).move_to(LEFT)
        circleB = Circle(radius=2).rotate(PI).move_to(RIGHT)

        self.add(dotA)
        self.wait()
        self.play(AnimationGroup(FadeIn(lableA), Indicate(dotA), lag_ratio=0))
        self.add(dotB)
        self.wait()
        self.play(AnimationGroup(FadeIn(lableB), Indicate(dotB), lag_ratio=0))
        self.wait()

        arrowA = Arrow(dotA, dotB, buff=0, stroke_width=2, tip_length=0.2)
        self.play(FadeIn(arrowA))
        self.add(circleA)
        self.play(Create(circleA, rate_func=linear), 
                Rotate(arrowA, about_point=dotA.get_center(), angle=2*PI, rate_func=linear), 
                run_time=2)
        self.play(FadeOut(arrowA))
        self.wait()

        arrowB = Arrow(dotB, dotA, buff=0, stroke_width=2, tip_length=0.2)
        self.play(FadeIn(arrowB))
        self.add(circleB)
        self.play(Create(circleB, rate_func=linear), 
                Rotate(arrowB, about_point=dotB.get_center(), angle=2*PI, rate_func=linear), 
                run_time=2)
        self.play(FadeOut(arrowB))
        self.wait()

        #  print(VGroup(circleA, circleB).get_all_points())
        inter = Intersection(circleA, circleB)
        dotC = Dot(inter.get_top())
        lableC = Text("C").next_to(dotC, UP)
        self.add(dotC, lableC)
        self.play(FadeIn(lableC), Indicate(dotC))
        self.wait()
        self.add(lableD, lableE)
        self.play(FadeIn(lableD), FadeIn(lableE))
        self.wait()

        triangle = Polygon(dotA.get_center(), dotB.get_center(), dotC.get_center(),
                fill_opacity=0)
        self.add(triangle)
        self.play(Create(triangle, rate_func=linear), run_time=2)
        #  self.play(ShowPassingFlash(triangle))
        self.wait()

        lineAB = VGroup(lableA.copy(), lableB.copy(), Line(dotA, dotB))
        self.add(lineAB)
        lableAB = Text("AB").move_to(UP*2.5+RIGHT*3)
        self.play(ReplacementTransform(lineAB, lableAB))
        eq1 = Text("=").next_to(lableAB, RIGHT)
        self.add(eq1)
        self.play(FadeIn(eq1))

        lineAC = VGroup(lableA.copy(), lableC.copy(), Line(dotA, dotC))
        self.add(lineAC)
        lableAC = Text("AC").next_to(eq1, RIGHT)
        self.play(ReplacementTransform(lineAC, lableAC))
        eq2 = Text("=").next_to(lableAC, RIGHT)
        self.add(eq2)
        self.play(FadeIn(eq2))

        lineBC = VGroup(lableB.copy(), lableC.copy(), Line(dotB, dotC))
        self.add(lineBC)
        lableBC = Text("BC").next_to(eq2, RIGHT)
        self.play(ReplacementTransform(lineBC, lableBC))
        self.wait()

        prove = Tex("证明", color=YELLOW, font_size=40).next_to(lableAC, UP)
        self.play(FadeIn(prove))
        self.play(Indicate(prove))
        self.wait()

        graphs = VGroup(dotA, lableA, dotB, lableB, dotC, lableC, lableD, lableE,
                circleA, circleB, triangle)
        self.play(graphs.animate.to_edge(LEFT))
        self.wait()

        textBCD = Tex("BCD是以A为圆心的同一圆上不同点 -> AC = AB"
                ).next_to(lableBC, DOWN).align_to(lableBC, RIGHT)
        textACE = Tex("ACE是以B为圆心的同一圆上不同点 -> BA = BC"
                ).next_to(textBCD, DOWN).align_to(textBCD, RIGHT)
        textABBA = Tex("AB即BA").next_to(textACE, DOWN).align_to(textACE, RIGHT)
        textConclution = MathTex(r"\therefore AC = AB(BA) = BC"
                ).next_to(textABBA, DOWN).align_to(textABBA, RIGHT)
        textConclution1 = Tex("AC = AB = BC"
                ).next_to(textConclution, DOWN).align_to(textConclution, RIGHT)
        textFinal = MathTex(r"\therefore AB = AC = BC", color=YELLOW,
                ).next_to(textConclution1, DOWN).align_to(textConclution1, RIGHT)
        ed = Tex("得证", color=YELLOW, font_size=40).next_to(textFinal, DOWN)

        textGroup = VGroup(textBCD, textACE, textABBA,
                textConclution, textConclution1, textFinal, ed)
        for txt in textGroup:
            self.add(txt)
            self.play(Write(txt), run_time=2)
            self.wait()

        self.wait(3)

