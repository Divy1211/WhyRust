from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc
from src.why_rust.make_code import make_code


class Conclusion(VoiceoverScene):
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

        self.add(points[1])

        with self.voiceover(text = (
            "These features make Rust a great programming language, and very ergonomic to use. The borrow checker helps "
            "prevent memory related bugs in everyday code, and you get fine grained low level control with unsafe "
            "where required. The other features mentioned here are super cool as well, but they're not unique to Rust. "
            "I might cover them in detail in a future video, but until then, thanks for watching, and see you next time!"
        )):
            self.play(*[FadeIn(point) for i, point in enumerate(points) if i != 1])
