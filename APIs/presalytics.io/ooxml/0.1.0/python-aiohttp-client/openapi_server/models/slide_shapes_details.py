# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.shared_effects_details import SharedEffectsDetails
from openapi_server.models.shared_fill_map_details import SharedFillMapDetails
from openapi_server.models.shared_lines_details import SharedLinesDetails
from openapi_server.models.shared_text_container_details import SharedTextContainerDetails
from openapi_server.models.slide_group_elements_details import SlideGroupElementsDetails
from openapi_server import util


class SlideShapesDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_element_blob_url: str=None, changed_base_element_blob_url: str=None, date_created: datetime=None, date_modified: datetime=None, effect: SharedEffectsDetails=None, fill_map: SharedFillMapDetails=None, flip_horizontal: bool=None, flip_vertical: bool=None, free_form_path_xml: str=None, group_element: SlideGroupElementsDetails=None, group_elements_id: str=None, height: int=None, hidden: bool=None, id: str=None, is_theme_effect: bool=None, is_theme_fill: bool=None, is_theme_line: bool=None, line: SharedLinesDetails=None, name: str=None, ooxml_id: int=None, package_uri: str=None, preset_type_id: str=None, rotation: int=None, svg_blob_url: str=None, text_container: SharedTextContainerDetails=None, user_created: str=None, user_modified: str=None, width: int=None, x_offset: int=None, y_offset: int=None):
        """SlideShapesDetails - a model defined in OpenAPI

        :param base_element_blob_url: The base_element_blob_url of this SlideShapesDetails.
        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideShapesDetails.
        :param date_created: The date_created of this SlideShapesDetails.
        :param date_modified: The date_modified of this SlideShapesDetails.
        :param effect: The effect of this SlideShapesDetails.
        :param fill_map: The fill_map of this SlideShapesDetails.
        :param flip_horizontal: The flip_horizontal of this SlideShapesDetails.
        :param flip_vertical: The flip_vertical of this SlideShapesDetails.
        :param free_form_path_xml: The free_form_path_xml of this SlideShapesDetails.
        :param group_element: The group_element of this SlideShapesDetails.
        :param group_elements_id: The group_elements_id of this SlideShapesDetails.
        :param height: The height of this SlideShapesDetails.
        :param hidden: The hidden of this SlideShapesDetails.
        :param id: The id of this SlideShapesDetails.
        :param is_theme_effect: The is_theme_effect of this SlideShapesDetails.
        :param is_theme_fill: The is_theme_fill of this SlideShapesDetails.
        :param is_theme_line: The is_theme_line of this SlideShapesDetails.
        :param line: The line of this SlideShapesDetails.
        :param name: The name of this SlideShapesDetails.
        :param ooxml_id: The ooxml_id of this SlideShapesDetails.
        :param package_uri: The package_uri of this SlideShapesDetails.
        :param preset_type_id: The preset_type_id of this SlideShapesDetails.
        :param rotation: The rotation of this SlideShapesDetails.
        :param svg_blob_url: The svg_blob_url of this SlideShapesDetails.
        :param text_container: The text_container of this SlideShapesDetails.
        :param user_created: The user_created of this SlideShapesDetails.
        :param user_modified: The user_modified of this SlideShapesDetails.
        :param width: The width of this SlideShapesDetails.
        :param x_offset: The x_offset of this SlideShapesDetails.
        :param y_offset: The y_offset of this SlideShapesDetails.
        """
        self.openapi_types = {
            'base_element_blob_url': str,
            'changed_base_element_blob_url': str,
            'date_created': datetime,
            'date_modified': datetime,
            'effect': SharedEffectsDetails,
            'fill_map': SharedFillMapDetails,
            'flip_horizontal': bool,
            'flip_vertical': bool,
            'free_form_path_xml': str,
            'group_element': SlideGroupElementsDetails,
            'group_elements_id': str,
            'height': int,
            'hidden': bool,
            'id': str,
            'is_theme_effect': bool,
            'is_theme_fill': bool,
            'is_theme_line': bool,
            'line': SharedLinesDetails,
            'name': str,
            'ooxml_id': int,
            'package_uri': str,
            'preset_type_id': str,
            'rotation': int,
            'svg_blob_url': str,
            'text_container': SharedTextContainerDetails,
            'user_created': str,
            'user_modified': str,
            'width': int,
            'x_offset': int,
            'y_offset': int
        }

        self.attribute_map = {
            'base_element_blob_url': 'baseElementBlobUrl',
            'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'effect': 'effect',
            'fill_map': 'fillMap',
            'flip_horizontal': 'flipHorizontal',
            'flip_vertical': 'flipVertical',
            'free_form_path_xml': 'freeFormPathXml',
            'group_element': 'groupElement',
            'group_elements_id': 'groupElementsId',
            'height': 'height',
            'hidden': 'hidden',
            'id': 'id',
            'is_theme_effect': 'isThemeEffect',
            'is_theme_fill': 'isThemeFill',
            'is_theme_line': 'isThemeLine',
            'line': 'line',
            'name': 'name',
            'ooxml_id': 'ooxmlId',
            'package_uri': 'packageUri',
            'preset_type_id': 'presetTypeId',
            'rotation': 'rotation',
            'svg_blob_url': 'svgBlobUrl',
            'text_container': 'textContainer',
            'user_created': 'userCreated',
            'user_modified': 'userModified',
            'width': 'width',
            'x_offset': 'xOffset',
            'y_offset': 'yOffset'
        }

        self._base_element_blob_url = base_element_blob_url
        self._changed_base_element_blob_url = changed_base_element_blob_url
        self._date_created = date_created
        self._date_modified = date_modified
        self._effect = effect
        self._fill_map = fill_map
        self._flip_horizontal = flip_horizontal
        self._flip_vertical = flip_vertical
        self._free_form_path_xml = free_form_path_xml
        self._group_element = group_element
        self._group_elements_id = group_elements_id
        self._height = height
        self._hidden = hidden
        self._id = id
        self._is_theme_effect = is_theme_effect
        self._is_theme_fill = is_theme_fill
        self._is_theme_line = is_theme_line
        self._line = line
        self._name = name
        self._ooxml_id = ooxml_id
        self._package_uri = package_uri
        self._preset_type_id = preset_type_id
        self._rotation = rotation
        self._svg_blob_url = svg_blob_url
        self._text_container = text_container
        self._user_created = user_created
        self._user_modified = user_modified
        self._width = width
        self._x_offset = x_offset
        self._y_offset = y_offset

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SlideShapesDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Slide.Shapes.Details of this SlideShapesDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this SlideShapesDetails.


        :return: The base_element_blob_url of this SlideShapesDetails.
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this SlideShapesDetails.


        :param base_element_blob_url: The base_element_blob_url of this SlideShapesDetails.
        :type base_element_blob_url: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this SlideShapesDetails.


        :return: The changed_base_element_blob_url of this SlideShapesDetails.
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this SlideShapesDetails.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideShapesDetails.
        :type changed_base_element_blob_url: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def date_created(self):
        """Gets the date_created of this SlideShapesDetails.


        :return: The date_created of this SlideShapesDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideShapesDetails.


        :param date_created: The date_created of this SlideShapesDetails.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideShapesDetails.


        :return: The date_modified of this SlideShapesDetails.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideShapesDetails.


        :param date_modified: The date_modified of this SlideShapesDetails.
        :type date_modified: datetime
        """

        self._date_modified = date_modified

    @property
    def effect(self):
        """Gets the effect of this SlideShapesDetails.


        :return: The effect of this SlideShapesDetails.
        :rtype: SharedEffectsDetails
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this SlideShapesDetails.


        :param effect: The effect of this SlideShapesDetails.
        :type effect: SharedEffectsDetails
        """

        self._effect = effect

    @property
    def fill_map(self):
        """Gets the fill_map of this SlideShapesDetails.


        :return: The fill_map of this SlideShapesDetails.
        :rtype: SharedFillMapDetails
        """
        return self._fill_map

    @fill_map.setter
    def fill_map(self, fill_map):
        """Sets the fill_map of this SlideShapesDetails.


        :param fill_map: The fill_map of this SlideShapesDetails.
        :type fill_map: SharedFillMapDetails
        """

        self._fill_map = fill_map

    @property
    def flip_horizontal(self):
        """Gets the flip_horizontal of this SlideShapesDetails.


        :return: The flip_horizontal of this SlideShapesDetails.
        :rtype: bool
        """
        return self._flip_horizontal

    @flip_horizontal.setter
    def flip_horizontal(self, flip_horizontal):
        """Sets the flip_horizontal of this SlideShapesDetails.


        :param flip_horizontal: The flip_horizontal of this SlideShapesDetails.
        :type flip_horizontal: bool
        """

        self._flip_horizontal = flip_horizontal

    @property
    def flip_vertical(self):
        """Gets the flip_vertical of this SlideShapesDetails.


        :return: The flip_vertical of this SlideShapesDetails.
        :rtype: bool
        """
        return self._flip_vertical

    @flip_vertical.setter
    def flip_vertical(self, flip_vertical):
        """Sets the flip_vertical of this SlideShapesDetails.


        :param flip_vertical: The flip_vertical of this SlideShapesDetails.
        :type flip_vertical: bool
        """

        self._flip_vertical = flip_vertical

    @property
    def free_form_path_xml(self):
        """Gets the free_form_path_xml of this SlideShapesDetails.


        :return: The free_form_path_xml of this SlideShapesDetails.
        :rtype: str
        """
        return self._free_form_path_xml

    @free_form_path_xml.setter
    def free_form_path_xml(self, free_form_path_xml):
        """Sets the free_form_path_xml of this SlideShapesDetails.


        :param free_form_path_xml: The free_form_path_xml of this SlideShapesDetails.
        :type free_form_path_xml: str
        """

        self._free_form_path_xml = free_form_path_xml

    @property
    def group_element(self):
        """Gets the group_element of this SlideShapesDetails.


        :return: The group_element of this SlideShapesDetails.
        :rtype: SlideGroupElementsDetails
        """
        return self._group_element

    @group_element.setter
    def group_element(self, group_element):
        """Sets the group_element of this SlideShapesDetails.


        :param group_element: The group_element of this SlideShapesDetails.
        :type group_element: SlideGroupElementsDetails
        """

        self._group_element = group_element

    @property
    def group_elements_id(self):
        """Gets the group_elements_id of this SlideShapesDetails.


        :return: The group_elements_id of this SlideShapesDetails.
        :rtype: str
        """
        return self._group_elements_id

    @group_elements_id.setter
    def group_elements_id(self, group_elements_id):
        """Sets the group_elements_id of this SlideShapesDetails.


        :param group_elements_id: The group_elements_id of this SlideShapesDetails.
        :type group_elements_id: str
        """

        self._group_elements_id = group_elements_id

    @property
    def height(self):
        """Gets the height of this SlideShapesDetails.


        :return: The height of this SlideShapesDetails.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SlideShapesDetails.


        :param height: The height of this SlideShapesDetails.
        :type height: int
        """

        self._height = height

    @property
    def hidden(self):
        """Gets the hidden of this SlideShapesDetails.


        :return: The hidden of this SlideShapesDetails.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this SlideShapesDetails.


        :param hidden: The hidden of this SlideShapesDetails.
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this SlideShapesDetails.


        :return: The id of this SlideShapesDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideShapesDetails.


        :param id: The id of this SlideShapesDetails.
        :type id: str
        """

        self._id = id

    @property
    def is_theme_effect(self):
        """Gets the is_theme_effect of this SlideShapesDetails.


        :return: The is_theme_effect of this SlideShapesDetails.
        :rtype: bool
        """
        return self._is_theme_effect

    @is_theme_effect.setter
    def is_theme_effect(self, is_theme_effect):
        """Sets the is_theme_effect of this SlideShapesDetails.


        :param is_theme_effect: The is_theme_effect of this SlideShapesDetails.
        :type is_theme_effect: bool
        """

        self._is_theme_effect = is_theme_effect

    @property
    def is_theme_fill(self):
        """Gets the is_theme_fill of this SlideShapesDetails.


        :return: The is_theme_fill of this SlideShapesDetails.
        :rtype: bool
        """
        return self._is_theme_fill

    @is_theme_fill.setter
    def is_theme_fill(self, is_theme_fill):
        """Sets the is_theme_fill of this SlideShapesDetails.


        :param is_theme_fill: The is_theme_fill of this SlideShapesDetails.
        :type is_theme_fill: bool
        """

        self._is_theme_fill = is_theme_fill

    @property
    def is_theme_line(self):
        """Gets the is_theme_line of this SlideShapesDetails.


        :return: The is_theme_line of this SlideShapesDetails.
        :rtype: bool
        """
        return self._is_theme_line

    @is_theme_line.setter
    def is_theme_line(self, is_theme_line):
        """Sets the is_theme_line of this SlideShapesDetails.


        :param is_theme_line: The is_theme_line of this SlideShapesDetails.
        :type is_theme_line: bool
        """

        self._is_theme_line = is_theme_line

    @property
    def line(self):
        """Gets the line of this SlideShapesDetails.


        :return: The line of this SlideShapesDetails.
        :rtype: SharedLinesDetails
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this SlideShapesDetails.


        :param line: The line of this SlideShapesDetails.
        :type line: SharedLinesDetails
        """

        self._line = line

    @property
    def name(self):
        """Gets the name of this SlideShapesDetails.


        :return: The name of this SlideShapesDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlideShapesDetails.


        :param name: The name of this SlideShapesDetails.
        :type name: str
        """

        self._name = name

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideShapesDetails.


        :return: The ooxml_id of this SlideShapesDetails.
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideShapesDetails.


        :param ooxml_id: The ooxml_id of this SlideShapesDetails.
        :type ooxml_id: int
        """

        self._ooxml_id = ooxml_id

    @property
    def package_uri(self):
        """Gets the package_uri of this SlideShapesDetails.


        :return: The package_uri of this SlideShapesDetails.
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this SlideShapesDetails.


        :param package_uri: The package_uri of this SlideShapesDetails.
        :type package_uri: str
        """

        self._package_uri = package_uri

    @property
    def preset_type_id(self):
        """Gets the preset_type_id of this SlideShapesDetails.


        :return: The preset_type_id of this SlideShapesDetails.
        :rtype: str
        """
        return self._preset_type_id

    @preset_type_id.setter
    def preset_type_id(self, preset_type_id):
        """Sets the preset_type_id of this SlideShapesDetails.


        :param preset_type_id: The preset_type_id of this SlideShapesDetails.
        :type preset_type_id: str
        """

        self._preset_type_id = preset_type_id

    @property
    def rotation(self):
        """Gets the rotation of this SlideShapesDetails.


        :return: The rotation of this SlideShapesDetails.
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this SlideShapesDetails.


        :param rotation: The rotation of this SlideShapesDetails.
        :type rotation: int
        """

        self._rotation = rotation

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideShapesDetails.


        :return: The svg_blob_url of this SlideShapesDetails.
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideShapesDetails.


        :param svg_blob_url: The svg_blob_url of this SlideShapesDetails.
        :type svg_blob_url: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def text_container(self):
        """Gets the text_container of this SlideShapesDetails.


        :return: The text_container of this SlideShapesDetails.
        :rtype: SharedTextContainerDetails
        """
        return self._text_container

    @text_container.setter
    def text_container(self, text_container):
        """Sets the text_container of this SlideShapesDetails.


        :param text_container: The text_container of this SlideShapesDetails.
        :type text_container: SharedTextContainerDetails
        """

        self._text_container = text_container

    @property
    def user_created(self):
        """Gets the user_created of this SlideShapesDetails.


        :return: The user_created of this SlideShapesDetails.
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideShapesDetails.


        :param user_created: The user_created of this SlideShapesDetails.
        :type user_created: str
        """

        self._user_created = user_created

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideShapesDetails.


        :return: The user_modified of this SlideShapesDetails.
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideShapesDetails.


        :param user_modified: The user_modified of this SlideShapesDetails.
        :type user_modified: str
        """

        self._user_modified = user_modified

    @property
    def width(self):
        """Gets the width of this SlideShapesDetails.


        :return: The width of this SlideShapesDetails.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SlideShapesDetails.


        :param width: The width of this SlideShapesDetails.
        :type width: int
        """

        self._width = width

    @property
    def x_offset(self):
        """Gets the x_offset of this SlideShapesDetails.


        :return: The x_offset of this SlideShapesDetails.
        :rtype: int
        """
        return self._x_offset

    @x_offset.setter
    def x_offset(self, x_offset):
        """Sets the x_offset of this SlideShapesDetails.


        :param x_offset: The x_offset of this SlideShapesDetails.
        :type x_offset: int
        """

        self._x_offset = x_offset

    @property
    def y_offset(self):
        """Gets the y_offset of this SlideShapesDetails.


        :return: The y_offset of this SlideShapesDetails.
        :rtype: int
        """
        return self._y_offset

    @y_offset.setter
    def y_offset(self, y_offset):
        """Sets the y_offset of this SlideShapesDetails.


        :param y_offset: The y_offset of this SlideShapesDetails.
        :type y_offset: int
        """

        self._y_offset = y_offset
