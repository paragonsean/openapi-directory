# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PodcastMinimumRss(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, image: str=None, listennotes_url: str=None, publisher: str=None, rss: str=None, thumbnail: str=None, title: str=None):
        """PodcastMinimumRss - a model defined in OpenAPI

        :param id: The id of this PodcastMinimumRss.
        :param image: The image of this PodcastMinimumRss.
        :param listennotes_url: The listennotes_url of this PodcastMinimumRss.
        :param publisher: The publisher of this PodcastMinimumRss.
        :param rss: The rss of this PodcastMinimumRss.
        :param thumbnail: The thumbnail of this PodcastMinimumRss.
        :param title: The title of this PodcastMinimumRss.
        """
        self.openapi_types = {
            'id': str,
            'image': str,
            'listennotes_url': str,
            'publisher': str,
            'rss': str,
            'thumbnail': str,
            'title': str
        }

        self.attribute_map = {
            'id': 'id',
            'image': 'image',
            'listennotes_url': 'listennotes_url',
            'publisher': 'publisher',
            'rss': 'rss',
            'thumbnail': 'thumbnail',
            'title': 'title'
        }

        self._id = id
        self._image = image
        self._listennotes_url = listennotes_url
        self._publisher = publisher
        self._rss = rss
        self._thumbnail = thumbnail
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PodcastMinimumRss':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PodcastMinimumRss of this PodcastMinimumRss.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PodcastMinimumRss.

        Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`.

        :return: The id of this PodcastMinimumRss.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PodcastMinimumRss.

        Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`.

        :param id: The id of this PodcastMinimumRss.
        :type id: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this PodcastMinimumRss.

        Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's a high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**, low resolution image (300x300). 

        :return: The image of this PodcastMinimumRss.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PodcastMinimumRss.

        Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's a high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**, low resolution image (300x300). 

        :param image: The image of this PodcastMinimumRss.
        :type image: str
        """

        self._image = image

    @property
    def listennotes_url(self):
        """Gets the listennotes_url of this PodcastMinimumRss.

        The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com).

        :return: The listennotes_url of this PodcastMinimumRss.
        :rtype: str
        """
        return self._listennotes_url

    @listennotes_url.setter
    def listennotes_url(self, listennotes_url):
        """Sets the listennotes_url of this PodcastMinimumRss.

        The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com).

        :param listennotes_url: The listennotes_url of this PodcastMinimumRss.
        :type listennotes_url: str
        """

        self._listennotes_url = listennotes_url

    @property
    def publisher(self):
        """Gets the publisher of this PodcastMinimumRss.

        Podcast publisher name.

        :return: The publisher of this PodcastMinimumRss.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this PodcastMinimumRss.

        Podcast publisher name.

        :param publisher: The publisher of this PodcastMinimumRss.
        :type publisher: str
        """

        self._publisher = publisher

    @property
    def rss(self):
        """Gets the rss of this PodcastMinimumRss.

        RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan.

        :return: The rss of this PodcastMinimumRss.
        :rtype: str
        """
        return self._rss

    @rss.setter
    def rss(self, rss):
        """Sets the rss of this PodcastMinimumRss.

        RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan.

        :param rss: The rss of this PodcastMinimumRss.
        :type rss: str
        """

        self._rss = rss

    @property
    def thumbnail(self):
        """Gets the thumbnail of this PodcastMinimumRss.

        Thumbnail image url for this podcast's artwork (300x300).

        :return: The thumbnail of this PodcastMinimumRss.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this PodcastMinimumRss.

        Thumbnail image url for this podcast's artwork (300x300).

        :param thumbnail: The thumbnail of this PodcastMinimumRss.
        :type thumbnail: str
        """

        self._thumbnail = thumbnail

    @property
    def title(self):
        """Gets the title of this PodcastMinimumRss.

        Podcast name.

        :return: The title of this PodcastMinimumRss.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PodcastMinimumRss.

        Podcast name.

        :param title: The title of this PodcastMinimumRss.
        :type title: str
        """

        self._title = title
