# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Project(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, published_date: str=None, title: str=None, url: str=None):
        """Project - a model defined in OpenAPI

        :param id: The id of this Project.
        :param published_date: The published_date of this Project.
        :param title: The title of this Project.
        :param url: The url of this Project.
        """
        self.openapi_types = {
            'id': int,
            'published_date': str,
            'title': str,
            'url': str
        }

        self.attribute_map = {
            'id': 'id',
            'published_date': 'published_date',
            'title': 'title',
            'url': 'url'
        }

        self._id = id
        self._published_date = published_date
        self._title = title
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Project':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Project of this Project.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Project.

        Project id

        :return: The id of this Project.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        Project id

        :param id: The id of this Project.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def published_date(self):
        """Gets the published_date of this Project.

        Date when project was published

        :return: The published_date of this Project.
        :rtype: str
        """
        return self._published_date

    @published_date.setter
    def published_date(self, published_date):
        """Sets the published_date of this Project.

        Date when project was published

        :param published_date: The published_date of this Project.
        :type published_date: str
        """
        if published_date is None:
            raise ValueError("Invalid value for `published_date`, must not be `None`")

        self._published_date = published_date

    @property
    def title(self):
        """Gets the title of this Project.

        Project title

        :return: The title of this Project.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Project.

        Project title

        :param title: The title of this Project.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def url(self):
        """Gets the url of this Project.

        Api endpoint

        :return: The url of this Project.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Project.

        Api endpoint

        :param url: The url of this Project.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url
