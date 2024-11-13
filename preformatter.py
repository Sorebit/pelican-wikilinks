import re


def preformat(document: str) -> str:
    def format_match(match):
        """This could split document, section, text"""
        link = match.group(1)  # why 1? Because 0 is the whle thing
        section = None
        text = link
        return f"[{text}](/{link})"

    pattern = r'\[\[([^\]\]]+?)\]\]'
    return re.sub(pattern, format_match, document)


def report(i, o, e):
    print("In / Out / Expect")
    print(i)
    print(o)
    print(e)


def test_format_0():
    in_text_0 = """
    I like text. [[Text is good]].
    Text is [[even better]].
    What about this -> [[]].  Unchanged?
    [[[[]]
    [[]]]]
    [[]]]
    
    """
    out_text_0 = """
    I like text. [Text is good](/Text is good).
    Text is [even better](/even better).
    What about this -> [[]].  Unchanged?
    4: [[[](/[[)
    5: [[]]]] czy coś innego?
    6: [[]]]
    """
    result = preformat(in_text_0)
    
    report(in_text_0, result, out_text_0)
    assert result == out_text_0


def test_multiline():
    """I dont know what to expect here. Consult Obsidian."""
    ins = ("""[[

    ]]
    """,
     """"""
    )
    result = preformat(ins[0])
    report(ins[0], result, ins[1])


def test_format_custom_text():
    in_text = """
    A [[slug|Custom text.]]
    A [[slug#section_0|Custom text.]]
    """

    out_text = """
    A [Custom text](/slug)
    A [Custom text](/slug#section_0)
    """
    result = preformat(in_text)
    
    report(in_text, result, out_text)
    assert result == out_text


test_multiline()
test_format_custom_text()
test_format_0()
