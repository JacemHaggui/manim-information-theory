from manim import *

class LetterGuessingGame(Scene):
    def construct(self):

        # Initial letters A-H
        letters = list("ABCDEFGH")
        letter_mobs = [Text(l, font_size=72) for l in letters]
        letter_group = VGroup(*letter_mobs).arrange(RIGHT, buff=0.6).move_to(DOWN * 1.5)
        self.play(*[FadeIn(l) for l in letter_group])
        self.wait(1)

        # Question 1
        q1 = Text("You: Is it in the first half — A to D?", font_size=28).to_edge(UP).shift(DOWN*0.5)
        a1 = Text("Me: Yes.", font_size=28).next_to(q1, DOWN)
        self.play(Write(q1))
        self.wait(0.5)
        self.play(Write(a1))
        self.wait(0.5)

        # Eliminate E-H
        to_remove_1 = letter_mobs[4:]
        self.play(*[l.animate.set_color(RED) for l in to_remove_1])
        self.wait(0.3)
        self.play(*[FadeOut(l, shift=DOWN) for l in to_remove_1])
        
        # Add this to recenter remaining letters A-D
        remaining_letters = VGroup(*letter_mobs[0:4])
        self.play(remaining_letters.animate.move_to(DOWN * 1.5))
        
        # Question 2
        q2 = Text("You: Is it in the first half — A or B?", font_size=28).next_to(a1, DOWN)
        a2 = Text("Me: No.", font_size=28).next_to(q2, DOWN)
        self.play(Write(q2))
        self.wait(0.5)
        self.play(Write(a2))
        self.wait(0.5)

        # Eliminate A, B
        to_remove_2 = letter_mobs[0:2]
        self.play(*[l.animate.set_color(RED) for l in to_remove_2])
        self.wait(0.3)
        self.play(*[FadeOut(l, shift=DOWN) for l in to_remove_2])

        # Add this to recenter remaining letters C-D
        remaining_letters = VGroup(*letter_mobs[2:4])
        self.play(remaining_letters.animate.move_to(DOWN * 1.5))

        # Question 3
        q3 = Text("You: Is it C?", font_size=28).next_to(a2, DOWN)
        a3 = Text("Me: Yes.", font_size=28).next_to(q3, DOWN)
        self.play(Write(q3))
        self.wait(0.5)
        self.play(Write(a3))
        self.wait(0.5)

        # Highlight C, remove D
        c_letter = letter_mobs[2]
        d_letter = letter_mobs[3]
        self.play(d_letter.animate.set_color(RED))
        self.wait(0.3)
        self.play(FadeOut(d_letter, shift=DOWN))


        # Recenter the final letter C
        final_letter = VGroup(c_letter)
        self.play(final_letter.animate.move_to(DOWN * 1.5))
        self.wait(0.5)

        # Highlight C
        self.play(c_letter.animate.set_color(GREEN))
        self.wait(1)

        # Final message
        final_msg = Text("You got it in 3 questions.\nThat’s 3 bits of information!", font_size=30)
        self.play(FadeOut(q1, a1, q2, a2, q3, a3))
        self.play(Write(final_msg))
        self.wait(2)