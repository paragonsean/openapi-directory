# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.slide_slides_details import SlideSlidesDetails
from openapi_server.models.theme_background_fills_details import ThemeBackgroundFillsDetails
from openapi_server.models.theme_colors_details import ThemeColorsDetails
from openapi_server.models.theme_custom_colors_details import ThemeCustomColorsDetails
from openapi_server.models.theme_effect_map_details import ThemeEffectMapDetails
from openapi_server.models.theme_fills_details import ThemeFillsDetails
from openapi_server.models.theme_fonts_details import ThemeFontsDetails
from openapi_server.models.theme_line_map_details import ThemeLineMapDetails
from openapi_server import util


class ThemeThemesDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, background_fills: List[ThemeBackgroundFillsDetails]=None, base_element_blob_url: str=None, changed_base_element_blob_url: str=None, colors: ThemeColorsDetails=None, custom_colors: List[ThemeCustomColorsDetails]=None, date_created: datetime=None, date_modified: datetime=None, effect_maps: List[ThemeEffectMapDetails]=None, fills: List[ThemeFillsDetails]=None, fonts: ThemeFontsDetails=None, id: str=None, line_maps: List[ThemeLineMapDetails]=None, name: str=None, package_uri: str=None, slide: SlideSlidesDetails=None, slide_id: str=None, user_created: str=None, user_modified: str=None):
        """ThemeThemesDetails - a model defined in OpenAPI

        :param background_fills: The background_fills of this ThemeThemesDetails.
        :param base_element_blob_url: The base_element_blob_url of this ThemeThemesDetails.
        :param changed_base_element_blob_url: The changed_base_element_blob_url of this ThemeThemesDetails.
        :param colors: The colors of this ThemeThemesDetails.
        :param custom_colors: The custom_colors of this ThemeThemesDetails.
        :param date_created: The date_created of this ThemeThemesDetails.
        :param date_modified: The date_modified of this ThemeThemesDetails.
        :param effect_maps: The effect_maps of this ThemeThemesDetails.
        :param fills: The fills of this ThemeThemesDetails.
        :param fonts: The fonts of this ThemeThemesDetails.
        :param id: The id of this ThemeThemesDetails.
        :param line_maps: The line_maps of this ThemeThemesDetails.
        :param name: The name of this ThemeThemesDetails.
        :param package_uri: The package_uri of this ThemeThemesDetails.
        :param slide: The slide of this ThemeThemesDetails.
        :param slide_id: The slide_id of this ThemeThemesDetails.
        :param user_created: The user_created of this ThemeThemesDetails.
        :param user_modified: The user_modified of this ThemeThemesDetails.
        """
        self.openapi_types = {
            'background_fills': List[ThemeBackgroundFillsDetails],
            'base_element_blob_url': str,
            'changed_base_element_blob_url': str,
            'colors': ThemeColorsDetails,
            'custom_colors': List[ThemeCustomColorsDetails],
            'date_created': datetime,
            'date_modified': datetime,
            'effect_maps': List[ThemeEffectMapDetails],
            'fills': List[ThemeFillsDetails],
            'fonts': ThemeFontsDetails,
            'id': str,
            'line_maps': List[ThemeLineMapDetails],
            'name': str,
            'package_uri': str,
            'slide': SlideSlidesDetails,
            'slide_id': str,
            'user_created': str,
            'user_modified': str
        }

        self.attribute_map = {
            'background_fills': 'backgroundFills',
            'base_element_blob_url': 'baseElementBlobUrl',
            'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
            'colors': 'colors',
            'custom_colors': 'customColors',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'effect_maps': 'effectMaps',
            'fills': 'fills',
            'fonts': 'fonts',
            'id': 'id',
            'line_maps': 'lineMaps',
            'name': 'name',
            'package_uri': 'packageUri',
            'slide': 'slide',
            'slide_id': 'slideId',
            'user_created': 'userCreated',
            'user_modified': 'userModified'
        }

        self._background_fills = background_fills
        self._base_element_blob_url = base_element_blob_url
        self._changed_base_element_blob_url = changed_base_element_blob_url
        self._colors = colors
        self._custom_colors = custom_colors
        self._date_created = date_created
        self._date_modified = date_modified
        self._effect_maps = effect_maps
        self._fills = fills
        self._fonts = fonts
        self._id = id
        self._line_maps = line_maps
        self._name = name
        self._package_uri = package_uri
        self._slide = slide
        self._slide_id = slide_id
        self._user_created = user_created
        self._user_modified = user_modified

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ThemeThemesDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Theme.Themes.Details of this ThemeThemesDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def background_fills(self):
        """Gets the background_fills of this ThemeThemesDetails.


        :return: The background_fills of this ThemeThemesDetails.
        :rtype: List[ThemeBackgroundFillsDetails]
        """
        return self._background_fills

    @background_fills.setter
    def background_fills(self, background_fills):
        """Sets the background_fills of this ThemeThemesDetails.


        :param background_fills: The background_fills of this ThemeThemesDetails.
        :type background_fills: List[ThemeBackgroundFillsDetails]
        """

        self._background_fills = background_fills

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this ThemeThemesDetails.


        :return: The base_element_blob_url of this ThemeThemesDetails.
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this ThemeThemesDetails.


        :param base_element_blob_url: The base_element_blob_url of this ThemeThemesDetails.
        :type base_element_blob_url: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this ThemeThemesDetails.


        :return: The changed_base_element_blob_url of this ThemeThemesDetails.
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this ThemeThemesDetails.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this ThemeThemesDetails.
        :type changed_base_element_blob_url: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def colors(self):
        """Gets the colors of this ThemeThemesDetails.


        :return: The colors of this ThemeThemesDetails.
        :rtype: ThemeColorsDetails
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this ThemeThemesDetails.


        :param colors: The colors of this ThemeThemesDetails.
        :type colors: ThemeColorsDetails
        """

        self._colors = colors

    @property
    def custom_colors(self):
        """Gets the custom_colors of this ThemeThemesDetails.


        :return: The custom_colors of this ThemeThemesDetails.
        :rtype: List[ThemeCustomColorsDetails]
        """
        return self._custom_colors

    @custom_colors.setter
    def custom_colors(self, custom_colors):
        """Sets the custom_colors of this ThemeThemesDetails.


        :param custom_colors: The custom_colors of this ThemeThemesDetails.
        :type custom_colors: List[ThemeCustomColorsDetails]
        """

        self._custom_colors = custom_colors

    @property
    def date_created(self):
        """Gets the date_created of this ThemeThemesDetails.


        :return: The date_created of this ThemeThemesDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ThemeThemesDetails.


        :param date_created: The date_created of this ThemeThemesDetails.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ThemeThemesDetails.


        :return: The date_modified of this ThemeThemesDetails.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ThemeThemesDetails.


        :param date_modified: The date_modified of this ThemeThemesDetails.
        :type date_modified: datetime
        """

        self._date_modified = date_modified

    @property
    def effect_maps(self):
        """Gets the effect_maps of this ThemeThemesDetails.


        :return: The effect_maps of this ThemeThemesDetails.
        :rtype: List[ThemeEffectMapDetails]
        """
        return self._effect_maps

    @effect_maps.setter
    def effect_maps(self, effect_maps):
        """Sets the effect_maps of this ThemeThemesDetails.


        :param effect_maps: The effect_maps of this ThemeThemesDetails.
        :type effect_maps: List[ThemeEffectMapDetails]
        """

        self._effect_maps = effect_maps

    @property
    def fills(self):
        """Gets the fills of this ThemeThemesDetails.


        :return: The fills of this ThemeThemesDetails.
        :rtype: List[ThemeFillsDetails]
        """
        return self._fills

    @fills.setter
    def fills(self, fills):
        """Sets the fills of this ThemeThemesDetails.


        :param fills: The fills of this ThemeThemesDetails.
        :type fills: List[ThemeFillsDetails]
        """

        self._fills = fills

    @property
    def fonts(self):
        """Gets the fonts of this ThemeThemesDetails.


        :return: The fonts of this ThemeThemesDetails.
        :rtype: ThemeFontsDetails
        """
        return self._fonts

    @fonts.setter
    def fonts(self, fonts):
        """Sets the fonts of this ThemeThemesDetails.


        :param fonts: The fonts of this ThemeThemesDetails.
        :type fonts: ThemeFontsDetails
        """

        self._fonts = fonts

    @property
    def id(self):
        """Gets the id of this ThemeThemesDetails.


        :return: The id of this ThemeThemesDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThemeThemesDetails.


        :param id: The id of this ThemeThemesDetails.
        :type id: str
        """

        self._id = id

    @property
    def line_maps(self):
        """Gets the line_maps of this ThemeThemesDetails.


        :return: The line_maps of this ThemeThemesDetails.
        :rtype: List[ThemeLineMapDetails]
        """
        return self._line_maps

    @line_maps.setter
    def line_maps(self, line_maps):
        """Sets the line_maps of this ThemeThemesDetails.


        :param line_maps: The line_maps of this ThemeThemesDetails.
        :type line_maps: List[ThemeLineMapDetails]
        """

        self._line_maps = line_maps

    @property
    def name(self):
        """Gets the name of this ThemeThemesDetails.


        :return: The name of this ThemeThemesDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThemeThemesDetails.


        :param name: The name of this ThemeThemesDetails.
        :type name: str
        """

        self._name = name

    @property
    def package_uri(self):
        """Gets the package_uri of this ThemeThemesDetails.


        :return: The package_uri of this ThemeThemesDetails.
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this ThemeThemesDetails.


        :param package_uri: The package_uri of this ThemeThemesDetails.
        :type package_uri: str
        """

        self._package_uri = package_uri

    @property
    def slide(self):
        """Gets the slide of this ThemeThemesDetails.


        :return: The slide of this ThemeThemesDetails.
        :rtype: SlideSlidesDetails
        """
        return self._slide

    @slide.setter
    def slide(self, slide):
        """Sets the slide of this ThemeThemesDetails.


        :param slide: The slide of this ThemeThemesDetails.
        :type slide: SlideSlidesDetails
        """

        self._slide = slide

    @property
    def slide_id(self):
        """Gets the slide_id of this ThemeThemesDetails.


        :return: The slide_id of this ThemeThemesDetails.
        :rtype: str
        """
        return self._slide_id

    @slide_id.setter
    def slide_id(self, slide_id):
        """Sets the slide_id of this ThemeThemesDetails.


        :param slide_id: The slide_id of this ThemeThemesDetails.
        :type slide_id: str
        """

        self._slide_id = slide_id

    @property
    def user_created(self):
        """Gets the user_created of this ThemeThemesDetails.


        :return: The user_created of this ThemeThemesDetails.
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ThemeThemesDetails.


        :param user_created: The user_created of this ThemeThemesDetails.
        :type user_created: str
        """

        self._user_created = user_created

    @property
    def user_modified(self):
        """Gets the user_modified of this ThemeThemesDetails.


        :return: The user_modified of this ThemeThemesDetails.
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ThemeThemesDetails.


        :param user_modified: The user_modified of this ThemeThemesDetails.
        :type user_modified: str
        """

        self._user_modified = user_modified
