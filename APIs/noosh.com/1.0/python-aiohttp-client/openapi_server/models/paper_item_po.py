# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PaperItemPO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, min_uom_qty: int=None, paper_id: int=None, price_1: object=None, price_2: object=None, price_3: object=None, price_4: object=None, price_5: object=None, price_per_tonne: object=None, qty_uom: str=None, quantity_1: int=None, quantity_2: int=None, quantity_3: int=None, quantity_4: int=None, quantity_5: int=None, size: str=None, sku: str=None, unit_price_1: object=None, unit_price_2: object=None, unit_price_3: object=None, unit_price_4: object=None, unit_price_5: object=None):
        """PaperItemPO - a model defined in OpenAPI

        :param min_uom_qty: The min_uom_qty of this PaperItemPO.
        :param paper_id: The paper_id of this PaperItemPO.
        :param price_1: The price_1 of this PaperItemPO.
        :param price_2: The price_2 of this PaperItemPO.
        :param price_3: The price_3 of this PaperItemPO.
        :param price_4: The price_4 of this PaperItemPO.
        :param price_5: The price_5 of this PaperItemPO.
        :param price_per_tonne: The price_per_tonne of this PaperItemPO.
        :param qty_uom: The qty_uom of this PaperItemPO.
        :param quantity_1: The quantity_1 of this PaperItemPO.
        :param quantity_2: The quantity_2 of this PaperItemPO.
        :param quantity_3: The quantity_3 of this PaperItemPO.
        :param quantity_4: The quantity_4 of this PaperItemPO.
        :param quantity_5: The quantity_5 of this PaperItemPO.
        :param size: The size of this PaperItemPO.
        :param sku: The sku of this PaperItemPO.
        :param unit_price_1: The unit_price_1 of this PaperItemPO.
        :param unit_price_2: The unit_price_2 of this PaperItemPO.
        :param unit_price_3: The unit_price_3 of this PaperItemPO.
        :param unit_price_4: The unit_price_4 of this PaperItemPO.
        :param unit_price_5: The unit_price_5 of this PaperItemPO.
        """
        self.openapi_types = {
            'min_uom_qty': int,
            'paper_id': int,
            'price_1': object,
            'price_2': object,
            'price_3': object,
            'price_4': object,
            'price_5': object,
            'price_per_tonne': object,
            'qty_uom': str,
            'quantity_1': int,
            'quantity_2': int,
            'quantity_3': int,
            'quantity_4': int,
            'quantity_5': int,
            'size': str,
            'sku': str,
            'unit_price_1': object,
            'unit_price_2': object,
            'unit_price_3': object,
            'unit_price_4': object,
            'unit_price_5': object
        }

        self.attribute_map = {
            'min_uom_qty': 'min_uom_qty',
            'paper_id': 'paper_id',
            'price_1': 'price_1',
            'price_2': 'price_2',
            'price_3': 'price_3',
            'price_4': 'price_4',
            'price_5': 'price_5',
            'price_per_tonne': 'price_per_tonne',
            'qty_uom': 'qty_uom',
            'quantity_1': 'quantity_1',
            'quantity_2': 'quantity_2',
            'quantity_3': 'quantity_3',
            'quantity_4': 'quantity_4',
            'quantity_5': 'quantity_5',
            'size': 'size',
            'sku': 'sku',
            'unit_price_1': 'unit_price_1',
            'unit_price_2': 'unit_price_2',
            'unit_price_3': 'unit_price_3',
            'unit_price_4': 'unit_price_4',
            'unit_price_5': 'unit_price_5'
        }

        self._min_uom_qty = min_uom_qty
        self._paper_id = paper_id
        self._price_1 = price_1
        self._price_2 = price_2
        self._price_3 = price_3
        self._price_4 = price_4
        self._price_5 = price_5
        self._price_per_tonne = price_per_tonne
        self._qty_uom = qty_uom
        self._quantity_1 = quantity_1
        self._quantity_2 = quantity_2
        self._quantity_3 = quantity_3
        self._quantity_4 = quantity_4
        self._quantity_5 = quantity_5
        self._size = size
        self._sku = sku
        self._unit_price_1 = unit_price_1
        self._unit_price_2 = unit_price_2
        self._unit_price_3 = unit_price_3
        self._unit_price_4 = unit_price_4
        self._unit_price_5 = unit_price_5

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaperItemPO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaperItemPO of this PaperItemPO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_uom_qty(self):
        """Gets the min_uom_qty of this PaperItemPO.

        

        :return: The min_uom_qty of this PaperItemPO.
        :rtype: int
        """
        return self._min_uom_qty

    @min_uom_qty.setter
    def min_uom_qty(self, min_uom_qty):
        """Sets the min_uom_qty of this PaperItemPO.

        

        :param min_uom_qty: The min_uom_qty of this PaperItemPO.
        :type min_uom_qty: int
        """

        self._min_uom_qty = min_uom_qty

    @property
    def paper_id(self):
        """Gets the paper_id of this PaperItemPO.

        

        :return: The paper_id of this PaperItemPO.
        :rtype: int
        """
        return self._paper_id

    @paper_id.setter
    def paper_id(self, paper_id):
        """Sets the paper_id of this PaperItemPO.

        

        :param paper_id: The paper_id of this PaperItemPO.
        :type paper_id: int
        """

        self._paper_id = paper_id

    @property
    def price_1(self):
        """Gets the price_1 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The price_1 of this PaperItemPO.
        :rtype: object
        """
        return self._price_1

    @price_1.setter
    def price_1(self, price_1):
        """Sets the price_1 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param price_1: The price_1 of this PaperItemPO.
        :type price_1: object
        """

        self._price_1 = price_1

    @property
    def price_2(self):
        """Gets the price_2 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The price_2 of this PaperItemPO.
        :rtype: object
        """
        return self._price_2

    @price_2.setter
    def price_2(self, price_2):
        """Sets the price_2 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param price_2: The price_2 of this PaperItemPO.
        :type price_2: object
        """

        self._price_2 = price_2

    @property
    def price_3(self):
        """Gets the price_3 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The price_3 of this PaperItemPO.
        :rtype: object
        """
        return self._price_3

    @price_3.setter
    def price_3(self, price_3):
        """Sets the price_3 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param price_3: The price_3 of this PaperItemPO.
        :type price_3: object
        """

        self._price_3 = price_3

    @property
    def price_4(self):
        """Gets the price_4 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The price_4 of this PaperItemPO.
        :rtype: object
        """
        return self._price_4

    @price_4.setter
    def price_4(self, price_4):
        """Sets the price_4 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param price_4: The price_4 of this PaperItemPO.
        :type price_4: object
        """

        self._price_4 = price_4

    @property
    def price_5(self):
        """Gets the price_5 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The price_5 of this PaperItemPO.
        :rtype: object
        """
        return self._price_5

    @price_5.setter
    def price_5(self, price_5):
        """Sets the price_5 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param price_5: The price_5 of this PaperItemPO.
        :type price_5: object
        """

        self._price_5 = price_5

    @property
    def price_per_tonne(self):
        """Gets the price_per_tonne of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The price_per_tonne of this PaperItemPO.
        :rtype: object
        """
        return self._price_per_tonne

    @price_per_tonne.setter
    def price_per_tonne(self, price_per_tonne):
        """Sets the price_per_tonne of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param price_per_tonne: The price_per_tonne of this PaperItemPO.
        :type price_per_tonne: object
        """

        self._price_per_tonne = price_per_tonne

    @property
    def qty_uom(self):
        """Gets the qty_uom of this PaperItemPO.

        

        :return: The qty_uom of this PaperItemPO.
        :rtype: str
        """
        return self._qty_uom

    @qty_uom.setter
    def qty_uom(self, qty_uom):
        """Sets the qty_uom of this PaperItemPO.

        

        :param qty_uom: The qty_uom of this PaperItemPO.
        :type qty_uom: str
        """

        self._qty_uom = qty_uom

    @property
    def quantity_1(self):
        """Gets the quantity_1 of this PaperItemPO.

        

        :return: The quantity_1 of this PaperItemPO.
        :rtype: int
        """
        return self._quantity_1

    @quantity_1.setter
    def quantity_1(self, quantity_1):
        """Sets the quantity_1 of this PaperItemPO.

        

        :param quantity_1: The quantity_1 of this PaperItemPO.
        :type quantity_1: int
        """

        self._quantity_1 = quantity_1

    @property
    def quantity_2(self):
        """Gets the quantity_2 of this PaperItemPO.

        

        :return: The quantity_2 of this PaperItemPO.
        :rtype: int
        """
        return self._quantity_2

    @quantity_2.setter
    def quantity_2(self, quantity_2):
        """Sets the quantity_2 of this PaperItemPO.

        

        :param quantity_2: The quantity_2 of this PaperItemPO.
        :type quantity_2: int
        """

        self._quantity_2 = quantity_2

    @property
    def quantity_3(self):
        """Gets the quantity_3 of this PaperItemPO.

        

        :return: The quantity_3 of this PaperItemPO.
        :rtype: int
        """
        return self._quantity_3

    @quantity_3.setter
    def quantity_3(self, quantity_3):
        """Sets the quantity_3 of this PaperItemPO.

        

        :param quantity_3: The quantity_3 of this PaperItemPO.
        :type quantity_3: int
        """

        self._quantity_3 = quantity_3

    @property
    def quantity_4(self):
        """Gets the quantity_4 of this PaperItemPO.

        

        :return: The quantity_4 of this PaperItemPO.
        :rtype: int
        """
        return self._quantity_4

    @quantity_4.setter
    def quantity_4(self, quantity_4):
        """Sets the quantity_4 of this PaperItemPO.

        

        :param quantity_4: The quantity_4 of this PaperItemPO.
        :type quantity_4: int
        """

        self._quantity_4 = quantity_4

    @property
    def quantity_5(self):
        """Gets the quantity_5 of this PaperItemPO.

        

        :return: The quantity_5 of this PaperItemPO.
        :rtype: int
        """
        return self._quantity_5

    @quantity_5.setter
    def quantity_5(self, quantity_5):
        """Sets the quantity_5 of this PaperItemPO.

        

        :param quantity_5: The quantity_5 of this PaperItemPO.
        :type quantity_5: int
        """

        self._quantity_5 = quantity_5

    @property
    def size(self):
        """Gets the size of this PaperItemPO.

        

        :return: The size of this PaperItemPO.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PaperItemPO.

        

        :param size: The size of this PaperItemPO.
        :type size: str
        """

        self._size = size

    @property
    def sku(self):
        """Gets the sku of this PaperItemPO.

        

        :return: The sku of this PaperItemPO.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this PaperItemPO.

        

        :param sku: The sku of this PaperItemPO.
        :type sku: str
        """

        self._sku = sku

    @property
    def unit_price_1(self):
        """Gets the unit_price_1 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The unit_price_1 of this PaperItemPO.
        :rtype: object
        """
        return self._unit_price_1

    @unit_price_1.setter
    def unit_price_1(self, unit_price_1):
        """Sets the unit_price_1 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param unit_price_1: The unit_price_1 of this PaperItemPO.
        :type unit_price_1: object
        """

        self._unit_price_1 = unit_price_1

    @property
    def unit_price_2(self):
        """Gets the unit_price_2 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The unit_price_2 of this PaperItemPO.
        :rtype: object
        """
        return self._unit_price_2

    @unit_price_2.setter
    def unit_price_2(self, unit_price_2):
        """Sets the unit_price_2 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param unit_price_2: The unit_price_2 of this PaperItemPO.
        :type unit_price_2: object
        """

        self._unit_price_2 = unit_price_2

    @property
    def unit_price_3(self):
        """Gets the unit_price_3 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The unit_price_3 of this PaperItemPO.
        :rtype: object
        """
        return self._unit_price_3

    @unit_price_3.setter
    def unit_price_3(self, unit_price_3):
        """Sets the unit_price_3 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param unit_price_3: The unit_price_3 of this PaperItemPO.
        :type unit_price_3: object
        """

        self._unit_price_3 = unit_price_3

    @property
    def unit_price_4(self):
        """Gets the unit_price_4 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The unit_price_4 of this PaperItemPO.
        :rtype: object
        """
        return self._unit_price_4

    @unit_price_4.setter
    def unit_price_4(self, unit_price_4):
        """Sets the unit_price_4 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param unit_price_4: The unit_price_4 of this PaperItemPO.
        :type unit_price_4: object
        """

        self._unit_price_4 = unit_price_4

    @property
    def unit_price_5(self):
        """Gets the unit_price_5 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :return: The unit_price_5 of this PaperItemPO.
        :rtype: object
        """
        return self._unit_price_5

    @unit_price_5.setter
    def unit_price_5(self, unit_price_5):
        """Sets the unit_price_5 of this PaperItemPO.

        Java type: java.math.BigDecimal

        :param unit_price_5: The unit_price_5 of this PaperItemPO.
        :type unit_price_5: object
        """

        self._unit_price_5 = unit_price_5
