# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.podcast_episode_list_episodes_item import PodcastEpisodeListEpisodesItem
from openapi_server import util


class PodcastEpisodeList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, episodes: List[PodcastEpisodeListEpisodesItem]=None, no_of_pages: int=None, page: int=None, page_size: int=None, total: int=None):
        """PodcastEpisodeList - a model defined in OpenAPI

        :param episodes: The episodes of this PodcastEpisodeList.
        :param no_of_pages: The no_of_pages of this PodcastEpisodeList.
        :param page: The page of this PodcastEpisodeList.
        :param page_size: The page_size of this PodcastEpisodeList.
        :param total: The total of this PodcastEpisodeList.
        """
        self.openapi_types = {
            'episodes': List[PodcastEpisodeListEpisodesItem],
            'no_of_pages': int,
            'page': int,
            'page_size': int,
            'total': int
        }

        self.attribute_map = {
            'episodes': 'episodes',
            'no_of_pages': 'noOfPages',
            'page': 'page',
            'page_size': 'pageSize',
            'total': 'total'
        }

        self._episodes = episodes
        self._no_of_pages = no_of_pages
        self._page = page
        self._page_size = page_size
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PodcastEpisodeList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PodcastEpisodeList of this PodcastEpisodeList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def episodes(self):
        """Gets the episodes of this PodcastEpisodeList.


        :return: The episodes of this PodcastEpisodeList.
        :rtype: List[PodcastEpisodeListEpisodesItem]
        """
        return self._episodes

    @episodes.setter
    def episodes(self, episodes):
        """Sets the episodes of this PodcastEpisodeList.


        :param episodes: The episodes of this PodcastEpisodeList.
        :type episodes: List[PodcastEpisodeListEpisodesItem]
        """

        self._episodes = episodes

    @property
    def no_of_pages(self):
        """Gets the no_of_pages of this PodcastEpisodeList.


        :return: The no_of_pages of this PodcastEpisodeList.
        :rtype: int
        """
        return self._no_of_pages

    @no_of_pages.setter
    def no_of_pages(self, no_of_pages):
        """Sets the no_of_pages of this PodcastEpisodeList.


        :param no_of_pages: The no_of_pages of this PodcastEpisodeList.
        :type no_of_pages: int
        """

        self._no_of_pages = no_of_pages

    @property
    def page(self):
        """Gets the page of this PodcastEpisodeList.


        :return: The page of this PodcastEpisodeList.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PodcastEpisodeList.


        :param page: The page of this PodcastEpisodeList.
        :type page: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this PodcastEpisodeList.


        :return: The page_size of this PodcastEpisodeList.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PodcastEpisodeList.


        :param page_size: The page_size of this PodcastEpisodeList.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this PodcastEpisodeList.


        :return: The total of this PodcastEpisodeList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PodcastEpisodeList.


        :param total: The total of this PodcastEpisodeList.
        :type total: int
        """

        self._total = total
