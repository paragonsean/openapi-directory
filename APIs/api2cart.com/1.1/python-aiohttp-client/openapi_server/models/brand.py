# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.image import Image
from openapi_server import util


class Brand(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, active: bool=None, additional_fields: object=None, created_time: str=None, custom_fields: object=None, full_description: str=None, id: str=None, images: List[Image]=None, meta_description: str=None, meta_keywords: str=None, meta_title: str=None, modified_time: str=None, name: str=None, short_description: str=None, stores_ids: List[str]=None, url: str=None):
        """Brand - a model defined in OpenAPI

        :param active: The active of this Brand.
        :param additional_fields: The additional_fields of this Brand.
        :param created_time: The created_time of this Brand.
        :param custom_fields: The custom_fields of this Brand.
        :param full_description: The full_description of this Brand.
        :param id: The id of this Brand.
        :param images: The images of this Brand.
        :param meta_description: The meta_description of this Brand.
        :param meta_keywords: The meta_keywords of this Brand.
        :param meta_title: The meta_title of this Brand.
        :param modified_time: The modified_time of this Brand.
        :param name: The name of this Brand.
        :param short_description: The short_description of this Brand.
        :param stores_ids: The stores_ids of this Brand.
        :param url: The url of this Brand.
        """
        self.openapi_types = {
            'active': bool,
            'additional_fields': object,
            'created_time': str,
            'custom_fields': object,
            'full_description': str,
            'id': str,
            'images': List[Image],
            'meta_description': str,
            'meta_keywords': str,
            'meta_title': str,
            'modified_time': str,
            'name': str,
            'short_description': str,
            'stores_ids': List[str],
            'url': str
        }

        self.attribute_map = {
            'active': 'active',
            'additional_fields': 'additional_fields',
            'created_time': 'created_time',
            'custom_fields': 'custom_fields',
            'full_description': 'full_description',
            'id': 'id',
            'images': 'images',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'meta_title': 'meta_title',
            'modified_time': 'modified_time',
            'name': 'name',
            'short_description': 'short_description',
            'stores_ids': 'stores_ids',
            'url': 'url'
        }

        self._active = active
        self._additional_fields = additional_fields
        self._created_time = created_time
        self._custom_fields = custom_fields
        self._full_description = full_description
        self._id = id
        self._images = images
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._meta_title = meta_title
        self._modified_time = modified_time
        self._name = name
        self._short_description = short_description
        self._stores_ids = stores_ids
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Brand':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Brand of this Brand.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active(self):
        """Gets the active of this Brand.


        :return: The active of this Brand.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Brand.


        :param active: The active of this Brand.
        :type active: bool
        """

        self._active = active

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Brand.


        :return: The additional_fields of this Brand.
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Brand.


        :param additional_fields: The additional_fields of this Brand.
        :type additional_fields: object
        """

        self._additional_fields = additional_fields

    @property
    def created_time(self):
        """Gets the created_time of this Brand.


        :return: The created_time of this Brand.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Brand.


        :param created_time: The created_time of this Brand.
        :type created_time: str
        """

        self._created_time = created_time

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Brand.


        :return: The custom_fields of this Brand.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Brand.


        :param custom_fields: The custom_fields of this Brand.
        :type custom_fields: object
        """

        self._custom_fields = custom_fields

    @property
    def full_description(self):
        """Gets the full_description of this Brand.


        :return: The full_description of this Brand.
        :rtype: str
        """
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        """Sets the full_description of this Brand.


        :param full_description: The full_description of this Brand.
        :type full_description: str
        """

        self._full_description = full_description

    @property
    def id(self):
        """Gets the id of this Brand.


        :return: The id of this Brand.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Brand.


        :param id: The id of this Brand.
        :type id: str
        """

        self._id = id

    @property
    def images(self):
        """Gets the images of this Brand.


        :return: The images of this Brand.
        :rtype: List[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Brand.


        :param images: The images of this Brand.
        :type images: List[Image]
        """

        self._images = images

    @property
    def meta_description(self):
        """Gets the meta_description of this Brand.


        :return: The meta_description of this Brand.
        :rtype: str
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """Sets the meta_description of this Brand.


        :param meta_description: The meta_description of this Brand.
        :type meta_description: str
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """Gets the meta_keywords of this Brand.


        :return: The meta_keywords of this Brand.
        :rtype: str
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """Sets the meta_keywords of this Brand.


        :param meta_keywords: The meta_keywords of this Brand.
        :type meta_keywords: str
        """

        self._meta_keywords = meta_keywords

    @property
    def meta_title(self):
        """Gets the meta_title of this Brand.


        :return: The meta_title of this Brand.
        :rtype: str
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """Sets the meta_title of this Brand.


        :param meta_title: The meta_title of this Brand.
        :type meta_title: str
        """

        self._meta_title = meta_title

    @property
    def modified_time(self):
        """Gets the modified_time of this Brand.


        :return: The modified_time of this Brand.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this Brand.


        :param modified_time: The modified_time of this Brand.
        :type modified_time: str
        """

        self._modified_time = modified_time

    @property
    def name(self):
        """Gets the name of this Brand.


        :return: The name of this Brand.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Brand.


        :param name: The name of this Brand.
        :type name: str
        """

        self._name = name

    @property
    def short_description(self):
        """Gets the short_description of this Brand.


        :return: The short_description of this Brand.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Brand.


        :param short_description: The short_description of this Brand.
        :type short_description: str
        """

        self._short_description = short_description

    @property
    def stores_ids(self):
        """Gets the stores_ids of this Brand.


        :return: The stores_ids of this Brand.
        :rtype: List[str]
        """
        return self._stores_ids

    @stores_ids.setter
    def stores_ids(self, stores_ids):
        """Sets the stores_ids of this Brand.


        :param stores_ids: The stores_ids of this Brand.
        :type stores_ids: List[str]
        """

        self._stores_ids = stores_ids

    @property
    def url(self):
        """Gets the url of this Brand.


        :return: The url of this Brand.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Brand.


        :param url: The url of this Brand.
        :type url: str
        """

        self._url = url
