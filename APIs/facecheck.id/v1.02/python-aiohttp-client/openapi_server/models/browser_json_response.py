# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.input_image import InputImage
from openapi_server.models.search_results import SearchResults
from openapi_server import util


class BrowserJsonResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, error: str=None, has_empty_images: bool=None, id_search: str=None, input: List[InputImage]=None, message: str=None, output: SearchResults=None, progress: int=None):
        """BrowserJsonResponse - a model defined in OpenAPI

        :param code: The code of this BrowserJsonResponse.
        :param error: The error of this BrowserJsonResponse.
        :param has_empty_images: The has_empty_images of this BrowserJsonResponse.
        :param id_search: The id_search of this BrowserJsonResponse.
        :param input: The input of this BrowserJsonResponse.
        :param message: The message of this BrowserJsonResponse.
        :param output: The output of this BrowserJsonResponse.
        :param progress: The progress of this BrowserJsonResponse.
        """
        self.openapi_types = {
            'code': str,
            'error': str,
            'has_empty_images': bool,
            'id_search': str,
            'input': List[InputImage],
            'message': str,
            'output': SearchResults,
            'progress': int
        }

        self.attribute_map = {
            'code': 'code',
            'error': 'error',
            'has_empty_images': 'hasEmptyImages',
            'id_search': 'id_search',
            'input': 'input',
            'message': 'message',
            'output': 'output',
            'progress': 'progress'
        }

        self._code = code
        self._error = error
        self._has_empty_images = has_empty_images
        self._id_search = id_search
        self._input = input
        self._message = message
        self._output = output
        self._progress = progress

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BrowserJsonResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BrowserJsonResponse of this BrowserJsonResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this BrowserJsonResponse.


        :return: The code of this BrowserJsonResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BrowserJsonResponse.


        :param code: The code of this BrowserJsonResponse.
        :type code: str
        """

        self._code = code

    @property
    def error(self):
        """Gets the error of this BrowserJsonResponse.


        :return: The error of this BrowserJsonResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this BrowserJsonResponse.


        :param error: The error of this BrowserJsonResponse.
        :type error: str
        """

        self._error = error

    @property
    def has_empty_images(self):
        """Gets the has_empty_images of this BrowserJsonResponse.


        :return: The has_empty_images of this BrowserJsonResponse.
        :rtype: bool
        """
        return self._has_empty_images

    @has_empty_images.setter
    def has_empty_images(self, has_empty_images):
        """Sets the has_empty_images of this BrowserJsonResponse.


        :param has_empty_images: The has_empty_images of this BrowserJsonResponse.
        :type has_empty_images: bool
        """

        self._has_empty_images = has_empty_images

    @property
    def id_search(self):
        """Gets the id_search of this BrowserJsonResponse.


        :return: The id_search of this BrowserJsonResponse.
        :rtype: str
        """
        return self._id_search

    @id_search.setter
    def id_search(self, id_search):
        """Sets the id_search of this BrowserJsonResponse.


        :param id_search: The id_search of this BrowserJsonResponse.
        :type id_search: str
        """

        self._id_search = id_search

    @property
    def input(self):
        """Gets the input of this BrowserJsonResponse.


        :return: The input of this BrowserJsonResponse.
        :rtype: List[InputImage]
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this BrowserJsonResponse.


        :param input: The input of this BrowserJsonResponse.
        :type input: List[InputImage]
        """

        self._input = input

    @property
    def message(self):
        """Gets the message of this BrowserJsonResponse.


        :return: The message of this BrowserJsonResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BrowserJsonResponse.


        :param message: The message of this BrowserJsonResponse.
        :type message: str
        """

        self._message = message

    @property
    def output(self):
        """Gets the output of this BrowserJsonResponse.


        :return: The output of this BrowserJsonResponse.
        :rtype: SearchResults
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this BrowserJsonResponse.


        :param output: The output of this BrowserJsonResponse.
        :type output: SearchResults
        """

        self._output = output

    @property
    def progress(self):
        """Gets the progress of this BrowserJsonResponse.


        :return: The progress of this BrowserJsonResponse.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this BrowserJsonResponse.


        :param progress: The progress of this BrowserJsonResponse.
        :type progress: int
        """

        self._progress = progress
