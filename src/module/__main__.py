#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main module of the package module

Classes:
    DefaultConfig
    Files
    Main(dict, dict, str)
"""

from src.info import Info
from src.module.files.complementary_files import ComplementaryFilesCreation
from src.module.files.base import BaseFileCreation
from src.module.config.user import UserConfigHandler
from src.module.config.images import IconsFormatConfig
from src.module.files.images import ImageFilesCreation

from src.services.logs import Logs, SpecialMessages


class Config(IconsFormatConfig):
    """Have the default config classes"""
    pass


class Files(BaseFileCreation, ComplementaryFilesCreation, ImageFilesCreation):
    """Class used to handle the generation of files

    Methods:
        all_files -> dict
    """
    def all_files(self) -> dict:
        """Return a dict with the structure of all files"""
        return dict(self.full_index(), **self.full_complementary_files())


class Main(Config, Files, UserConfigHandler, Logs, SpecialMessages):
    """Main class

    The entire sub-modules serve this class

    Init:
        icons_config dict = {}: icons format settings
        user_config dict = {}: user settings
        output_path str = '': output folder
    """
    info = Info.get_info()

    def __init__(self, icons_config: dict = {}, user_config: dict = {},
                 main_path: str = ''):
        self.config = self.transform(user_config, main_path)
        self.icons_config = icons_config or self.default_icons_config()
