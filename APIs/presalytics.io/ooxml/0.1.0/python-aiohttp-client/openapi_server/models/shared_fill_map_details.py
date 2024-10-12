# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.shared_effect_attributes_details import SharedEffectAttributesDetails
from openapi_server.models.shared_gradient_fills_details import SharedGradientFillsDetails
from openapi_server.models.shared_image_fills_details import SharedImageFillsDetails
from openapi_server.models.shared_solid_fills_details import SharedSolidFillsDetails
from openapi_server.models.slide_connector_details import SlideConnectorDetails
from openapi_server.models.slide_shapes_details import SlideShapesDetails
from openapi_server.models.table_cells_details import TableCellsDetails
from openapi_server.models.theme_background_fills_details import ThemeBackgroundFillsDetails
from openapi_server.models.theme_fills_details import ThemeFillsDetails
from openapi_server import util


class SharedFillMapDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, connector: SlideConnectorDetails=None, connector_id: str=None, date_created: datetime=None, date_modified: datetime=None, effect_attribute: SharedEffectAttributesDetails=None, effect_attribute_id: str=None, fill_type_id: int=None, gradient_fill: SharedGradientFillsDetails=None, id: str=None, image_fill: SharedImageFillsDetails=None, shape: SlideShapesDetails=None, shape_id: str=None, solid_fill: SharedSolidFillsDetails=None, table_cell: TableCellsDetails=None, table_cell_id: str=None, theme_background_fill: ThemeBackgroundFillsDetails=None, theme_background_fill_id: str=None, theme_fill: ThemeFillsDetails=None, theme_fill_id: str=None, user_created: str=None, user_modified: str=None):
        """SharedFillMapDetails - a model defined in OpenAPI

        :param connector: The connector of this SharedFillMapDetails.
        :param connector_id: The connector_id of this SharedFillMapDetails.
        :param date_created: The date_created of this SharedFillMapDetails.
        :param date_modified: The date_modified of this SharedFillMapDetails.
        :param effect_attribute: The effect_attribute of this SharedFillMapDetails.
        :param effect_attribute_id: The effect_attribute_id of this SharedFillMapDetails.
        :param fill_type_id: The fill_type_id of this SharedFillMapDetails.
        :param gradient_fill: The gradient_fill of this SharedFillMapDetails.
        :param id: The id of this SharedFillMapDetails.
        :param image_fill: The image_fill of this SharedFillMapDetails.
        :param shape: The shape of this SharedFillMapDetails.
        :param shape_id: The shape_id of this SharedFillMapDetails.
        :param solid_fill: The solid_fill of this SharedFillMapDetails.
        :param table_cell: The table_cell of this SharedFillMapDetails.
        :param table_cell_id: The table_cell_id of this SharedFillMapDetails.
        :param theme_background_fill: The theme_background_fill of this SharedFillMapDetails.
        :param theme_background_fill_id: The theme_background_fill_id of this SharedFillMapDetails.
        :param theme_fill: The theme_fill of this SharedFillMapDetails.
        :param theme_fill_id: The theme_fill_id of this SharedFillMapDetails.
        :param user_created: The user_created of this SharedFillMapDetails.
        :param user_modified: The user_modified of this SharedFillMapDetails.
        """
        self.openapi_types = {
            'connector': SlideConnectorDetails,
            'connector_id': str,
            'date_created': datetime,
            'date_modified': datetime,
            'effect_attribute': SharedEffectAttributesDetails,
            'effect_attribute_id': str,
            'fill_type_id': int,
            'gradient_fill': SharedGradientFillsDetails,
            'id': str,
            'image_fill': SharedImageFillsDetails,
            'shape': SlideShapesDetails,
            'shape_id': str,
            'solid_fill': SharedSolidFillsDetails,
            'table_cell': TableCellsDetails,
            'table_cell_id': str,
            'theme_background_fill': ThemeBackgroundFillsDetails,
            'theme_background_fill_id': str,
            'theme_fill': ThemeFillsDetails,
            'theme_fill_id': str,
            'user_created': str,
            'user_modified': str
        }

        self.attribute_map = {
            'connector': 'connector',
            'connector_id': 'connectorId',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'effect_attribute': 'effectAttribute',
            'effect_attribute_id': 'effectAttributeId',
            'fill_type_id': 'fillTypeId',
            'gradient_fill': 'gradientFill',
            'id': 'id',
            'image_fill': 'imageFill',
            'shape': 'shape',
            'shape_id': 'shapeId',
            'solid_fill': 'solidFill',
            'table_cell': 'tableCell',
            'table_cell_id': 'tableCellId',
            'theme_background_fill': 'themeBackgroundFill',
            'theme_background_fill_id': 'themeBackgroundFillId',
            'theme_fill': 'themeFill',
            'theme_fill_id': 'themeFillId',
            'user_created': 'userCreated',
            'user_modified': 'userModified'
        }

        self._connector = connector
        self._connector_id = connector_id
        self._date_created = date_created
        self._date_modified = date_modified
        self._effect_attribute = effect_attribute
        self._effect_attribute_id = effect_attribute_id
        self._fill_type_id = fill_type_id
        self._gradient_fill = gradient_fill
        self._id = id
        self._image_fill = image_fill
        self._shape = shape
        self._shape_id = shape_id
        self._solid_fill = solid_fill
        self._table_cell = table_cell
        self._table_cell_id = table_cell_id
        self._theme_background_fill = theme_background_fill
        self._theme_background_fill_id = theme_background_fill_id
        self._theme_fill = theme_fill
        self._theme_fill_id = theme_fill_id
        self._user_created = user_created
        self._user_modified = user_modified

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SharedFillMapDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Shared.FillMap.Details of this SharedFillMapDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def connector(self):
        """Gets the connector of this SharedFillMapDetails.


        :return: The connector of this SharedFillMapDetails.
        :rtype: SlideConnectorDetails
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this SharedFillMapDetails.


        :param connector: The connector of this SharedFillMapDetails.
        :type connector: SlideConnectorDetails
        """

        self._connector = connector

    @property
    def connector_id(self):
        """Gets the connector_id of this SharedFillMapDetails.


        :return: The connector_id of this SharedFillMapDetails.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this SharedFillMapDetails.


        :param connector_id: The connector_id of this SharedFillMapDetails.
        :type connector_id: str
        """

        self._connector_id = connector_id

    @property
    def date_created(self):
        """Gets the date_created of this SharedFillMapDetails.


        :return: The date_created of this SharedFillMapDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedFillMapDetails.


        :param date_created: The date_created of this SharedFillMapDetails.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedFillMapDetails.


        :return: The date_modified of this SharedFillMapDetails.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedFillMapDetails.


        :param date_modified: The date_modified of this SharedFillMapDetails.
        :type date_modified: datetime
        """

        self._date_modified = date_modified

    @property
    def effect_attribute(self):
        """Gets the effect_attribute of this SharedFillMapDetails.


        :return: The effect_attribute of this SharedFillMapDetails.
        :rtype: SharedEffectAttributesDetails
        """
        return self._effect_attribute

    @effect_attribute.setter
    def effect_attribute(self, effect_attribute):
        """Sets the effect_attribute of this SharedFillMapDetails.


        :param effect_attribute: The effect_attribute of this SharedFillMapDetails.
        :type effect_attribute: SharedEffectAttributesDetails
        """

        self._effect_attribute = effect_attribute

    @property
    def effect_attribute_id(self):
        """Gets the effect_attribute_id of this SharedFillMapDetails.


        :return: The effect_attribute_id of this SharedFillMapDetails.
        :rtype: str
        """
        return self._effect_attribute_id

    @effect_attribute_id.setter
    def effect_attribute_id(self, effect_attribute_id):
        """Sets the effect_attribute_id of this SharedFillMapDetails.


        :param effect_attribute_id: The effect_attribute_id of this SharedFillMapDetails.
        :type effect_attribute_id: str
        """

        self._effect_attribute_id = effect_attribute_id

    @property
    def fill_type_id(self):
        """Gets the fill_type_id of this SharedFillMapDetails.


        :return: The fill_type_id of this SharedFillMapDetails.
        :rtype: int
        """
        return self._fill_type_id

    @fill_type_id.setter
    def fill_type_id(self, fill_type_id):
        """Sets the fill_type_id of this SharedFillMapDetails.


        :param fill_type_id: The fill_type_id of this SharedFillMapDetails.
        :type fill_type_id: int
        """

        self._fill_type_id = fill_type_id

    @property
    def gradient_fill(self):
        """Gets the gradient_fill of this SharedFillMapDetails.


        :return: The gradient_fill of this SharedFillMapDetails.
        :rtype: SharedGradientFillsDetails
        """
        return self._gradient_fill

    @gradient_fill.setter
    def gradient_fill(self, gradient_fill):
        """Sets the gradient_fill of this SharedFillMapDetails.


        :param gradient_fill: The gradient_fill of this SharedFillMapDetails.
        :type gradient_fill: SharedGradientFillsDetails
        """

        self._gradient_fill = gradient_fill

    @property
    def id(self):
        """Gets the id of this SharedFillMapDetails.


        :return: The id of this SharedFillMapDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedFillMapDetails.


        :param id: The id of this SharedFillMapDetails.
        :type id: str
        """

        self._id = id

    @property
    def image_fill(self):
        """Gets the image_fill of this SharedFillMapDetails.


        :return: The image_fill of this SharedFillMapDetails.
        :rtype: SharedImageFillsDetails
        """
        return self._image_fill

    @image_fill.setter
    def image_fill(self, image_fill):
        """Sets the image_fill of this SharedFillMapDetails.


        :param image_fill: The image_fill of this SharedFillMapDetails.
        :type image_fill: SharedImageFillsDetails
        """

        self._image_fill = image_fill

    @property
    def shape(self):
        """Gets the shape of this SharedFillMapDetails.


        :return: The shape of this SharedFillMapDetails.
        :rtype: SlideShapesDetails
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this SharedFillMapDetails.


        :param shape: The shape of this SharedFillMapDetails.
        :type shape: SlideShapesDetails
        """

        self._shape = shape

    @property
    def shape_id(self):
        """Gets the shape_id of this SharedFillMapDetails.


        :return: The shape_id of this SharedFillMapDetails.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """Sets the shape_id of this SharedFillMapDetails.


        :param shape_id: The shape_id of this SharedFillMapDetails.
        :type shape_id: str
        """

        self._shape_id = shape_id

    @property
    def solid_fill(self):
        """Gets the solid_fill of this SharedFillMapDetails.


        :return: The solid_fill of this SharedFillMapDetails.
        :rtype: SharedSolidFillsDetails
        """
        return self._solid_fill

    @solid_fill.setter
    def solid_fill(self, solid_fill):
        """Sets the solid_fill of this SharedFillMapDetails.


        :param solid_fill: The solid_fill of this SharedFillMapDetails.
        :type solid_fill: SharedSolidFillsDetails
        """

        self._solid_fill = solid_fill

    @property
    def table_cell(self):
        """Gets the table_cell of this SharedFillMapDetails.


        :return: The table_cell of this SharedFillMapDetails.
        :rtype: TableCellsDetails
        """
        return self._table_cell

    @table_cell.setter
    def table_cell(self, table_cell):
        """Sets the table_cell of this SharedFillMapDetails.


        :param table_cell: The table_cell of this SharedFillMapDetails.
        :type table_cell: TableCellsDetails
        """

        self._table_cell = table_cell

    @property
    def table_cell_id(self):
        """Gets the table_cell_id of this SharedFillMapDetails.


        :return: The table_cell_id of this SharedFillMapDetails.
        :rtype: str
        """
        return self._table_cell_id

    @table_cell_id.setter
    def table_cell_id(self, table_cell_id):
        """Sets the table_cell_id of this SharedFillMapDetails.


        :param table_cell_id: The table_cell_id of this SharedFillMapDetails.
        :type table_cell_id: str
        """

        self._table_cell_id = table_cell_id

    @property
    def theme_background_fill(self):
        """Gets the theme_background_fill of this SharedFillMapDetails.


        :return: The theme_background_fill of this SharedFillMapDetails.
        :rtype: ThemeBackgroundFillsDetails
        """
        return self._theme_background_fill

    @theme_background_fill.setter
    def theme_background_fill(self, theme_background_fill):
        """Sets the theme_background_fill of this SharedFillMapDetails.


        :param theme_background_fill: The theme_background_fill of this SharedFillMapDetails.
        :type theme_background_fill: ThemeBackgroundFillsDetails
        """

        self._theme_background_fill = theme_background_fill

    @property
    def theme_background_fill_id(self):
        """Gets the theme_background_fill_id of this SharedFillMapDetails.


        :return: The theme_background_fill_id of this SharedFillMapDetails.
        :rtype: str
        """
        return self._theme_background_fill_id

    @theme_background_fill_id.setter
    def theme_background_fill_id(self, theme_background_fill_id):
        """Sets the theme_background_fill_id of this SharedFillMapDetails.


        :param theme_background_fill_id: The theme_background_fill_id of this SharedFillMapDetails.
        :type theme_background_fill_id: str
        """

        self._theme_background_fill_id = theme_background_fill_id

    @property
    def theme_fill(self):
        """Gets the theme_fill of this SharedFillMapDetails.


        :return: The theme_fill of this SharedFillMapDetails.
        :rtype: ThemeFillsDetails
        """
        return self._theme_fill

    @theme_fill.setter
    def theme_fill(self, theme_fill):
        """Sets the theme_fill of this SharedFillMapDetails.


        :param theme_fill: The theme_fill of this SharedFillMapDetails.
        :type theme_fill: ThemeFillsDetails
        """

        self._theme_fill = theme_fill

    @property
    def theme_fill_id(self):
        """Gets the theme_fill_id of this SharedFillMapDetails.


        :return: The theme_fill_id of this SharedFillMapDetails.
        :rtype: str
        """
        return self._theme_fill_id

    @theme_fill_id.setter
    def theme_fill_id(self, theme_fill_id):
        """Sets the theme_fill_id of this SharedFillMapDetails.


        :param theme_fill_id: The theme_fill_id of this SharedFillMapDetails.
        :type theme_fill_id: str
        """

        self._theme_fill_id = theme_fill_id

    @property
    def user_created(self):
        """Gets the user_created of this SharedFillMapDetails.


        :return: The user_created of this SharedFillMapDetails.
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedFillMapDetails.


        :param user_created: The user_created of this SharedFillMapDetails.
        :type user_created: str
        """

        self._user_created = user_created

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedFillMapDetails.


        :return: The user_modified of this SharedFillMapDetails.
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedFillMapDetails.


        :param user_modified: The user_modified of this SharedFillMapDetails.
        :type user_modified: str
        """

        self._user_modified = user_modified
