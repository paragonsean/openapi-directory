# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ReleaseDestinationResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, mandatory_update: bool=None, provisioning_status_url: str=None):
        """ReleaseDestinationResponse - a model defined in OpenAPI

        :param id: The id of this ReleaseDestinationResponse.
        :param mandatory_update: The mandatory_update of this ReleaseDestinationResponse.
        :param provisioning_status_url: The provisioning_status_url of this ReleaseDestinationResponse.
        """
        self.openapi_types = {
            'id': str,
            'mandatory_update': bool,
            'provisioning_status_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'mandatory_update': 'mandatory_update',
            'provisioning_status_url': 'provisioning_status_url'
        }

        self._id = id
        self._mandatory_update = mandatory_update
        self._provisioning_status_url = provisioning_status_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReleaseDestinationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ReleaseDestinationResponse of this ReleaseDestinationResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ReleaseDestinationResponse.

        Unique id for the release destination

        :return: The id of this ReleaseDestinationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReleaseDestinationResponse.

        Unique id for the release destination

        :param id: The id of this ReleaseDestinationResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def mandatory_update(self):
        """Gets the mandatory_update of this ReleaseDestinationResponse.

        Flag to mark the release for the provided destinations as mandatory

        :return: The mandatory_update of this ReleaseDestinationResponse.
        :rtype: bool
        """
        return self._mandatory_update

    @mandatory_update.setter
    def mandatory_update(self, mandatory_update):
        """Sets the mandatory_update of this ReleaseDestinationResponse.

        Flag to mark the release for the provided destinations as mandatory

        :param mandatory_update: The mandatory_update of this ReleaseDestinationResponse.
        :type mandatory_update: bool
        """
        if mandatory_update is None:
            raise ValueError("Invalid value for `mandatory_update`, must not be `None`")

        self._mandatory_update = mandatory_update

    @property
    def provisioning_status_url(self):
        """Gets the provisioning_status_url of this ReleaseDestinationResponse.

        The url to check provisioning status.

        :return: The provisioning_status_url of this ReleaseDestinationResponse.
        :rtype: str
        """
        return self._provisioning_status_url

    @provisioning_status_url.setter
    def provisioning_status_url(self, provisioning_status_url):
        """Sets the provisioning_status_url of this ReleaseDestinationResponse.

        The url to check provisioning status.

        :param provisioning_status_url: The provisioning_status_url of this ReleaseDestinationResponse.
        :type provisioning_status_url: str
        """

        self._provisioning_status_url = provisioning_status_url
