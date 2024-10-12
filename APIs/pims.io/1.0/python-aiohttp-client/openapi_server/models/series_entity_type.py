# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SeriesEntityType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, label: str=None):
        """SeriesEntityType - a model defined in OpenAPI

        :param id: The id of this SeriesEntityType.
        :param label: The label of this SeriesEntityType.
        """
        self.openapi_types = {
            'id': str,
            'label': str
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label'
        }

        self._id = id
        self._label = label

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SeriesEntityType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SeriesEntity_type of this SeriesEntityType.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SeriesEntityType.

        String identifying the series type.

        :return: The id of this SeriesEntityType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SeriesEntityType.

        String identifying the series type.

        :param id: The id of this SeriesEntityType.
        :type id: str
        """
        allowed_values = ["TOU", "LGS"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def label(self):
        """Gets the label of this SeriesEntityType.

        Label of the series type. This value is translated according to the 'Accept-Language' header.

        :return: The label of this SeriesEntityType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SeriesEntityType.

        Label of the series type. This value is translated according to the 'Accept-Language' header.

        :param label: The label of this SeriesEntityType.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label
