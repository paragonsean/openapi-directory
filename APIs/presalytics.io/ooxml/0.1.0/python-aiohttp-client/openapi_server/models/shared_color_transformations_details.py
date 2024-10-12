# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.shared_color_transformation_attributes_details import SharedColorTransformationAttributesDetails
from openapi_server.models.shared_solid_fills_details import SharedSolidFillsDetails
from openapi_server import util


class SharedColorTransformationsDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, color_transformation_attributes: List[SharedColorTransformationAttributesDetails]=None, date_created: datetime=None, date_modified: datetime=None, id: str=None, name: str=None, parent_solid_fill: SharedSolidFillsDetails=None, solid_fills_id: str=None, user_created: str=None, user_modified: str=None):
        """SharedColorTransformationsDetails - a model defined in OpenAPI

        :param color_transformation_attributes: The color_transformation_attributes of this SharedColorTransformationsDetails.
        :param date_created: The date_created of this SharedColorTransformationsDetails.
        :param date_modified: The date_modified of this SharedColorTransformationsDetails.
        :param id: The id of this SharedColorTransformationsDetails.
        :param name: The name of this SharedColorTransformationsDetails.
        :param parent_solid_fill: The parent_solid_fill of this SharedColorTransformationsDetails.
        :param solid_fills_id: The solid_fills_id of this SharedColorTransformationsDetails.
        :param user_created: The user_created of this SharedColorTransformationsDetails.
        :param user_modified: The user_modified of this SharedColorTransformationsDetails.
        """
        self.openapi_types = {
            'color_transformation_attributes': List[SharedColorTransformationAttributesDetails],
            'date_created': datetime,
            'date_modified': datetime,
            'id': str,
            'name': str,
            'parent_solid_fill': SharedSolidFillsDetails,
            'solid_fills_id': str,
            'user_created': str,
            'user_modified': str
        }

        self.attribute_map = {
            'color_transformation_attributes': 'colorTransformationAttributes',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'id': 'id',
            'name': 'name',
            'parent_solid_fill': 'parentSolidFill',
            'solid_fills_id': 'solidFillsId',
            'user_created': 'userCreated',
            'user_modified': 'userModified'
        }

        self._color_transformation_attributes = color_transformation_attributes
        self._date_created = date_created
        self._date_modified = date_modified
        self._id = id
        self._name = name
        self._parent_solid_fill = parent_solid_fill
        self._solid_fills_id = solid_fills_id
        self._user_created = user_created
        self._user_modified = user_modified

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SharedColorTransformationsDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Shared.ColorTransformations.Details of this SharedColorTransformationsDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def color_transformation_attributes(self):
        """Gets the color_transformation_attributes of this SharedColorTransformationsDetails.


        :return: The color_transformation_attributes of this SharedColorTransformationsDetails.
        :rtype: List[SharedColorTransformationAttributesDetails]
        """
        return self._color_transformation_attributes

    @color_transformation_attributes.setter
    def color_transformation_attributes(self, color_transformation_attributes):
        """Sets the color_transformation_attributes of this SharedColorTransformationsDetails.


        :param color_transformation_attributes: The color_transformation_attributes of this SharedColorTransformationsDetails.
        :type color_transformation_attributes: List[SharedColorTransformationAttributesDetails]
        """

        self._color_transformation_attributes = color_transformation_attributes

    @property
    def date_created(self):
        """Gets the date_created of this SharedColorTransformationsDetails.


        :return: The date_created of this SharedColorTransformationsDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedColorTransformationsDetails.


        :param date_created: The date_created of this SharedColorTransformationsDetails.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedColorTransformationsDetails.


        :return: The date_modified of this SharedColorTransformationsDetails.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedColorTransformationsDetails.


        :param date_modified: The date_modified of this SharedColorTransformationsDetails.
        :type date_modified: datetime
        """

        self._date_modified = date_modified

    @property
    def id(self):
        """Gets the id of this SharedColorTransformationsDetails.


        :return: The id of this SharedColorTransformationsDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedColorTransformationsDetails.


        :param id: The id of this SharedColorTransformationsDetails.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SharedColorTransformationsDetails.


        :return: The name of this SharedColorTransformationsDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedColorTransformationsDetails.


        :param name: The name of this SharedColorTransformationsDetails.
        :type name: str
        """

        self._name = name

    @property
    def parent_solid_fill(self):
        """Gets the parent_solid_fill of this SharedColorTransformationsDetails.


        :return: The parent_solid_fill of this SharedColorTransformationsDetails.
        :rtype: SharedSolidFillsDetails
        """
        return self._parent_solid_fill

    @parent_solid_fill.setter
    def parent_solid_fill(self, parent_solid_fill):
        """Sets the parent_solid_fill of this SharedColorTransformationsDetails.


        :param parent_solid_fill: The parent_solid_fill of this SharedColorTransformationsDetails.
        :type parent_solid_fill: SharedSolidFillsDetails
        """

        self._parent_solid_fill = parent_solid_fill

    @property
    def solid_fills_id(self):
        """Gets the solid_fills_id of this SharedColorTransformationsDetails.


        :return: The solid_fills_id of this SharedColorTransformationsDetails.
        :rtype: str
        """
        return self._solid_fills_id

    @solid_fills_id.setter
    def solid_fills_id(self, solid_fills_id):
        """Sets the solid_fills_id of this SharedColorTransformationsDetails.


        :param solid_fills_id: The solid_fills_id of this SharedColorTransformationsDetails.
        :type solid_fills_id: str
        """

        self._solid_fills_id = solid_fills_id

    @property
    def user_created(self):
        """Gets the user_created of this SharedColorTransformationsDetails.


        :return: The user_created of this SharedColorTransformationsDetails.
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedColorTransformationsDetails.


        :param user_created: The user_created of this SharedColorTransformationsDetails.
        :type user_created: str
        """

        self._user_created = user_created

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedColorTransformationsDetails.


        :return: The user_modified of this SharedColorTransformationsDetails.
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedColorTransformationsDetails.


        :param user_modified: The user_modified of this SharedColorTransformationsDetails.
        :type user_modified: str
        """

        self._user_modified = user_modified
