# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.air_travel_document import AirTravelDocument
from openapi_server.models.associated_record import AssociatedRecord
from openapi_server.models.automated_process import AutomatedProcess
from openapi_server.models.contact import Contact
from openapi_server.models.flight_offer import FlightOffer
from openapi_server.models.form_of_identification import FormOfIdentification
from openapi_server.models.form_of_payment import FormOfPayment
from openapi_server.models.remarks import Remarks
from openapi_server.models.ticketing_agreement import TicketingAgreement
from openapi_server.models.traveler import Traveler
from openapi_server import util


class FlightOrder(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, associated_records: List[AssociatedRecord]=None, automated_process: List[AutomatedProcess]=None, contacts: List[Contact]=None, flight_offers: List[FlightOffer]=None, form_of_identifications: List[FormOfIdentification]=None, form_of_payments: List[FormOfPayment]=None, id: str=None, owner_office_id: str=None, queuing_office_id: str=None, remarks: Remarks=None, ticketing_agreement: TicketingAgreement=None, tickets: List[AirTravelDocument]=None, travelers: List[Traveler]=None, type: str=None):
        """FlightOrder - a model defined in OpenAPI

        :param associated_records: The associated_records of this FlightOrder.
        :param automated_process: The automated_process of this FlightOrder.
        :param contacts: The contacts of this FlightOrder.
        :param flight_offers: The flight_offers of this FlightOrder.
        :param form_of_identifications: The form_of_identifications of this FlightOrder.
        :param form_of_payments: The form_of_payments of this FlightOrder.
        :param id: The id of this FlightOrder.
        :param owner_office_id: The owner_office_id of this FlightOrder.
        :param queuing_office_id: The queuing_office_id of this FlightOrder.
        :param remarks: The remarks of this FlightOrder.
        :param ticketing_agreement: The ticketing_agreement of this FlightOrder.
        :param tickets: The tickets of this FlightOrder.
        :param travelers: The travelers of this FlightOrder.
        :param type: The type of this FlightOrder.
        """
        self.openapi_types = {
            'associated_records': List[AssociatedRecord],
            'automated_process': List[AutomatedProcess],
            'contacts': List[Contact],
            'flight_offers': List[FlightOffer],
            'form_of_identifications': List[FormOfIdentification],
            'form_of_payments': List[FormOfPayment],
            'id': str,
            'owner_office_id': str,
            'queuing_office_id': str,
            'remarks': Remarks,
            'ticketing_agreement': TicketingAgreement,
            'tickets': List[AirTravelDocument],
            'travelers': List[Traveler],
            'type': str
        }

        self.attribute_map = {
            'associated_records': 'associatedRecords',
            'automated_process': 'automatedProcess',
            'contacts': 'contacts',
            'flight_offers': 'flightOffers',
            'form_of_identifications': 'formOfIdentifications',
            'form_of_payments': 'formOfPayments',
            'id': 'id',
            'owner_office_id': 'ownerOfficeId',
            'queuing_office_id': 'queuingOfficeId',
            'remarks': 'remarks',
            'ticketing_agreement': 'ticketingAgreement',
            'tickets': 'tickets',
            'travelers': 'travelers',
            'type': 'type'
        }

        self._associated_records = associated_records
        self._automated_process = automated_process
        self._contacts = contacts
        self._flight_offers = flight_offers
        self._form_of_identifications = form_of_identifications
        self._form_of_payments = form_of_payments
        self._id = id
        self._owner_office_id = owner_office_id
        self._queuing_office_id = queuing_office_id
        self._remarks = remarks
        self._ticketing_agreement = ticketing_agreement
        self._tickets = tickets
        self._travelers = travelers
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FlightOrder':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FlightOrder of this FlightOrder.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associated_records(self):
        """Gets the associated_records of this FlightOrder.

        list of associated record

        :return: The associated_records of this FlightOrder.
        :rtype: List[AssociatedRecord]
        """
        return self._associated_records

    @associated_records.setter
    def associated_records(self, associated_records):
        """Sets the associated_records of this FlightOrder.

        list of associated record

        :param associated_records: The associated_records of this FlightOrder.
        :type associated_records: List[AssociatedRecord]
        """

        self._associated_records = associated_records

    @property
    def automated_process(self):
        """Gets the automated_process of this FlightOrder.

        list of automatic queuing

        :return: The automated_process of this FlightOrder.
        :rtype: List[AutomatedProcess]
        """
        return self._automated_process

    @automated_process.setter
    def automated_process(self, automated_process):
        """Sets the automated_process of this FlightOrder.

        list of automatic queuing

        :param automated_process: The automated_process of this FlightOrder.
        :type automated_process: List[AutomatedProcess]
        """
        if automated_process is not None and len(automated_process) > 31:
            raise ValueError("Invalid value for `automated_process`, number of items must be less than or equal to `31`")
        if automated_process is not None and len(automated_process) < 0:
            raise ValueError("Invalid value for `automated_process`, number of items must be greater than or equal to `0`")

        self._automated_process = automated_process

    @property
    def contacts(self):
        """Gets the contacts of this FlightOrder.

        list of general contact information

        :return: The contacts of this FlightOrder.
        :rtype: List[Contact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this FlightOrder.

        list of general contact information

        :param contacts: The contacts of this FlightOrder.
        :type contacts: List[Contact]
        """

        self._contacts = contacts

    @property
    def flight_offers(self):
        """Gets the flight_offers of this FlightOrder.

        list of flight offer

        :return: The flight_offers of this FlightOrder.
        :rtype: List[FlightOffer]
        """
        return self._flight_offers

    @flight_offers.setter
    def flight_offers(self, flight_offers):
        """Sets the flight_offers of this FlightOrder.

        list of flight offer

        :param flight_offers: The flight_offers of this FlightOrder.
        :type flight_offers: List[FlightOffer]
        """
        if flight_offers is None:
            raise ValueError("Invalid value for `flight_offers`, must not be `None`")
        if flight_offers is not None and len(flight_offers) > 6:
            raise ValueError("Invalid value for `flight_offers`, number of items must be less than or equal to `6`")
        if flight_offers is not None and len(flight_offers) < 1:
            raise ValueError("Invalid value for `flight_offers`, number of items must be greater than or equal to `1`")

        self._flight_offers = flight_offers

    @property
    def form_of_identifications(self):
        """Gets the form_of_identifications of this FlightOrder.

        list of forms of identifications applicable to travelers by airline

        :return: The form_of_identifications of this FlightOrder.
        :rtype: List[FormOfIdentification]
        """
        return self._form_of_identifications

    @form_of_identifications.setter
    def form_of_identifications(self, form_of_identifications):
        """Sets the form_of_identifications of this FlightOrder.

        list of forms of identifications applicable to travelers by airline

        :param form_of_identifications: The form_of_identifications of this FlightOrder.
        :type form_of_identifications: List[FormOfIdentification]
        """

        self._form_of_identifications = form_of_identifications

    @property
    def form_of_payments(self):
        """Gets the form_of_payments of this FlightOrder.

        list of form of payments

        :return: The form_of_payments of this FlightOrder.
        :rtype: List[FormOfPayment]
        """
        return self._form_of_payments

    @form_of_payments.setter
    def form_of_payments(self, form_of_payments):
        """Sets the form_of_payments of this FlightOrder.

        list of form of payments

        :param form_of_payments: The form_of_payments of this FlightOrder.
        :type form_of_payments: List[FormOfPayment]
        """
        if form_of_payments is not None and len(form_of_payments) > 6:
            raise ValueError("Invalid value for `form_of_payments`, number of items must be less than or equal to `6`")
        if form_of_payments is not None and len(form_of_payments) < 1:
            raise ValueError("Invalid value for `form_of_payments`, number of items must be greater than or equal to `1`")

        self._form_of_payments = form_of_payments

    @property
    def id(self):
        """Gets the id of this FlightOrder.

        unique identifier of the flight order

        :return: The id of this FlightOrder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlightOrder.

        unique identifier of the flight order

        :param id: The id of this FlightOrder.
        :type id: str
        """

        self._id = id

    @property
    def owner_office_id(self):
        """Gets the owner_office_id of this FlightOrder.

        office Id where will be transfered the ownership of the order

        :return: The owner_office_id of this FlightOrder.
        :rtype: str
        """
        return self._owner_office_id

    @owner_office_id.setter
    def owner_office_id(self, owner_office_id):
        """Sets the owner_office_id of this FlightOrder.

        office Id where will be transfered the ownership of the order

        :param owner_office_id: The owner_office_id of this FlightOrder.
        :type owner_office_id: str
        """

        self._owner_office_id = owner_office_id

    @property
    def queuing_office_id(self):
        """Gets the queuing_office_id of this FlightOrder.

        office Id where to queue the order

        :return: The queuing_office_id of this FlightOrder.
        :rtype: str
        """
        return self._queuing_office_id

    @queuing_office_id.setter
    def queuing_office_id(self, queuing_office_id):
        """Sets the queuing_office_id of this FlightOrder.

        office Id where to queue the order

        :param queuing_office_id: The queuing_office_id of this FlightOrder.
        :type queuing_office_id: str
        """

        self._queuing_office_id = queuing_office_id

    @property
    def remarks(self):
        """Gets the remarks of this FlightOrder.


        :return: The remarks of this FlightOrder.
        :rtype: Remarks
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this FlightOrder.


        :param remarks: The remarks of this FlightOrder.
        :type remarks: Remarks
        """

        self._remarks = remarks

    @property
    def ticketing_agreement(self):
        """Gets the ticketing_agreement of this FlightOrder.


        :return: The ticketing_agreement of this FlightOrder.
        :rtype: TicketingAgreement
        """
        return self._ticketing_agreement

    @ticketing_agreement.setter
    def ticketing_agreement(self, ticketing_agreement):
        """Sets the ticketing_agreement of this FlightOrder.


        :param ticketing_agreement: The ticketing_agreement of this FlightOrder.
        :type ticketing_agreement: TicketingAgreement
        """

        self._ticketing_agreement = ticketing_agreement

    @property
    def tickets(self):
        """Gets the tickets of this FlightOrder.

        list of tickets

        :return: The tickets of this FlightOrder.
        :rtype: List[AirTravelDocument]
        """
        return self._tickets

    @tickets.setter
    def tickets(self, tickets):
        """Sets the tickets of this FlightOrder.

        list of tickets

        :param tickets: The tickets of this FlightOrder.
        :type tickets: List[AirTravelDocument]
        """

        self._tickets = tickets

    @property
    def travelers(self):
        """Gets the travelers of this FlightOrder.

        list of travelers

        :return: The travelers of this FlightOrder.
        :rtype: List[Traveler]
        """
        return self._travelers

    @travelers.setter
    def travelers(self, travelers):
        """Sets the travelers of this FlightOrder.

        list of travelers

        :param travelers: The travelers of this FlightOrder.
        :type travelers: List[Traveler]
        """
        if travelers is not None and len(travelers) > 18:
            raise ValueError("Invalid value for `travelers`, number of items must be less than or equal to `18`")
        if travelers is not None and len(travelers) < 1:
            raise ValueError("Invalid value for `travelers`, number of items must be greater than or equal to `1`")

        self._travelers = travelers

    @property
    def type(self):
        """Gets the type of this FlightOrder.

        the resource name

        :return: The type of this FlightOrder.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FlightOrder.

        the resource name

        :param type: The type of this FlightOrder.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
