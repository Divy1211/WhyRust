from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class TheBorrowChecker1(VoiceoverScene):
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

        cpp_code.scale(0.5)
        rust_code.scale(0.5)

        cpp_code.next_to(point1, DOWN)

        with self.voiceover(text = (
            "Let's start by discussing ownership. "
            "I'll make a <bookmark mark='A'/> class in C++, which holds some kind of resource, and for the sake of "
            "example, the resource is just a heap allocated int here, but the idea applies to any managed resource. "
            "Let's give the class <bookmark mark='B'/> a constructor and a destructor, and an <bookmark mark='C'/>"
            " accessor method for this precious resource"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(cpp_code[2][:6]), Write(cpp_code[1][:6]))
            self.wait_until_bookmark("B")
            self.play(Write(cpp_code[2][6:15]), Write(cpp_code[1][6:15]))
            self.wait_until_bookmark("C")
            self.play(Write(cpp_code[2][15:20]), Write(cpp_code[1][15:20]))

        self.wait(2)
        with self.voiceover(text = (
            "Now imagine that while using the class <bookmark mark='A'/> you fetch the data, and at some point, some "
            "obscure part of the code that you are working with <bookmark mark='B'/> ends up freeing the foo variable "
            "without you realising it. Now the data pointer is dangling <bookmark mark='C'/>, and if you try to "
            "dereference it, bad things happen!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(cpp_code[2][20:25]), Write(cpp_code[1][20:25]))
            self.wait_until_bookmark("B")
            self.play(Write(cpp_code[2][25:27]), Write(cpp_code[1][25:27]))
            self.wait_until_bookmark("C")
            self.play(Write(cpp_code[2][27:]), Write(cpp_code[1][27:]))

        self.wait(2)
        with self.voiceover(text = (
            "Of course, in this example it is fairly obvious, but a use after free is one of the most common bugs that"
            " can happen in a C++ program! At best, your program will crash, and at worst it will continue running with "
            "garbage data! The compiler does nothing for us to help prevent such an error, and we've kind of accepted "
            "that the onus of ensuring no use after frees is always on the programmer."
        )):
            pass

        new_cpp_code = cpp_code.copy()
        code_group = VGroup(new_cpp_code, rust_code)
        code_group.arrange(RIGHT, buff = 1, aligned_edge = UP)
        code_group.next_to(point1, DOWN)

        self.wait(2)
        with self.voiceover(text = (
            "Enter Rust! We'll create a similar struct <bookmark mark='A'/> in Rust that will mimic the one we made in C++. "
            " In rust, a heap allocated object is wrapped in a Box<T>, so data has the type "
            "<bookmark mark='B'/> Box<i32>. Let's also add a function <bookmark mark='C'/> new which is equivalent to "
            "the constructor, and an accessor method <bookmark mark='D'/> that returns a reference to data"
        )):
            self.play(Transform(cpp_code, new_cpp_code))
            self.wait_until_bookmark("A")
            self.play(Write(rust_code[2][:5]), Write(rust_code[1][:5]))
            self.wait_until_bookmark("B")
            self.play(Indicate(rust_code[2][3][10:-1]))
            self.wait_until_bookmark("C")
            self.play(Write(rust_code[2][5:10]), Write(rust_code[1][5:10]))
            self.wait_until_bookmark("D")
            self.play(Write(rust_code[2][10:15]), Write(rust_code[1][10:15]))

        self.wait(2)
        with self.voiceover(text = (
            "Now let's use this function <bookmark mark='A'/> to fetch data. If for some reason, we end up "
            "dropping <bookmark mark='B'/> the value manually, Rust will no longer let us use the original reference "
            " <bookmark mark='C'/>, and this program no longer compiles! Rust has caught a use after free for us!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(rust_code[2][15:21]), Write(rust_code[1][15:21]))
            self.wait_until_bookmark("B")
            self.play(Write(rust_code[2][21:23]), Write(rust_code[1][21:23]))
            self.wait_until_bookmark("C")
            self.play(Write(rust_code[2][23:]), Write(rust_code[1][23:]))

        self.wait(2)

        new_rust_code =  rust_code.copy().set_x(cpp_code.get_x())
        self.play(FadeOut(cpp_code), Transform(rust_code, new_rust_code))
        return [rust_code]
