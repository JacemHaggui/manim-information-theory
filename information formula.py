from manim import *


class LetterGuessingGame(Scene):
    def construct(self):
        # Create the information content formula
        formula1 = MathTex(
            r"\text{Information Content} = \log_2(\text{Total Number of Outcomes})"
        )
        
        # Display the formula by fading it in
        self.play(Write(formula1))
        
        # Wait for a few seconds before ending
        self.wait(2)
