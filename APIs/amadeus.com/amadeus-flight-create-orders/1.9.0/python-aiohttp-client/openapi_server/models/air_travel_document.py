# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AirTravelDocument(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, document_number: str=None, document_status: str=None, document_type: str=None, segment_ids: List[str]=None, traveler_id: str=None):
        """AirTravelDocument - a model defined in OpenAPI

        :param document_number: The document_number of this AirTravelDocument.
        :param document_status: The document_status of this AirTravelDocument.
        :param document_type: The document_type of this AirTravelDocument.
        :param segment_ids: The segment_ids of this AirTravelDocument.
        :param traveler_id: The traveler_id of this AirTravelDocument.
        """
        self.openapi_types = {
            'document_number': str,
            'document_status': str,
            'document_type': str,
            'segment_ids': List[str],
            'traveler_id': str
        }

        self.attribute_map = {
            'document_number': 'documentNumber',
            'document_status': 'documentStatus',
            'document_type': 'documentType',
            'segment_ids': 'segmentIds',
            'traveler_id': 'travelerId'
        }

        self._document_number = document_number
        self._document_status = document_status
        self._document_type = document_type
        self._segment_ids = segment_ids
        self._traveler_id = traveler_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AirTravelDocument':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AirTravelDocument of this AirTravelDocument.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def document_number(self):
        """Gets the document_number of this AirTravelDocument.

        Identifier of the travel document prefixed by its owner code [NALC - 3 digits]. Can either be a primary or a conjunctive document number. Necessary for TicketingReference definition.

        :return: The document_number of this AirTravelDocument.
        :rtype: str
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this AirTravelDocument.

        Identifier of the travel document prefixed by its owner code [NALC - 3 digits]. Can either be a primary or a conjunctive document number. Necessary for TicketingReference definition.

        :param document_number: The document_number of this AirTravelDocument.
        :type document_number: str
        """

        self._document_number = document_number

    @property
    def document_status(self):
        """Gets the document_status of this AirTravelDocument.

        Status of the travel document contained in the fare element

        :return: The document_status of this AirTravelDocument.
        :rtype: str
        """
        return self._document_status

    @document_status.setter
    def document_status(self, document_status):
        """Sets the document_status of this AirTravelDocument.

        Status of the travel document contained in the fare element

        :param document_status: The document_status of this AirTravelDocument.
        :type document_status: str
        """
        allowed_values = ["ISSUED", "REFUNDED", "VOID", "ORIGINAL", "EXCHANGED"]  # noqa: E501
        if document_status not in allowed_values:
            raise ValueError(
                "Invalid value for `document_status` ({0}), must be one of {1}"
                .format(document_status, allowed_values)
            )

        self._document_status = document_status

    @property
    def document_type(self):
        """Gets the document_type of this AirTravelDocument.

        Type of the travel document

        :return: The document_type of this AirTravelDocument.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this AirTravelDocument.

        Type of the travel document

        :param document_type: The document_type of this AirTravelDocument.
        :type document_type: str
        """
        allowed_values = ["ETICKET", "PTICKET", "EMD", "MCO"]  # noqa: E501
        if document_type not in allowed_values:
            raise ValueError(
                "Invalid value for `document_type` ({0}), must be one of {1}"
                .format(document_type, allowed_values)
            )

        self._document_type = document_type

    @property
    def segment_ids(self):
        """Gets the segment_ids of this AirTravelDocument.

        Ids of the impacted segments

        :return: The segment_ids of this AirTravelDocument.
        :rtype: List[str]
        """
        return self._segment_ids

    @segment_ids.setter
    def segment_ids(self, segment_ids):
        """Sets the segment_ids of this AirTravelDocument.

        Ids of the impacted segments

        :param segment_ids: The segment_ids of this AirTravelDocument.
        :type segment_ids: List[str]
        """

        self._segment_ids = segment_ids

    @property
    def traveler_id(self):
        """Gets the traveler_id of this AirTravelDocument.

        id of the impacted traveler

        :return: The traveler_id of this AirTravelDocument.
        :rtype: str
        """
        return self._traveler_id

    @traveler_id.setter
    def traveler_id(self, traveler_id):
        """Sets the traveler_id of this AirTravelDocument.

        id of the impacted traveler

        :param traveler_id: The traveler_id of this AirTravelDocument.
        :type traveler_id: str
        """

        self._traveler_id = traveler_id
