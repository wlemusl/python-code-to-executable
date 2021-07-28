import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("alien_invasion.py", base=base)]
bin_inc = 'C:\\Users\\willi\\anaconda3\\Lib\\site-packages\\pygame'

cx_Freeze.setup(
    name="alien invasion",
    options={"build_exe": {"packages":["pygame"],
                        "excludes":["tkinter"],
                        "include_files":['images/', "ai_high_score.txt"],
                        "bin_path_includes": bin_inc}},
    executables = executables
    )
