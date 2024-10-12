# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.link import Link
from openapi_server import util


class EventDocument(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, classification: str=None, _date: str=None, links: List[Link]=None, note: str=None):
        """EventDocument - a model defined in OpenAPI

        :param classification: The classification of this EventDocument.
        :param _date: The _date of this EventDocument.
        :param links: The links of this EventDocument.
        :param note: The note of this EventDocument.
        """
        self.openapi_types = {
            'classification': str,
            '_date': str,
            'links': List[Link],
            'note': str
        }

        self.attribute_map = {
            'classification': 'classification',
            '_date': 'date',
            'links': 'links',
            'note': 'note'
        }

        self._classification = classification
        self.__date = _date
        self._links = links
        self._note = note

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EventDocument':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EventDocument of this EventDocument.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def classification(self):
        """Gets the classification of this EventDocument.


        :return: The classification of this EventDocument.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this EventDocument.


        :param classification: The classification of this EventDocument.
        :type classification: str
        """
        if classification is None:
            raise ValueError("Invalid value for `classification`, must not be `None`")

        self._classification = classification

    @property
    def _date(self):
        """Gets the _date of this EventDocument.


        :return: The _date of this EventDocument.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EventDocument.


        :param _date: The _date of this EventDocument.
        :type _date: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")

        self.__date = _date

    @property
    def links(self):
        """Gets the links of this EventDocument.


        :return: The links of this EventDocument.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EventDocument.


        :param links: The links of this EventDocument.
        :type links: List[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")

        self._links = links

    @property
    def note(self):
        """Gets the note of this EventDocument.


        :return: The note of this EventDocument.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EventDocument.


        :param note: The note of this EventDocument.
        :type note: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")

        self._note = note
