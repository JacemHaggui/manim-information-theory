from manim import *

class ProbabilityDistribution(Scene):
    def construct(self):
        # Title
        title = Text("ABACADAE")
        title.to_edge(UL)
        title.scale(0.7)
        self.play(Write(title))
        
        # Create probability labels
        letters = ["A", "B", "C", "D", "E"]
        probs = [
            (r"\frac{1}{2}", "50\\%"),
            (r"\frac{1}{8}", "12.5\\%"),
            (r"\frac{1}{8}", "12.5\\%"),
            (r"\frac{1}{8}", "12.5\\%"),
            (r"\frac{1}{8}", "12.5\\%")
        ]
        
        # Create VGroups for letters and their probabilities
        distributions = VGroup()
        
        for letter, (frac, perc) in zip(letters, probs):
            label = MathTex(f"{letter}: P({letter}) = {frac} \\approx {perc}")
            distributions.add(label)
        
        distributions.scale(0.7)
        distributions.arrange(DOWN, buff=0.4)
        # Move distributions down to make room for title
        distributions.next_to(title, DOWN, buff=0.5)
        distributions.to_edge(LEFT, buff=1)
        
        # Create vertical line
        line = Line(start=UP * 3, end=DOWN * 3)
        line.next_to(distributions, RIGHT, buff=1)
        
        # Add entropy formula reminder with new positioning
        entropy_formula = MathTex(r"\text{Information} = -\log_2(P(x))")
        entropy_formula.set_color(RED)
        entropy_formula.scale(1)
        entropy_formula.to_edge(UR, buff=1)

        # Create explanation text
        explanation = VGroup()
        texts = [
            r"A: -\frac{1}{2} \log_2(\frac{1}{2}) = \frac{1}{2} \text{ bits}",
            r"B: -\frac{1}{8} \log_2(\frac{1}{8}) = \frac{3}{8} \text{ bits}",
            r"C,D,E: -3 \cdot \frac{1}{8} \log_2(\frac{1}{8}) = \frac{9}{8} \text{ bits}",
            r"\text{Total entropy} = \frac{1}{2} + \frac{3}{8} + \frac{9}{8} = 2 \text{ bits}"
        ]
        
        for text in texts:
            expr = MathTex(text)
            expr.scale(0.7)
            explanation.add(expr)
        
        explanation.arrange(DOWN, buff=0.5)
        explanation.next_to(entropy_formula, DOWN, buff=0.5)
        explanation.to_edge(RIGHT, buff=1)
        
        # Animations
        for item in distributions:
            self.play(Write(item), run_time=0.4)
        self.play(Create(line))
        
        self.play(Write(entropy_formula))
        self.wait(2)

        for expr in explanation:
            self.play(Write(expr), run_time=2)
            self.wait(1)
        
        final = MathTex("\\text{Average questions needed} = 2")
        final.scale(0.8)
        final.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(final), run_time=1)
        self.wait(1)