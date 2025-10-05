from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class Unsafe1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        point2 = Text("2. Safe and Unsafe Rust", font_size = 32)
        point2.align_on_border(UP)
        self.add(point2)

        rust_code1 = make_code(
            code_file = r"./src/why_rust/examples/unsafe1.rs"
        )

        rust_code2 = make_code(
            code_file = r"./src/why_rust/examples/unsafe2.rs"
        )

        rust_code3 = make_code(
            code_file = r"./src/why_rust/examples/unsafe3a.rs"
        )

        rust_code1.scale(0.5)
        rust_code2.scale(0.5)
        rust_code3.scale(0.5)

        code_group = VGroup(rust_code1, rust_code2)
        code_group.arrange(RIGHT, buff = 1, aligned_edge = UP)
        code_group.next_to(point2, DOWN)

        code_group2 = VGroup(rust_code1, rust_code3)
        code_group2.arrange(RIGHT, buff = 1, aligned_edge = UP)
        code_group2.next_to(point2, DOWN)

        # print("POS = ", rust_code1.get_x(), rust_code1.get_y(), rust_code1.get_z())

        with self.voiceover(text = (
            "The fact that mutable borrows are exclusive is extremely useful for proving correctness in a lot of cases, "
            "but it can also be quite inconvenient when working with structs or arrays. <bookmark mark='A'/>"
            "Take this code for example. Here, fields <bookmark mark='B'/> num1, num2, and num3 are separately borrowed "
            "and the borrow checker understands that they are disjoint, and this rust code compiles just fine."
        )):
            self.wait_until_bookmark('A')
            self.play(Write(rust_code1))
            self.wait_until_bookmark('B')
            self.play(
                Indicate(rust_code1[2][9][8:8 + 4]),
                Indicate(rust_code1[2][9][15:15 + 4]),
                Indicate(rust_code1[2][9][28:28 + 4]),
            )
            self.play(
                Indicate(rust_code1[2][10][8:8 + 4]),
                Indicate(rust_code1[2][10][15:15 + 4]),
                Indicate(rust_code1[2][10][28:28 + 4]),
            )
            self.play(
                Indicate(rust_code1[2][11][8:8 + 4]),
                Indicate(rust_code1[2][11][15:15 + 1]),
                Indicate(rust_code1[2][11][24:24 + 4]),
            )

        with self.voiceover(text = (
            "However, if you <bookmark mark='A'/> tried the same with a vector, you cannot borrow different indices "
            " separately. The borrow checker does not understand that these <bookmark mark='B'/> borrows are disjoint. "
            "This is where unsafe Rust comes in. Using unsafe Rust allows us to teach the borrow checker new rules."
        )):
            self.wait_until_bookmark('A')
            self.play(Write(rust_code2))
            self.wait_until_bookmark('B')
            self.play(
                Indicate(rust_code2[2][2][8:8 + 4]),
                Indicate(rust_code2[2][2][15:15 + 4]),
                Indicate(rust_code2[2][2][22:22 + 1]),

                Indicate(rust_code2[2][3][8:8 + 4]),
                Indicate(rust_code2[2][3][15:15 + 4]),
                Indicate(rust_code2[2][3][22:22 + 1]),

                Indicate(rust_code2[2][4][8:8 + 4]),
                Indicate(rust_code2[2][4][15:15 + 1]),
                Indicate(rust_code2[2][4][18:18 + 1]),
            )

        with self.voiceover(text = (
            "Let's define a new function split_three, which will take the vector, and return us "
            "two mutable references to the first and second indices, and one immutable reference to third index."
        )):
            self.play(
                Transform(rust_code2[1][:2], rust_code3[1][16:16+2]), Transform(rust_code2[2][:2], rust_code3[2][16:16+2]),
                Transform(rust_code2[1][2], rust_code3[1][18]), Transform(rust_code2[2][2], rust_code3[2][18]),
                Transform(rust_code2[1][3], rust_code3[1][19]), Transform(rust_code2[2][3], rust_code3[2][19]),
                Transform(rust_code2[1][4], rust_code3[1][20]), Transform(rust_code2[2][4], rust_code3[2][20]),
                Transform(rust_code2[1][5:], rust_code3[1][20:]), Transform(rust_code2[2][5:], rust_code3[2][20:]),
                Write(rust_code3[1][:16])
            )
            self.play(Write(rust_code3[2][:3]), FadeOut(rust_code2[1][4]), FadeOut(rust_code2[2][4]))

        return self.mobjects
