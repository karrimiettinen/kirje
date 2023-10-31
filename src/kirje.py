"""
A framing library for content with headers and body.
"""
from dataclasses import dataclass, field

__version__ = "0.0.2"
__author__ = "Karri Miettinen"
__license__ = "MIT"
__status__ = "Development"

@dataclass
class KirjeDetails:
    content: str = ""
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

class Kirje:
    PAD = int(2)
    ROUNDED = "─│╭╯╰╮├┬┤┴┼"
    details: KirjeDetails
    def __init__(self, details: KirjeDetails = KirjeDetails()) -> None:
        self.details = details
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
                header = f"{key}: {value}"
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
    def displayRounded(self) -> None:
        align = Kirje.convertAlignment(self.details.align_title)
        width = self._getWidth()
        title = " " + self.getTitle() + " "
        print("{0}{1:{fill}{align}{width}}{2}".format(
            self.ROUNDED[2],
            title,
            self.ROUNDED[5],
            align=align,
            fill=self.ROUNDED[0],
            width=width))
        headers = self.details.headers
        for key in headers:
            _key = str(key)
            if (_key.lower() != 'title'):
                row = f"{key}: {headers[key]}"
                print(self.pad(self.ROUNDED[1], width, row))
        print("{0}{1:{fill}{align}{width}}{2}".format(
            self.ROUNDED[6],
            '',
            self.ROUNDED[8],
            align=align,
            fill=self.ROUNDED[0],
            width=width))
        rows = self.details.content.split('\n')
        for row in rows:
            row = self.pad(self.ROUNDED[1], width, row)
            print(row)
        print("{0}{1:{fill}{align}{width}}{2}".format(
            self.ROUNDED[4],
            '',
            self.ROUNDED[3],
            align=align,
            fill=self.ROUNDED[0],
            width=width))
        return None
    def displayDefault(self) -> None:
        align = Kirje.convertAlignment(self.details.align_title)
        width = self._getWidth()
        title = self.getTitle()
        print("+{0:{fill}{align}{width}}+".format(
            title,
            align=align,
            fill='-',
            width=width))
        show_headers = False
        if ((len(self.details.headers) > 1) and (title != '')):
            show_headers = True
        if (show_headers):
            headers = self.details.headers
            for key in headers:
                _key = str(key)
                if (_key.lower() != 'title'):
                    row = f"{key}: {headers[key]}"
                    print(self.pad('|', width, row))
            print("+{0:{fill}{align}{width}}+".format(
                '',
                align=align,
                fill='-',
                width=width))
        rows = self.details.content.split('\n')
        for row in rows:
            row = self.pad('|', width, row)
            print(row)
        print("+{0:{fill}{align}{width}}+".format(
            '',
            align=align,
            fill='-',
            width=width))
        return None
    def display(self, style = 'default') -> None:
        if (style == None):
            style = self.details.style
        match style:
            case 'rounded':
                self.displayRounded()
            case 'default':
                self.displayDefault()
        return None
