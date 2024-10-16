# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SupplierWorkgroupBasicVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bu_supplier_workgroup_id: int=None, bu_supplier_workgroup_name: str=None):
        """SupplierWorkgroupBasicVO - a model defined in OpenAPI

        :param bu_supplier_workgroup_id: The bu_supplier_workgroup_id of this SupplierWorkgroupBasicVO.
        :param bu_supplier_workgroup_name: The bu_supplier_workgroup_name of this SupplierWorkgroupBasicVO.
        """
        self.openapi_types = {
            'bu_supplier_workgroup_id': int,
            'bu_supplier_workgroup_name': str
        }

        self.attribute_map = {
            'bu_supplier_workgroup_id': 'bu_supplier_workgroup_id',
            'bu_supplier_workgroup_name': 'bu_supplier_workgroup_name'
        }

        self._bu_supplier_workgroup_id = bu_supplier_workgroup_id
        self._bu_supplier_workgroup_name = bu_supplier_workgroup_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SupplierWorkgroupBasicVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SupplierWorkgroupBasicVO of this SupplierWorkgroupBasicVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bu_supplier_workgroup_id(self):
        """Gets the bu_supplier_workgroup_id of this SupplierWorkgroupBasicVO.

        

        :return: The bu_supplier_workgroup_id of this SupplierWorkgroupBasicVO.
        :rtype: int
        """
        return self._bu_supplier_workgroup_id

    @bu_supplier_workgroup_id.setter
    def bu_supplier_workgroup_id(self, bu_supplier_workgroup_id):
        """Sets the bu_supplier_workgroup_id of this SupplierWorkgroupBasicVO.

        

        :param bu_supplier_workgroup_id: The bu_supplier_workgroup_id of this SupplierWorkgroupBasicVO.
        :type bu_supplier_workgroup_id: int
        """

        self._bu_supplier_workgroup_id = bu_supplier_workgroup_id

    @property
    def bu_supplier_workgroup_name(self):
        """Gets the bu_supplier_workgroup_name of this SupplierWorkgroupBasicVO.

        

        :return: The bu_supplier_workgroup_name of this SupplierWorkgroupBasicVO.
        :rtype: str
        """
        return self._bu_supplier_workgroup_name

    @bu_supplier_workgroup_name.setter
    def bu_supplier_workgroup_name(self, bu_supplier_workgroup_name):
        """Sets the bu_supplier_workgroup_name of this SupplierWorkgroupBasicVO.

        

        :param bu_supplier_workgroup_name: The bu_supplier_workgroup_name of this SupplierWorkgroupBasicVO.
        :type bu_supplier_workgroup_name: str
        """

        self._bu_supplier_workgroup_name = bu_supplier_workgroup_name
