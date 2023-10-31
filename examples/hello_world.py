import os
import sys
sys.path.append(os.getcwd())

from src.kirje.kirje import Kirje, KirjeDetails

details = KirjeDetails(
    headers={
        'ID': 2,
        'Title': 'Hello world',
        'Created': '2023-10-27 14:18:14',
        'Modified': '2023-10-27 14:18:25'
    },
    content="Hello\nworld."
)

message = Kirje(details)

print("Default style letter:")
message.display()
print("")
print("Rounded style letter:")
message.display("rounded")
