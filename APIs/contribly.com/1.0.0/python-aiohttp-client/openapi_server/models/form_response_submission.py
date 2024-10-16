# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FormResponseSubmission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, contribution: str=None, form: str=None, responses: Dict[str, str]=None):
        """FormResponseSubmission - a model defined in OpenAPI

        :param contribution: The contribution of this FormResponseSubmission.
        :param form: The form of this FormResponseSubmission.
        :param responses: The responses of this FormResponseSubmission.
        """
        self.openapi_types = {
            'contribution': str,
            'form': str,
            'responses': Dict[str, str]
        }

        self.attribute_map = {
            'contribution': 'contribution',
            'form': 'form',
            'responses': 'responses'
        }

        self._contribution = contribution
        self._form = form
        self._responses = responses

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FormResponseSubmission':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FormResponseSubmission of this FormResponseSubmission.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contribution(self):
        """Gets the contribution of this FormResponseSubmission.


        :return: The contribution of this FormResponseSubmission.
        :rtype: str
        """
        return self._contribution

    @contribution.setter
    def contribution(self, contribution):
        """Sets the contribution of this FormResponseSubmission.


        :param contribution: The contribution of this FormResponseSubmission.
        :type contribution: str
        """

        self._contribution = contribution

    @property
    def form(self):
        """Gets the form of this FormResponseSubmission.


        :return: The form of this FormResponseSubmission.
        :rtype: str
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this FormResponseSubmission.


        :param form: The form of this FormResponseSubmission.
        :type form: str
        """

        self._form = form

    @property
    def responses(self):
        """Gets the responses of this FormResponseSubmission.


        :return: The responses of this FormResponseSubmission.
        :rtype: Dict[str, str]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this FormResponseSubmission.


        :param responses: The responses of this FormResponseSubmission.
        :type responses: Dict[str, str]
        """

        self._responses = responses
