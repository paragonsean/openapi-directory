# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.email_history_resource_relationships_receiver import EmailHistoryResourceRelationshipsReceiver
from openapi_server.models.reward_earning_fulfillment_resource_relationships_patient import RewardEarningFulfillmentResourceRelationshipsPatient
from openapi_server import util


class RewardResourceRelationships(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, patient: RewardEarningFulfillmentResourceRelationshipsPatient=None, reward_program_activation: EmailHistoryResourceRelationshipsReceiver=None):
        """RewardResourceRelationships - a model defined in OpenAPI

        :param patient: The patient of this RewardResourceRelationships.
        :param reward_program_activation: The reward_program_activation of this RewardResourceRelationships.
        """
        self.openapi_types = {
            'patient': RewardEarningFulfillmentResourceRelationshipsPatient,
            'reward_program_activation': EmailHistoryResourceRelationshipsReceiver
        }

        self.attribute_map = {
            'patient': 'patient',
            'reward_program_activation': 'reward_program_activation'
        }

        self._patient = patient
        self._reward_program_activation = reward_program_activation

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RewardResourceRelationships':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RewardResource_relationships of this RewardResourceRelationships.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def patient(self):
        """Gets the patient of this RewardResourceRelationships.


        :return: The patient of this RewardResourceRelationships.
        :rtype: RewardEarningFulfillmentResourceRelationshipsPatient
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this RewardResourceRelationships.


        :param patient: The patient of this RewardResourceRelationships.
        :type patient: RewardEarningFulfillmentResourceRelationshipsPatient
        """

        self._patient = patient

    @property
    def reward_program_activation(self):
        """Gets the reward_program_activation of this RewardResourceRelationships.


        :return: The reward_program_activation of this RewardResourceRelationships.
        :rtype: EmailHistoryResourceRelationshipsReceiver
        """
        return self._reward_program_activation

    @reward_program_activation.setter
    def reward_program_activation(self, reward_program_activation):
        """Sets the reward_program_activation of this RewardResourceRelationships.


        :param reward_program_activation: The reward_program_activation of this RewardResourceRelationships.
        :type reward_program_activation: EmailHistoryResourceRelationshipsReceiver
        """
        if reward_program_activation is None:
            raise ValueError("Invalid value for `reward_program_activation`, must not be `None`")

        self._reward_program_activation = reward_program_activation
