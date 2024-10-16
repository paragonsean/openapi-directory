# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.category_summary import CategorySummary
from openapi_server.models.image import Image
from openapi_server.models.network_summary import NetworkSummary
from openapi_server.models.podcast_episode_summary import PodcastEpisodeSummary
from openapi_server.models.podcast_synopses import PodcastSynopses
from openapi_server.models.programme_titles import ProgrammeTitles
from openapi_server import util


class Podcast(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, category_summaries: List[CategorySummary]=None, days_available: int=None, entity_type: str=None, first_published_date: str=None, frequency: str=None, images: List[Image]=None, latest_available_episodes: List[PodcastEpisodeSummary]=None, network_summary: NetworkSummary=None, pid: str=None, rss_url: str=None, synopses: PodcastSynopses=None, territory: str=None, titles: ProgrammeTitles=None, total_available_episodes: int=None, type: str=None, updated_at: str=None):
        """Podcast - a model defined in OpenAPI

        :param category_summaries: The category_summaries of this Podcast.
        :param days_available: The days_available of this Podcast.
        :param entity_type: The entity_type of this Podcast.
        :param first_published_date: The first_published_date of this Podcast.
        :param frequency: The frequency of this Podcast.
        :param images: The images of this Podcast.
        :param latest_available_episodes: The latest_available_episodes of this Podcast.
        :param network_summary: The network_summary of this Podcast.
        :param pid: The pid of this Podcast.
        :param rss_url: The rss_url of this Podcast.
        :param synopses: The synopses of this Podcast.
        :param territory: The territory of this Podcast.
        :param titles: The titles of this Podcast.
        :param total_available_episodes: The total_available_episodes of this Podcast.
        :param type: The type of this Podcast.
        :param updated_at: The updated_at of this Podcast.
        """
        self.openapi_types = {
            'category_summaries': List[CategorySummary],
            'days_available': int,
            'entity_type': str,
            'first_published_date': str,
            'frequency': str,
            'images': List[Image],
            'latest_available_episodes': List[PodcastEpisodeSummary],
            'network_summary': NetworkSummary,
            'pid': str,
            'rss_url': str,
            'synopses': PodcastSynopses,
            'territory': str,
            'titles': ProgrammeTitles,
            'total_available_episodes': int,
            'type': str,
            'updated_at': str
        }

        self.attribute_map = {
            'category_summaries': 'category_summaries',
            'days_available': 'days_available',
            'entity_type': 'entity_type',
            'first_published_date': 'first_published_date',
            'frequency': 'frequency',
            'images': 'images',
            'latest_available_episodes': 'latest_available_episodes',
            'network_summary': 'network_summary',
            'pid': 'pid',
            'rss_url': 'rss_url',
            'synopses': 'synopses',
            'territory': 'territory',
            'titles': 'titles',
            'total_available_episodes': 'total_available_episodes',
            'type': 'type',
            'updated_at': 'updated_at'
        }

        self._category_summaries = category_summaries
        self._days_available = days_available
        self._entity_type = entity_type
        self._first_published_date = first_published_date
        self._frequency = frequency
        self._images = images
        self._latest_available_episodes = latest_available_episodes
        self._network_summary = network_summary
        self._pid = pid
        self._rss_url = rss_url
        self._synopses = synopses
        self._territory = territory
        self._titles = titles
        self._total_available_episodes = total_available_episodes
        self._type = type
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Podcast':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Podcast of this Podcast.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category_summaries(self):
        """Gets the category_summaries of this Podcast.


        :return: The category_summaries of this Podcast.
        :rtype: List[CategorySummary]
        """
        return self._category_summaries

    @category_summaries.setter
    def category_summaries(self, category_summaries):
        """Sets the category_summaries of this Podcast.


        :param category_summaries: The category_summaries of this Podcast.
        :type category_summaries: List[CategorySummary]
        """
        if category_summaries is None:
            raise ValueError("Invalid value for `category_summaries`, must not be `None`")

        self._category_summaries = category_summaries

    @property
    def days_available(self):
        """Gets the days_available of this Podcast.


        :return: The days_available of this Podcast.
        :rtype: int
        """
        return self._days_available

    @days_available.setter
    def days_available(self, days_available):
        """Sets the days_available of this Podcast.


        :param days_available: The days_available of this Podcast.
        :type days_available: int
        """
        if days_available is None:
            raise ValueError("Invalid value for `days_available`, must not be `None`")

        self._days_available = days_available

    @property
    def entity_type(self):
        """Gets the entity_type of this Podcast.


        :return: The entity_type of this Podcast.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Podcast.


        :param entity_type: The entity_type of this Podcast.
        :type entity_type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")

        self._entity_type = entity_type

    @property
    def first_published_date(self):
        """Gets the first_published_date of this Podcast.


        :return: The first_published_date of this Podcast.
        :rtype: str
        """
        return self._first_published_date

    @first_published_date.setter
    def first_published_date(self, first_published_date):
        """Sets the first_published_date of this Podcast.


        :param first_published_date: The first_published_date of this Podcast.
        :type first_published_date: str
        """
        if first_published_date is None:
            raise ValueError("Invalid value for `first_published_date`, must not be `None`")

        self._first_published_date = first_published_date

    @property
    def frequency(self):
        """Gets the frequency of this Podcast.


        :return: The frequency of this Podcast.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this Podcast.


        :param frequency: The frequency of this Podcast.
        :type frequency: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")

        self._frequency = frequency

    @property
    def images(self):
        """Gets the images of this Podcast.


        :return: The images of this Podcast.
        :rtype: List[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Podcast.


        :param images: The images of this Podcast.
        :type images: List[Image]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")

        self._images = images

    @property
    def latest_available_episodes(self):
        """Gets the latest_available_episodes of this Podcast.


        :return: The latest_available_episodes of this Podcast.
        :rtype: List[PodcastEpisodeSummary]
        """
        return self._latest_available_episodes

    @latest_available_episodes.setter
    def latest_available_episodes(self, latest_available_episodes):
        """Sets the latest_available_episodes of this Podcast.


        :param latest_available_episodes: The latest_available_episodes of this Podcast.
        :type latest_available_episodes: List[PodcastEpisodeSummary]
        """
        if latest_available_episodes is None:
            raise ValueError("Invalid value for `latest_available_episodes`, must not be `None`")

        self._latest_available_episodes = latest_available_episodes

    @property
    def network_summary(self):
        """Gets the network_summary of this Podcast.


        :return: The network_summary of this Podcast.
        :rtype: NetworkSummary
        """
        return self._network_summary

    @network_summary.setter
    def network_summary(self, network_summary):
        """Sets the network_summary of this Podcast.


        :param network_summary: The network_summary of this Podcast.
        :type network_summary: NetworkSummary
        """
        if network_summary is None:
            raise ValueError("Invalid value for `network_summary`, must not be `None`")

        self._network_summary = network_summary

    @property
    def pid(self):
        """Gets the pid of this Podcast.


        :return: The pid of this Podcast.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this Podcast.


        :param pid: The pid of this Podcast.
        :type pid: str
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")

        self._pid = pid

    @property
    def rss_url(self):
        """Gets the rss_url of this Podcast.


        :return: The rss_url of this Podcast.
        :rtype: str
        """
        return self._rss_url

    @rss_url.setter
    def rss_url(self, rss_url):
        """Sets the rss_url of this Podcast.


        :param rss_url: The rss_url of this Podcast.
        :type rss_url: str
        """
        if rss_url is None:
            raise ValueError("Invalid value for `rss_url`, must not be `None`")

        self._rss_url = rss_url

    @property
    def synopses(self):
        """Gets the synopses of this Podcast.


        :return: The synopses of this Podcast.
        :rtype: PodcastSynopses
        """
        return self._synopses

    @synopses.setter
    def synopses(self, synopses):
        """Sets the synopses of this Podcast.


        :param synopses: The synopses of this Podcast.
        :type synopses: PodcastSynopses
        """
        if synopses is None:
            raise ValueError("Invalid value for `synopses`, must not be `None`")

        self._synopses = synopses

    @property
    def territory(self):
        """Gets the territory of this Podcast.


        :return: The territory of this Podcast.
        :rtype: str
        """
        return self._territory

    @territory.setter
    def territory(self, territory):
        """Sets the territory of this Podcast.


        :param territory: The territory of this Podcast.
        :type territory: str
        """
        if territory is None:
            raise ValueError("Invalid value for `territory`, must not be `None`")

        self._territory = territory

    @property
    def titles(self):
        """Gets the titles of this Podcast.


        :return: The titles of this Podcast.
        :rtype: ProgrammeTitles
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """Sets the titles of this Podcast.


        :param titles: The titles of this Podcast.
        :type titles: ProgrammeTitles
        """
        if titles is None:
            raise ValueError("Invalid value for `titles`, must not be `None`")

        self._titles = titles

    @property
    def total_available_episodes(self):
        """Gets the total_available_episodes of this Podcast.


        :return: The total_available_episodes of this Podcast.
        :rtype: int
        """
        return self._total_available_episodes

    @total_available_episodes.setter
    def total_available_episodes(self, total_available_episodes):
        """Sets the total_available_episodes of this Podcast.


        :param total_available_episodes: The total_available_episodes of this Podcast.
        :type total_available_episodes: int
        """
        if total_available_episodes is None:
            raise ValueError("Invalid value for `total_available_episodes`, must not be `None`")

        self._total_available_episodes = total_available_episodes

    @property
    def type(self):
        """Gets the type of this Podcast.


        :return: The type of this Podcast.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Podcast.


        :param type: The type of this Podcast.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Podcast.


        :return: The updated_at of this Podcast.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Podcast.


        :param updated_at: The updated_at of this Podcast.
        :type updated_at: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at
