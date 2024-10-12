# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SlideColorMaps(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accent1: int=None, accent2: int=None, accent3: int=None, accent4: int=None, accent5: int=None, accent6: int=None, background1: int=None, background2: int=None, followed_hyperlink: int=None, hyperlink: int=None, id: str=None, slide_master_id: str=None, text1: int=None, text2: int=None):
        """SlideColorMaps - a model defined in OpenAPI

        :param accent1: The accent1 of this SlideColorMaps.
        :param accent2: The accent2 of this SlideColorMaps.
        :param accent3: The accent3 of this SlideColorMaps.
        :param accent4: The accent4 of this SlideColorMaps.
        :param accent5: The accent5 of this SlideColorMaps.
        :param accent6: The accent6 of this SlideColorMaps.
        :param background1: The background1 of this SlideColorMaps.
        :param background2: The background2 of this SlideColorMaps.
        :param followed_hyperlink: The followed_hyperlink of this SlideColorMaps.
        :param hyperlink: The hyperlink of this SlideColorMaps.
        :param id: The id of this SlideColorMaps.
        :param slide_master_id: The slide_master_id of this SlideColorMaps.
        :param text1: The text1 of this SlideColorMaps.
        :param text2: The text2 of this SlideColorMaps.
        """
        self.openapi_types = {
            'accent1': int,
            'accent2': int,
            'accent3': int,
            'accent4': int,
            'accent5': int,
            'accent6': int,
            'background1': int,
            'background2': int,
            'followed_hyperlink': int,
            'hyperlink': int,
            'id': str,
            'slide_master_id': str,
            'text1': int,
            'text2': int
        }

        self.attribute_map = {
            'accent1': 'accent1',
            'accent2': 'accent2',
            'accent3': 'accent3',
            'accent4': 'accent4',
            'accent5': 'accent5',
            'accent6': 'accent6',
            'background1': 'background1',
            'background2': 'background2',
            'followed_hyperlink': 'followedHyperlink',
            'hyperlink': 'hyperlink',
            'id': 'id',
            'slide_master_id': 'slideMasterId',
            'text1': 'text1',
            'text2': 'text2'
        }

        self._accent1 = accent1
        self._accent2 = accent2
        self._accent3 = accent3
        self._accent4 = accent4
        self._accent5 = accent5
        self._accent6 = accent6
        self._background1 = background1
        self._background2 = background2
        self._followed_hyperlink = followed_hyperlink
        self._hyperlink = hyperlink
        self._id = id
        self._slide_master_id = slide_master_id
        self._text1 = text1
        self._text2 = text2

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SlideColorMaps':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Slide.ColorMaps of this SlideColorMaps.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accent1(self):
        """Gets the accent1 of this SlideColorMaps.


        :return: The accent1 of this SlideColorMaps.
        :rtype: int
        """
        return self._accent1

    @accent1.setter
    def accent1(self, accent1):
        """Sets the accent1 of this SlideColorMaps.


        :param accent1: The accent1 of this SlideColorMaps.
        :type accent1: int
        """

        self._accent1 = accent1

    @property
    def accent2(self):
        """Gets the accent2 of this SlideColorMaps.


        :return: The accent2 of this SlideColorMaps.
        :rtype: int
        """
        return self._accent2

    @accent2.setter
    def accent2(self, accent2):
        """Sets the accent2 of this SlideColorMaps.


        :param accent2: The accent2 of this SlideColorMaps.
        :type accent2: int
        """

        self._accent2 = accent2

    @property
    def accent3(self):
        """Gets the accent3 of this SlideColorMaps.


        :return: The accent3 of this SlideColorMaps.
        :rtype: int
        """
        return self._accent3

    @accent3.setter
    def accent3(self, accent3):
        """Sets the accent3 of this SlideColorMaps.


        :param accent3: The accent3 of this SlideColorMaps.
        :type accent3: int
        """

        self._accent3 = accent3

    @property
    def accent4(self):
        """Gets the accent4 of this SlideColorMaps.


        :return: The accent4 of this SlideColorMaps.
        :rtype: int
        """
        return self._accent4

    @accent4.setter
    def accent4(self, accent4):
        """Sets the accent4 of this SlideColorMaps.


        :param accent4: The accent4 of this SlideColorMaps.
        :type accent4: int
        """

        self._accent4 = accent4

    @property
    def accent5(self):
        """Gets the accent5 of this SlideColorMaps.


        :return: The accent5 of this SlideColorMaps.
        :rtype: int
        """
        return self._accent5

    @accent5.setter
    def accent5(self, accent5):
        """Sets the accent5 of this SlideColorMaps.


        :param accent5: The accent5 of this SlideColorMaps.
        :type accent5: int
        """

        self._accent5 = accent5

    @property
    def accent6(self):
        """Gets the accent6 of this SlideColorMaps.


        :return: The accent6 of this SlideColorMaps.
        :rtype: int
        """
        return self._accent6

    @accent6.setter
    def accent6(self, accent6):
        """Sets the accent6 of this SlideColorMaps.


        :param accent6: The accent6 of this SlideColorMaps.
        :type accent6: int
        """

        self._accent6 = accent6

    @property
    def background1(self):
        """Gets the background1 of this SlideColorMaps.


        :return: The background1 of this SlideColorMaps.
        :rtype: int
        """
        return self._background1

    @background1.setter
    def background1(self, background1):
        """Sets the background1 of this SlideColorMaps.


        :param background1: The background1 of this SlideColorMaps.
        :type background1: int
        """

        self._background1 = background1

    @property
    def background2(self):
        """Gets the background2 of this SlideColorMaps.


        :return: The background2 of this SlideColorMaps.
        :rtype: int
        """
        return self._background2

    @background2.setter
    def background2(self, background2):
        """Sets the background2 of this SlideColorMaps.


        :param background2: The background2 of this SlideColorMaps.
        :type background2: int
        """

        self._background2 = background2

    @property
    def followed_hyperlink(self):
        """Gets the followed_hyperlink of this SlideColorMaps.


        :return: The followed_hyperlink of this SlideColorMaps.
        :rtype: int
        """
        return self._followed_hyperlink

    @followed_hyperlink.setter
    def followed_hyperlink(self, followed_hyperlink):
        """Sets the followed_hyperlink of this SlideColorMaps.


        :param followed_hyperlink: The followed_hyperlink of this SlideColorMaps.
        :type followed_hyperlink: int
        """

        self._followed_hyperlink = followed_hyperlink

    @property
    def hyperlink(self):
        """Gets the hyperlink of this SlideColorMaps.


        :return: The hyperlink of this SlideColorMaps.
        :rtype: int
        """
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, hyperlink):
        """Sets the hyperlink of this SlideColorMaps.


        :param hyperlink: The hyperlink of this SlideColorMaps.
        :type hyperlink: int
        """

        self._hyperlink = hyperlink

    @property
    def id(self):
        """Gets the id of this SlideColorMaps.


        :return: The id of this SlideColorMaps.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideColorMaps.


        :param id: The id of this SlideColorMaps.
        :type id: str
        """

        self._id = id

    @property
    def slide_master_id(self):
        """Gets the slide_master_id of this SlideColorMaps.


        :return: The slide_master_id of this SlideColorMaps.
        :rtype: str
        """
        return self._slide_master_id

    @slide_master_id.setter
    def slide_master_id(self, slide_master_id):
        """Sets the slide_master_id of this SlideColorMaps.


        :param slide_master_id: The slide_master_id of this SlideColorMaps.
        :type slide_master_id: str
        """

        self._slide_master_id = slide_master_id

    @property
    def text1(self):
        """Gets the text1 of this SlideColorMaps.


        :return: The text1 of this SlideColorMaps.
        :rtype: int
        """
        return self._text1

    @text1.setter
    def text1(self, text1):
        """Sets the text1 of this SlideColorMaps.


        :param text1: The text1 of this SlideColorMaps.
        :type text1: int
        """

        self._text1 = text1

    @property
    def text2(self):
        """Gets the text2 of this SlideColorMaps.


        :return: The text2 of this SlideColorMaps.
        :rtype: int
        """
        return self._text2

    @text2.setter
    def text2(self, text2):
        """Sets the text2 of this SlideColorMaps.


        :param text2: The text2 of this SlideColorMaps.
        :type text2: int
        """

        self._text2 = text2
