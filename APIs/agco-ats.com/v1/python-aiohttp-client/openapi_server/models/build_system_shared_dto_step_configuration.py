# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildSystemSharedDTOStepConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, configurations: List[str]=None, step_implementation_id: str=None):
        """BuildSystemSharedDTOStepConfiguration - a model defined in OpenAPI

        :param configurations: The configurations of this BuildSystemSharedDTOStepConfiguration.
        :param step_implementation_id: The step_implementation_id of this BuildSystemSharedDTOStepConfiguration.
        """
        self.openapi_types = {
            'configurations': List[str],
            'step_implementation_id': str
        }

        self.attribute_map = {
            'configurations': 'Configurations',
            'step_implementation_id': 'StepImplementationID'
        }

        self._configurations = configurations
        self._step_implementation_id = step_implementation_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildSystemSharedDTOStepConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BuildSystem.Shared.DTO.StepConfiguration of this BuildSystemSharedDTOStepConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def configurations(self):
        """Gets the configurations of this BuildSystemSharedDTOStepConfiguration.

        The configuration names supported.  The configurations collection is empty for steps which do not require configuration.

        :return: The configurations of this BuildSystemSharedDTOStepConfiguration.
        :rtype: List[str]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this BuildSystemSharedDTOStepConfiguration.

        The configuration names supported.  The configurations collection is empty for steps which do not require configuration.

        :param configurations: The configurations of this BuildSystemSharedDTOStepConfiguration.
        :type configurations: List[str]
        """

        self._configurations = configurations

    @property
    def step_implementation_id(self):
        """Gets the step_implementation_id of this BuildSystemSharedDTOStepConfiguration.

        The Implementation ID of the step this configuration is for

        :return: The step_implementation_id of this BuildSystemSharedDTOStepConfiguration.
        :rtype: str
        """
        return self._step_implementation_id

    @step_implementation_id.setter
    def step_implementation_id(self, step_implementation_id):
        """Sets the step_implementation_id of this BuildSystemSharedDTOStepConfiguration.

        The Implementation ID of the step this configuration is for

        :param step_implementation_id: The step_implementation_id of this BuildSystemSharedDTOStepConfiguration.
        :type step_implementation_id: str
        """
        if step_implementation_id is None:
            raise ValueError("Invalid value for `step_implementation_id`, must not be `None`")

        self._step_implementation_id = step_implementation_id
