from manim import *

class LetterGuessingGame(Scene):
    def construct(self):
        # Initial letters A-H
        letters = list("ABACADAF")
        letter_mobs = [Text(l, font_size=72) for l in letters]
        letter_group = VGroup(*letter_mobs).arrange(RIGHT, buff=0.6)
        self.play(*[FadeIn(l) for l in letter_group])
        self.wait(2)

        # Highlight non-A letters first
        other_letters = [letter_mobs[1], letter_mobs[3], letter_mobs[5], letter_mobs[7]]  # B, C, D, F
        other_highlights = []
        
        for letter in other_letters:
            highlight = SurroundingRectangle(letter, color=YELLOW, buff=0.1)
            other_highlights.append(highlight)
        
        # Create and animate highlights for non-A letters
        for highlight in other_highlights:
            self.play(Create(highlight), run_time=0.5)
            
        self.wait(2)
        
        # Fade out non-A highlights
        self.play(*[FadeOut(highlight) for highlight in other_highlights], run_time=1)
        self.wait(1)

        # Create the four groups
        group1 = VGroup(letter_mobs[0], letter_mobs[1])  # AB
        group2 = VGroup(letter_mobs[2], letter_mobs[3])  # AC
        group3 = VGroup(letter_mobs[4], letter_mobs[5])  # AD
        group4 = VGroup(letter_mobs[6], letter_mobs[7])  # AF

        # Define target positions for each group
        positions = [
            UP * 2 + LEFT * 3,    # Group 1 position
            UP * 2 + RIGHT * 3,   # Group 2 position
            DOWN * 2 + LEFT * 3,  # Group 3 position
            DOWN * 2 + RIGHT * 3, # Group 4 position
        ]

        # Animate the separation
        self.play(
            group1.animate.move_to(positions[0]),
            group2.animate.move_to(positions[1]),
            group3.animate.move_to(positions[2]),
            group4.animate.move_to(positions[3]),
            run_time=2
        )
        self.wait(1)

        # Highlight all A's
        a_letters = [letter_mobs[0], letter_mobs[2], letter_mobs[4], letter_mobs[6]]  # All A's
        highlights = []
        
        for a_letter in a_letters:
            highlight = SurroundingRectangle(a_letter, color=GREEN, buff=0.1)
            highlights.append(highlight)
        
        # Create and animate highlights one by one
        for highlight in highlights:
            self.play(Create(highlight), run_time=0.5)
            
        self.wait(2)
        
        # Fade out all highlights
        self.play(*[FadeOut(highlight) for highlight in highlights], run_time=1)
        self.wait(1)

        # Create final text
        final_text = Text("A X", font_size=72).move_to(ORIGIN)
        
        # Create copies of final text for each transformation
        final_texts = [final_text]
        for _ in range(3):
            final_texts.append(final_text.copy())
            
        # Create math equation
        math_eq = MathTex(r"\log_2(2) = 1 \text{ bit}").next_to(final_text, DOWN, buff=0.5)

        # Transform all groups into A X with a smooth transition
        self.play(
            ReplacementTransform(group1, final_texts[0]),
            ReplacementTransform(group2, final_texts[1]),
            ReplacementTransform(group3, final_texts[2]),
            ReplacementTransform(group4, final_texts[3]),
            run_time=2
        )
        self.wait(2)

        # Fade in the equation
        self.play(Write(math_eq), run_time=1)
        self.wait(1)
        
        # Clear everything
        self.play(
            *[FadeOut(text) for text in final_texts],
            FadeOut(math_eq),
            run_time=1
        )
        self.wait(1)
        
        # Add combined explanatory text and math visualizations
        explanation1 = Text("We divide total outcomes by occurrences:", font_size=36).move_to(UP * 3)
        step1 = MathTex(
            r"\frac{\text{Total Outcomes}}{\text{Occurrences}} = \frac{1}{\frac{\text{Occurrences}}{\text{Total Outcomes}}}"
        ).next_to(explanation1, DOWN, buff=0.5)
        
        explanation2 = Text("This is the inverse of probability because:", font_size=36).move_to(ORIGIN + UP * 0.4)
        step2 = MathTex(
            r"\frac{\text{Occurrences}}{\text{Total Outcomes}} = P(\text{outcome})"
        ).next_to(explanation2, DOWN, buff=0.5)
        
        explanation3 = Text("Therefore:", font_size=36).move_to(DOWN * 2)
        step3 = MathTex(
            r"\frac{\text{Total Outcomes}}{\text{Occurrences}} = \frac{1}{P(\text{outcome})}"
        ).next_to(explanation3, DOWN, buff=0.5)

        # Create boxes to highlight transformations
        box1 = SurroundingRectangle(step1.get_part_by_tex(r"\frac{\text{Occurrences}}{\text{Total Outcomes}}"), color=YELLOW)
        box2 = SurroundingRectangle(step2.get_part_by_tex(r"P(\text{outcome})"), color=YELLOW)
        
        # Animate the combined steps
        self.play(Write(explanation1), run_time=1)
        self.play(Write(step1), run_time=2)
        self.wait(1)
        
        self.play(Write(explanation2), run_time=1)
        self.play(Write(step2), run_time=2)
        self.wait(1)
        
        # Highlight the equivalent parts
        self.play(Create(box1), Create(box2))
        self.wait(2)
        
        # Show the conclusion
        self.play(Write(explanation3), run_time=1)
        self.play(Write(step3), run_time=2)
        self.wait(2)
        
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in [explanation1, step1, explanation2, step2, explanation3, step3, box1, box2]],
            run_time=1
        )
        self.wait(1)
        
        # Continue with your information content formulas...
        formula1 = MathTex(
            r"\text{Information} = \log_2(\frac{\text{Total Outcomes}}{\text{Occurrences of }x})"
        ).move_to(UP * 2)
        
        formula2 = MathTex(
            r"= \log_2(\frac{1}{P(x)})"
        ).next_to(formula1, DOWN, buff=0.5)

        formula3 = MathTex(
            r"= -\log_2(P(x))"
        ).next_to(formula2, DOWN, buff=0.5)

        # Add log rule explanation
        log_rule = MathTex(
            r"\text{(since } \log_2(\frac{1}{x}) = -\log_2(x) \text{)}"
        ).next_to(formula3, RIGHT, buff=-0.2).scale(0.7)
        
        # Update animation sequence
        self.play(Write(formula1), run_time=2)
        self.wait(1)
        self.play(Write(formula2), run_time=2)
        self.play(Write(formula3), run_time=2)
        self.wait(1)
        self.play(Write(log_rule), run_time=1.5)
        
        # Optional: highlight the transformations
        arrow1 = Arrow(formula1.get_bottom() + LEFT * 2, formula2.get_top() + LEFT * 2)
        arrow2 = Arrow(formula2.get_bottom() + LEFT * 2, formula3.get_top() + LEFT * 2)
        
        self.play(Create(arrow1), Create(arrow2))
        self.wait(2)
        
        # Update fade out to include log_rule
        self.play(
            *[FadeOut(mob) for mob in [formula1, formula2, formula3, log_rule, arrow1, arrow2]],
            run_time=1
        )
        
        self.wait(4)

