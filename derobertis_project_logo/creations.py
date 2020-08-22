from derobertis_project_logo.project_logo import ProjectLogo
from derobertis_project_logo.triangle import Triangle

_pyexlatex_logo = Triangle()
_pyexlatex_logo.set_color("1", "#9c6ff4")
_pyexlatex_logo.set_color("2", "#8eab89")
_pyexlatex_logo.set_color("3", "#113ae1")
_pyexlatex_logo.set_color("4", "#75b415")
_pyexlatex_logo.set_color("5", "#d68556")
_pyexlatex_logo.set_color("6", "#783b98")
_pyexlatex_logo.set_color("7", "#2233d2")
_pyexlatex_logo.set_color("8", "#a8d887")
_pyexlatex_logo.set_color("9", "#f918c5")
_pyexlatex_logo.set_color("10", "#c0797f")
_pyexlatex_logo.set_color("11", "#5e0558")
_pyexlatex_logo.set_color("12", "#e05bd1")
_pyexlatex_logo.set_color("border", "#000")
pyexlatex_logo = ProjectLogo("pyexlatex", _pyexlatex_logo)


LOGOS = [obj for obj in globals().values() if isinstance(obj, ProjectLogo)]
