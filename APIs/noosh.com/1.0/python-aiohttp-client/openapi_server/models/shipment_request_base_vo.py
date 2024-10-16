# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.property_pa_and_att_vo import PropertyPaAndAttVO
from openapi_server import util


class ShipmentRequestBaseVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, company_name: str=None, country: str=None, country_code: str=None, custom_fields: List[PropertyPaAndAttVO]=None, description_or_title: str=None, due_date: date=None, email: str=None, first_name: str=None, is_use_spec_packaging: bool=None, last_name: str=None, line_1: str=None, line_2: str=None, line_3: str=None, location_id: int=None, middle_name: str=None, postal: str=None, proof_type: str=None, qty_received: int=None, qty_requested: int=None, qty_shipped: int=None, received_comments: str=None, received_date: date=None, requested_shipping_carrier: str=None, requested_shipping_method: str=None, shipped_comments: str=None, shipped_date: date=None, shipped_in_units: int=None, shipped_in_uofm: str=None, shipped_shipping_carrier: str=None, shipped_shipping_method: str=None, shipping_cost: object=None, shipping_instruction: str=None, state: str=None, tax: object=None, tracking_number: str=None, type: str=None, weight: object=None, weight_uofm: str=None, work_phone_number: str=None, workgroup_name: str=None):
        """ShipmentRequestBaseVO - a model defined in OpenAPI

        :param city: The city of this ShipmentRequestBaseVO.
        :param company_name: The company_name of this ShipmentRequestBaseVO.
        :param country: The country of this ShipmentRequestBaseVO.
        :param country_code: The country_code of this ShipmentRequestBaseVO.
        :param custom_fields: The custom_fields of this ShipmentRequestBaseVO.
        :param description_or_title: The description_or_title of this ShipmentRequestBaseVO.
        :param due_date: The due_date of this ShipmentRequestBaseVO.
        :param email: The email of this ShipmentRequestBaseVO.
        :param first_name: The first_name of this ShipmentRequestBaseVO.
        :param is_use_spec_packaging: The is_use_spec_packaging of this ShipmentRequestBaseVO.
        :param last_name: The last_name of this ShipmentRequestBaseVO.
        :param line_1: The line_1 of this ShipmentRequestBaseVO.
        :param line_2: The line_2 of this ShipmentRequestBaseVO.
        :param line_3: The line_3 of this ShipmentRequestBaseVO.
        :param location_id: The location_id of this ShipmentRequestBaseVO.
        :param middle_name: The middle_name of this ShipmentRequestBaseVO.
        :param postal: The postal of this ShipmentRequestBaseVO.
        :param proof_type: The proof_type of this ShipmentRequestBaseVO.
        :param qty_received: The qty_received of this ShipmentRequestBaseVO.
        :param qty_requested: The qty_requested of this ShipmentRequestBaseVO.
        :param qty_shipped: The qty_shipped of this ShipmentRequestBaseVO.
        :param received_comments: The received_comments of this ShipmentRequestBaseVO.
        :param received_date: The received_date of this ShipmentRequestBaseVO.
        :param requested_shipping_carrier: The requested_shipping_carrier of this ShipmentRequestBaseVO.
        :param requested_shipping_method: The requested_shipping_method of this ShipmentRequestBaseVO.
        :param shipped_comments: The shipped_comments of this ShipmentRequestBaseVO.
        :param shipped_date: The shipped_date of this ShipmentRequestBaseVO.
        :param shipped_in_units: The shipped_in_units of this ShipmentRequestBaseVO.
        :param shipped_in_uofm: The shipped_in_uofm of this ShipmentRequestBaseVO.
        :param shipped_shipping_carrier: The shipped_shipping_carrier of this ShipmentRequestBaseVO.
        :param shipped_shipping_method: The shipped_shipping_method of this ShipmentRequestBaseVO.
        :param shipping_cost: The shipping_cost of this ShipmentRequestBaseVO.
        :param shipping_instruction: The shipping_instruction of this ShipmentRequestBaseVO.
        :param state: The state of this ShipmentRequestBaseVO.
        :param tax: The tax of this ShipmentRequestBaseVO.
        :param tracking_number: The tracking_number of this ShipmentRequestBaseVO.
        :param type: The type of this ShipmentRequestBaseVO.
        :param weight: The weight of this ShipmentRequestBaseVO.
        :param weight_uofm: The weight_uofm of this ShipmentRequestBaseVO.
        :param work_phone_number: The work_phone_number of this ShipmentRequestBaseVO.
        :param workgroup_name: The workgroup_name of this ShipmentRequestBaseVO.
        """
        self.openapi_types = {
            'city': str,
            'company_name': str,
            'country': str,
            'country_code': str,
            'custom_fields': List[PropertyPaAndAttVO],
            'description_or_title': str,
            'due_date': date,
            'email': str,
            'first_name': str,
            'is_use_spec_packaging': bool,
            'last_name': str,
            'line_1': str,
            'line_2': str,
            'line_3': str,
            'location_id': int,
            'middle_name': str,
            'postal': str,
            'proof_type': str,
            'qty_received': int,
            'qty_requested': int,
            'qty_shipped': int,
            'received_comments': str,
            'received_date': date,
            'requested_shipping_carrier': str,
            'requested_shipping_method': str,
            'shipped_comments': str,
            'shipped_date': date,
            'shipped_in_units': int,
            'shipped_in_uofm': str,
            'shipped_shipping_carrier': str,
            'shipped_shipping_method': str,
            'shipping_cost': object,
            'shipping_instruction': str,
            'state': str,
            'tax': object,
            'tracking_number': str,
            'type': str,
            'weight': object,
            'weight_uofm': str,
            'work_phone_number': str,
            'workgroup_name': str
        }

        self.attribute_map = {
            'city': 'city',
            'company_name': 'company_name',
            'country': 'country',
            'country_code': 'country_code',
            'custom_fields': 'custom_fields',
            'description_or_title': 'description_or_title',
            'due_date': 'due_date',
            'email': 'email',
            'first_name': 'first_name',
            'is_use_spec_packaging': 'is_use_spec_packaging',
            'last_name': 'last_name',
            'line_1': 'line_1',
            'line_2': 'line_2',
            'line_3': 'line_3',
            'location_id': 'location_id',
            'middle_name': 'middle_name',
            'postal': 'postal',
            'proof_type': 'proof_type',
            'qty_received': 'qty_received',
            'qty_requested': 'qty_requested',
            'qty_shipped': 'qty_shipped',
            'received_comments': 'received_comments',
            'received_date': 'received_date',
            'requested_shipping_carrier': 'requested_shipping_carrier',
            'requested_shipping_method': 'requested_shipping_method',
            'shipped_comments': 'shipped_comments',
            'shipped_date': 'shipped_date',
            'shipped_in_units': 'shipped_in_units',
            'shipped_in_uofm': 'shipped_in_uofm',
            'shipped_shipping_carrier': 'shipped_shipping_carrier',
            'shipped_shipping_method': 'shipped_shipping_method',
            'shipping_cost': 'shipping_cost',
            'shipping_instruction': 'shipping_instruction',
            'state': 'state',
            'tax': 'tax',
            'tracking_number': 'tracking_number',
            'type': 'type',
            'weight': 'weight',
            'weight_uofm': 'weight_uofm',
            'work_phone_number': 'work_phone_number',
            'workgroup_name': 'workgroup_name'
        }

        self._city = city
        self._company_name = company_name
        self._country = country
        self._country_code = country_code
        self._custom_fields = custom_fields
        self._description_or_title = description_or_title
        self._due_date = due_date
        self._email = email
        self._first_name = first_name
        self._is_use_spec_packaging = is_use_spec_packaging
        self._last_name = last_name
        self._line_1 = line_1
        self._line_2 = line_2
        self._line_3 = line_3
        self._location_id = location_id
        self._middle_name = middle_name
        self._postal = postal
        self._proof_type = proof_type
        self._qty_received = qty_received
        self._qty_requested = qty_requested
        self._qty_shipped = qty_shipped
        self._received_comments = received_comments
        self._received_date = received_date
        self._requested_shipping_carrier = requested_shipping_carrier
        self._requested_shipping_method = requested_shipping_method
        self._shipped_comments = shipped_comments
        self._shipped_date = shipped_date
        self._shipped_in_units = shipped_in_units
        self._shipped_in_uofm = shipped_in_uofm
        self._shipped_shipping_carrier = shipped_shipping_carrier
        self._shipped_shipping_method = shipped_shipping_method
        self._shipping_cost = shipping_cost
        self._shipping_instruction = shipping_instruction
        self._state = state
        self._tax = tax
        self._tracking_number = tracking_number
        self._type = type
        self._weight = weight
        self._weight_uofm = weight_uofm
        self._work_phone_number = work_phone_number
        self._workgroup_name = workgroup_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ShipmentRequestBaseVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ShipmentRequestBaseVO of this ShipmentRequestBaseVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self):
        """Gets the city of this ShipmentRequestBaseVO.

        

        :return: The city of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ShipmentRequestBaseVO.

        

        :param city: The city of this ShipmentRequestBaseVO.
        :type city: str
        """

        self._city = city

    @property
    def company_name(self):
        """Gets the company_name of this ShipmentRequestBaseVO.

        

        :return: The company_name of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ShipmentRequestBaseVO.

        

        :param company_name: The company_name of this ShipmentRequestBaseVO.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def country(self):
        """Gets the country of this ShipmentRequestBaseVO.

        

        :return: The country of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShipmentRequestBaseVO.

        

        :param country: The country of this ShipmentRequestBaseVO.
        :type country: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this ShipmentRequestBaseVO.

        

        :return: The country_code of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ShipmentRequestBaseVO.

        

        :param country_code: The country_code of this ShipmentRequestBaseVO.
        :type country_code: str
        """

        self._country_code = country_code

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ShipmentRequestBaseVO.

        

        :return: The custom_fields of this ShipmentRequestBaseVO.
        :rtype: List[PropertyPaAndAttVO]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ShipmentRequestBaseVO.

        

        :param custom_fields: The custom_fields of this ShipmentRequestBaseVO.
        :type custom_fields: List[PropertyPaAndAttVO]
        """

        self._custom_fields = custom_fields

    @property
    def description_or_title(self):
        """Gets the description_or_title of this ShipmentRequestBaseVO.

        

        :return: The description_or_title of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._description_or_title

    @description_or_title.setter
    def description_or_title(self, description_or_title):
        """Sets the description_or_title of this ShipmentRequestBaseVO.

        

        :param description_or_title: The description_or_title of this ShipmentRequestBaseVO.
        :type description_or_title: str
        """

        self._description_or_title = description_or_title

    @property
    def due_date(self):
        """Gets the due_date of this ShipmentRequestBaseVO.

        

        :return: The due_date of this ShipmentRequestBaseVO.
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this ShipmentRequestBaseVO.

        

        :param due_date: The due_date of this ShipmentRequestBaseVO.
        :type due_date: date
        """

        self._due_date = due_date

    @property
    def email(self):
        """Gets the email of this ShipmentRequestBaseVO.

        

        :return: The email of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ShipmentRequestBaseVO.

        

        :param email: The email of this ShipmentRequestBaseVO.
        :type email: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this ShipmentRequestBaseVO.

        

        :return: The first_name of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ShipmentRequestBaseVO.

        

        :param first_name: The first_name of this ShipmentRequestBaseVO.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def is_use_spec_packaging(self):
        """Gets the is_use_spec_packaging of this ShipmentRequestBaseVO.

        

        :return: The is_use_spec_packaging of this ShipmentRequestBaseVO.
        :rtype: bool
        """
        return self._is_use_spec_packaging

    @is_use_spec_packaging.setter
    def is_use_spec_packaging(self, is_use_spec_packaging):
        """Sets the is_use_spec_packaging of this ShipmentRequestBaseVO.

        

        :param is_use_spec_packaging: The is_use_spec_packaging of this ShipmentRequestBaseVO.
        :type is_use_spec_packaging: bool
        """

        self._is_use_spec_packaging = is_use_spec_packaging

    @property
    def last_name(self):
        """Gets the last_name of this ShipmentRequestBaseVO.

        

        :return: The last_name of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ShipmentRequestBaseVO.

        

        :param last_name: The last_name of this ShipmentRequestBaseVO.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def line_1(self):
        """Gets the line_1 of this ShipmentRequestBaseVO.

        

        :return: The line_1 of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._line_1

    @line_1.setter
    def line_1(self, line_1):
        """Sets the line_1 of this ShipmentRequestBaseVO.

        

        :param line_1: The line_1 of this ShipmentRequestBaseVO.
        :type line_1: str
        """

        self._line_1 = line_1

    @property
    def line_2(self):
        """Gets the line_2 of this ShipmentRequestBaseVO.

        

        :return: The line_2 of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._line_2

    @line_2.setter
    def line_2(self, line_2):
        """Sets the line_2 of this ShipmentRequestBaseVO.

        

        :param line_2: The line_2 of this ShipmentRequestBaseVO.
        :type line_2: str
        """

        self._line_2 = line_2

    @property
    def line_3(self):
        """Gets the line_3 of this ShipmentRequestBaseVO.

        

        :return: The line_3 of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._line_3

    @line_3.setter
    def line_3(self, line_3):
        """Sets the line_3 of this ShipmentRequestBaseVO.

        

        :param line_3: The line_3 of this ShipmentRequestBaseVO.
        :type line_3: str
        """

        self._line_3 = line_3

    @property
    def location_id(self):
        """Gets the location_id of this ShipmentRequestBaseVO.

        

        :return: The location_id of this ShipmentRequestBaseVO.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this ShipmentRequestBaseVO.

        

        :param location_id: The location_id of this ShipmentRequestBaseVO.
        :type location_id: int
        """

        self._location_id = location_id

    @property
    def middle_name(self):
        """Gets the middle_name of this ShipmentRequestBaseVO.

        

        :return: The middle_name of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this ShipmentRequestBaseVO.

        

        :param middle_name: The middle_name of this ShipmentRequestBaseVO.
        :type middle_name: str
        """

        self._middle_name = middle_name

    @property
    def postal(self):
        """Gets the postal of this ShipmentRequestBaseVO.

        

        :return: The postal of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._postal

    @postal.setter
    def postal(self, postal):
        """Sets the postal of this ShipmentRequestBaseVO.

        

        :param postal: The postal of this ShipmentRequestBaseVO.
        :type postal: str
        """

        self._postal = postal

    @property
    def proof_type(self):
        """Gets the proof_type of this ShipmentRequestBaseVO.

        

        :return: The proof_type of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._proof_type

    @proof_type.setter
    def proof_type(self, proof_type):
        """Sets the proof_type of this ShipmentRequestBaseVO.

        

        :param proof_type: The proof_type of this ShipmentRequestBaseVO.
        :type proof_type: str
        """

        self._proof_type = proof_type

    @property
    def qty_received(self):
        """Gets the qty_received of this ShipmentRequestBaseVO.

        

        :return: The qty_received of this ShipmentRequestBaseVO.
        :rtype: int
        """
        return self._qty_received

    @qty_received.setter
    def qty_received(self, qty_received):
        """Sets the qty_received of this ShipmentRequestBaseVO.

        

        :param qty_received: The qty_received of this ShipmentRequestBaseVO.
        :type qty_received: int
        """

        self._qty_received = qty_received

    @property
    def qty_requested(self):
        """Gets the qty_requested of this ShipmentRequestBaseVO.

        

        :return: The qty_requested of this ShipmentRequestBaseVO.
        :rtype: int
        """
        return self._qty_requested

    @qty_requested.setter
    def qty_requested(self, qty_requested):
        """Sets the qty_requested of this ShipmentRequestBaseVO.

        

        :param qty_requested: The qty_requested of this ShipmentRequestBaseVO.
        :type qty_requested: int
        """

        self._qty_requested = qty_requested

    @property
    def qty_shipped(self):
        """Gets the qty_shipped of this ShipmentRequestBaseVO.

        

        :return: The qty_shipped of this ShipmentRequestBaseVO.
        :rtype: int
        """
        return self._qty_shipped

    @qty_shipped.setter
    def qty_shipped(self, qty_shipped):
        """Sets the qty_shipped of this ShipmentRequestBaseVO.

        

        :param qty_shipped: The qty_shipped of this ShipmentRequestBaseVO.
        :type qty_shipped: int
        """

        self._qty_shipped = qty_shipped

    @property
    def received_comments(self):
        """Gets the received_comments of this ShipmentRequestBaseVO.

        

        :return: The received_comments of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._received_comments

    @received_comments.setter
    def received_comments(self, received_comments):
        """Sets the received_comments of this ShipmentRequestBaseVO.

        

        :param received_comments: The received_comments of this ShipmentRequestBaseVO.
        :type received_comments: str
        """

        self._received_comments = received_comments

    @property
    def received_date(self):
        """Gets the received_date of this ShipmentRequestBaseVO.

        

        :return: The received_date of this ShipmentRequestBaseVO.
        :rtype: date
        """
        return self._received_date

    @received_date.setter
    def received_date(self, received_date):
        """Sets the received_date of this ShipmentRequestBaseVO.

        

        :param received_date: The received_date of this ShipmentRequestBaseVO.
        :type received_date: date
        """

        self._received_date = received_date

    @property
    def requested_shipping_carrier(self):
        """Gets the requested_shipping_carrier of this ShipmentRequestBaseVO.

        

        :return: The requested_shipping_carrier of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._requested_shipping_carrier

    @requested_shipping_carrier.setter
    def requested_shipping_carrier(self, requested_shipping_carrier):
        """Sets the requested_shipping_carrier of this ShipmentRequestBaseVO.

        

        :param requested_shipping_carrier: The requested_shipping_carrier of this ShipmentRequestBaseVO.
        :type requested_shipping_carrier: str
        """

        self._requested_shipping_carrier = requested_shipping_carrier

    @property
    def requested_shipping_method(self):
        """Gets the requested_shipping_method of this ShipmentRequestBaseVO.

        

        :return: The requested_shipping_method of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._requested_shipping_method

    @requested_shipping_method.setter
    def requested_shipping_method(self, requested_shipping_method):
        """Sets the requested_shipping_method of this ShipmentRequestBaseVO.

        

        :param requested_shipping_method: The requested_shipping_method of this ShipmentRequestBaseVO.
        :type requested_shipping_method: str
        """

        self._requested_shipping_method = requested_shipping_method

    @property
    def shipped_comments(self):
        """Gets the shipped_comments of this ShipmentRequestBaseVO.

        

        :return: The shipped_comments of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._shipped_comments

    @shipped_comments.setter
    def shipped_comments(self, shipped_comments):
        """Sets the shipped_comments of this ShipmentRequestBaseVO.

        

        :param shipped_comments: The shipped_comments of this ShipmentRequestBaseVO.
        :type shipped_comments: str
        """

        self._shipped_comments = shipped_comments

    @property
    def shipped_date(self):
        """Gets the shipped_date of this ShipmentRequestBaseVO.

        

        :return: The shipped_date of this ShipmentRequestBaseVO.
        :rtype: date
        """
        return self._shipped_date

    @shipped_date.setter
    def shipped_date(self, shipped_date):
        """Sets the shipped_date of this ShipmentRequestBaseVO.

        

        :param shipped_date: The shipped_date of this ShipmentRequestBaseVO.
        :type shipped_date: date
        """

        self._shipped_date = shipped_date

    @property
    def shipped_in_units(self):
        """Gets the shipped_in_units of this ShipmentRequestBaseVO.

        

        :return: The shipped_in_units of this ShipmentRequestBaseVO.
        :rtype: int
        """
        return self._shipped_in_units

    @shipped_in_units.setter
    def shipped_in_units(self, shipped_in_units):
        """Sets the shipped_in_units of this ShipmentRequestBaseVO.

        

        :param shipped_in_units: The shipped_in_units of this ShipmentRequestBaseVO.
        :type shipped_in_units: int
        """

        self._shipped_in_units = shipped_in_units

    @property
    def shipped_in_uofm(self):
        """Gets the shipped_in_uofm of this ShipmentRequestBaseVO.

        

        :return: The shipped_in_uofm of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._shipped_in_uofm

    @shipped_in_uofm.setter
    def shipped_in_uofm(self, shipped_in_uofm):
        """Sets the shipped_in_uofm of this ShipmentRequestBaseVO.

        

        :param shipped_in_uofm: The shipped_in_uofm of this ShipmentRequestBaseVO.
        :type shipped_in_uofm: str
        """

        self._shipped_in_uofm = shipped_in_uofm

    @property
    def shipped_shipping_carrier(self):
        """Gets the shipped_shipping_carrier of this ShipmentRequestBaseVO.

        

        :return: The shipped_shipping_carrier of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._shipped_shipping_carrier

    @shipped_shipping_carrier.setter
    def shipped_shipping_carrier(self, shipped_shipping_carrier):
        """Sets the shipped_shipping_carrier of this ShipmentRequestBaseVO.

        

        :param shipped_shipping_carrier: The shipped_shipping_carrier of this ShipmentRequestBaseVO.
        :type shipped_shipping_carrier: str
        """

        self._shipped_shipping_carrier = shipped_shipping_carrier

    @property
    def shipped_shipping_method(self):
        """Gets the shipped_shipping_method of this ShipmentRequestBaseVO.

        

        :return: The shipped_shipping_method of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._shipped_shipping_method

    @shipped_shipping_method.setter
    def shipped_shipping_method(self, shipped_shipping_method):
        """Sets the shipped_shipping_method of this ShipmentRequestBaseVO.

        

        :param shipped_shipping_method: The shipped_shipping_method of this ShipmentRequestBaseVO.
        :type shipped_shipping_method: str
        """

        self._shipped_shipping_method = shipped_shipping_method

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this ShipmentRequestBaseVO.

        Java type: java.math.BigDecimal

        :return: The shipping_cost of this ShipmentRequestBaseVO.
        :rtype: object
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this ShipmentRequestBaseVO.

        Java type: java.math.BigDecimal

        :param shipping_cost: The shipping_cost of this ShipmentRequestBaseVO.
        :type shipping_cost: object
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_instruction(self):
        """Gets the shipping_instruction of this ShipmentRequestBaseVO.

        

        :return: The shipping_instruction of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._shipping_instruction

    @shipping_instruction.setter
    def shipping_instruction(self, shipping_instruction):
        """Sets the shipping_instruction of this ShipmentRequestBaseVO.

        

        :param shipping_instruction: The shipping_instruction of this ShipmentRequestBaseVO.
        :type shipping_instruction: str
        """

        self._shipping_instruction = shipping_instruction

    @property
    def state(self):
        """Gets the state of this ShipmentRequestBaseVO.

        

        :return: The state of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShipmentRequestBaseVO.

        

        :param state: The state of this ShipmentRequestBaseVO.
        :type state: str
        """

        self._state = state

    @property
    def tax(self):
        """Gets the tax of this ShipmentRequestBaseVO.

        Java type: java.math.BigDecimal

        :return: The tax of this ShipmentRequestBaseVO.
        :rtype: object
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this ShipmentRequestBaseVO.

        Java type: java.math.BigDecimal

        :param tax: The tax of this ShipmentRequestBaseVO.
        :type tax: object
        """

        self._tax = tax

    @property
    def tracking_number(self):
        """Gets the tracking_number of this ShipmentRequestBaseVO.

        

        :return: The tracking_number of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this ShipmentRequestBaseVO.

        

        :param tracking_number: The tracking_number of this ShipmentRequestBaseVO.
        :type tracking_number: str
        """

        self._tracking_number = tracking_number

    @property
    def type(self):
        """Gets the type of this ShipmentRequestBaseVO.

        

        :return: The type of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShipmentRequestBaseVO.

        

        :param type: The type of this ShipmentRequestBaseVO.
        :type type: str
        """

        self._type = type

    @property
    def weight(self):
        """Gets the weight of this ShipmentRequestBaseVO.

        Java type: java.math.BigDecimal

        :return: The weight of this ShipmentRequestBaseVO.
        :rtype: object
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ShipmentRequestBaseVO.

        Java type: java.math.BigDecimal

        :param weight: The weight of this ShipmentRequestBaseVO.
        :type weight: object
        """

        self._weight = weight

    @property
    def weight_uofm(self):
        """Gets the weight_uofm of this ShipmentRequestBaseVO.

        

        :return: The weight_uofm of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._weight_uofm

    @weight_uofm.setter
    def weight_uofm(self, weight_uofm):
        """Sets the weight_uofm of this ShipmentRequestBaseVO.

        

        :param weight_uofm: The weight_uofm of this ShipmentRequestBaseVO.
        :type weight_uofm: str
        """

        self._weight_uofm = weight_uofm

    @property
    def work_phone_number(self):
        """Gets the work_phone_number of this ShipmentRequestBaseVO.

        

        :return: The work_phone_number of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._work_phone_number

    @work_phone_number.setter
    def work_phone_number(self, work_phone_number):
        """Sets the work_phone_number of this ShipmentRequestBaseVO.

        

        :param work_phone_number: The work_phone_number of this ShipmentRequestBaseVO.
        :type work_phone_number: str
        """

        self._work_phone_number = work_phone_number

    @property
    def workgroup_name(self):
        """Gets the workgroup_name of this ShipmentRequestBaseVO.

        

        :return: The workgroup_name of this ShipmentRequestBaseVO.
        :rtype: str
        """
        return self._workgroup_name

    @workgroup_name.setter
    def workgroup_name(self, workgroup_name):
        """Sets the workgroup_name of this ShipmentRequestBaseVO.

        

        :param workgroup_name: The workgroup_name of this ShipmentRequestBaseVO.
        :type workgroup_name: str
        """

        self._workgroup_name = workgroup_name
