# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SharedText(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, color_solid_fills_id: str=None, font: str=None, font_size: int=None, id: str=None, is_bold: bool=None, is_italic: bool=None, is_theme_font: bool=None, is_underline: bool=None, paragraph_id: str=None, raw_text: str=None, sequence: int=None):
        """SharedText - a model defined in OpenAPI

        :param color_solid_fills_id: The color_solid_fills_id of this SharedText.
        :param font: The font of this SharedText.
        :param font_size: The font_size of this SharedText.
        :param id: The id of this SharedText.
        :param is_bold: The is_bold of this SharedText.
        :param is_italic: The is_italic of this SharedText.
        :param is_theme_font: The is_theme_font of this SharedText.
        :param is_underline: The is_underline of this SharedText.
        :param paragraph_id: The paragraph_id of this SharedText.
        :param raw_text: The raw_text of this SharedText.
        :param sequence: The sequence of this SharedText.
        """
        self.openapi_types = {
            'color_solid_fills_id': str,
            'font': str,
            'font_size': int,
            'id': str,
            'is_bold': bool,
            'is_italic': bool,
            'is_theme_font': bool,
            'is_underline': bool,
            'paragraph_id': str,
            'raw_text': str,
            'sequence': int
        }

        self.attribute_map = {
            'color_solid_fills_id': 'colorSolidFillsId',
            'font': 'font',
            'font_size': 'fontSize',
            'id': 'id',
            'is_bold': 'isBold',
            'is_italic': 'isItalic',
            'is_theme_font': 'isThemeFont',
            'is_underline': 'isUnderline',
            'paragraph_id': 'paragraphId',
            'raw_text': 'rawText',
            'sequence': 'sequence'
        }

        self._color_solid_fills_id = color_solid_fills_id
        self._font = font
        self._font_size = font_size
        self._id = id
        self._is_bold = is_bold
        self._is_italic = is_italic
        self._is_theme_font = is_theme_font
        self._is_underline = is_underline
        self._paragraph_id = paragraph_id
        self._raw_text = raw_text
        self._sequence = sequence

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SharedText':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Shared.Text of this SharedText.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def color_solid_fills_id(self):
        """Gets the color_solid_fills_id of this SharedText.


        :return: The color_solid_fills_id of this SharedText.
        :rtype: str
        """
        return self._color_solid_fills_id

    @color_solid_fills_id.setter
    def color_solid_fills_id(self, color_solid_fills_id):
        """Sets the color_solid_fills_id of this SharedText.


        :param color_solid_fills_id: The color_solid_fills_id of this SharedText.
        :type color_solid_fills_id: str
        """

        self._color_solid_fills_id = color_solid_fills_id

    @property
    def font(self):
        """Gets the font of this SharedText.


        :return: The font of this SharedText.
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this SharedText.


        :param font: The font of this SharedText.
        :type font: str
        """

        self._font = font

    @property
    def font_size(self):
        """Gets the font_size of this SharedText.


        :return: The font_size of this SharedText.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this SharedText.


        :param font_size: The font_size of this SharedText.
        :type font_size: int
        """

        self._font_size = font_size

    @property
    def id(self):
        """Gets the id of this SharedText.


        :return: The id of this SharedText.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedText.


        :param id: The id of this SharedText.
        :type id: str
        """

        self._id = id

    @property
    def is_bold(self):
        """Gets the is_bold of this SharedText.


        :return: The is_bold of this SharedText.
        :rtype: bool
        """
        return self._is_bold

    @is_bold.setter
    def is_bold(self, is_bold):
        """Sets the is_bold of this SharedText.


        :param is_bold: The is_bold of this SharedText.
        :type is_bold: bool
        """

        self._is_bold = is_bold

    @property
    def is_italic(self):
        """Gets the is_italic of this SharedText.


        :return: The is_italic of this SharedText.
        :rtype: bool
        """
        return self._is_italic

    @is_italic.setter
    def is_italic(self, is_italic):
        """Sets the is_italic of this SharedText.


        :param is_italic: The is_italic of this SharedText.
        :type is_italic: bool
        """

        self._is_italic = is_italic

    @property
    def is_theme_font(self):
        """Gets the is_theme_font of this SharedText.


        :return: The is_theme_font of this SharedText.
        :rtype: bool
        """
        return self._is_theme_font

    @is_theme_font.setter
    def is_theme_font(self, is_theme_font):
        """Sets the is_theme_font of this SharedText.


        :param is_theme_font: The is_theme_font of this SharedText.
        :type is_theme_font: bool
        """

        self._is_theme_font = is_theme_font

    @property
    def is_underline(self):
        """Gets the is_underline of this SharedText.


        :return: The is_underline of this SharedText.
        :rtype: bool
        """
        return self._is_underline

    @is_underline.setter
    def is_underline(self, is_underline):
        """Sets the is_underline of this SharedText.


        :param is_underline: The is_underline of this SharedText.
        :type is_underline: bool
        """

        self._is_underline = is_underline

    @property
    def paragraph_id(self):
        """Gets the paragraph_id of this SharedText.


        :return: The paragraph_id of this SharedText.
        :rtype: str
        """
        return self._paragraph_id

    @paragraph_id.setter
    def paragraph_id(self, paragraph_id):
        """Sets the paragraph_id of this SharedText.


        :param paragraph_id: The paragraph_id of this SharedText.
        :type paragraph_id: str
        """

        self._paragraph_id = paragraph_id

    @property
    def raw_text(self):
        """Gets the raw_text of this SharedText.


        :return: The raw_text of this SharedText.
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this SharedText.


        :param raw_text: The raw_text of this SharedText.
        :type raw_text: str
        """

        self._raw_text = raw_text

    @property
    def sequence(self):
        """Gets the sequence of this SharedText.


        :return: The sequence of this SharedText.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this SharedText.


        :param sequence: The sequence of this SharedText.
        :type sequence: int
        """

        self._sequence = sequence
