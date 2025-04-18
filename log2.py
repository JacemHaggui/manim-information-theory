from manim import *
import math

class LogBase2Intro(Scene):
    def construct(self):
        title = Tex(r"\textbf{Understanding }$\log_2(x)$").scale(1.2).to_edge(UP)
        self.play(Write(title))

        expl = Text('"2 to the power of what gives me x?"', font_size=30).scale(2)
        self.play(Write(expl))
        self.wait(2)
        self.play(expl.animate.next_to(title, direction=DOWN, buff=1).scale(0.8))

        eq1 = MathTex(r"\log_2(8)", r"=", r"3")
        eq2 = MathTex(r"2^3", r"=",r"2 \times 2 \times 2", r"=", r"8").next_to(eq1, DOWN)

        expl2 = Text('"2 to the power of 3 gives me 8"', font_size=30).next_to(eq2, DOWN, buff=0.8).scale(1.6)

        
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Write(eq2))
        self.wait(0.5)
        self.play(Write(expl2))
        self.wait(1)

class PlotLogBase2(Scene):
    def construct(self):
        # Title
        title = Tex(r"$y = \log_2(x)$").to_edge(UP)
        self.play(Write(title))

        # Axes setup
        axes = Axes(
            x_range=[0, 10, 1],  # x-axis starts from 0
            y_range=[-3, 4, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": True},
            x_axis_config={"numbers_to_include": [1, 2, 4, 8]},
            y_axis_config={"numbers_to_include": [-3, -2, -1, 0, 1, 2, 3]},
        ).to_edge(DOWN)

        # Plot log_2(x), but only from x = 0.125 to 10
        graph = axes.plot(lambda x: math.log(x, 2), color=BLUE, x_range=[0.125, 10])
        graph_label = axes.get_graph_label(graph, label=r"\log_2(x)", x_val=6, direction=DOWN)

        # Animate
        self.play(Create(axes))
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # Optional dots on key points
        dots = VGroup(
            Dot(axes.c2p(2, 1), color=YELLOW),
            Dot(axes.c2p(4, 2), color=YELLOW),
            Dot(axes.c2p(8, 3), color=YELLOW),
        )
        labels = VGroup(
            MathTex(r"(2, 1)").next_to(dots[0], UP),
            MathTex(r"(4, 2)").next_to(dots[1], UP),
            MathTex(r"(8, 3)").next_to(dots[2], UP),
        )

        for dot, label in zip(dots, labels):
            self.play(FadeIn(dot), Write(label))
            self.wait(0.3)

class LogBaseNGeneral(Scene):
    def construct(self):
        title = Tex(r"\textbf{Generalizing to }$\log_n(x)$").scale(1.2).to_edge(UP)
        self.play(Write(title))

        eq1 = MathTex(r"\log_n(x)", r"=", r"y")
        eq2 = MathTex(r"n^y", r"=", r"x").next_to(eq1, DOWN)

        # Adding the explanation with animation
        expl = Text('"n to the power of what gives me x?"', font_size=30).scale(2)
        self.play(Write(expl))
        self.wait(2)
        self.play(expl.animate.next_to(title, DOWN, buff=1).scale(0.8))

        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Write(eq2))
        self.wait(0.5)
        self.wait(1)


class LogExamples(Scene):
    def construct(self):
        title = Tex(r"\textbf{Examples}").scale(1.2).to_edge(UP)
        self.play(Write(title))

        examples = VGroup(
            MathTex(r"\log_2(16) = 4"),
            MathTex(r"\log_3(9) = 2"),
            MathTex(r"\log_{10}(1000) = 3"),
            MathTex(r"\log_5(25) = 2"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(title, DOWN, buff=0.8)

        for ex in examples:
            self.play(Write(ex))
            self.wait(1)