# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Document(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_element_blob_url: str=None, blob_location: str=None, changed_base_element_blob_url: str=None, document_type_id: int=None, filename: str=None, id: str=None, name: str=None, owner_guid: str=None, package_uri: str=None, story_id: str=None, table_styles_xml_blob_url: str=None, title: str=None):
        """Document - a model defined in OpenAPI

        :param base_element_blob_url: The base_element_blob_url of this Document.
        :param blob_location: The blob_location of this Document.
        :param changed_base_element_blob_url: The changed_base_element_blob_url of this Document.
        :param document_type_id: The document_type_id of this Document.
        :param filename: The filename of this Document.
        :param id: The id of this Document.
        :param name: The name of this Document.
        :param owner_guid: The owner_guid of this Document.
        :param package_uri: The package_uri of this Document.
        :param story_id: The story_id of this Document.
        :param table_styles_xml_blob_url: The table_styles_xml_blob_url of this Document.
        :param title: The title of this Document.
        """
        self.openapi_types = {
            'base_element_blob_url': str,
            'blob_location': str,
            'changed_base_element_blob_url': str,
            'document_type_id': int,
            'filename': str,
            'id': str,
            'name': str,
            'owner_guid': str,
            'package_uri': str,
            'story_id': str,
            'table_styles_xml_blob_url': str,
            'title': str
        }

        self.attribute_map = {
            'base_element_blob_url': 'baseElementBlobUrl',
            'blob_location': 'blobLocation',
            'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
            'document_type_id': 'documentTypeId',
            'filename': 'filename',
            'id': 'id',
            'name': 'name',
            'owner_guid': 'ownerGuid',
            'package_uri': 'packageUri',
            'story_id': 'storyId',
            'table_styles_xml_blob_url': 'tableStylesXmlBlobUrl',
            'title': 'title'
        }

        self._base_element_blob_url = base_element_blob_url
        self._blob_location = blob_location
        self._changed_base_element_blob_url = changed_base_element_blob_url
        self._document_type_id = document_type_id
        self._filename = filename
        self._id = id
        self._name = name
        self._owner_guid = owner_guid
        self._package_uri = package_uri
        self._story_id = story_id
        self._table_styles_xml_blob_url = table_styles_xml_blob_url
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Document':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Document of this Document.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this Document.


        :return: The base_element_blob_url of this Document.
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this Document.


        :param base_element_blob_url: The base_element_blob_url of this Document.
        :type base_element_blob_url: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def blob_location(self):
        """Gets the blob_location of this Document.


        :return: The blob_location of this Document.
        :rtype: str
        """
        return self._blob_location

    @blob_location.setter
    def blob_location(self, blob_location):
        """Sets the blob_location of this Document.


        :param blob_location: The blob_location of this Document.
        :type blob_location: str
        """

        self._blob_location = blob_location

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this Document.


        :return: The changed_base_element_blob_url of this Document.
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this Document.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this Document.
        :type changed_base_element_blob_url: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def document_type_id(self):
        """Gets the document_type_id of this Document.


        :return: The document_type_id of this Document.
        :rtype: int
        """
        return self._document_type_id

    @document_type_id.setter
    def document_type_id(self, document_type_id):
        """Sets the document_type_id of this Document.


        :param document_type_id: The document_type_id of this Document.
        :type document_type_id: int
        """

        self._document_type_id = document_type_id

    @property
    def filename(self):
        """Gets the filename of this Document.


        :return: The filename of this Document.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Document.


        :param filename: The filename of this Document.
        :type filename: str
        """

        self._filename = filename

    @property
    def id(self):
        """Gets the id of this Document.


        :return: The id of this Document.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Document.


        :param id: The id of this Document.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Document.


        :return: The name of this Document.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Document.


        :param name: The name of this Document.
        :type name: str
        """

        self._name = name

    @property
    def owner_guid(self):
        """Gets the owner_guid of this Document.


        :return: The owner_guid of this Document.
        :rtype: str
        """
        return self._owner_guid

    @owner_guid.setter
    def owner_guid(self, owner_guid):
        """Sets the owner_guid of this Document.


        :param owner_guid: The owner_guid of this Document.
        :type owner_guid: str
        """

        self._owner_guid = owner_guid

    @property
    def package_uri(self):
        """Gets the package_uri of this Document.


        :return: The package_uri of this Document.
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this Document.


        :param package_uri: The package_uri of this Document.
        :type package_uri: str
        """

        self._package_uri = package_uri

    @property
    def story_id(self):
        """Gets the story_id of this Document.


        :return: The story_id of this Document.
        :rtype: str
        """
        return self._story_id

    @story_id.setter
    def story_id(self, story_id):
        """Sets the story_id of this Document.


        :param story_id: The story_id of this Document.
        :type story_id: str
        """

        self._story_id = story_id

    @property
    def table_styles_xml_blob_url(self):
        """Gets the table_styles_xml_blob_url of this Document.


        :return: The table_styles_xml_blob_url of this Document.
        :rtype: str
        """
        return self._table_styles_xml_blob_url

    @table_styles_xml_blob_url.setter
    def table_styles_xml_blob_url(self, table_styles_xml_blob_url):
        """Sets the table_styles_xml_blob_url of this Document.


        :param table_styles_xml_blob_url: The table_styles_xml_blob_url of this Document.
        :type table_styles_xml_blob_url: str
        """

        self._table_styles_xml_blob_url = table_styles_xml_blob_url

    @property
    def title(self):
        """Gets the title of this Document.


        :return: The title of this Document.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Document.


        :param title: The title of this Document.
        :type title: str
        """

        self._title = title
