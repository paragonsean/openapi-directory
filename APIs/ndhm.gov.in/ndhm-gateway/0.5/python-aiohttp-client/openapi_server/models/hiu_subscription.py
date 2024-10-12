# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.consent_manager_patient_id import ConsentManagerPatientID
from openapi_server.models.hiu_subscription_context import HIUSubscriptionContext
from openapi_server.models.organization_representation import OrganizationRepresentation
from openapi_server import util


class HIUSubscription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hiu: OrganizationRepresentation=None, id: str=None, patient: ConsentManagerPatientID=None, sources: List[HIUSubscriptionContext]=None):
        """HIUSubscription - a model defined in OpenAPI

        :param hiu: The hiu of this HIUSubscription.
        :param id: The id of this HIUSubscription.
        :param patient: The patient of this HIUSubscription.
        :param sources: The sources of this HIUSubscription.
        """
        self.openapi_types = {
            'hiu': OrganizationRepresentation,
            'id': str,
            'patient': ConsentManagerPatientID,
            'sources': List[HIUSubscriptionContext]
        }

        self.attribute_map = {
            'hiu': 'hiu',
            'id': 'id',
            'patient': 'patient',
            'sources': 'sources'
        }

        self._hiu = hiu
        self._id = id
        self._patient = patient
        self._sources = sources

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HIUSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HIUSubscription of this HIUSubscription.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hiu(self):
        """Gets the hiu of this HIUSubscription.


        :return: The hiu of this HIUSubscription.
        :rtype: OrganizationRepresentation
        """
        return self._hiu

    @hiu.setter
    def hiu(self, hiu):
        """Sets the hiu of this HIUSubscription.


        :param hiu: The hiu of this HIUSubscription.
        :type hiu: OrganizationRepresentation
        """
        if hiu is None:
            raise ValueError("Invalid value for `hiu`, must not be `None`")

        self._hiu = hiu

    @property
    def id(self):
        """Gets the id of this HIUSubscription.


        :return: The id of this HIUSubscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HIUSubscription.


        :param id: The id of this HIUSubscription.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def patient(self):
        """Gets the patient of this HIUSubscription.


        :return: The patient of this HIUSubscription.
        :rtype: ConsentManagerPatientID
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this HIUSubscription.


        :param patient: The patient of this HIUSubscription.
        :type patient: ConsentManagerPatientID
        """
        if patient is None:
            raise ValueError("Invalid value for `patient`, must not be `None`")

        self._patient = patient

    @property
    def sources(self):
        """Gets the sources of this HIUSubscription.


        :return: The sources of this HIUSubscription.
        :rtype: List[HIUSubscriptionContext]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this HIUSubscription.


        :param sources: The sources of this HIUSubscription.
        :type sources: List[HIUSubscriptionContext]
        """
        if sources is None:
            raise ValueError("Invalid value for `sources`, must not be `None`")

        self._sources = sources
