# Kirje

A framing library for content with headers and body.

Installation: `pip install kirje`

## Usage

Import `Kirje` and `KirjeDetails`. Initialize `KirjeDetails` and use it as parameter to construct concrete `Kirje` object. 

```py
from kirje import Kirje, KirjeDetails

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
message.display("rounded")
```

Expected output:

```
╭──────────Hello world──────────╮
│ ID: 2                         │
│ Created: 2023-10-27 14:18:14  │
│ Modified: 2023-10-27 14:18:25 │
├───────────────────────────────┤
│ Hello                         │
│ world.                        │
╰───────────────────────────────╯
```

## Styles

**Default:**

```
+----------Hello world----------+
| ID: 2                         |
| Created: 2023-10-27 14:18:14  |
| Modified: 2023-10-27 14:18:25 |
+-------------------------------+
| Hello                         |
| world.                        |
+-------------------------------+
```

**Rounded:**

```
╭──────────Hello world──────────╮
│ ID: 2                         │
│ Created: 2023-10-27 14:18:14  │
│ Modified: 2023-10-27 14:18:25 │
├───────────────────────────────┤
│ Hello                         │
│ world.                        │
╰───────────────────────────────╯
```

**Doubled style letter:**

```
+==========Hello world==========+
‖ ID: 2                         ‖
‖ Created: 2023-10-27 14:18:14  ‖
‖ Modified: 2023-10-27 14:18:25 ‖
+===============================+
‖ Hello                         ‖
‖ world.                        ‖
+===============================+
```

**Streamlined style letter:**

```
+==========Hello world==========+
| ID: 2                         |
| Created: 2023-10-27 14:18:14  |
| Modified: 2023-10-27 14:18:25 |
+-------------------------------+
| Hello                         |
| world.                        |
+===============================+
```