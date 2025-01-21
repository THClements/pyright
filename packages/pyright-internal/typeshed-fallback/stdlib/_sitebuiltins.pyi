import sys
from collections.abc import Iterable
from typing import ClassVar, Literal, NoReturn

class Quitter:
    name: str
    eof: str
    def __init__(self, name: str, eof: str) -> None: ...
    def __call__(self, code: sys._ExitCode = None) -> NoReturn: ...

class _Printer:
    MAXLINES: ClassVar[Literal[23]]
    def __init__(self, name: str, data: str, files: Iterable[str] = (), dirs: Iterable[str] = ()) -> None: ...
    def __call__(self) -> None: ...

class _Helper:
    def __call__(self, request: object = ...) -> None: ...
