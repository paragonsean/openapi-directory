# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.app_about import AppAbout
from openapi_server.models.app_legal import AppLegal
from openapi_server import util


class App(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, about: AppAbout=None, id: float=None, legal: AppLegal=None):
        """App - a model defined in OpenAPI

        :param about: The about of this App.
        :param id: The id of this App.
        :param legal: The legal of this App.
        """
        self.openapi_types = {
            'about': AppAbout,
            'id': float,
            'legal': AppLegal
        }

        self.attribute_map = {
            'about': 'about',
            'id': 'id',
            'legal': 'legal'
        }

        self._about = about
        self._id = id
        self._legal = legal

    @classmethod
    def from_dict(cls, dikt: dict) -> 'App':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The App of this App.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def about(self):
        """Gets the about of this App.


        :return: The about of this App.
        :rtype: AppAbout
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this App.


        :param about: The about of this App.
        :type about: AppAbout
        """

        self._about = about

    @property
    def id(self):
        """Gets the id of this App.


        :return: The id of this App.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this App.


        :param id: The id of this App.
        :type id: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def legal(self):
        """Gets the legal of this App.


        :return: The legal of this App.
        :rtype: AppLegal
        """
        return self._legal

    @legal.setter
    def legal(self, legal):
        """Sets the legal of this App.


        :param legal: The legal of this App.
        :type legal: AppLegal
        """

        self._legal = legal
