from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class TheBorrowChecker4(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        point1 = Text("1. The Borrow Checker", font_size = 32)
        point1.align_on_border(UP)
        self.add(point1)

        rust_code = make_code(
            code_file = r"./src/why_rust/examples/borrow_checker1a.rs"
        )

        rust_code1 = make_code(
            code_file = r"./src/why_rust/examples/borrow_checker1b.rs"
        )

        rust_code2 = make_code(
            code_file = r"./src/why_rust/examples/borrow_checker1c.rs"
        )

        rust_code.scale(0.5)
        rust_code1.scale(0.5)
        rust_code2.scale(0.5)

        rust_code.next_to(point1, DOWN)
        rust_code1.next_to(point1, DOWN)
        rust_code2.next_to(point1, DOWN)

        with self.voiceover(text = (
            "Now we come back to the original example and can proceed to answer the other question. How does Rust "
            "know that the data method returns a reference to the int owned by self? The rust compiler can actually "
            "determine at compile time how long an object lives for - and this idea is called the lifetime of the object "
            "The compiler is smart enough to automatically deduce the lifetimes in this example, but let's make them "
            "<bookmark mark='A'/> explicit. This <bookmark mark='B'/> 'a denotes a lifetime, and what it says is "
            "that the returned int reference is valid as long as the self object is. This, is the core idea that allows "
            "the Rust compiler to ensure that we don't accidentally use after free! You can also make lifetimes more "
            "complicated, <bookmark mark='C'/> as in this example where the return type needs to check two lifetimes! "
        )):
            self.play(Write(rust_code))
            self.wait_until_bookmark("A")
            self.play(Transform(rust_code, rust_code1))
            self.wait_until_bookmark("B")
            self.play(
                Indicate(rust_code[2][9][12:12 + 2]),
                Indicate(rust_code[2][9][17:17 + 2]),
                Indicate(rust_code[2][9][30:30 + 2]),
            )
            self.wait_until_bookmark("C")
            self.play(Transform(rust_code, rust_code2))

        return [point1]
