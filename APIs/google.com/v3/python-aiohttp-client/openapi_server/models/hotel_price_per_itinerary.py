# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.model_date import ModelDate
from openapi_server import util


class HotelPricePerItinerary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, checkin_date: ModelDate=None, currency_code: str=None, fees: float=None, length_of_stay_days: int=None, price: float=None, taxes: float=None, update_time: str=None):
        """HotelPricePerItinerary - a model defined in OpenAPI

        :param checkin_date: The checkin_date of this HotelPricePerItinerary.
        :param currency_code: The currency_code of this HotelPricePerItinerary.
        :param fees: The fees of this HotelPricePerItinerary.
        :param length_of_stay_days: The length_of_stay_days of this HotelPricePerItinerary.
        :param price: The price of this HotelPricePerItinerary.
        :param taxes: The taxes of this HotelPricePerItinerary.
        :param update_time: The update_time of this HotelPricePerItinerary.
        """
        self.openapi_types = {
            'checkin_date': ModelDate,
            'currency_code': str,
            'fees': float,
            'length_of_stay_days': int,
            'price': float,
            'taxes': float,
            'update_time': str
        }

        self.attribute_map = {
            'checkin_date': 'checkinDate',
            'currency_code': 'currencyCode',
            'fees': 'fees',
            'length_of_stay_days': 'lengthOfStayDays',
            'price': 'price',
            'taxes': 'taxes',
            'update_time': 'updateTime'
        }

        self._checkin_date = checkin_date
        self._currency_code = currency_code
        self._fees = fees
        self._length_of_stay_days = length_of_stay_days
        self._price = price
        self._taxes = taxes
        self._update_time = update_time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HotelPricePerItinerary':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HotelPricePerItinerary of this HotelPricePerItinerary.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def checkin_date(self):
        """Gets the checkin_date of this HotelPricePerItinerary.


        :return: The checkin_date of this HotelPricePerItinerary.
        :rtype: ModelDate
        """
        return self._checkin_date

    @checkin_date.setter
    def checkin_date(self, checkin_date):
        """Sets the checkin_date of this HotelPricePerItinerary.


        :param checkin_date: The checkin_date of this HotelPricePerItinerary.
        :type checkin_date: ModelDate
        """

        self._checkin_date = checkin_date

    @property
    def currency_code(self):
        """Gets the currency_code of this HotelPricePerItinerary.

        Currency for `price`, `taxes`, and `fees`.

        :return: The currency_code of this HotelPricePerItinerary.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this HotelPricePerItinerary.

        Currency for `price`, `taxes`, and `fees`.

        :param currency_code: The currency_code of this HotelPricePerItinerary.
        :type currency_code: str
        """

        self._currency_code = currency_code

    @property
    def fees(self):
        """Gets the fees of this HotelPricePerItinerary.

        Fees for this itinerary.

        :return: The fees of this HotelPricePerItinerary.
        :rtype: float
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this HotelPricePerItinerary.

        Fees for this itinerary.

        :param fees: The fees of this HotelPricePerItinerary.
        :type fees: float
        """

        self._fees = fees

    @property
    def length_of_stay_days(self):
        """Gets the length_of_stay_days of this HotelPricePerItinerary.

        Number of nights for the itinerary.

        :return: The length_of_stay_days of this HotelPricePerItinerary.
        :rtype: int
        """
        return self._length_of_stay_days

    @length_of_stay_days.setter
    def length_of_stay_days(self, length_of_stay_days):
        """Sets the length_of_stay_days of this HotelPricePerItinerary.

        Number of nights for the itinerary.

        :param length_of_stay_days: The length_of_stay_days of this HotelPricePerItinerary.
        :type length_of_stay_days: int
        """

        self._length_of_stay_days = length_of_stay_days

    @property
    def price(self):
        """Gets the price of this HotelPricePerItinerary.

        Hotel price for this itinerary.

        :return: The price of this HotelPricePerItinerary.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this HotelPricePerItinerary.

        Hotel price for this itinerary.

        :param price: The price of this HotelPricePerItinerary.
        :type price: float
        """

        self._price = price

    @property
    def taxes(self):
        """Gets the taxes of this HotelPricePerItinerary.

        Taxes for this itinerary.

        :return: The taxes of this HotelPricePerItinerary.
        :rtype: float
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this HotelPricePerItinerary.

        Taxes for this itinerary.

        :param taxes: The taxes of this HotelPricePerItinerary.
        :type taxes: float
        """

        self._taxes = taxes

    @property
    def update_time(self):
        """Gets the update_time of this HotelPricePerItinerary.

        Update timestamp for this hotel price.

        :return: The update_time of this HotelPricePerItinerary.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this HotelPricePerItinerary.

        Update timestamp for this hotel price.

        :param update_time: The update_time of this HotelPricePerItinerary.
        :type update_time: str
        """

        self._update_time = update_time
