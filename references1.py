from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class References1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        point1 = Text("1. The Borrow Checker", font_size = 32)
        point1.align_on_border(UP)
        self.add(point1)

        cpp_code = make_code(
            code_file = r"./src/why_rust/examples/references1.cpp"
        )

        rust_code = make_code(
            code_file = r"./src/why_rust/examples/references1.rs"
        )

        cpp_code.scale(0.5)
        rust_code.scale(0.5)

        cpp_code.next_to(point1, DOWN)

        with self.voiceover(text = (
            "Earlier, we discussed that in Rust, you are only allowed to have either shared immutable references to"
            " values, or one unique mutable reference, but not both. So how does this rule help? Consider the following "
            "C++ code: <bookmark mark='A'/>. We create a vector and then make an iterator to it. Somewhere along the"
            " line, we <bookmark mark='B'/> modify the vector. Now if we tried to read out of the original iterator,"
            " <bookmark mark='C'/> we get undefined behaviour!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(cpp_code[2][:6]), Write(cpp_code[1][:6]))
            self.wait_until_bookmark("B")
            self.play(Write(cpp_code[2][6:7]), Write(cpp_code[1][6:7]))
            self.wait_until_bookmark("C")
            self.play(Write(cpp_code[2][7:]), Write(cpp_code[1][7:]))

        new_cpp_code = cpp_code.copy()
        code_group = VGroup(new_cpp_code, rust_code)
        code_group.arrange(RIGHT, buff = 1, aligned_edge = UP)
        code_group.next_to(point1, DOWN)

        self.wait(1)
        with self.voiceover(text = (
            "The equivalent Rust code would look something like this: "
            "Here, trying to push to v is a compile error, because that requires mutably borrowing v, but an immutable "
            "reference to v already exists in the iterator"
        )):
            self.play(Transform(cpp_code, new_cpp_code))
            self.play(Write(rust_code))

        self.wait(2)
        with self.voiceover(text = (
            "Following this interaction between lifetimes and references, the Rust compiler is able to eliminate "
            "virtually all memory related bugs, including data races, from safe code!"
        )):
            pass

        new_point1 = Text("1. The Borrow Checker", font_size = 24)
        new_point1.align_on_border(UP + LEFT)

        self.play(FadeOut(rust_code), FadeOut(cpp_code), Transform(point1, new_point1))

        return [point1]
