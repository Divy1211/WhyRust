from manim import *

from manim_voiceover import VoiceoverScene

from src.why_rust.conclusion import Conclusion
from src.why_rust.interlude1 import Interlude1
from src.why_rust.intro1 import Intro1
from src.why_rust.intro2 import Intro2
from src.why_rust.references1 import References1
from src.why_rust.the_borrow_checker1 import TheBorrowChecker1
from src.why_rust.the_borrow_checker2 import TheBorrowChecker2
from src.why_rust.the_borrow_checker3 import TheBorrowChecker3
from src.why_rust.the_borrow_checker4 import TheBorrowChecker4
from src.why_rust.unsafe1 import Unsafe1
from src.why_rust.unsafe2 import Unsafe2


class WhyRust(VoiceoverScene):
    def construct(self):
        for cls in [
            Intro1,
            Intro2,
            TheBorrowChecker1,
            TheBorrowChecker2,
            TheBorrowChecker3,
            TheBorrowChecker4,
            References1,
            Interlude1,
            Unsafe1,
            Unsafe2,
            Conclusion,
        ]:
            exclude = cls.construct(self) or []
            ls = [FadeOut(obj) for obj in self.mobjects if obj not in exclude]
            if len(ls) > 0:
                self.play(*ls)
            if len(exclude) > 0:
                self.remove(*exclude)
