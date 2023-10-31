import os
import sys
sys.path.append(os.getcwd())
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.kirje.kirje import Kirje, KirjeDetails

rows: list(tuple) = [
    ("content")
]

rounded_text = """╭───────── Hello world ─────────╮
│ ID: 2                         │
│ Created: 2023-10-27 14:18:14  │
│ Modified: 2023-10-27 14:18:25 │
├───────────────────────────────┤
│ Hello                         │
│ world.                        │
╰───────────────────────────────╯"""

class KirjeTest(TestCase):
    kirje: Kirje
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        details = KirjeDetails(
            headers = [
                
            ],
            content='First\nmessage.',
        )
        details = KirjeDetails(
            headers={
                'ID': 2,
                'Title': 'Hello world',
                'Created': '2023-10-27 14:18:14',
                'Modified': '2023-10-27 14:18:25'
            },
            content="Hello\nworld."
        )
        self.kirje = Kirje(details)
        return None
    def testDefaultKirje(self) -> None:
        self.kirje.display()
        # self.assertRaises(TypeError, ...)
        return None
    def testPolymorphism(self) -> None:
        with patch('sys.stdout', new = StringIO()) as fake_out:
            fake_out.truncate(0)
            fake_out.seek(0)
            self.kirje.display("rounded")
            rounded_display_text = fake_out.getvalue()
            self.assertTrue(rounded_display_text == rounded_text, "Display not showing text properly.")
        return None
