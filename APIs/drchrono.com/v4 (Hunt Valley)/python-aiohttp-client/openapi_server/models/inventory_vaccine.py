# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InventoryVaccine(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, category: int=None, cost: float=None, created_at: str=None, current_quantity: int=None, cvx_code: str=None, doctor: int=None, expiry: str=None, id: int=None, lot_number: str=None, manufacturer: str=None, manufacturer_code: str=None, name: str=None, note: str=None, original_quantity: int=None, price: float=None, price_with_tax: float=None, sales_tax_applicable: bool=None, status: str=None, updated_at: str=None, vaccination_type: str=None):
        """InventoryVaccine - a model defined in OpenAPI

        :param category: The category of this InventoryVaccine.
        :param cost: The cost of this InventoryVaccine.
        :param created_at: The created_at of this InventoryVaccine.
        :param current_quantity: The current_quantity of this InventoryVaccine.
        :param cvx_code: The cvx_code of this InventoryVaccine.
        :param doctor: The doctor of this InventoryVaccine.
        :param expiry: The expiry of this InventoryVaccine.
        :param id: The id of this InventoryVaccine.
        :param lot_number: The lot_number of this InventoryVaccine.
        :param manufacturer: The manufacturer of this InventoryVaccine.
        :param manufacturer_code: The manufacturer_code of this InventoryVaccine.
        :param name: The name of this InventoryVaccine.
        :param note: The note of this InventoryVaccine.
        :param original_quantity: The original_quantity of this InventoryVaccine.
        :param price: The price of this InventoryVaccine.
        :param price_with_tax: The price_with_tax of this InventoryVaccine.
        :param sales_tax_applicable: The sales_tax_applicable of this InventoryVaccine.
        :param status: The status of this InventoryVaccine.
        :param updated_at: The updated_at of this InventoryVaccine.
        :param vaccination_type: The vaccination_type of this InventoryVaccine.
        """
        self.openapi_types = {
            'category': int,
            'cost': float,
            'created_at': str,
            'current_quantity': int,
            'cvx_code': str,
            'doctor': int,
            'expiry': str,
            'id': int,
            'lot_number': str,
            'manufacturer': str,
            'manufacturer_code': str,
            'name': str,
            'note': str,
            'original_quantity': int,
            'price': float,
            'price_with_tax': float,
            'sales_tax_applicable': bool,
            'status': str,
            'updated_at': str,
            'vaccination_type': str
        }

        self.attribute_map = {
            'category': 'category',
            'cost': 'cost',
            'created_at': 'created_at',
            'current_quantity': 'current_quantity',
            'cvx_code': 'cvx_code',
            'doctor': 'doctor',
            'expiry': 'expiry',
            'id': 'id',
            'lot_number': 'lot_number',
            'manufacturer': 'manufacturer',
            'manufacturer_code': 'manufacturer_code',
            'name': 'name',
            'note': 'note',
            'original_quantity': 'original_quantity',
            'price': 'price',
            'price_with_tax': 'price_with_tax',
            'sales_tax_applicable': 'sales_tax_applicable',
            'status': 'status',
            'updated_at': 'updated_at',
            'vaccination_type': 'vaccination_type'
        }

        self._category = category
        self._cost = cost
        self._created_at = created_at
        self._current_quantity = current_quantity
        self._cvx_code = cvx_code
        self._doctor = doctor
        self._expiry = expiry
        self._id = id
        self._lot_number = lot_number
        self._manufacturer = manufacturer
        self._manufacturer_code = manufacturer_code
        self._name = name
        self._note = note
        self._original_quantity = original_quantity
        self._price = price
        self._price_with_tax = price_with_tax
        self._sales_tax_applicable = sales_tax_applicable
        self._status = status
        self._updated_at = updated_at
        self._vaccination_type = vaccination_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InventoryVaccine':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InventoryVaccine of this InventoryVaccine.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category(self):
        """Gets the category of this InventoryVaccine.

        ID of `/api/inventory_categories`

        :return: The category of this InventoryVaccine.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this InventoryVaccine.

        ID of `/api/inventory_categories`

        :param category: The category of this InventoryVaccine.
        :type category: int
        """

        self._category = category

    @property
    def cost(self):
        """Gets the cost of this InventoryVaccine.

        Base cost for consumables.

        :return: The cost of this InventoryVaccine.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this InventoryVaccine.

        Base cost for consumables.

        :param cost: The cost of this InventoryVaccine.
        :type cost: float
        """

        self._cost = cost

    @property
    def created_at(self):
        """Gets the created_at of this InventoryVaccine.

        

        :return: The created_at of this InventoryVaccine.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InventoryVaccine.

        

        :param created_at: The created_at of this InventoryVaccine.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def current_quantity(self):
        """Gets the current_quantity of this InventoryVaccine.

        This field can onlyu be changed by creating new patient vaccine record. Current quantity of an inventory vaccine is calculated by subtract number of records pointing to this inventory from the original quantity value.

        :return: The current_quantity of this InventoryVaccine.
        :rtype: int
        """
        return self._current_quantity

    @current_quantity.setter
    def current_quantity(self, current_quantity):
        """Sets the current_quantity of this InventoryVaccine.

        This field can onlyu be changed by creating new patient vaccine record. Current quantity of an inventory vaccine is calculated by subtract number of records pointing to this inventory from the original quantity value.

        :param current_quantity: The current_quantity of this InventoryVaccine.
        :type current_quantity: int
        """

        self._current_quantity = current_quantity

    @property
    def cvx_code(self):
        """Gets the cvx_code of this InventoryVaccine.

        

        :return: The cvx_code of this InventoryVaccine.
        :rtype: str
        """
        return self._cvx_code

    @cvx_code.setter
    def cvx_code(self, cvx_code):
        """Sets the cvx_code of this InventoryVaccine.

        

        :param cvx_code: The cvx_code of this InventoryVaccine.
        :type cvx_code: str
        """

        self._cvx_code = cvx_code

    @property
    def doctor(self):
        """Gets the doctor of this InventoryVaccine.

        

        :return: The doctor of this InventoryVaccine.
        :rtype: int
        """
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        """Sets the doctor of this InventoryVaccine.

        

        :param doctor: The doctor of this InventoryVaccine.
        :type doctor: int
        """
        if doctor is None:
            raise ValueError("Invalid value for `doctor`, must not be `None`")

        self._doctor = doctor

    @property
    def expiry(self):
        """Gets the expiry of this InventoryVaccine.

        When will the vaccine expire

        :return: The expiry of this InventoryVaccine.
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this InventoryVaccine.

        When will the vaccine expire

        :param expiry: The expiry of this InventoryVaccine.
        :type expiry: str
        """

        self._expiry = expiry

    @property
    def id(self):
        """Gets the id of this InventoryVaccine.

        

        :return: The id of this InventoryVaccine.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryVaccine.

        

        :param id: The id of this InventoryVaccine.
        :type id: int
        """

        self._id = id

    @property
    def lot_number(self):
        """Gets the lot_number of this InventoryVaccine.

        

        :return: The lot_number of this InventoryVaccine.
        :rtype: str
        """
        return self._lot_number

    @lot_number.setter
    def lot_number(self, lot_number):
        """Sets the lot_number of this InventoryVaccine.

        

        :param lot_number: The lot_number of this InventoryVaccine.
        :type lot_number: str
        """

        self._lot_number = lot_number

    @property
    def manufacturer(self):
        """Gets the manufacturer of this InventoryVaccine.

        

        :return: The manufacturer of this InventoryVaccine.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this InventoryVaccine.

        

        :param manufacturer: The manufacturer of this InventoryVaccine.
        :type manufacturer: str
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_code(self):
        """Gets the manufacturer_code of this InventoryVaccine.

        

        :return: The manufacturer_code of this InventoryVaccine.
        :rtype: str
        """
        return self._manufacturer_code

    @manufacturer_code.setter
    def manufacturer_code(self, manufacturer_code):
        """Sets the manufacturer_code of this InventoryVaccine.

        

        :param manufacturer_code: The manufacturer_code of this InventoryVaccine.
        :type manufacturer_code: str
        """
        if manufacturer_code is None:
            raise ValueError("Invalid value for `manufacturer_code`, must not be `None`")

        self._manufacturer_code = manufacturer_code

    @property
    def name(self):
        """Gets the name of this InventoryVaccine.

        

        :return: The name of this InventoryVaccine.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InventoryVaccine.

        

        :param name: The name of this InventoryVaccine.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def note(self):
        """Gets the note of this InventoryVaccine.

        

        :return: The note of this InventoryVaccine.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this InventoryVaccine.

        

        :param note: The note of this InventoryVaccine.
        :type note: str
        """

        self._note = note

    @property
    def original_quantity(self):
        """Gets the original_quantity of this InventoryVaccine.

        Default to zero

        :return: The original_quantity of this InventoryVaccine.
        :rtype: int
        """
        return self._original_quantity

    @original_quantity.setter
    def original_quantity(self, original_quantity):
        """Sets the original_quantity of this InventoryVaccine.

        Default to zero

        :param original_quantity: The original_quantity of this InventoryVaccine.
        :type original_quantity: int
        """

        self._original_quantity = original_quantity

    @property
    def price(self):
        """Gets the price of this InventoryVaccine.

        

        :return: The price of this InventoryVaccine.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InventoryVaccine.

        

        :param price: The price of this InventoryVaccine.
        :type price: float
        """

        self._price = price

    @property
    def price_with_tax(self):
        """Gets the price_with_tax of this InventoryVaccine.

        

        :return: The price_with_tax of this InventoryVaccine.
        :rtype: float
        """
        return self._price_with_tax

    @price_with_tax.setter
    def price_with_tax(self, price_with_tax):
        """Sets the price_with_tax of this InventoryVaccine.

        

        :param price_with_tax: The price_with_tax of this InventoryVaccine.
        :type price_with_tax: float
        """

        self._price_with_tax = price_with_tax

    @property
    def sales_tax_applicable(self):
        """Gets the sales_tax_applicable of this InventoryVaccine.

        Is sales tax applicable to this service/product? Default to false

        :return: The sales_tax_applicable of this InventoryVaccine.
        :rtype: bool
        """
        return self._sales_tax_applicable

    @sales_tax_applicable.setter
    def sales_tax_applicable(self, sales_tax_applicable):
        """Sets the sales_tax_applicable of this InventoryVaccine.

        Is sales tax applicable to this service/product? Default to false

        :param sales_tax_applicable: The sales_tax_applicable of this InventoryVaccine.
        :type sales_tax_applicable: bool
        """

        self._sales_tax_applicable = sales_tax_applicable

    @property
    def status(self):
        """Gets the status of this InventoryVaccine.

        Status of vaccine, could be one of `active`, `inactive`, `archived`, `voided`, default to `active`

        :return: The status of this InventoryVaccine.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InventoryVaccine.

        Status of vaccine, could be one of `active`, `inactive`, `archived`, `voided`, default to `active`

        :param status: The status of this InventoryVaccine.
        :type status: str
        """
        allowed_values = ["active", "inactive", "archived", "voided"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this InventoryVaccine.

        

        :return: The updated_at of this InventoryVaccine.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InventoryVaccine.

        

        :param updated_at: The updated_at of this InventoryVaccine.
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def vaccination_type(self):
        """Gets the vaccination_type of this InventoryVaccine.

        Default to `\"standard vaccine\"`

        :return: The vaccination_type of this InventoryVaccine.
        :rtype: str
        """
        return self._vaccination_type

    @vaccination_type.setter
    def vaccination_type(self, vaccination_type):
        """Sets the vaccination_type of this InventoryVaccine.

        Default to `\"standard vaccine\"`

        :param vaccination_type: The vaccination_type of this InventoryVaccine.
        :type vaccination_type: str
        """

        self._vaccination_type = vaccination_type
