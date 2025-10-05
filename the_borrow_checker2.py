from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class TheBorrowChecker2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        point1 = Text("1. The Borrow Checker", font_size = 32)
        point1.align_on_border(UP)
        self.add(point1)

        cpp_code = make_code(
            code_file = r"./src/why_rust/examples/borrow_checker1.cpp"
        )
        rust_code = make_code(
            code_file = r"./src/why_rust/examples/borrow_checker1.rs"
        )
        drop_code = make_code(
            code_string = r"pub fn drop<T>(_x: T) {}",
            lang = "rs"
        )

        with open(r"./src/why_rust/examples/borrow_checker1.rs") as file:
            lines = file.read().splitlines()
            lines[0] = r"fn my_drop<T>(_x: T) {}"
            lines[22] = r"    my_drop(foo);"
            my_drop_code = make_code(
                code_string = "\n".join(lines),
                lang = "rs",
            )

        cpp_code.scale(0.5)
        rust_code.scale(0.5)
        drop_code.scale(0.5)
        my_drop_code.scale(0.5)

        code_group = VGroup(cpp_code, rust_code)
        code_group.arrange(RIGHT, buff = 1, aligned_edge = UP)
        code_group.next_to(point1, DOWN)

        drop_code.move_to(rust_code[2][0])
        rust_code.set_x(cpp_code.get_x())

        self.add(rust_code)

        with self.voiceover(text = (
            "So, what kind of magic is being done inside the <bookmark mark='A'/> drop function? Let's look "
            "at its definition <bookmark mark='B'/> for a clue!"
        )):
            self.wait_until_bookmark("A")
            self.play(Indicate(rust_code[2][22]))
            self.wait_until_bookmark("B")
            self.play(Write(drop_code))

        my_drop_code.move_to(rust_code)

        with self.voiceover(text = (
            "Wait, it's just an empty function? Is there some compiler magic involved here? Actually, no! There is "
            "nothing special about this function, and the code would still work <bookmark mark='A'/> if you defined "
            "it yourself. <bookmark mark='B'/> "
        )):
            self.wait_until_bookmark("A")
            self.play(Transform(rust_code[2][0], my_drop_code[2][0]))
            self.play(Indicate(rust_code[2][0]))
            self.wait_until_bookmark("B")
            self.play(Transform(rust_code[2][22], my_drop_code[2][22]))
            self.play(Indicate(rust_code[2][22]))

        with self.voiceover(text = (
            "So, how does it work then? To understand this, we're going to have to dive deeper into ownership!"
        )):
            pass

        return [point1]