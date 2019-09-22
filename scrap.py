from argparse import Namespace
from src.scrapper.scrapper import SimpleScrapper as Scrapper
from src.cli import get_args
from src.dependency_builder.builder import Builder

args: Namespace = get_args()

dependency: dict = Builder.build(args)

Scrapper(**dependency).process(urls=args.urls)
