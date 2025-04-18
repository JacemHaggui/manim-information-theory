from manim import *

class BinaryEliminationFinal(Scene):
    def construct(self):
        binary_str = "1011"
        powers = [8, 4, 2, 1]
        exponents = [3, 2, 1, 0]
        bits = [int(b) for b in binary_str]

        # 1. Display numbers 0 to 15
        numbers = [Text(str(i), font_size=45) for i in range(16)]
        number_line = VGroup(*numbers).arrange(RIGHT, buff=0.5)
        number_line.move_to(UP * 2)
        self.play(*[Write(n) for n in numbers], run_time=4)

        self.wait(1)
        # 2. Display binary number and powers
        bit_group = VGroup()
        for bit, power, exp in zip(bits, powers, exponents):
            bit_txt = Text(str(bit), font_size=48)
            power_txt = MathTex(f"2^{exp} = {power}").scale(0.8)
            power_txt.next_to(bit_txt, DOWN)
            pair = VGroup(bit_txt, power_txt)
            bit_group.add(pair)

        bit_group.arrange(RIGHT, buff=1)
        bit_group.next_to(number_line, DOWN, buff=1)
        self.play(Write(bit_group), run_time=2)

        # Add a frame box around the binary number group
        frame_box = SurroundingRectangle(bit_group, color=BLUE, buff=0.3)
        self.play(Create(frame_box))
        self.wait(4)

        remaining = list(range(16))
        eliminated = []

        questions = [
            ("Is the number ≥ 8?", lambda r: [i for i in r if i < 8]),
            ("Is the number ≥ 8+4 = 12?", lambda r: [i for i in r if i >= 12]),
            ("Is the number ≥ 8+2 = 10?", lambda r: [i for i in r if i < 10 and i >= 8]),
            ("Is the number ≥ 10+1 = 11?", lambda r: [i for i in r if i == 10]),
        ]

        for idx, (question_text, to_eliminate_fn) in enumerate(questions):
            bit_val = bits[idx]
            bit_box = SurroundingRectangle(bit_group[idx][0], color=YELLOW)
            self.play(Create(bit_box))
            self.wait(1)
            # Show question
            question = Text(question_text, font_size=36)
            question.next_to(bit_box, DOWN, buff=1)
            self.play(Write(question), run_time=2)
            self.wait(1)

            # Update box color depending on bit
            if bit_val == 1:
                new_box = SurroundingRectangle(bit_group[idx][0], color=GREEN)
                answer = Text("Yes", font_size=36, color=GREEN)
            else:
                new_box = SurroundingRectangle(bit_group[idx][0], color=RED)
                answer = Text("No", font_size=36, color=RED)

            answer.next_to(question, DOWN)
            self.play(Transform(bit_box, new_box), Write(answer))
            self.wait(0.5)

            # Eliminate numbers
            to_fade = to_eliminate_fn(remaining)
            self.play(*[FadeOut(numbers[i], shift=DOWN*0.5) for i in to_fade])
            remaining = [i for i in remaining if i not in to_fade]
            self.wait(0.5)

            # Fade out question + answer + highlight
            self.play(FadeOut(question), FadeOut(answer), FadeOut(bit_box))

        # Final answer
        final_result = Text(f"Final Answer: {remaining[0]}", font_size=40)
        final_result.next_to(bit_group, DOWN, buff=2)
        self.play(Write(final_result))
        self.wait(2)