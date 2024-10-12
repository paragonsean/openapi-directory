# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.care_context import CareContext
from openapi_server import util


class PatientLinkReferenceRequestPatient(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, care_contexts: List[CareContext]=None, id: str=None, reference_number: str=None):
        """PatientLinkReferenceRequestPatient - a model defined in OpenAPI

        :param care_contexts: The care_contexts of this PatientLinkReferenceRequestPatient.
        :param id: The id of this PatientLinkReferenceRequestPatient.
        :param reference_number: The reference_number of this PatientLinkReferenceRequestPatient.
        """
        self.openapi_types = {
            'care_contexts': List[CareContext],
            'id': str,
            'reference_number': str
        }

        self.attribute_map = {
            'care_contexts': 'careContexts',
            'id': 'id',
            'reference_number': 'referenceNumber'
        }

        self._care_contexts = care_contexts
        self._id = id
        self._reference_number = reference_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientLinkReferenceRequestPatient':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientLinkReferenceRequest_patient of this PatientLinkReferenceRequestPatient.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def care_contexts(self):
        """Gets the care_contexts of this PatientLinkReferenceRequestPatient.


        :return: The care_contexts of this PatientLinkReferenceRequestPatient.
        :rtype: List[CareContext]
        """
        return self._care_contexts

    @care_contexts.setter
    def care_contexts(self, care_contexts):
        """Sets the care_contexts of this PatientLinkReferenceRequestPatient.


        :param care_contexts: The care_contexts of this PatientLinkReferenceRequestPatient.
        :type care_contexts: List[CareContext]
        """
        if care_contexts is None:
            raise ValueError("Invalid value for `care_contexts`, must not be `None`")

        self._care_contexts = care_contexts

    @property
    def id(self):
        """Gets the id of this PatientLinkReferenceRequestPatient.


        :return: The id of this PatientLinkReferenceRequestPatient.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatientLinkReferenceRequestPatient.


        :param id: The id of this PatientLinkReferenceRequestPatient.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def reference_number(self):
        """Gets the reference_number of this PatientLinkReferenceRequestPatient.


        :return: The reference_number of this PatientLinkReferenceRequestPatient.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this PatientLinkReferenceRequestPatient.


        :param reference_number: The reference_number of this PatientLinkReferenceRequestPatient.
        :type reference_number: str
        """
        if reference_number is None:
            raise ValueError("Invalid value for `reference_number`, must not be `None`")

        self._reference_number = reference_number
