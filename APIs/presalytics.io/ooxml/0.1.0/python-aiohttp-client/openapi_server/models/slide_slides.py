# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SlideSlides(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_element_blob_url: str=None, changed_base_element_blob_url: str=None, document_id: str=None, id: str=None, name: str=None, number: int=None, ooxml_id: int=None, package_uri: str=None, slide_document_url: str=None, svg_blob_url: str=None):
        """SlideSlides - a model defined in OpenAPI

        :param base_element_blob_url: The base_element_blob_url of this SlideSlides.
        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideSlides.
        :param document_id: The document_id of this SlideSlides.
        :param id: The id of this SlideSlides.
        :param name: The name of this SlideSlides.
        :param number: The number of this SlideSlides.
        :param ooxml_id: The ooxml_id of this SlideSlides.
        :param package_uri: The package_uri of this SlideSlides.
        :param slide_document_url: The slide_document_url of this SlideSlides.
        :param svg_blob_url: The svg_blob_url of this SlideSlides.
        """
        self.openapi_types = {
            'base_element_blob_url': str,
            'changed_base_element_blob_url': str,
            'document_id': str,
            'id': str,
            'name': str,
            'number': int,
            'ooxml_id': int,
            'package_uri': str,
            'slide_document_url': str,
            'svg_blob_url': str
        }

        self.attribute_map = {
            'base_element_blob_url': 'baseElementBlobUrl',
            'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
            'document_id': 'documentId',
            'id': 'id',
            'name': 'name',
            'number': 'number',
            'ooxml_id': 'ooxmlId',
            'package_uri': 'packageUri',
            'slide_document_url': 'slideDocumentUrl',
            'svg_blob_url': 'svgBlobUrl'
        }

        self._base_element_blob_url = base_element_blob_url
        self._changed_base_element_blob_url = changed_base_element_blob_url
        self._document_id = document_id
        self._id = id
        self._name = name
        self._number = number
        self._ooxml_id = ooxml_id
        self._package_uri = package_uri
        self._slide_document_url = slide_document_url
        self._svg_blob_url = svg_blob_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SlideSlides':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Slide.Slides of this SlideSlides.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this SlideSlides.


        :return: The base_element_blob_url of this SlideSlides.
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this SlideSlides.


        :param base_element_blob_url: The base_element_blob_url of this SlideSlides.
        :type base_element_blob_url: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this SlideSlides.


        :return: The changed_base_element_blob_url of this SlideSlides.
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this SlideSlides.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideSlides.
        :type changed_base_element_blob_url: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def document_id(self):
        """Gets the document_id of this SlideSlides.


        :return: The document_id of this SlideSlides.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this SlideSlides.


        :param document_id: The document_id of this SlideSlides.
        :type document_id: str
        """

        self._document_id = document_id

    @property
    def id(self):
        """Gets the id of this SlideSlides.


        :return: The id of this SlideSlides.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideSlides.


        :param id: The id of this SlideSlides.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SlideSlides.


        :return: The name of this SlideSlides.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlideSlides.


        :param name: The name of this SlideSlides.
        :type name: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this SlideSlides.


        :return: The number of this SlideSlides.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SlideSlides.


        :param number: The number of this SlideSlides.
        :type number: int
        """

        self._number = number

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideSlides.


        :return: The ooxml_id of this SlideSlides.
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideSlides.


        :param ooxml_id: The ooxml_id of this SlideSlides.
        :type ooxml_id: int
        """

        self._ooxml_id = ooxml_id

    @property
    def package_uri(self):
        """Gets the package_uri of this SlideSlides.


        :return: The package_uri of this SlideSlides.
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this SlideSlides.


        :param package_uri: The package_uri of this SlideSlides.
        :type package_uri: str
        """

        self._package_uri = package_uri

    @property
    def slide_document_url(self):
        """Gets the slide_document_url of this SlideSlides.


        :return: The slide_document_url of this SlideSlides.
        :rtype: str
        """
        return self._slide_document_url

    @slide_document_url.setter
    def slide_document_url(self, slide_document_url):
        """Sets the slide_document_url of this SlideSlides.


        :param slide_document_url: The slide_document_url of this SlideSlides.
        :type slide_document_url: str
        """

        self._slide_document_url = slide_document_url

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideSlides.


        :return: The svg_blob_url of this SlideSlides.
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideSlides.


        :param svg_blob_url: The svg_blob_url of this SlideSlides.
        :type svg_blob_url: str
        """

        self._svg_blob_url = svg_blob_url
