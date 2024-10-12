# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.air_data_seats_inner import AirDataSeatsInner
from openapi_server.models.aircraft import Aircraft
from openapi_server.models.arrival_air import ArrivalAir
from openapi_server.models.arrival_airport_location import ArrivalAirportLocation
from openapi_server.models.baggages import Baggages
from openapi_server.models.departure_air import DepartureAir
from openapi_server.models.departure_airport_location import DepartureAirportLocation
from openapi_server.models.marketing import Marketing
from openapi_server.models.meal import Meal
from openapi_server.models.operating import Operating
from openapi_server import util


class AirData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aircraft: Aircraft=None, arrival: ArrivalAir=None, arrival_airport_location: ArrivalAirportLocation=None, baggages: Baggages=None, confirmation_number: str=None, departure: DepartureAir=None, departure_airport_location: DepartureAirportLocation=None, marketing: Marketing=None, meal: Meal=None, operating: Operating=None, seats: List[AirDataSeatsInner]=None):
        """AirData - a model defined in OpenAPI

        :param aircraft: The aircraft of this AirData.
        :param arrival: The arrival of this AirData.
        :param arrival_airport_location: The arrival_airport_location of this AirData.
        :param baggages: The baggages of this AirData.
        :param confirmation_number: The confirmation_number of this AirData.
        :param departure: The departure of this AirData.
        :param departure_airport_location: The departure_airport_location of this AirData.
        :param marketing: The marketing of this AirData.
        :param meal: The meal of this AirData.
        :param operating: The operating of this AirData.
        :param seats: The seats of this AirData.
        """
        self.openapi_types = {
            'aircraft': Aircraft,
            'arrival': ArrivalAir,
            'arrival_airport_location': ArrivalAirportLocation,
            'baggages': Baggages,
            'confirmation_number': str,
            'departure': DepartureAir,
            'departure_airport_location': DepartureAirportLocation,
            'marketing': Marketing,
            'meal': Meal,
            'operating': Operating,
            'seats': List[AirDataSeatsInner]
        }

        self.attribute_map = {
            'aircraft': 'aircraft',
            'arrival': 'arrival',
            'arrival_airport_location': 'arrivalAirportLocation',
            'baggages': 'baggages',
            'confirmation_number': 'confirmationNumber',
            'departure': 'departure',
            'departure_airport_location': 'departureAirportLocation',
            'marketing': 'marketing',
            'meal': 'meal',
            'operating': 'operating',
            'seats': 'seats'
        }

        self._aircraft = aircraft
        self._arrival = arrival
        self._arrival_airport_location = arrival_airport_location
        self._baggages = baggages
        self._confirmation_number = confirmation_number
        self._departure = departure
        self._departure_airport_location = departure_airport_location
        self._marketing = marketing
        self._meal = meal
        self._operating = operating
        self._seats = seats

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AirData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The airData of this AirData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aircraft(self):
        """Gets the aircraft of this AirData.


        :return: The aircraft of this AirData.
        :rtype: Aircraft
        """
        return self._aircraft

    @aircraft.setter
    def aircraft(self, aircraft):
        """Sets the aircraft of this AirData.


        :param aircraft: The aircraft of this AirData.
        :type aircraft: Aircraft
        """

        self._aircraft = aircraft

    @property
    def arrival(self):
        """Gets the arrival of this AirData.


        :return: The arrival of this AirData.
        :rtype: ArrivalAir
        """
        return self._arrival

    @arrival.setter
    def arrival(self, arrival):
        """Sets the arrival of this AirData.


        :param arrival: The arrival of this AirData.
        :type arrival: ArrivalAir
        """

        self._arrival = arrival

    @property
    def arrival_airport_location(self):
        """Gets the arrival_airport_location of this AirData.


        :return: The arrival_airport_location of this AirData.
        :rtype: ArrivalAirportLocation
        """
        return self._arrival_airport_location

    @arrival_airport_location.setter
    def arrival_airport_location(self, arrival_airport_location):
        """Sets the arrival_airport_location of this AirData.


        :param arrival_airport_location: The arrival_airport_location of this AirData.
        :type arrival_airport_location: ArrivalAirportLocation
        """

        self._arrival_airport_location = arrival_airport_location

    @property
    def baggages(self):
        """Gets the baggages of this AirData.


        :return: The baggages of this AirData.
        :rtype: Baggages
        """
        return self._baggages

    @baggages.setter
    def baggages(self, baggages):
        """Sets the baggages of this AirData.


        :param baggages: The baggages of this AirData.
        :type baggages: Baggages
        """

        self._baggages = baggages

    @property
    def confirmation_number(self):
        """Gets the confirmation_number of this AirData.


        :return: The confirmation_number of this AirData.
        :rtype: str
        """
        return self._confirmation_number

    @confirmation_number.setter
    def confirmation_number(self, confirmation_number):
        """Sets the confirmation_number of this AirData.


        :param confirmation_number: The confirmation_number of this AirData.
        :type confirmation_number: str
        """

        self._confirmation_number = confirmation_number

    @property
    def departure(self):
        """Gets the departure of this AirData.


        :return: The departure of this AirData.
        :rtype: DepartureAir
        """
        return self._departure

    @departure.setter
    def departure(self, departure):
        """Sets the departure of this AirData.


        :param departure: The departure of this AirData.
        :type departure: DepartureAir
        """

        self._departure = departure

    @property
    def departure_airport_location(self):
        """Gets the departure_airport_location of this AirData.


        :return: The departure_airport_location of this AirData.
        :rtype: DepartureAirportLocation
        """
        return self._departure_airport_location

    @departure_airport_location.setter
    def departure_airport_location(self, departure_airport_location):
        """Sets the departure_airport_location of this AirData.


        :param departure_airport_location: The departure_airport_location of this AirData.
        :type departure_airport_location: DepartureAirportLocation
        """

        self._departure_airport_location = departure_airport_location

    @property
    def marketing(self):
        """Gets the marketing of this AirData.


        :return: The marketing of this AirData.
        :rtype: Marketing
        """
        return self._marketing

    @marketing.setter
    def marketing(self, marketing):
        """Sets the marketing of this AirData.


        :param marketing: The marketing of this AirData.
        :type marketing: Marketing
        """

        self._marketing = marketing

    @property
    def meal(self):
        """Gets the meal of this AirData.


        :return: The meal of this AirData.
        :rtype: Meal
        """
        return self._meal

    @meal.setter
    def meal(self, meal):
        """Sets the meal of this AirData.


        :param meal: The meal of this AirData.
        :type meal: Meal
        """

        self._meal = meal

    @property
    def operating(self):
        """Gets the operating of this AirData.


        :return: The operating of this AirData.
        :rtype: Operating
        """
        return self._operating

    @operating.setter
    def operating(self, operating):
        """Sets the operating of this AirData.


        :param operating: The operating of this AirData.
        :type operating: Operating
        """

        self._operating = operating

    @property
    def seats(self):
        """Gets the seats of this AirData.


        :return: The seats of this AirData.
        :rtype: List[AirDataSeatsInner]
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this AirData.


        :param seats: The seats of this AirData.
        :type seats: List[AirDataSeatsInner]
        """

        self._seats = seats
