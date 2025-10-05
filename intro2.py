from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc


class Intro2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        points = [
            Text("1. The Borrow Checker", font_size = 24),
            Text("2. Safe and Unsafe Rust", font_size = 24),
            Text("3. Hindley Milner Type Inference", font_size = 16, color = GRAY),
            Text("4. Trait-Bounded Polymorphism", font_size = 16, color = GRAY),
            Text("5. Algebraic Data Types", font_size = 16, color = GRAY),
            Text("6. Rust Macros", font_size = 16, color = GRAY),
        ]

        points[0].align_on_border(UP + LEFT)
        for previous, point, in zip(points, points[1:]):
            point.next_to(previous, DOWN)
            point.align_on_border(LEFT)

        with self.voiceover(text = (
            "Primarily, the two biggest innovations in Rust are <bookmark mark='A'/> 1. The borrow checker,"
            "<bookmark mark='B'/> 2. The split between Safe and Unsafe Rust"
        )):
            self.wait_until_bookmark('A')
            self.play(Write(points[0], run_time = 0.5))
            self.wait_until_bookmark('B')
            self.play(Write(points[1], run_time = 0.5))

        self.wait(1)
        with self.voiceover(text = (
            "This is not all though, there are four more reasons"
            "<bookmark mark='A'/> to like Rust, but they're not unique to rust, and not the highlight of this video"
        )):
            self.wait_until_bookmark('A')
            self.play(*[Write(point, run_time = 0.5) for point in points[2:]])

        new_point1 = Text("1. The Borrow Checker", font_size = 32)
        new_point1.align_on_border(UP)
        self.play(
            Transform(points[0], new_point1),
            *[FadeOut(point) for point in points[1:]]
        )
        return [points[0]]
