from manim import *

class BinaryExample(Scene):
    def construct(self):
        binary_str = "1011"
        powers = [8, 4, 2, 1]  # 2^3, 2^2, 2^1, 2^0
        exponents = [3, 2, 1, 0]
        active_bits = [int(b) for b in binary_str]

        # Title
        binary_text = Text(f"Binary: {binary_str}", font_size=80)
        binary_text.to_edge(UP)
        self.play(Write(binary_text))

        # Group for bit and power pairs
        bit_power_group = VGroup()

        for bit, power, exp in zip(active_bits, powers, exponents):
            bit_text = Text(str(bit), font_size=110)
            power_text = MathTex(f"2^{{{exp}}} = {power}").scale(1.4)
            power_text.next_to(bit_text, DOWN)
            pair = VGroup(bit_text, power_text)
            bit_power_group.add(pair)

        # Space out and center
        bit_power_group.arrange(RIGHT, buff=1)
        bit_power_group.move_to(ORIGIN)

        # Animate each bit and power
        for pair in bit_power_group:
            self.play(Write(pair[0]), Write(pair[1]))

        self.wait(1)

        # Highlight 1s
        included_terms = []
        total = 0
        for pair, bit, power in zip(bit_power_group, active_bits, powers):
            if bit == 1:
                highlight = SurroundingRectangle(pair[0], color=YELLOW)
                self.play(Create(highlight))
                included_terms.append(str(power))
                total += power

        self.wait(0.5)

        # Final addition
        addition = Text(" + ".join(included_terms) + f" = {total}", font_size=70)
        addition.next_to(bit_power_group, DOWN, buff=1)
        self.play(Write(addition))

        self.wait(2)


