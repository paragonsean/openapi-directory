# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.order_print import OrderPrint
from openapi_server.models.shipping_address import ShippingAddress
from openapi_server import util


class Order(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, customer_contact_email: str=None, customer_name: str=None, id: int=None, notes: str=None, prints: List[OrderPrint]=None, reference: str=None, ship_by: str=None, shipping_address: ShippingAddress=None):
        """Order - a model defined in OpenAPI

        :param customer_contact_email: The customer_contact_email of this Order.
        :param customer_name: The customer_name of this Order.
        :param id: The id of this Order.
        :param notes: The notes of this Order.
        :param prints: The prints of this Order.
        :param reference: The reference of this Order.
        :param ship_by: The ship_by of this Order.
        :param shipping_address: The shipping_address of this Order.
        """
        self.openapi_types = {
            'customer_contact_email': str,
            'customer_name': str,
            'id': int,
            'notes': str,
            'prints': List[OrderPrint],
            'reference': str,
            'ship_by': str,
            'shipping_address': ShippingAddress
        }

        self.attribute_map = {
            'customer_contact_email': 'customer_contact_email',
            'customer_name': 'customer_name',
            'id': 'id',
            'notes': 'notes',
            'prints': 'prints',
            'reference': 'reference',
            'ship_by': 'ship_by',
            'shipping_address': 'shipping_address'
        }

        self._customer_contact_email = customer_contact_email
        self._customer_name = customer_name
        self._id = id
        self._notes = notes
        self._prints = prints
        self._reference = reference
        self._ship_by = ship_by
        self._shipping_address = shipping_address

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Order of this Order.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_contact_email(self):
        """Gets the customer_contact_email of this Order.

        Customer's email address.

        :return: The customer_contact_email of this Order.
        :rtype: str
        """
        return self._customer_contact_email

    @customer_contact_email.setter
    def customer_contact_email(self, customer_contact_email):
        """Sets the customer_contact_email of this Order.

        Customer's email address.

        :param customer_contact_email: The customer_contact_email of this Order.
        :type customer_contact_email: str
        """

        self._customer_contact_email = customer_contact_email

    @property
    def customer_name(self):
        """Gets the customer_name of this Order.

        Customer's name.

        :return: The customer_name of this Order.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this Order.

        Customer's name.

        :param customer_name: The customer_name of this Order.
        :type customer_name: str
        """

        self._customer_name = customer_name

    @property
    def id(self):
        """Gets the id of this Order.

        Unique identifier for this order. Reference should be displayed and used for lookups instead of this field.

        :return: The id of this Order.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.

        Unique identifier for this order. Reference should be displayed and used for lookups instead of this field.

        :param id: The id of this Order.
        :type id: int
        """

        self._id = id

    @property
    def notes(self):
        """Gets the notes of this Order.

        The notes field that was submitted with this order.

        :return: The notes of this Order.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Order.

        The notes field that was submitted with this order.

        :param notes: The notes of this Order.
        :type notes: str
        """

        self._notes = notes

    @property
    def prints(self):
        """Gets the prints of this Order.


        :return: The prints of this Order.
        :rtype: List[OrderPrint]
        """
        return self._prints

    @prints.setter
    def prints(self, prints):
        """Sets the prints of this Order.


        :param prints: The prints of this Order.
        :type prints: List[OrderPrint]
        """

        self._prints = prints

    @property
    def reference(self):
        """Gets the reference of this Order.

        Unique identifier for this order. Used to retrieve info for a specific order from /order/{order_id}.

        :return: The reference of this Order.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Order.

        Unique identifier for this order. Used to retrieve info for a specific order from /order/{order_id}.

        :param reference: The reference of this Order.
        :type reference: str
        """

        self._reference = reference

    @property
    def ship_by(self):
        """Gets the ship_by of this Order.

        Planned ship date for this order.

        :return: The ship_by of this Order.
        :rtype: str
        """
        return self._ship_by

    @ship_by.setter
    def ship_by(self, ship_by):
        """Sets the ship_by of this Order.

        Planned ship date for this order.

        :param ship_by: The ship_by of this Order.
        :type ship_by: str
        """

        self._ship_by = ship_by

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Order.


        :return: The shipping_address of this Order.
        :rtype: ShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Order.


        :param shipping_address: The shipping_address of this Order.
        :type shipping_address: ShippingAddress
        """

        self._shipping_address = shipping_address
