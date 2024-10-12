# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SlideShapes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_element_blob_url: str=None, changed_base_element_blob_url: str=None, flip_horizontal: bool=None, flip_vertical: bool=None, free_form_path_xml: str=None, group_elements_id: str=None, height: int=None, hidden: bool=None, id: str=None, is_theme_effect: bool=None, is_theme_fill: bool=None, is_theme_line: bool=None, name: str=None, ooxml_id: int=None, package_uri: str=None, preset_type_id: str=None, rotation: int=None, svg_blob_url: str=None, width: int=None, x_offset: int=None, y_offset: int=None):
        """SlideShapes - a model defined in OpenAPI

        :param base_element_blob_url: The base_element_blob_url of this SlideShapes.
        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideShapes.
        :param flip_horizontal: The flip_horizontal of this SlideShapes.
        :param flip_vertical: The flip_vertical of this SlideShapes.
        :param free_form_path_xml: The free_form_path_xml of this SlideShapes.
        :param group_elements_id: The group_elements_id of this SlideShapes.
        :param height: The height of this SlideShapes.
        :param hidden: The hidden of this SlideShapes.
        :param id: The id of this SlideShapes.
        :param is_theme_effect: The is_theme_effect of this SlideShapes.
        :param is_theme_fill: The is_theme_fill of this SlideShapes.
        :param is_theme_line: The is_theme_line of this SlideShapes.
        :param name: The name of this SlideShapes.
        :param ooxml_id: The ooxml_id of this SlideShapes.
        :param package_uri: The package_uri of this SlideShapes.
        :param preset_type_id: The preset_type_id of this SlideShapes.
        :param rotation: The rotation of this SlideShapes.
        :param svg_blob_url: The svg_blob_url of this SlideShapes.
        :param width: The width of this SlideShapes.
        :param x_offset: The x_offset of this SlideShapes.
        :param y_offset: The y_offset of this SlideShapes.
        """
        self.openapi_types = {
            'base_element_blob_url': str,
            'changed_base_element_blob_url': str,
            'flip_horizontal': bool,
            'flip_vertical': bool,
            'free_form_path_xml': str,
            'group_elements_id': str,
            'height': int,
            'hidden': bool,
            'id': str,
            'is_theme_effect': bool,
            'is_theme_fill': bool,
            'is_theme_line': bool,
            'name': str,
            'ooxml_id': int,
            'package_uri': str,
            'preset_type_id': str,
            'rotation': int,
            'svg_blob_url': str,
            'width': int,
            'x_offset': int,
            'y_offset': int
        }

        self.attribute_map = {
            'base_element_blob_url': 'baseElementBlobUrl',
            'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
            'flip_horizontal': 'flipHorizontal',
            'flip_vertical': 'flipVertical',
            'free_form_path_xml': 'freeFormPathXml',
            'group_elements_id': 'groupElementsId',
            'height': 'height',
            'hidden': 'hidden',
            'id': 'id',
            'is_theme_effect': 'isThemeEffect',
            'is_theme_fill': 'isThemeFill',
            'is_theme_line': 'isThemeLine',
            'name': 'name',
            'ooxml_id': 'ooxmlId',
            'package_uri': 'packageUri',
            'preset_type_id': 'presetTypeId',
            'rotation': 'rotation',
            'svg_blob_url': 'svgBlobUrl',
            'width': 'width',
            'x_offset': 'xOffset',
            'y_offset': 'yOffset'
        }

        self._base_element_blob_url = base_element_blob_url
        self._changed_base_element_blob_url = changed_base_element_blob_url
        self._flip_horizontal = flip_horizontal
        self._flip_vertical = flip_vertical
        self._free_form_path_xml = free_form_path_xml
        self._group_elements_id = group_elements_id
        self._height = height
        self._hidden = hidden
        self._id = id
        self._is_theme_effect = is_theme_effect
        self._is_theme_fill = is_theme_fill
        self._is_theme_line = is_theme_line
        self._name = name
        self._ooxml_id = ooxml_id
        self._package_uri = package_uri
        self._preset_type_id = preset_type_id
        self._rotation = rotation
        self._svg_blob_url = svg_blob_url
        self._width = width
        self._x_offset = x_offset
        self._y_offset = y_offset

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SlideShapes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Slide.Shapes of this SlideShapes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this SlideShapes.


        :return: The base_element_blob_url of this SlideShapes.
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this SlideShapes.


        :param base_element_blob_url: The base_element_blob_url of this SlideShapes.
        :type base_element_blob_url: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this SlideShapes.


        :return: The changed_base_element_blob_url of this SlideShapes.
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this SlideShapes.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideShapes.
        :type changed_base_element_blob_url: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def flip_horizontal(self):
        """Gets the flip_horizontal of this SlideShapes.


        :return: The flip_horizontal of this SlideShapes.
        :rtype: bool
        """
        return self._flip_horizontal

    @flip_horizontal.setter
    def flip_horizontal(self, flip_horizontal):
        """Sets the flip_horizontal of this SlideShapes.


        :param flip_horizontal: The flip_horizontal of this SlideShapes.
        :type flip_horizontal: bool
        """

        self._flip_horizontal = flip_horizontal

    @property
    def flip_vertical(self):
        """Gets the flip_vertical of this SlideShapes.


        :return: The flip_vertical of this SlideShapes.
        :rtype: bool
        """
        return self._flip_vertical

    @flip_vertical.setter
    def flip_vertical(self, flip_vertical):
        """Sets the flip_vertical of this SlideShapes.


        :param flip_vertical: The flip_vertical of this SlideShapes.
        :type flip_vertical: bool
        """

        self._flip_vertical = flip_vertical

    @property
    def free_form_path_xml(self):
        """Gets the free_form_path_xml of this SlideShapes.


        :return: The free_form_path_xml of this SlideShapes.
        :rtype: str
        """
        return self._free_form_path_xml

    @free_form_path_xml.setter
    def free_form_path_xml(self, free_form_path_xml):
        """Sets the free_form_path_xml of this SlideShapes.


        :param free_form_path_xml: The free_form_path_xml of this SlideShapes.
        :type free_form_path_xml: str
        """

        self._free_form_path_xml = free_form_path_xml

    @property
    def group_elements_id(self):
        """Gets the group_elements_id of this SlideShapes.


        :return: The group_elements_id of this SlideShapes.
        :rtype: str
        """
        return self._group_elements_id

    @group_elements_id.setter
    def group_elements_id(self, group_elements_id):
        """Sets the group_elements_id of this SlideShapes.


        :param group_elements_id: The group_elements_id of this SlideShapes.
        :type group_elements_id: str
        """

        self._group_elements_id = group_elements_id

    @property
    def height(self):
        """Gets the height of this SlideShapes.


        :return: The height of this SlideShapes.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SlideShapes.


        :param height: The height of this SlideShapes.
        :type height: int
        """

        self._height = height

    @property
    def hidden(self):
        """Gets the hidden of this SlideShapes.


        :return: The hidden of this SlideShapes.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this SlideShapes.


        :param hidden: The hidden of this SlideShapes.
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this SlideShapes.


        :return: The id of this SlideShapes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideShapes.


        :param id: The id of this SlideShapes.
        :type id: str
        """

        self._id = id

    @property
    def is_theme_effect(self):
        """Gets the is_theme_effect of this SlideShapes.


        :return: The is_theme_effect of this SlideShapes.
        :rtype: bool
        """
        return self._is_theme_effect

    @is_theme_effect.setter
    def is_theme_effect(self, is_theme_effect):
        """Sets the is_theme_effect of this SlideShapes.


        :param is_theme_effect: The is_theme_effect of this SlideShapes.
        :type is_theme_effect: bool
        """

        self._is_theme_effect = is_theme_effect

    @property
    def is_theme_fill(self):
        """Gets the is_theme_fill of this SlideShapes.


        :return: The is_theme_fill of this SlideShapes.
        :rtype: bool
        """
        return self._is_theme_fill

    @is_theme_fill.setter
    def is_theme_fill(self, is_theme_fill):
        """Sets the is_theme_fill of this SlideShapes.


        :param is_theme_fill: The is_theme_fill of this SlideShapes.
        :type is_theme_fill: bool
        """

        self._is_theme_fill = is_theme_fill

    @property
    def is_theme_line(self):
        """Gets the is_theme_line of this SlideShapes.


        :return: The is_theme_line of this SlideShapes.
        :rtype: bool
        """
        return self._is_theme_line

    @is_theme_line.setter
    def is_theme_line(self, is_theme_line):
        """Sets the is_theme_line of this SlideShapes.


        :param is_theme_line: The is_theme_line of this SlideShapes.
        :type is_theme_line: bool
        """

        self._is_theme_line = is_theme_line

    @property
    def name(self):
        """Gets the name of this SlideShapes.


        :return: The name of this SlideShapes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlideShapes.


        :param name: The name of this SlideShapes.
        :type name: str
        """

        self._name = name

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideShapes.


        :return: The ooxml_id of this SlideShapes.
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideShapes.


        :param ooxml_id: The ooxml_id of this SlideShapes.
        :type ooxml_id: int
        """

        self._ooxml_id = ooxml_id

    @property
    def package_uri(self):
        """Gets the package_uri of this SlideShapes.


        :return: The package_uri of this SlideShapes.
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this SlideShapes.


        :param package_uri: The package_uri of this SlideShapes.
        :type package_uri: str
        """

        self._package_uri = package_uri

    @property
    def preset_type_id(self):
        """Gets the preset_type_id of this SlideShapes.


        :return: The preset_type_id of this SlideShapes.
        :rtype: str
        """
        return self._preset_type_id

    @preset_type_id.setter
    def preset_type_id(self, preset_type_id):
        """Sets the preset_type_id of this SlideShapes.


        :param preset_type_id: The preset_type_id of this SlideShapes.
        :type preset_type_id: str
        """

        self._preset_type_id = preset_type_id

    @property
    def rotation(self):
        """Gets the rotation of this SlideShapes.


        :return: The rotation of this SlideShapes.
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this SlideShapes.


        :param rotation: The rotation of this SlideShapes.
        :type rotation: int
        """

        self._rotation = rotation

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideShapes.


        :return: The svg_blob_url of this SlideShapes.
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideShapes.


        :param svg_blob_url: The svg_blob_url of this SlideShapes.
        :type svg_blob_url: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def width(self):
        """Gets the width of this SlideShapes.


        :return: The width of this SlideShapes.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SlideShapes.


        :param width: The width of this SlideShapes.
        :type width: int
        """

        self._width = width

    @property
    def x_offset(self):
        """Gets the x_offset of this SlideShapes.


        :return: The x_offset of this SlideShapes.
        :rtype: int
        """
        return self._x_offset

    @x_offset.setter
    def x_offset(self, x_offset):
        """Sets the x_offset of this SlideShapes.


        :param x_offset: The x_offset of this SlideShapes.
        :type x_offset: int
        """

        self._x_offset = x_offset

    @property
    def y_offset(self):
        """Gets the y_offset of this SlideShapes.


        :return: The y_offset of this SlideShapes.
        :rtype: int
        """
        return self._y_offset

    @y_offset.setter
    def y_offset(self, y_offset):
        """Sets the y_offset of this SlideShapes.


        :param y_offset: The y_offset of this SlideShapes.
        :type y_offset: int
        """

        self._y_offset = y_offset
