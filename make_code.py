from manim import *

def make_code(code_file: str | None = None, code_string: str | None = None, lang: str | None = None):
    if code_file is not None:
        return Code(
                code_file = code_file,
                formatter_style = "one-dark",
                language = code_file.split(".")[-1],
                background_config = {"fill_opacity": 0, "stroke_width": 0},
                paragraph_config = {"font": "Spline Sans Mono"},
            ).set_stroke(0)
    if code_string is not None and lang is not None:
        return Code(
            code_string = code_string,
            formatter_style = "one-dark",
            language = lang,
            background_config = {"fill_opacity": 0, "stroke_width": 0},
            paragraph_config = {"font": "Spline Sans Mono"},
        ).set_stroke(0)

    raise ValueError("Wrong code arguments")
