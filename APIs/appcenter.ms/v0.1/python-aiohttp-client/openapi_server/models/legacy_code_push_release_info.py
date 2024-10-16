# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LegacyCodePushReleaseInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_version: str=None, description: str=None, is_disabled: bool=None, is_mandatory: bool=None, rollout: int=None):
        """LegacyCodePushReleaseInfo - a model defined in OpenAPI

        :param app_version: The app_version of this LegacyCodePushReleaseInfo.
        :param description: The description of this LegacyCodePushReleaseInfo.
        :param is_disabled: The is_disabled of this LegacyCodePushReleaseInfo.
        :param is_mandatory: The is_mandatory of this LegacyCodePushReleaseInfo.
        :param rollout: The rollout of this LegacyCodePushReleaseInfo.
        """
        self.openapi_types = {
            'app_version': str,
            'description': str,
            'is_disabled': bool,
            'is_mandatory': bool,
            'rollout': int
        }

        self.attribute_map = {
            'app_version': 'appVersion',
            'description': 'description',
            'is_disabled': 'isDisabled',
            'is_mandatory': 'isMandatory',
            'rollout': 'rollout'
        }

        self._app_version = app_version
        self._description = description
        self._is_disabled = is_disabled
        self._is_mandatory = is_mandatory
        self._rollout = rollout

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LegacyCodePushReleaseInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LegacyCodePushReleaseInfo of this LegacyCodePushReleaseInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_version(self):
        """Gets the app_version of this LegacyCodePushReleaseInfo.


        :return: The app_version of this LegacyCodePushReleaseInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this LegacyCodePushReleaseInfo.


        :param app_version: The app_version of this LegacyCodePushReleaseInfo.
        :type app_version: str
        """

        self._app_version = app_version

    @property
    def description(self):
        """Gets the description of this LegacyCodePushReleaseInfo.


        :return: The description of this LegacyCodePushReleaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LegacyCodePushReleaseInfo.


        :param description: The description of this LegacyCodePushReleaseInfo.
        :type description: str
        """

        self._description = description

    @property
    def is_disabled(self):
        """Gets the is_disabled of this LegacyCodePushReleaseInfo.


        :return: The is_disabled of this LegacyCodePushReleaseInfo.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this LegacyCodePushReleaseInfo.


        :param is_disabled: The is_disabled of this LegacyCodePushReleaseInfo.
        :type is_disabled: bool
        """

        self._is_disabled = is_disabled

    @property
    def is_mandatory(self):
        """Gets the is_mandatory of this LegacyCodePushReleaseInfo.


        :return: The is_mandatory of this LegacyCodePushReleaseInfo.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """Sets the is_mandatory of this LegacyCodePushReleaseInfo.


        :param is_mandatory: The is_mandatory of this LegacyCodePushReleaseInfo.
        :type is_mandatory: bool
        """

        self._is_mandatory = is_mandatory

    @property
    def rollout(self):
        """Gets the rollout of this LegacyCodePushReleaseInfo.


        :return: The rollout of this LegacyCodePushReleaseInfo.
        :rtype: int
        """
        return self._rollout

    @rollout.setter
    def rollout(self, rollout):
        """Sets the rollout of this LegacyCodePushReleaseInfo.


        :param rollout: The rollout of this LegacyCodePushReleaseInfo.
        :type rollout: int
        """

        self._rollout = rollout
