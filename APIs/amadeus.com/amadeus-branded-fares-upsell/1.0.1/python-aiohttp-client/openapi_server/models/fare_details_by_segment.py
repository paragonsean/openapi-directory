# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.additional_services_request import AdditionalServicesRequest
from openapi_server.models.allotment_details import AllotmentDetails
from openapi_server.models.amenity import Amenity
from openapi_server.models.baggage_allowance import BaggageAllowance
from openapi_server.models.slice_dice_indicator import SliceDiceIndicator
from openapi_server.models.travel_class import TravelClass
import re
from openapi_server import util


class FareDetailsBySegment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_services: AdditionalServicesRequest=None, allotment_details: AllotmentDetails=None, amenities: List[Amenity]=None, branded_fare: str=None, cabin: TravelClass=None, _class: str=None, fare_basis: str=None, included_checked_bags: BaggageAllowance=None, is_allotment: bool=None, segment_id: str=None, slice_dice_indicator: SliceDiceIndicator=None):
        """FareDetailsBySegment - a model defined in OpenAPI

        :param additional_services: The additional_services of this FareDetailsBySegment.
        :param allotment_details: The allotment_details of this FareDetailsBySegment.
        :param amenities: The amenities of this FareDetailsBySegment.
        :param branded_fare: The branded_fare of this FareDetailsBySegment.
        :param cabin: The cabin of this FareDetailsBySegment.
        :param _class: The _class of this FareDetailsBySegment.
        :param fare_basis: The fare_basis of this FareDetailsBySegment.
        :param included_checked_bags: The included_checked_bags of this FareDetailsBySegment.
        :param is_allotment: The is_allotment of this FareDetailsBySegment.
        :param segment_id: The segment_id of this FareDetailsBySegment.
        :param slice_dice_indicator: The slice_dice_indicator of this FareDetailsBySegment.
        """
        self.openapi_types = {
            'additional_services': AdditionalServicesRequest,
            'allotment_details': AllotmentDetails,
            'amenities': List[Amenity],
            'branded_fare': str,
            'cabin': TravelClass,
            '_class': str,
            'fare_basis': str,
            'included_checked_bags': BaggageAllowance,
            'is_allotment': bool,
            'segment_id': str,
            'slice_dice_indicator': SliceDiceIndicator
        }

        self.attribute_map = {
            'additional_services': 'additionalServices',
            'allotment_details': 'allotmentDetails',
            'amenities': 'amenities',
            'branded_fare': 'brandedFare',
            'cabin': 'cabin',
            '_class': 'class',
            'fare_basis': 'fareBasis',
            'included_checked_bags': 'includedCheckedBags',
            'is_allotment': 'isAllotment',
            'segment_id': 'segmentId',
            'slice_dice_indicator': 'sliceDiceIndicator'
        }

        self._additional_services = additional_services
        self._allotment_details = allotment_details
        self._amenities = amenities
        self._branded_fare = branded_fare
        self._cabin = cabin
        self.__class = _class
        self._fare_basis = fare_basis
        self._included_checked_bags = included_checked_bags
        self._is_allotment = is_allotment
        self._segment_id = segment_id
        self._slice_dice_indicator = slice_dice_indicator

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FareDetailsBySegment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FareDetailsBySegment of this FareDetailsBySegment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_services(self):
        """Gets the additional_services of this FareDetailsBySegment.


        :return: The additional_services of this FareDetailsBySegment.
        :rtype: AdditionalServicesRequest
        """
        return self._additional_services

    @additional_services.setter
    def additional_services(self, additional_services):
        """Sets the additional_services of this FareDetailsBySegment.


        :param additional_services: The additional_services of this FareDetailsBySegment.
        :type additional_services: AdditionalServicesRequest
        """

        self._additional_services = additional_services

    @property
    def allotment_details(self):
        """Gets the allotment_details of this FareDetailsBySegment.


        :return: The allotment_details of this FareDetailsBySegment.
        :rtype: AllotmentDetails
        """
        return self._allotment_details

    @allotment_details.setter
    def allotment_details(self, allotment_details):
        """Sets the allotment_details of this FareDetailsBySegment.


        :param allotment_details: The allotment_details of this FareDetailsBySegment.
        :type allotment_details: AllotmentDetails
        """

        self._allotment_details = allotment_details

    @property
    def amenities(self):
        """Gets the amenities of this FareDetailsBySegment.


        :return: The amenities of this FareDetailsBySegment.
        :rtype: List[Amenity]
        """
        return self._amenities

    @amenities.setter
    def amenities(self, amenities):
        """Sets the amenities of this FareDetailsBySegment.


        :param amenities: The amenities of this FareDetailsBySegment.
        :type amenities: List[Amenity]
        """

        self._amenities = amenities

    @property
    def branded_fare(self):
        """Gets the branded_fare of this FareDetailsBySegment.

        The name of the Fare Family corresponding to the fares. Only for the GDS provider and if the airline has fare families filled

        :return: The branded_fare of this FareDetailsBySegment.
        :rtype: str
        """
        return self._branded_fare

    @branded_fare.setter
    def branded_fare(self, branded_fare):
        """Sets the branded_fare of this FareDetailsBySegment.

        The name of the Fare Family corresponding to the fares. Only for the GDS provider and if the airline has fare families filled

        :param branded_fare: The branded_fare of this FareDetailsBySegment.
        :type branded_fare: str
        """

        self._branded_fare = branded_fare

    @property
    def cabin(self):
        """Gets the cabin of this FareDetailsBySegment.


        :return: The cabin of this FareDetailsBySegment.
        :rtype: TravelClass
        """
        return self._cabin

    @cabin.setter
    def cabin(self, cabin):
        """Sets the cabin of this FareDetailsBySegment.


        :param cabin: The cabin of this FareDetailsBySegment.
        :type cabin: TravelClass
        """

        self._cabin = cabin

    @property
    def _class(self):
        """Gets the _class of this FareDetailsBySegment.

        The code of the booking class, a.k.a. class of service or Reservations/Booking Designator (RBD)

        :return: The _class of this FareDetailsBySegment.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this FareDetailsBySegment.

        The code of the booking class, a.k.a. class of service or Reservations/Booking Designator (RBD)

        :param _class: The _class of this FareDetailsBySegment.
        :type _class: str
        """
        if _class is not None and not re.search(r'[A-Z]{1}', _class):
            raise ValueError("Invalid value for `_class`, must be a follow pattern or equal to `/[A-Z]{1}/`")

        self.__class = _class

    @property
    def fare_basis(self):
        """Gets the fare_basis of this FareDetailsBySegment.

        Fare basis specifying the rules of a fare. Usually, though not always, is composed of the booking class code followed by a set of letters and digits representing other characteristics of the ticket, such as refundability, minimum stay requirements, discounts or special promotional elements.

        :return: The fare_basis of this FareDetailsBySegment.
        :rtype: str
        """
        return self._fare_basis

    @fare_basis.setter
    def fare_basis(self, fare_basis):
        """Sets the fare_basis of this FareDetailsBySegment.

        Fare basis specifying the rules of a fare. Usually, though not always, is composed of the booking class code followed by a set of letters and digits representing other characteristics of the ticket, such as refundability, minimum stay requirements, discounts or special promotional elements.

        :param fare_basis: The fare_basis of this FareDetailsBySegment.
        :type fare_basis: str
        """
        if fare_basis is not None and not re.search(r'[[A-Z0-9]{1,18}', fare_basis):
            raise ValueError("Invalid value for `fare_basis`, must be a follow pattern or equal to `/[[A-Z0-9]{1,18}/`")

        self._fare_basis = fare_basis

    @property
    def included_checked_bags(self):
        """Gets the included_checked_bags of this FareDetailsBySegment.


        :return: The included_checked_bags of this FareDetailsBySegment.
        :rtype: BaggageAllowance
        """
        return self._included_checked_bags

    @included_checked_bags.setter
    def included_checked_bags(self, included_checked_bags):
        """Sets the included_checked_bags of this FareDetailsBySegment.


        :param included_checked_bags: The included_checked_bags of this FareDetailsBySegment.
        :type included_checked_bags: BaggageAllowance
        """

        self._included_checked_bags = included_checked_bags

    @property
    def is_allotment(self):
        """Gets the is_allotment of this FareDetailsBySegment.

        True if the corresponding booking class is in an allotment

        :return: The is_allotment of this FareDetailsBySegment.
        :rtype: bool
        """
        return self._is_allotment

    @is_allotment.setter
    def is_allotment(self, is_allotment):
        """Sets the is_allotment of this FareDetailsBySegment.

        True if the corresponding booking class is in an allotment

        :param is_allotment: The is_allotment of this FareDetailsBySegment.
        :type is_allotment: bool
        """

        self._is_allotment = is_allotment

    @property
    def segment_id(self):
        """Gets the segment_id of this FareDetailsBySegment.

        Id of the segment

        :return: The segment_id of this FareDetailsBySegment.
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this FareDetailsBySegment.

        Id of the segment

        :param segment_id: The segment_id of this FareDetailsBySegment.
        :type segment_id: str
        """
        if segment_id is None:
            raise ValueError("Invalid value for `segment_id`, must not be `None`")

        self._segment_id = segment_id

    @property
    def slice_dice_indicator(self):
        """Gets the slice_dice_indicator of this FareDetailsBySegment.


        :return: The slice_dice_indicator of this FareDetailsBySegment.
        :rtype: SliceDiceIndicator
        """
        return self._slice_dice_indicator

    @slice_dice_indicator.setter
    def slice_dice_indicator(self, slice_dice_indicator):
        """Sets the slice_dice_indicator of this FareDetailsBySegment.


        :param slice_dice_indicator: The slice_dice_indicator of this FareDetailsBySegment.
        :type slice_dice_indicator: SliceDiceIndicator
        """

        self._slice_dice_indicator = slice_dice_indicator
