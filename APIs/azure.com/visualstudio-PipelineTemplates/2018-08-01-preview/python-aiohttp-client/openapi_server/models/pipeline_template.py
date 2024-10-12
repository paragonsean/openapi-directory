# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.input_descriptor import InputDescriptor
from openapi_server import util


class PipelineTemplate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, id: str=None, inputs: List[InputDescriptor]=None):
        """PipelineTemplate - a model defined in OpenAPI

        :param description: The description of this PipelineTemplate.
        :param id: The id of this PipelineTemplate.
        :param inputs: The inputs of this PipelineTemplate.
        """
        self.openapi_types = {
            'description': str,
            'id': str,
            'inputs': List[InputDescriptor]
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'inputs': 'inputs'
        }

        self._description = description
        self._id = id
        self._inputs = inputs

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PipelineTemplate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PipelineTemplate of this PipelineTemplate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this PipelineTemplate.

        Description of the pipeline which this template enables.

        :return: The description of this PipelineTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineTemplate.

        Description of the pipeline which this template enables.

        :param description: The description of this PipelineTemplate.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this PipelineTemplate.

        Unique id of pipeline template.

        :return: The id of this PipelineTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineTemplate.

        Unique id of pipeline template.

        :param id: The id of this PipelineTemplate.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def inputs(self):
        """Gets the inputs of this PipelineTemplate.

        Inputs required by this template to create pipeline.

        :return: The inputs of this PipelineTemplate.
        :rtype: List[InputDescriptor]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this PipelineTemplate.

        Inputs required by this template to create pipeline.

        :param inputs: The inputs of this PipelineTemplate.
        :type inputs: List[InputDescriptor]
        """

        self._inputs = inputs
