# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.pdf_metadata_dto import PdfMetadataDto
from openapi_server import util


class FoTransformRequestDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fo_document_base64_string: str=None, metadata: PdfMetadataDto=None, resources: Dict[str, str]=None, xml_data_document_base64_string: str=None):
        """FoTransformRequestDto - a model defined in OpenAPI

        :param fo_document_base64_string: The fo_document_base64_string of this FoTransformRequestDto.
        :param metadata: The metadata of this FoTransformRequestDto.
        :param resources: The resources of this FoTransformRequestDto.
        :param xml_data_document_base64_string: The xml_data_document_base64_string of this FoTransformRequestDto.
        """
        self.openapi_types = {
            'fo_document_base64_string': str,
            'metadata': PdfMetadataDto,
            'resources': Dict[str, str],
            'xml_data_document_base64_string': str
        }

        self.attribute_map = {
            'fo_document_base64_string': 'foDocumentBase64String',
            'metadata': 'metadata',
            'resources': 'resources',
            'xml_data_document_base64_string': 'xmlDataDocumentBase64String'
        }

        self._fo_document_base64_string = fo_document_base64_string
        self._metadata = metadata
        self._resources = resources
        self._xml_data_document_base64_string = xml_data_document_base64_string

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FoTransformRequestDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FoTransformRequestDto of this FoTransformRequestDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fo_document_base64_string(self):
        """Gets the fo_document_base64_string of this FoTransformRequestDto.

        This is the complete XSL-FO document provided using Base64 encoding.

        :return: The fo_document_base64_string of this FoTransformRequestDto.
        :rtype: str
        """
        return self._fo_document_base64_string

    @fo_document_base64_string.setter
    def fo_document_base64_string(self, fo_document_base64_string):
        """Sets the fo_document_base64_string of this FoTransformRequestDto.

        This is the complete XSL-FO document provided using Base64 encoding.

        :param fo_document_base64_string: The fo_document_base64_string of this FoTransformRequestDto.
        :type fo_document_base64_string: str
        """

        self._fo_document_base64_string = fo_document_base64_string

    @property
    def metadata(self):
        """Gets the metadata of this FoTransformRequestDto.


        :return: The metadata of this FoTransformRequestDto.
        :rtype: PdfMetadataDto
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FoTransformRequestDto.


        :param metadata: The metadata of this FoTransformRequestDto.
        :type metadata: PdfMetadataDto
        """

        self._metadata = metadata

    @property
    def resources(self):
        """Gets the resources of this FoTransformRequestDto.

        This is a set of key-value pairs of digital resources like images that is referenced in the XSL-FO document. It uses the filename as key and the data is provided as a Base64 encoded string.

        :return: The resources of this FoTransformRequestDto.
        :rtype: Dict[str, str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this FoTransformRequestDto.

        This is a set of key-value pairs of digital resources like images that is referenced in the XSL-FO document. It uses the filename as key and the data is provided as a Base64 encoded string.

        :param resources: The resources of this FoTransformRequestDto.
        :type resources: Dict[str, str]
        """

        self._resources = resources

    @property
    def xml_data_document_base64_string(self):
        """Gets the xml_data_document_base64_string of this FoTransformRequestDto.

        This is xml data document on which the XSL-FO transform document is applied. Provided using Base64 encoding.

        :return: The xml_data_document_base64_string of this FoTransformRequestDto.
        :rtype: str
        """
        return self._xml_data_document_base64_string

    @xml_data_document_base64_string.setter
    def xml_data_document_base64_string(self, xml_data_document_base64_string):
        """Sets the xml_data_document_base64_string of this FoTransformRequestDto.

        This is xml data document on which the XSL-FO transform document is applied. Provided using Base64 encoding.

        :param xml_data_document_base64_string: The xml_data_document_base64_string of this FoTransformRequestDto.
        :type xml_data_document_base64_string: str
        """

        self._xml_data_document_base64_string = xml_data_document_base64_string
