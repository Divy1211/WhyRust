from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class TheBorrowChecker3(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        point1 = Text("1. The Borrow Checker", font_size = 32)
        point1.align_on_border(UP)
        self.add(point1)

        cpp_code = make_code(
            code_file = r"./src/why_rust/examples/borrow_checker2.cpp"
        )

        rust_code = make_code(
            code_file = r"./src/why_rust/examples/borrow_checker2.rs"
        )

        cpp_code.scale(0.5)
        rust_code.scale(0.5)

        rust_code.next_to(point1, DOWN)

        new_rust_code = rust_code.copy()
        code_group = VGroup(new_rust_code, cpp_code)
        code_group.arrange(RIGHT, buff = 1, aligned_edge = UP)
        code_group.next_to(point1, DOWN)

        with self.voiceover(text = (
            "Here's an example class that has four functions. Notice that the four functions have different types for "
            "the self argument. We'll look at the equivalent C++ <bookmark mark='A'/> code to understand the Rust "
            "semantics better."
        )):
            self.play(Write(rust_code))
            self.wait_until_bookmark("A")
            self.play(Transform(rust_code, new_rust_code))
            self.play(Write(cpp_code))

        with self.voiceover(text = (
            "In Rust, const is the default, and mutability is explicit. So this first method<bookmark mark='A'/> is "
            "equivalent to having a const specifier in C++. The ampersand <bookmark mark='B'/> here means that this "
            "method takes self by shared and immutable reference. As the name implies, you can have multiple shared"
            " references to the same object, but you can't change the object being referenced"
        )):
            self.wait_until_bookmark("A")
            self.play(Indicate(rust_code[2][6][21:21 + 5]), Indicate(cpp_code[2][7][24:24 + 5]))
            self.wait_until_bookmark("B")
            self.play(Indicate(rust_code[2][6][21]), Flash(rust_code[2][6][21]))

        self.wait(2)
        with self.voiceover(text = (
            "The next method uses the mut keyword <bookmark mark='A'/> which says that it takes self "
            "by unique and mutable reference. This is the default in C++. The fact that the uniqueness of mutable "
            "references is guaranteed by the type system lies at the heart of Rust's safety guarantees for concurrent "
            "code."
        )):
            self.wait_until_bookmark("A")
            self.play(Indicate(rust_code[2][10][21:21 + 9]), Indicate(cpp_code[2][11][4:4 + 19]))

        self.wait(2)
        with self.voiceover(text = (
            "The third method takes self by <bookmark mark='A'/> immutable value. This is almost the same as an "
            "immutable reference, but the difference is that self was moved into this method by its caller, which "
            "means 1. The caller no longer owns self, and 2. As the owner, this method is now responsible for dropping "
            "self. And now you may be able to guess how the drop function we looked at initially works! At the end of "
            "every function, <bookmark mark='B'/> Rust automatically drops all owned values in reverse order of their "
            "declarations. So the drop function being empty is just a consequence of ownership semantics! Isn't that "
            "really elegant?"
        )):
            self.wait_until_bookmark("A")
            self.play(
                Indicate(rust_code[2][14][21:21 + 4]), Indicate(cpp_code[2][15][24:24 + 5]),
            )
            self.wait_until_bookmark("B")
            self.play(Indicate(cpp_code[2][17][8:8 + 12]))

        self.wait(2)
        with self.voiceover(text = (
            "The last method takes self by <bookmark mark='A'/> mutable value. This is basically exactly the same as the "
            "previous method, with the difference being that self is mutable here. It has the same <bookmark mark='B'/> "
            "dropping semantics"
        )):
            self.wait_until_bookmark("A")
            self.play(
                Indicate(rust_code[2][18][21:21 + 8]), Indicate(cpp_code[2][20][4:4 + 19]),
            )
            self.wait_until_bookmark("B")
            self.play(Indicate(cpp_code[2][22][8:8 + 12]))

        return [point1]
