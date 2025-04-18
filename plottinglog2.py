from manim import *
import math

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