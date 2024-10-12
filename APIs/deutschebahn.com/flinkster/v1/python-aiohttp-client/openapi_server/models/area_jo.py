# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.address_jo import AddressJO
from openapi_server.models.geometry_jo import GeometryJO
from openapi_server.models.link_jo import LinkJO
from openapi_server.models.provider_jo import ProviderJO
from openapi_server import util


class AreaJO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: List[LinkJO]=None, address: AddressJO=None, attributes: Dict[str, object]=None, description: str=None, expand: str=None, geometry: GeometryJO=None, href: str=None, name: str=None, provider: ProviderJO=None, provider_area_id: str=None, provider_network_ids: List[int]=None, type: str=None, uid: str=None):
        """AreaJO - a model defined in OpenAPI

        :param links: The links of this AreaJO.
        :param address: The address of this AreaJO.
        :param attributes: The attributes of this AreaJO.
        :param description: The description of this AreaJO.
        :param expand: The expand of this AreaJO.
        :param geometry: The geometry of this AreaJO.
        :param href: The href of this AreaJO.
        :param name: The name of this AreaJO.
        :param provider: The provider of this AreaJO.
        :param provider_area_id: The provider_area_id of this AreaJO.
        :param provider_network_ids: The provider_network_ids of this AreaJO.
        :param type: The type of this AreaJO.
        :param uid: The uid of this AreaJO.
        """
        self.openapi_types = {
            'links': List[LinkJO],
            'address': AddressJO,
            'attributes': Dict[str, object],
            'description': str,
            'expand': str,
            'geometry': GeometryJO,
            'href': str,
            'name': str,
            'provider': ProviderJO,
            'provider_area_id': str,
            'provider_network_ids': List[int],
            'type': str,
            'uid': str
        }

        self.attribute_map = {
            'links': '_links',
            'address': 'address',
            'attributes': 'attributes',
            'description': 'description',
            'expand': 'expand',
            'geometry': 'geometry',
            'href': 'href',
            'name': 'name',
            'provider': 'provider',
            'provider_area_id': 'providerAreaId',
            'provider_network_ids': 'providerNetworkIds',
            'type': 'type',
            'uid': 'uid'
        }

        self._links = links
        self._address = address
        self._attributes = attributes
        self._description = description
        self._expand = expand
        self._geometry = geometry
        self._href = href
        self._name = name
        self._provider = provider
        self._provider_area_id = provider_area_id
        self._provider_network_ids = provider_network_ids
        self._type = type
        self._uid = uid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AreaJO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AreaJO of this AreaJO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this AreaJO.


        :return: The links of this AreaJO.
        :rtype: List[LinkJO]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AreaJO.


        :param links: The links of this AreaJO.
        :type links: List[LinkJO]
        """

        self._links = links

    @property
    def address(self):
        """Gets the address of this AreaJO.


        :return: The address of this AreaJO.
        :rtype: AddressJO
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AreaJO.


        :param address: The address of this AreaJO.
        :type address: AddressJO
        """

        self._address = address

    @property
    def attributes(self):
        """Gets the attributes of this AreaJO.


        :return: The attributes of this AreaJO.
        :rtype: Dict[str, object]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AreaJO.


        :param attributes: The attributes of this AreaJO.
        :type attributes: Dict[str, object]
        """

        self._attributes = attributes

    @property
    def description(self):
        """Gets the description of this AreaJO.


        :return: The description of this AreaJO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AreaJO.


        :param description: The description of this AreaJO.
        :type description: str
        """

        self._description = description

    @property
    def expand(self):
        """Gets the expand of this AreaJO.


        :return: The expand of this AreaJO.
        :rtype: str
        """
        return self._expand

    @expand.setter
    def expand(self, expand):
        """Sets the expand of this AreaJO.


        :param expand: The expand of this AreaJO.
        :type expand: str
        """

        self._expand = expand

    @property
    def geometry(self):
        """Gets the geometry of this AreaJO.


        :return: The geometry of this AreaJO.
        :rtype: GeometryJO
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this AreaJO.


        :param geometry: The geometry of this AreaJO.
        :type geometry: GeometryJO
        """

        self._geometry = geometry

    @property
    def href(self):
        """Gets the href of this AreaJO.


        :return: The href of this AreaJO.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AreaJO.


        :param href: The href of this AreaJO.
        :type href: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this AreaJO.


        :return: The name of this AreaJO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AreaJO.


        :param name: The name of this AreaJO.
        :type name: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this AreaJO.


        :return: The provider of this AreaJO.
        :rtype: ProviderJO
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AreaJO.


        :param provider: The provider of this AreaJO.
        :type provider: ProviderJO
        """

        self._provider = provider

    @property
    def provider_area_id(self):
        """Gets the provider_area_id of this AreaJO.


        :return: The provider_area_id of this AreaJO.
        :rtype: str
        """
        return self._provider_area_id

    @provider_area_id.setter
    def provider_area_id(self, provider_area_id):
        """Sets the provider_area_id of this AreaJO.


        :param provider_area_id: The provider_area_id of this AreaJO.
        :type provider_area_id: str
        """

        self._provider_area_id = provider_area_id

    @property
    def provider_network_ids(self):
        """Gets the provider_network_ids of this AreaJO.


        :return: The provider_network_ids of this AreaJO.
        :rtype: List[int]
        """
        return self._provider_network_ids

    @provider_network_ids.setter
    def provider_network_ids(self, provider_network_ids):
        """Sets the provider_network_ids of this AreaJO.


        :param provider_network_ids: The provider_network_ids of this AreaJO.
        :type provider_network_ids: List[int]
        """

        self._provider_network_ids = provider_network_ids

    @property
    def type(self):
        """Gets the type of this AreaJO.


        :return: The type of this AreaJO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AreaJO.


        :param type: The type of this AreaJO.
        :type type: str
        """
        allowed_values = ["STATION", "OPERATIONAREA", "PARKINGAREA", "GASSTATION", "UNKNOWN"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this AreaJO.


        :return: The uid of this AreaJO.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AreaJO.


        :param uid: The uid of this AreaJO.
        :type uid: str
        """

        self._uid = uid
