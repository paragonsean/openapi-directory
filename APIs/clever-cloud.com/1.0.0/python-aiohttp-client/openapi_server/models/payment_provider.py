# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PaymentProvider(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coming_soon: bool=False, img_url: str=None, name: str=None, title: str=None):
        """PaymentProvider - a model defined in OpenAPI

        :param coming_soon: The coming_soon of this PaymentProvider.
        :param img_url: The img_url of this PaymentProvider.
        :param name: The name of this PaymentProvider.
        :param title: The title of this PaymentProvider.
        """
        self.openapi_types = {
            'coming_soon': bool,
            'img_url': str,
            'name': str,
            'title': str
        }

        self.attribute_map = {
            'coming_soon': 'comingSoon',
            'img_url': 'imgUrl',
            'name': 'name',
            'title': 'title'
        }

        self._coming_soon = coming_soon
        self._img_url = img_url
        self._name = name
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaymentProvider':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Payment_Provider of this PaymentProvider.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coming_soon(self):
        """Gets the coming_soon of this PaymentProvider.


        :return: The coming_soon of this PaymentProvider.
        :rtype: bool
        """
        return self._coming_soon

    @coming_soon.setter
    def coming_soon(self, coming_soon):
        """Sets the coming_soon of this PaymentProvider.


        :param coming_soon: The coming_soon of this PaymentProvider.
        :type coming_soon: bool
        """
        if coming_soon is None:
            raise ValueError("Invalid value for `coming_soon`, must not be `None`")

        self._coming_soon = coming_soon

    @property
    def img_url(self):
        """Gets the img_url of this PaymentProvider.


        :return: The img_url of this PaymentProvider.
        :rtype: str
        """
        return self._img_url

    @img_url.setter
    def img_url(self, img_url):
        """Sets the img_url of this PaymentProvider.


        :param img_url: The img_url of this PaymentProvider.
        :type img_url: str
        """
        if img_url is None:
            raise ValueError("Invalid value for `img_url`, must not be `None`")

        self._img_url = img_url

    @property
    def name(self):
        """Gets the name of this PaymentProvider.


        :return: The name of this PaymentProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentProvider.


        :param name: The name of this PaymentProvider.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def title(self):
        """Gets the title of this PaymentProvider.


        :return: The title of this PaymentProvider.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PaymentProvider.


        :param title: The title of this PaymentProvider.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title
