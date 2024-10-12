# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content_submission_id: int=None, id: int=None, name: str=None, value: str=None):
        """ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute - a model defined in OpenAPI

        :param content_submission_id: The content_submission_id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :param id: The id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :param name: The name of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :param value: The value of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        """
        self.openapi_types = {
            'content_submission_id': int,
            'id': int,
            'name': str,
            'value': str
        }

        self.attribute_map = {
            'content_submission_id': 'ContentSubmissionID',
            'id': 'ID',
            'name': 'Name',
            'value': 'Value'
        }

        self._content_submission_id = content_submission_id
        self._id = id
        self._name = name
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ContentSubmission.Shared.BusinessEntities.ContentSubmissionAttribute of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content_submission_id(self):
        """Gets the content_submission_id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The ID of the content submission to which this attribute belongs.

        :return: The content_submission_id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :rtype: int
        """
        return self._content_submission_id

    @content_submission_id.setter
    def content_submission_id(self, content_submission_id):
        """Sets the content_submission_id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The ID of the content submission to which this attribute belongs.

        :param content_submission_id: The content_submission_id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :type content_submission_id: int
        """

        self._content_submission_id = content_submission_id

    @property
    def id(self):
        """Gets the id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The ID of this attribute.

        :return: The id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The ID of this attribute.

        :param id: The id of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The name of this Attribute.

        :return: The name of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The name of this Attribute.

        :param name: The name of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and not re.search(r'[a-zA-Z0-9]+', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/[a-zA-Z0-9]+/`")

        self._name = name

    @property
    def value(self):
        """Gets the value of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The value of this Attribute

        :return: The value of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.

        The value of this Attribute

        :param value: The value of this ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.
        :type value: str
        """

        self._value = value
