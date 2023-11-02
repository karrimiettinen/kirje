"""
A framing library for content with headers and body.
"""
from dataclasses import dataclass, field

__version__ = "0.2.0"
__author__ = "Karri Miettinen"
__license__ = "MIT"
__status__ = "Development"

@dataclass
class KirjeDetails:
    content: str = ""
    header_separation: str = ": "
    fixed_width: int = int(0)
    headers: dict = field(default_factory=dict)
    style: str = "default"
    """Styles: default"""
    decorator: str = '='
    align_title = 'center'
    """
    alignment options: 'center' | 'left' | 'right'
    @default: 'center'
    """

@dataclass
class Corner:
    top_right: str
    bottom_right: str
    bottom_left: str
    top_left: str

@dataclass
class Tack:
    up: str
    right: str
    down: str
    left: str

@dataclass
class Decoration:
    vertical: str
    separator: str
    horizontal: str
    corner: Corner
    tack: Tack
    cross: str

class Kirje:
    _DEFAULT: Decoration
    _DOUBLED: Decoration
    _ROUNDED: Decoration
    _STREAMLINED: Decoration
    PAD = int(2)
    details: KirjeDetails
    def __init__(self, details: KirjeDetails = KirjeDetails()) -> None:
        self.details = details
        self._DEFAULT = Decoration(
            horizontal='-',
            separator='-',
            vertical='|',
            corner=Corner('+', '+', '+', '+'),
            tack=Tack('+', '+', '+', '+'),
            cross='+'
        )
        self._DOUBLED = Decoration(
            horizontal='=',
            separator='=',
            vertical='‖',
            corner=Corner('+', '+', '+', '+'),
            tack=Tack('+', '+', '+', '+'),
            cross='+'
        )
        self._STREAMLINED = Decoration(
            horizontal='=',
            separator='-',
            vertical='|',
            corner=Corner('+', '+', '+', '+'),
            tack=Tack('+', '+', '+', '+'),
            cross='+'
        )
        self._ROUNDED = Decoration(
            horizontal='─',
            separator='─',
            vertical='│',
            corner=Corner('╮', '╯', '╰', '╭'),
            tack=Tack('┴', '├', '┬', '┤'),
            cross='┼'
        )
        return None
    def replaceContent(self, content: str) -> None:
        self.details.content = content
        return None
    @staticmethod
    def convertAlignment(align: str = 'center') -> str:
        match align:
            case 'center':
                align = '^'
            case 'right':
                align = '>'
            case 'left':
                align = '<'
            case _:
                """default to 'center'"""
                align = '^'
        return align
    def _getWidth(self) -> int:
        width = 0
        if (self.details.fixed_width > 0):
            width = self.details.fixed_width
        else:
            for key in self.details.headers:
                value = self.details.headers[key]
                header = f"{key}{self.details.header_separation}{value}"
                if (len(header) > width):
                    width = len(header)
            rows = self.details.content.split('\n')
            for row in rows:
                if (len(row) > width):
                    width = len(row)
        width += self.PAD
        return width
    def getTitle(self) -> str:
        title = ""
        if ('title' in self.details.headers):
            title = self.details.headers['title']
        elif ('Title' in self.details.headers):
            title = self.details.headers['Title']
        return title
    def pad(self, pad_char: str, width: int, row: str = '') -> str:
        width = width - self.PAD
        row = "{0} {1:<{width}} {0}".format(pad_char, row, width=width)
        return row
    def displayBasicEnvelope(self, decoration: Decoration) -> None:
        align = Kirje.convertAlignment(self.details.align_title)
        width = self._getWidth()
        title = self.getTitle()
        print("{0}{1:{fill}{align}{width}}{2}".format(
            decoration.corner.top_left,
            title,
            decoration.corner.top_right,
            align=align,
            fill=decoration.horizontal,
            width=width))
        show_headers = False
        if ((len(self.details.headers) > 1) and (title != '')):
            show_headers = True
        if (show_headers):
            headers = self.details.headers
            for key in headers:
                _key = str(key)
                if (_key.lower() != 'title'):
                    row = f"{key}{self.details.header_separation}{headers[key]}"
                    print(self.pad(decoration.vertical, width, row))
            print("{0}{1:{fill}{align}{width}}{2}".format(
                decoration.tack.right,
                '',
                decoration.tack.left,
                align=align,
                fill=decoration.separator,
                width=width)) # headers and body separator
        rows = self.details.content.split('\n')
        for row in rows:
            row = self.pad(decoration.vertical, width, row)
            print(row)
        print("{0}{1:{fill}{align}{width}}{2}".format(
            decoration.corner.bottom_left,
            '',
            decoration.corner.bottom_right,
            align=align,
            fill=decoration.horizontal,
            width=width))
        return None
    def display(self, style: str = None) -> None:
        """
        Parameters
        ----
            style (str): "default" | "doubled" | "rounded" | "streamlined"
        """
        if (style == None):
            style = self.details.style
        match style:
            case 'default':
                self.displayBasicEnvelope(self._DEFAULT)
            case 'doubled':
                self.displayBasicEnvelope(self._DOUBLED)
            case 'rounded':
                self.displayBasicEnvelope(self._ROUNDED)
            case 'streamlined':
                self.displayBasicEnvelope(self._STREAMLINED)
        return None
