from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc


class Interlude1(VoiceoverScene):
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

        self.add(points[0])

        with self.voiceover(text = (
            "And that's all that there is to borrow checking! Really, once you understand the ideas presented earlier, "
            "most of the compiler errors and lifetime related errors make a lot of sense, and you start seeing the "
            "compiler as your friend, than something to fight!"
        )):
            self.play(*[FadeIn(point) for point in points[1:]])

        self.wait(2)
        point2 = Text("2. Safe and Unsafe Rust", font_size = 32)
        point2.align_on_border(UP)

        with self.voiceover(text = (
            "Moving on, let's dive into safe and unsafe Rust!"
        )):
            self.play(
                Transform(points[1], point2),
                *[FadeOut(point) for i, point in enumerate(points) if i != 1]
            )

        return [points[1]]
