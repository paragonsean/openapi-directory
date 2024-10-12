# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RequisitionListDataRequisitionListItemInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, added_at: str=None, extension_attributes: object=None, id: int=None, options: List[str]=None, qty: float=None, requisition_list_id: int=None, sku: str=None, store_id: int=None):
        """RequisitionListDataRequisitionListItemInterface - a model defined in OpenAPI

        :param added_at: The added_at of this RequisitionListDataRequisitionListItemInterface.
        :param extension_attributes: The extension_attributes of this RequisitionListDataRequisitionListItemInterface.
        :param id: The id of this RequisitionListDataRequisitionListItemInterface.
        :param options: The options of this RequisitionListDataRequisitionListItemInterface.
        :param qty: The qty of this RequisitionListDataRequisitionListItemInterface.
        :param requisition_list_id: The requisition_list_id of this RequisitionListDataRequisitionListItemInterface.
        :param sku: The sku of this RequisitionListDataRequisitionListItemInterface.
        :param store_id: The store_id of this RequisitionListDataRequisitionListItemInterface.
        """
        self.openapi_types = {
            'added_at': str,
            'extension_attributes': object,
            'id': int,
            'options': List[str],
            'qty': float,
            'requisition_list_id': int,
            'sku': str,
            'store_id': int
        }

        self.attribute_map = {
            'added_at': 'added_at',
            'extension_attributes': 'extension_attributes',
            'id': 'id',
            'options': 'options',
            'qty': 'qty',
            'requisition_list_id': 'requisition_list_id',
            'sku': 'sku',
            'store_id': 'store_id'
        }

        self._added_at = added_at
        self._extension_attributes = extension_attributes
        self._id = id
        self._options = options
        self._qty = qty
        self._requisition_list_id = requisition_list_id
        self._sku = sku
        self._store_id = store_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RequisitionListDataRequisitionListItemInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The requisition-list-data-requisition-list-item-interface of this RequisitionListDataRequisitionListItemInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def added_at(self):
        """Gets the added_at of this RequisitionListDataRequisitionListItemInterface.

        Added_at value.

        :return: The added_at of this RequisitionListDataRequisitionListItemInterface.
        :rtype: str
        """
        return self._added_at

    @added_at.setter
    def added_at(self, added_at):
        """Sets the added_at of this RequisitionListDataRequisitionListItemInterface.

        Added_at value.

        :param added_at: The added_at of this RequisitionListDataRequisitionListItemInterface.
        :type added_at: str
        """
        if added_at is None:
            raise ValueError("Invalid value for `added_at`, must not be `None`")

        self._added_at = added_at

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this RequisitionListDataRequisitionListItemInterface.

        ExtensionInterface class for @see \\Magento\\RequisitionList\\Api\\Data\\RequisitionListItemInterface

        :return: The extension_attributes of this RequisitionListDataRequisitionListItemInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this RequisitionListDataRequisitionListItemInterface.

        ExtensionInterface class for @see \\Magento\\RequisitionList\\Api\\Data\\RequisitionListItemInterface

        :param extension_attributes: The extension_attributes of this RequisitionListDataRequisitionListItemInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def id(self):
        """Gets the id of this RequisitionListDataRequisitionListItemInterface.

        Requisition List ID.

        :return: The id of this RequisitionListDataRequisitionListItemInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RequisitionListDataRequisitionListItemInterface.

        Requisition List ID.

        :param id: The id of this RequisitionListDataRequisitionListItemInterface.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def options(self):
        """Gets the options of this RequisitionListDataRequisitionListItemInterface.

        Requisition list item options.

        :return: The options of this RequisitionListDataRequisitionListItemInterface.
        :rtype: List[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this RequisitionListDataRequisitionListItemInterface.

        Requisition list item options.

        :param options: The options of this RequisitionListDataRequisitionListItemInterface.
        :type options: List[str]
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")

        self._options = options

    @property
    def qty(self):
        """Gets the qty of this RequisitionListDataRequisitionListItemInterface.

        Product Qty.

        :return: The qty of this RequisitionListDataRequisitionListItemInterface.
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this RequisitionListDataRequisitionListItemInterface.

        Product Qty.

        :param qty: The qty of this RequisitionListDataRequisitionListItemInterface.
        :type qty: float
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")

        self._qty = qty

    @property
    def requisition_list_id(self):
        """Gets the requisition_list_id of this RequisitionListDataRequisitionListItemInterface.

        Requisition List ID.

        :return: The requisition_list_id of this RequisitionListDataRequisitionListItemInterface.
        :rtype: int
        """
        return self._requisition_list_id

    @requisition_list_id.setter
    def requisition_list_id(self, requisition_list_id):
        """Sets the requisition_list_id of this RequisitionListDataRequisitionListItemInterface.

        Requisition List ID.

        :param requisition_list_id: The requisition_list_id of this RequisitionListDataRequisitionListItemInterface.
        :type requisition_list_id: int
        """
        if requisition_list_id is None:
            raise ValueError("Invalid value for `requisition_list_id`, must not be `None`")

        self._requisition_list_id = requisition_list_id

    @property
    def sku(self):
        """Gets the sku of this RequisitionListDataRequisitionListItemInterface.

        Product SKU.

        :return: The sku of this RequisitionListDataRequisitionListItemInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this RequisitionListDataRequisitionListItemInterface.

        Product SKU.

        :param sku: The sku of this RequisitionListDataRequisitionListItemInterface.
        :type sku: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def store_id(self):
        """Gets the store_id of this RequisitionListDataRequisitionListItemInterface.

        Store ID.

        :return: The store_id of this RequisitionListDataRequisitionListItemInterface.
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this RequisitionListDataRequisitionListItemInterface.

        Store ID.

        :param store_id: The store_id of this RequisitionListDataRequisitionListItemInterface.
        :type store_id: int
        """
        if store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")

        self._store_id = store_id
