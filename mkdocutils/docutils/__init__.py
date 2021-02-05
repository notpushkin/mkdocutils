from types import MappingProxyType

from docutils.core import publish_parts
from docutils.parsers.rst import Parser as RSTParser
from docutils.writers.html5_polyglot import HTMLTranslator, Writer

from mkdocutils.docutils.myst_parser import MystDocutilsParser

PARSERS = MappingProxyType({
    ".markdown": MystDocutilsParser,
    ".md": MystDocutilsParser,
    ".myst": MystDocutilsParser,
    ".rst": RSTParser,
})


class MyWriter(Writer):
    def get_transforms(self) -> list:
        return super().get_transforms()  # + [AutoStructify]


def to_html(*, source: str, src_path: str, extension: str) -> str:
    """
    to_htmlvto_htmlto_htmlto_html

    Params:
        source: source file contents
        src_path: source file path
        extension: source file extension

    Returns:
        rendered HTML
    """
    html_writer = MyWriter()
    html_writer.translator_class = HTMLTranslator
    parts = publish_parts(
        source=source,
        source_path=src_path,
        parser=PARSERS[extension](),
        writer=html_writer,
        settings_overrides={
            "output_encoding": "unicode",
            "initial_header_level": 2,
            "stylesheet_path": [],
        },
    )
    return parts["body"]
