# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.podcast_list_podcasts_item import PodcastListPodcastsItem
from openapi_server import util


class PodcastList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, no_of_pages: int=None, page: int=None, page_size: int=None, podcasts: List[PodcastListPodcastsItem]=None, total: int=None):
        """PodcastList - a model defined in OpenAPI

        :param no_of_pages: The no_of_pages of this PodcastList.
        :param page: The page of this PodcastList.
        :param page_size: The page_size of this PodcastList.
        :param podcasts: The podcasts of this PodcastList.
        :param total: The total of this PodcastList.
        """
        self.openapi_types = {
            'no_of_pages': int,
            'page': int,
            'page_size': int,
            'podcasts': List[PodcastListPodcastsItem],
            'total': int
        }

        self.attribute_map = {
            'no_of_pages': 'noOfPages',
            'page': 'page',
            'page_size': 'pageSize',
            'podcasts': 'podcasts',
            'total': 'total'
        }

        self._no_of_pages = no_of_pages
        self._page = page
        self._page_size = page_size
        self._podcasts = podcasts
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PodcastList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PodcastList of this PodcastList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def no_of_pages(self):
        """Gets the no_of_pages of this PodcastList.


        :return: The no_of_pages of this PodcastList.
        :rtype: int
        """
        return self._no_of_pages

    @no_of_pages.setter
    def no_of_pages(self, no_of_pages):
        """Sets the no_of_pages of this PodcastList.


        :param no_of_pages: The no_of_pages of this PodcastList.
        :type no_of_pages: int
        """

        self._no_of_pages = no_of_pages

    @property
    def page(self):
        """Gets the page of this PodcastList.


        :return: The page of this PodcastList.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PodcastList.


        :param page: The page of this PodcastList.
        :type page: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this PodcastList.


        :return: The page_size of this PodcastList.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PodcastList.


        :param page_size: The page_size of this PodcastList.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def podcasts(self):
        """Gets the podcasts of this PodcastList.


        :return: The podcasts of this PodcastList.
        :rtype: List[PodcastListPodcastsItem]
        """
        return self._podcasts

    @podcasts.setter
    def podcasts(self, podcasts):
        """Sets the podcasts of this PodcastList.


        :param podcasts: The podcasts of this PodcastList.
        :type podcasts: List[PodcastListPodcastsItem]
        """

        self._podcasts = podcasts

    @property
    def total(self):
        """Gets the total of this PodcastList.


        :return: The total of this PodcastList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PodcastList.


        :param total: The total of this PodcastList.
        :type total: int
        """

        self._total = total
