# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.previous_next_mixin_previous_next_previous_next import PreviousNextMixinPreviousNextPreviousNext
from openapi_server.models.reference import Reference
from openapi_server import util


class PreviousNextMixinPreviousNext(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next: Reference=None, previous: Reference=None, previous_next: PreviousNextMixinPreviousNextPreviousNext=None):
        """PreviousNextMixinPreviousNext - a model defined in OpenAPI

        :param next: The next of this PreviousNextMixinPreviousNext.
        :param previous: The previous of this PreviousNextMixinPreviousNext.
        :param previous_next: The previous_next of this PreviousNextMixinPreviousNext.
        """
        self.openapi_types = {
            'next': Reference,
            'previous': Reference,
            'previous_next': PreviousNextMixinPreviousNextPreviousNext
        }

        self.attribute_map = {
            'next': 'next',
            'previous': 'previous',
            'previous_next': 'previous_next'
        }

        self._next = next
        self._previous = previous
        self._previous_next = previous_next

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PreviousNextMixinPreviousNext':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The previous_next_mixin_previous_next of this PreviousNextMixinPreviousNext.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next(self):
        """Gets the next of this PreviousNextMixinPreviousNext.


        :return: The next of this PreviousNextMixinPreviousNext.
        :rtype: Reference
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PreviousNextMixinPreviousNext.


        :param next: The next of this PreviousNextMixinPreviousNext.
        :type next: Reference
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this PreviousNextMixinPreviousNext.


        :return: The previous of this PreviousNextMixinPreviousNext.
        :rtype: Reference
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this PreviousNextMixinPreviousNext.


        :param previous: The previous of this PreviousNextMixinPreviousNext.
        :type previous: Reference
        """

        self._previous = previous

    @property
    def previous_next(self):
        """Gets the previous_next of this PreviousNextMixinPreviousNext.


        :return: The previous_next of this PreviousNextMixinPreviousNext.
        :rtype: PreviousNextMixinPreviousNextPreviousNext
        """
        return self._previous_next

    @previous_next.setter
    def previous_next(self, previous_next):
        """Sets the previous_next of this PreviousNextMixinPreviousNext.


        :param previous_next: The previous_next of this PreviousNextMixinPreviousNext.
        :type previous_next: PreviousNextMixinPreviousNextPreviousNext
        """
        if previous_next is None:
            raise ValueError("Invalid value for `previous_next`, must not be `None`")

        self._previous_next = previous_next
