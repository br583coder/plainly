import builtins
import sys
from pathlib import Path


_ORIGINAL_COMPILE = builtins.compile


def _plainly_compile(source, filename, mode="exec", flags=0, dont_inherit=False, optimize=-1):
    if mode == "exec" and filename and str(filename).endswith(".plainly"):
        repo_dir = str(Path(__file__).resolve().parent)
        if repo_dir not in sys.path:
            sys.path.insert(0, repo_dir)

        source_path = Path(filename)
        wrapper = (
            "import plainly\n"
            f"plainly.run_file(r'''{source_path}''', gui_enabled=False)\n"
        )
        return _ORIGINAL_COMPILE(wrapper, filename, mode, flags, dont_inherit, optimize)

    return _ORIGINAL_COMPILE(source, filename, mode, flags, dont_inherit, optimize)


builtins.compile = _plainly_compile
