# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Seriestypeupdatestatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, running: bool=None):
        """Seriestypeupdatestatus - a model defined in OpenAPI

        :param running: The running of this Seriestypeupdatestatus.
        """
        self.openapi_types = {
            'running': bool
        }

        self.attribute_map = {
            'running': 'running'
        }

        self._running = running

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Seriestypeupdatestatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The seriestypeupdatestatus of this Seriestypeupdatestatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def running(self):
        """Gets the running of this Seriestypeupdatestatus.


        :return: The running of this Seriestypeupdatestatus.
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this Seriestypeupdatestatus.


        :param running: The running of this Seriestypeupdatestatus.
        :type running: bool
        """
        if running is None:
            raise ValueError("Invalid value for `running`, must not be `None`")

        self._running = running
