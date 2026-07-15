# Plainly

Plainly is a tiny interpreter for a very small subset of Python written in plain English.

## Core essentials supported

This version keeps the language simple and beginner friendly. It supports:

- variables with Set
- numbers and text
- arithmetic such as plus, minus, times, divided by, and modulo
- comparisons such as is greater than and is equal to
- simple conditionals with If, Else, and End if
- simple loops with Repeat while and End repeat
- functions with Define a function called ... that takes ... and Return
- output with Say

## Minimal example

```text
Set x to 5.
If x is greater than 3.
    Say the text (big).
Else.
    Say the text (small).
End if.
```

## Run a file

```bash
python3 plainly.py path/to/program.plainly
```

If you want to execute a Plainly file directly, make it executable and run it like this:

```bash
chmod +x path/to/program.plainly
./path/to/program.plainly
```

You can also call the helper from Python:

```python
from plainly import run_file
run_file("path/to/program.plainly")
```

## Tests

Run the tests with:

```bash
python -m unittest discover -s tests -v
```
