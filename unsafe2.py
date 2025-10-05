from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class Unsafe2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        point2 = Text("2. Safe and Unsafe Rust", font_size = 32)
        point2.align_on_border(UP)
        self.add(point2)

        rust_code1 = make_code(
            code_file = r"./src/why_rust/examples/unsafe1.rs"
        )

        rust_code2 = make_code(
            code_file = r"./src/why_rust/examples/unsafe3a.rs"
        )

        rust_code3 = make_code(
            code_file = r"./src/why_rust/examples/unsafe3b.rs"
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

        rust_code1.set_x(-3.18759765)
        rust_code1.set_y(1.0825683375)
        self.add(
            rust_code1,
            rust_code2[1][:],
            rust_code2[2][:3],
            rust_code2[2][16:],
        )

        with self.voiceover(text = (
            "First, we'll ensure that the vector actually has three elements to split, otherwise "
            "we return None. Next, we convert the vector into a mutable pointer <bookmark mark='A'/>, and to return the "
            "first, second, and third elements, we can do good old pointer arithmetic <bookmark mark='B'/>. "
        )):
            self.play(Write(rust_code2[2][3:6]))
            self.wait_until_bookmark('A')
            self.play(Write(rust_code2[2][6:8]))
            self.wait_until_bookmark('B')
            self.play(Write(rust_code2[2][8:16]))

        with self.voiceover(text = (
            "Now here comes the unsafe part. Dereferencing a raw pointer like this <bookmark mark='A'/> is considered "
            "unsafe, and is thus not allowed. It is considered unsafe because the pointer could be null, or "
            "it could be pointing to garbage data that is of the incorrect type, or there might already be a mutable "
            "reference to the same address. Dereferencing the pointer in any of these cases will cause undefined behaviour. "
            "Thus, we must use the unsafe keyword <bookmark mark='B'/> here to tell the compiler that this is okay, and "
            "that we've fulfilled the preconditions before dereferencing to ensure that this does not blow up."
        )):
            self.wait_until_bookmark('A')
            self.play(
                Indicate(rust_code2[2][9][13:13+4]),
                Indicate(rust_code2[2][10][13:13+11]),
                Indicate(rust_code2[2][11][10:10+11]),
            )
            self.wait_until_bookmark('B')
            self.play(
                # move lines 1-8
                *[Transform(rust_code2[k][i], rust_code3[k][i]) for i in range(0, 8) for k in range(1, 3)],
                # move lines 9-13
                *[Transform(rust_code2[k][i], rust_code3[k][i + 1]) for i in range(8, 13) for k in range(1, 3)],
                 # insert `unsafe {` line 9
                *[Write(rust_code3[k][8]) for k in range(1, 3)],
                # insert `}` line 15
                *[Write(rust_code3[k][14]) for k in range(1, 3)],
                # move lines 13+
                *[Transform(rust_code2[k][i], rust_code3[k][i + 2]) for i in range(13, 26) for k in range(1, 3)],
            )

        self.wait(1)
        with self.voiceover(text = (
            "We've just abstracted unsafe code in a way such that safe code can call into it <bookmark mark='A'/>, "
            "without having to use the unsafe keyword! The Rust standard library provides several such abstractions "
            "already, which cover almost all common use cases, which means that you don't have to write unsafe code "
            "yourself."
        )):
            self.wait_until_bookmark('A')
            self.play(
                Indicate(rust_code2[2][18][29:]),
                Indicate(rust_code2[2][19][8:-1]),
            )

        self.wait(1)
        with self.voiceover(text = (
            "In a similar manner, when designing an API, you can mark your own functions as unsafe, which the caller "
            "must then call using the unsafe keyword. In this way, unsafe serves two purposes, the first one being that "
            "it clearly conveys that the API has preconditions which need to be met before calling it, and when using "
            "it in code as in this example, it serves as a promise from the programmer that what we are about to do is "
            "fine"
        )):
            pass

        self.wait(1)
        with self.voiceover(text = (
            "This split paradigm of safe and unsafe, is the second big reason for why safe rust code is usually free "
            "from memory related bugs. Safe code is prohibited from performing certain operations that may cause "
            "undefined behaviour, and unsafe code that uses those operations can be abstracted away, with it's usage"
            "clearly conveying the responsibility on the programmer to ensure that any preconditions have been taken "
            "care of."
        )):
            pass

        point1 = Text("1. The Borrow Checker", font_size = 24)
        point1.align_on_border(UP + LEFT)

        new_point2 = Text("2. Safe and Unsafe Rust", font_size = 24)
        new_point2.next_to(point1, DOWN)
        new_point2.align_on_border(LEFT)

        self.play(FadeOut(rust_code1), FadeOut(rust_code2), FadeOut(rust_code3), Transform(point2, new_point2))

        return [point2]
