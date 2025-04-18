from manim import *

class EntropyFormula(Scene):
    def construct(self):
        # Title
        main_title = Text("Entropy", font_size=36)
        main_title.to_edge(UP, buff=0.5)
        
        # Main entropy formula
        title = MathTex(r"H(X) = -\sum_{x \in X} P(x)\log_2(P(x))")
        title.scale(1.2)
        title.next_to(main_title, DOWN, buff=0.7)

        # Components explanation
        explanations = VGroup()
        
        components = [
            [r"X", ": The thing we want to describe"],
            [r"H(X)", ": Entropy of X (minimum average number of yes/no questions needed to describe X)"],
            [r"\sum_{x \in X}", ": Sum over all possible values of X"],
            ["P(x)", ": Probability of value x"],
            [r"\log_2", ": Logarithm base 2 (measures in bits)"],
            [r"-P(x)\log_2(P(x))", ": Information content weighted by its probability"]
        ]

        for formula, explanation in components:
            form = MathTex(formula)
            expl = Text(explanation, font_size=32)
            group = VGroup(form, expl).arrange(RIGHT, buff=0.5)
            explanations.add(group)

        explanations.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        explanations.next_to(title, DOWN, buff=-0.3)
        explanations.scale(0.7)

        # Animations
        self.play(Write(main_title))
        self.wait(0.5)
        self.play(Write(title), run_time=5)
        self.wait(4)

        for exp in explanations:
    
            if(exp == explanations[1]):
                self.play(Write(exp), run_time=6)
                self.wait(2)
            else:
                self.play(Write(exp), run_time=2)
                self.wait(1)

        self.wait(4)