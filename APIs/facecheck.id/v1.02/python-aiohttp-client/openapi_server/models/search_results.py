# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.search_item import SearchItem
from openapi_server import util


class SearchResults(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, demo: bool=None, face_per_sec: int=None, free_ram: float=None, images_in_bundle: int=None, items: List[SearchItem]=None, max_score: int=None, performance: str=None, scaned_till_index: int=None, searched_faces: int=None, took_seconds: float=None, took_seconds_download: float=None, took_seconds_queue: float=None):
        """SearchResults - a model defined in OpenAPI

        :param demo: The demo of this SearchResults.
        :param face_per_sec: The face_per_sec of this SearchResults.
        :param free_ram: The free_ram of this SearchResults.
        :param images_in_bundle: The images_in_bundle of this SearchResults.
        :param items: The items of this SearchResults.
        :param max_score: The max_score of this SearchResults.
        :param performance: The performance of this SearchResults.
        :param scaned_till_index: The scaned_till_index of this SearchResults.
        :param searched_faces: The searched_faces of this SearchResults.
        :param took_seconds: The took_seconds of this SearchResults.
        :param took_seconds_download: The took_seconds_download of this SearchResults.
        :param took_seconds_queue: The took_seconds_queue of this SearchResults.
        """
        self.openapi_types = {
            'demo': bool,
            'face_per_sec': int,
            'free_ram': float,
            'images_in_bundle': int,
            'items': List[SearchItem],
            'max_score': int,
            'performance': str,
            'scaned_till_index': int,
            'searched_faces': int,
            'took_seconds': float,
            'took_seconds_download': float,
            'took_seconds_queue': float
        }

        self.attribute_map = {
            'demo': 'demo',
            'face_per_sec': 'face_per_sec',
            'free_ram': 'freeRam',
            'images_in_bundle': 'images_in_bundle',
            'items': 'items',
            'max_score': 'max_score',
            'performance': 'performance',
            'scaned_till_index': 'scaned_till_index',
            'searched_faces': 'searchedFaces',
            'took_seconds': 'tookSeconds',
            'took_seconds_download': 'tookSecondsDownload',
            'took_seconds_queue': 'tookSecondsQueue'
        }

        self._demo = demo
        self._face_per_sec = face_per_sec
        self._free_ram = free_ram
        self._images_in_bundle = images_in_bundle
        self._items = items
        self._max_score = max_score
        self._performance = performance
        self._scaned_till_index = scaned_till_index
        self._searched_faces = searched_faces
        self._took_seconds = took_seconds
        self._took_seconds_download = took_seconds_download
        self._took_seconds_queue = took_seconds_queue

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SearchResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Search_Results of this SearchResults.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def demo(self):
        """Gets the demo of this SearchResults.


        :return: The demo of this SearchResults.
        :rtype: bool
        """
        return self._demo

    @demo.setter
    def demo(self, demo):
        """Sets the demo of this SearchResults.


        :param demo: The demo of this SearchResults.
        :type demo: bool
        """

        self._demo = demo

    @property
    def face_per_sec(self):
        """Gets the face_per_sec of this SearchResults.


        :return: The face_per_sec of this SearchResults.
        :rtype: int
        """
        return self._face_per_sec

    @face_per_sec.setter
    def face_per_sec(self, face_per_sec):
        """Sets the face_per_sec of this SearchResults.


        :param face_per_sec: The face_per_sec of this SearchResults.
        :type face_per_sec: int
        """

        self._face_per_sec = face_per_sec

    @property
    def free_ram(self):
        """Gets the free_ram of this SearchResults.


        :return: The free_ram of this SearchResults.
        :rtype: float
        """
        return self._free_ram

    @free_ram.setter
    def free_ram(self, free_ram):
        """Sets the free_ram of this SearchResults.


        :param free_ram: The free_ram of this SearchResults.
        :type free_ram: float
        """

        self._free_ram = free_ram

    @property
    def images_in_bundle(self):
        """Gets the images_in_bundle of this SearchResults.


        :return: The images_in_bundle of this SearchResults.
        :rtype: int
        """
        return self._images_in_bundle

    @images_in_bundle.setter
    def images_in_bundle(self, images_in_bundle):
        """Sets the images_in_bundle of this SearchResults.


        :param images_in_bundle: The images_in_bundle of this SearchResults.
        :type images_in_bundle: int
        """

        self._images_in_bundle = images_in_bundle

    @property
    def items(self):
        """Gets the items of this SearchResults.


        :return: The items of this SearchResults.
        :rtype: List[SearchItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SearchResults.


        :param items: The items of this SearchResults.
        :type items: List[SearchItem]
        """

        self._items = items

    @property
    def max_score(self):
        """Gets the max_score of this SearchResults.


        :return: The max_score of this SearchResults.
        :rtype: int
        """
        return self._max_score

    @max_score.setter
    def max_score(self, max_score):
        """Sets the max_score of this SearchResults.


        :param max_score: The max_score of this SearchResults.
        :type max_score: int
        """

        self._max_score = max_score

    @property
    def performance(self):
        """Gets the performance of this SearchResults.


        :return: The performance of this SearchResults.
        :rtype: str
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this SearchResults.


        :param performance: The performance of this SearchResults.
        :type performance: str
        """

        self._performance = performance

    @property
    def scaned_till_index(self):
        """Gets the scaned_till_index of this SearchResults.


        :return: The scaned_till_index of this SearchResults.
        :rtype: int
        """
        return self._scaned_till_index

    @scaned_till_index.setter
    def scaned_till_index(self, scaned_till_index):
        """Sets the scaned_till_index of this SearchResults.


        :param scaned_till_index: The scaned_till_index of this SearchResults.
        :type scaned_till_index: int
        """

        self._scaned_till_index = scaned_till_index

    @property
    def searched_faces(self):
        """Gets the searched_faces of this SearchResults.


        :return: The searched_faces of this SearchResults.
        :rtype: int
        """
        return self._searched_faces

    @searched_faces.setter
    def searched_faces(self, searched_faces):
        """Sets the searched_faces of this SearchResults.


        :param searched_faces: The searched_faces of this SearchResults.
        :type searched_faces: int
        """

        self._searched_faces = searched_faces

    @property
    def took_seconds(self):
        """Gets the took_seconds of this SearchResults.


        :return: The took_seconds of this SearchResults.
        :rtype: float
        """
        return self._took_seconds

    @took_seconds.setter
    def took_seconds(self, took_seconds):
        """Sets the took_seconds of this SearchResults.


        :param took_seconds: The took_seconds of this SearchResults.
        :type took_seconds: float
        """

        self._took_seconds = took_seconds

    @property
    def took_seconds_download(self):
        """Gets the took_seconds_download of this SearchResults.


        :return: The took_seconds_download of this SearchResults.
        :rtype: float
        """
        return self._took_seconds_download

    @took_seconds_download.setter
    def took_seconds_download(self, took_seconds_download):
        """Sets the took_seconds_download of this SearchResults.


        :param took_seconds_download: The took_seconds_download of this SearchResults.
        :type took_seconds_download: float
        """

        self._took_seconds_download = took_seconds_download

    @property
    def took_seconds_queue(self):
        """Gets the took_seconds_queue of this SearchResults.


        :return: The took_seconds_queue of this SearchResults.
        :rtype: float
        """
        return self._took_seconds_queue

    @took_seconds_queue.setter
    def took_seconds_queue(self, took_seconds_queue):
        """Sets the took_seconds_queue of this SearchResults.


        :param took_seconds_queue: The took_seconds_queue of this SearchResults.
        :type took_seconds_queue: float
        """

        self._took_seconds_queue = took_seconds_queue
