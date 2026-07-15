import sys
from pathlib import Path


def _run_plainly_script() -> None:
    if len(sys.argv) < 2:
        return

    script_path = sys.argv[0]
    if not script_path.endswith(".plainly"):
        return

    try:
        import plainly
    except Exception:
        return

    source_path = Path(script_path)
    if not source_path.exists():
        return

    with source_path.open("r", encoding="utf-8-sig") as handle:
        plainly.Interpreter(gui_enabled=False).interpret(handle.read())

    raise SystemExit(0)


_run_plainly_script()
