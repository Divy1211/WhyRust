from manim import *

from manim_voiceover import VoiceoverScene

from src.svc import svc

RUST_BROWN = "#763F1F"

class Intro1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        rust_logo = SVGMobject(r"./src/why_rust/rust-logo-blk.svg", stroke_color = RUST_BROWN)

        rust_logo.set_fill(RUST_BROWN, opacity = 1)

        for circle in rust_logo[40:]:
            circle.set_fill(BLACK, opacity = 1)

        rust_logo[39].set_opacity(0)
        rust_logo[1].set_fill(opacity = 0)
        rust_logo[1].set_stroke(width = 18)

        rust_logo.scale(2)

        # text = Text("Rust", font_size = 32)
        # text.next_to(rust_logo, DOWN)
        with self.voiceover(text = "Rust has quickly become an increasingly popular programming language"):
            self.play(
                Write(rust_logo, run_time = 1),
                # Write(text, run_time = 1)
            )
        self.wait(1)
        with self.voiceover(text = "But what actually makes it so unique?"):
            pass
