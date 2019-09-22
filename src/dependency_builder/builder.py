from argparse import Namespace

from adopted.terminalsize import get_terminal_size

from src.saver.console_saver import ConsoleSaver
from src.saver.filesystem_saver import FileSystemSaver
from src.loader.loaders import WebLoader
from src.extractor.extractor import Extractor
from src.extractor.graph_extractor import GraphExtractor
from src.formatter.simple_formatter import SimpleFormatter


class Builder:
    """Класс создания зависимостей для организации процесса извлечения данных"""

    @staticmethod
    def build(args: Namespace) -> dict:

        formatter = SimpleFormatter()
        if args.adaptive:
            w, h = get_terminal_size()
            formatter.width = w

        if args.here:
            saver = ConsoleSaver(args.ticker)
        else:
            saver = FileSystemSaver()
            saver.url_based_structure = args.urlstore
            if args.filename is not None:
                saver.file_name = args.filename

        return {
            'extractor_class': GraphExtractor,
            'loader': WebLoader(),
            'formatter': formatter,
            'saver': saver,
        }

