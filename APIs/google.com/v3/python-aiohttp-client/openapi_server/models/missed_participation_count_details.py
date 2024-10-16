# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.no_price_count_details import NoPriceCountDetails
from openapi_server.models.price_missing_count_details import PriceMissingCountDetails
from openapi_server.models.price_problem_count_details import PriceProblemCountDetails
from openapi_server.models.price_unavailable_count_details import PriceUnavailableCountDetails
from openapi_server import util


class MissedParticipationCountDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hotel_suspended_count: str=None, no_availability_count: str=None, no_landing_page_count: str=None, no_price_count: str=None, no_price_count_details: NoPriceCountDetails=None, no_tax_breakdown_count: str=None, other_reason_count: str=None, price_missing_count: str=None, price_missing_count_details: PriceMissingCountDetails=None, price_problem_count: str=None, price_problem_count_details: PriceProblemCountDetails=None, price_unavailable_count: str=None, price_unavailable_count_details: PriceUnavailableCountDetails=None):
        """MissedParticipationCountDetails - a model defined in OpenAPI

        :param hotel_suspended_count: The hotel_suspended_count of this MissedParticipationCountDetails.
        :param no_availability_count: The no_availability_count of this MissedParticipationCountDetails.
        :param no_landing_page_count: The no_landing_page_count of this MissedParticipationCountDetails.
        :param no_price_count: The no_price_count of this MissedParticipationCountDetails.
        :param no_price_count_details: The no_price_count_details of this MissedParticipationCountDetails.
        :param no_tax_breakdown_count: The no_tax_breakdown_count of this MissedParticipationCountDetails.
        :param other_reason_count: The other_reason_count of this MissedParticipationCountDetails.
        :param price_missing_count: The price_missing_count of this MissedParticipationCountDetails.
        :param price_missing_count_details: The price_missing_count_details of this MissedParticipationCountDetails.
        :param price_problem_count: The price_problem_count of this MissedParticipationCountDetails.
        :param price_problem_count_details: The price_problem_count_details of this MissedParticipationCountDetails.
        :param price_unavailable_count: The price_unavailable_count of this MissedParticipationCountDetails.
        :param price_unavailable_count_details: The price_unavailable_count_details of this MissedParticipationCountDetails.
        """
        self.openapi_types = {
            'hotel_suspended_count': str,
            'no_availability_count': str,
            'no_landing_page_count': str,
            'no_price_count': str,
            'no_price_count_details': NoPriceCountDetails,
            'no_tax_breakdown_count': str,
            'other_reason_count': str,
            'price_missing_count': str,
            'price_missing_count_details': PriceMissingCountDetails,
            'price_problem_count': str,
            'price_problem_count_details': PriceProblemCountDetails,
            'price_unavailable_count': str,
            'price_unavailable_count_details': PriceUnavailableCountDetails
        }

        self.attribute_map = {
            'hotel_suspended_count': 'hotelSuspendedCount',
            'no_availability_count': 'noAvailabilityCount',
            'no_landing_page_count': 'noLandingPageCount',
            'no_price_count': 'noPriceCount',
            'no_price_count_details': 'noPriceCountDetails',
            'no_tax_breakdown_count': 'noTaxBreakdownCount',
            'other_reason_count': 'otherReasonCount',
            'price_missing_count': 'priceMissingCount',
            'price_missing_count_details': 'priceMissingCountDetails',
            'price_problem_count': 'priceProblemCount',
            'price_problem_count_details': 'priceProblemCountDetails',
            'price_unavailable_count': 'priceUnavailableCount',
            'price_unavailable_count_details': 'priceUnavailableCountDetails'
        }

        self._hotel_suspended_count = hotel_suspended_count
        self._no_availability_count = no_availability_count
        self._no_landing_page_count = no_landing_page_count
        self._no_price_count = no_price_count
        self._no_price_count_details = no_price_count_details
        self._no_tax_breakdown_count = no_tax_breakdown_count
        self._other_reason_count = other_reason_count
        self._price_missing_count = price_missing_count
        self._price_missing_count_details = price_missing_count_details
        self._price_problem_count = price_problem_count
        self._price_problem_count_details = price_problem_count_details
        self._price_unavailable_count = price_unavailable_count
        self._price_unavailable_count_details = price_unavailable_count_details

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MissedParticipationCountDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MissedParticipationCountDetails of this MissedParticipationCountDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hotel_suspended_count(self):
        """Gets the hotel_suspended_count of this MissedParticipationCountDetails.

        The total number of missed participations due to one or more of your hotels being suspended due to price accuracy violations.

        :return: The hotel_suspended_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._hotel_suspended_count

    @hotel_suspended_count.setter
    def hotel_suspended_count(self, hotel_suspended_count):
        """Sets the hotel_suspended_count of this MissedParticipationCountDetails.

        The total number of missed participations due to one or more of your hotels being suspended due to price accuracy violations.

        :param hotel_suspended_count: The hotel_suspended_count of this MissedParticipationCountDetails.
        :type hotel_suspended_count: str
        """

        self._hotel_suspended_count = hotel_suspended_count

    @property
    def no_availability_count(self):
        """Gets the no_availability_count of this MissedParticipationCountDetails.

        The total number of missed participation due to the hotel/itinerary combination being unavailable, or the traveler was ineligible for the rates. To participate in these auctions, you may need to provide more pricing information.

        :return: The no_availability_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._no_availability_count

    @no_availability_count.setter
    def no_availability_count(self, no_availability_count):
        """Sets the no_availability_count of this MissedParticipationCountDetails.

        The total number of missed participation due to the hotel/itinerary combination being unavailable, or the traveler was ineligible for the rates. To participate in these auctions, you may need to provide more pricing information.

        :param no_availability_count: The no_availability_count of this MissedParticipationCountDetails.
        :type no_availability_count: str
        """

        self._no_availability_count = no_availability_count

    @property
    def no_landing_page_count(self):
        """Gets the no_landing_page_count of this MissedParticipationCountDetails.

        No landing page matched the user.

        :return: The no_landing_page_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._no_landing_page_count

    @no_landing_page_count.setter
    def no_landing_page_count(self, no_landing_page_count):
        """Sets the no_landing_page_count of this MissedParticipationCountDetails.

        No landing page matched the user.

        :param no_landing_page_count: The no_landing_page_count of this MissedParticipationCountDetails.
        :type no_landing_page_count: str
        """

        self._no_landing_page_count = no_landing_page_count

    @property
    def no_price_count(self):
        """Gets the no_price_count of this MissedParticipationCountDetails.

        The total number of missed participations due to a price not being offered for the requested itinerary.

        :return: The no_price_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._no_price_count

    @no_price_count.setter
    def no_price_count(self, no_price_count):
        """Sets the no_price_count of this MissedParticipationCountDetails.

        The total number of missed participations due to a price not being offered for the requested itinerary.

        :param no_price_count: The no_price_count of this MissedParticipationCountDetails.
        :type no_price_count: str
        """

        self._no_price_count = no_price_count

    @property
    def no_price_count_details(self):
        """Gets the no_price_count_details of this MissedParticipationCountDetails.


        :return: The no_price_count_details of this MissedParticipationCountDetails.
        :rtype: NoPriceCountDetails
        """
        return self._no_price_count_details

    @no_price_count_details.setter
    def no_price_count_details(self, no_price_count_details):
        """Sets the no_price_count_details of this MissedParticipationCountDetails.


        :param no_price_count_details: The no_price_count_details of this MissedParticipationCountDetails.
        :type no_price_count_details: NoPriceCountDetails
        """

        self._no_price_count_details = no_price_count_details

    @property
    def no_tax_breakdown_count(self):
        """Gets the no_tax_breakdown_count of this MissedParticipationCountDetails.

        The total number of missed participation due to one or more of your hotels not specifying taxes and fees separately.

        :return: The no_tax_breakdown_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._no_tax_breakdown_count

    @no_tax_breakdown_count.setter
    def no_tax_breakdown_count(self, no_tax_breakdown_count):
        """Sets the no_tax_breakdown_count of this MissedParticipationCountDetails.

        The total number of missed participation due to one or more of your hotels not specifying taxes and fees separately.

        :param no_tax_breakdown_count: The no_tax_breakdown_count of this MissedParticipationCountDetails.
        :type no_tax_breakdown_count: str
        """

        self._no_tax_breakdown_count = no_tax_breakdown_count

    @property
    def other_reason_count(self):
        """Gets the other_reason_count of this MissedParticipationCountDetails.

        Hotel did not participate for an unknown reason.

        :return: The other_reason_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._other_reason_count

    @other_reason_count.setter
    def other_reason_count(self, other_reason_count):
        """Sets the other_reason_count of this MissedParticipationCountDetails.

        Hotel did not participate for an unknown reason.

        :param other_reason_count: The other_reason_count of this MissedParticipationCountDetails.
        :type other_reason_count: str
        """

        self._other_reason_count = other_reason_count

    @property
    def price_missing_count(self):
        """Gets the price_missing_count of this MissedParticipationCountDetails.

        The total number of missed participations due to either a price not being present in Google's cache or failing to successfully respond to live pricing. Comprised of the following: * Bandwidth depleted * Cache rate missing * Itinerary blocked * Live pricing not set up * Live pricing timeout * Live pricing error

        :return: The price_missing_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._price_missing_count

    @price_missing_count.setter
    def price_missing_count(self, price_missing_count):
        """Sets the price_missing_count of this MissedParticipationCountDetails.

        The total number of missed participations due to either a price not being present in Google's cache or failing to successfully respond to live pricing. Comprised of the following: * Bandwidth depleted * Cache rate missing * Itinerary blocked * Live pricing not set up * Live pricing timeout * Live pricing error

        :param price_missing_count: The price_missing_count of this MissedParticipationCountDetails.
        :type price_missing_count: str
        """

        self._price_missing_count = price_missing_count

    @property
    def price_missing_count_details(self):
        """Gets the price_missing_count_details of this MissedParticipationCountDetails.


        :return: The price_missing_count_details of this MissedParticipationCountDetails.
        :rtype: PriceMissingCountDetails
        """
        return self._price_missing_count_details

    @price_missing_count_details.setter
    def price_missing_count_details(self, price_missing_count_details):
        """Sets the price_missing_count_details of this MissedParticipationCountDetails.


        :param price_missing_count_details: The price_missing_count_details of this MissedParticipationCountDetails.
        :type price_missing_count_details: PriceMissingCountDetails
        """

        self._price_missing_count_details = price_missing_count_details

    @property
    def price_problem_count(self):
        """Gets the price_problem_count of this MissedParticipationCountDetails.

        The total number of missed participation due to an issue with the accuracy of the price provided for the itinerary. Comprised of the following: * Hotel suspended * Price unusually high * Price unusually low * Taxes and feeds missing

        :return: The price_problem_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._price_problem_count

    @price_problem_count.setter
    def price_problem_count(self, price_problem_count):
        """Sets the price_problem_count of this MissedParticipationCountDetails.

        The total number of missed participation due to an issue with the accuracy of the price provided for the itinerary. Comprised of the following: * Hotel suspended * Price unusually high * Price unusually low * Taxes and feeds missing

        :param price_problem_count: The price_problem_count of this MissedParticipationCountDetails.
        :type price_problem_count: str
        """

        self._price_problem_count = price_problem_count

    @property
    def price_problem_count_details(self):
        """Gets the price_problem_count_details of this MissedParticipationCountDetails.


        :return: The price_problem_count_details of this MissedParticipationCountDetails.
        :rtype: PriceProblemCountDetails
        """
        return self._price_problem_count_details

    @price_problem_count_details.setter
    def price_problem_count_details(self, price_problem_count_details):
        """Sets the price_problem_count_details of this MissedParticipationCountDetails.


        :param price_problem_count_details: The price_problem_count_details of this MissedParticipationCountDetails.
        :type price_problem_count_details: PriceProblemCountDetails
        """

        self._price_problem_count_details = price_problem_count_details

    @property
    def price_unavailable_count(self):
        """Gets the price_unavailable_count of this MissedParticipationCountDetails.

        The total number of missed participation due to price listed as unavailable (-1) for the requested itinerary. Comprised of the following: * Price unavailable * Participation not likely * Other

        :return: The price_unavailable_count of this MissedParticipationCountDetails.
        :rtype: str
        """
        return self._price_unavailable_count

    @price_unavailable_count.setter
    def price_unavailable_count(self, price_unavailable_count):
        """Sets the price_unavailable_count of this MissedParticipationCountDetails.

        The total number of missed participation due to price listed as unavailable (-1) for the requested itinerary. Comprised of the following: * Price unavailable * Participation not likely * Other

        :param price_unavailable_count: The price_unavailable_count of this MissedParticipationCountDetails.
        :type price_unavailable_count: str
        """

        self._price_unavailable_count = price_unavailable_count

    @property
    def price_unavailable_count_details(self):
        """Gets the price_unavailable_count_details of this MissedParticipationCountDetails.


        :return: The price_unavailable_count_details of this MissedParticipationCountDetails.
        :rtype: PriceUnavailableCountDetails
        """
        return self._price_unavailable_count_details

    @price_unavailable_count_details.setter
    def price_unavailable_count_details(self, price_unavailable_count_details):
        """Sets the price_unavailable_count_details of this MissedParticipationCountDetails.


        :param price_unavailable_count_details: The price_unavailable_count_details of this MissedParticipationCountDetails.
        :type price_unavailable_count_details: PriceUnavailableCountDetails
        """

        self._price_unavailable_count_details = price_unavailable_count_details
