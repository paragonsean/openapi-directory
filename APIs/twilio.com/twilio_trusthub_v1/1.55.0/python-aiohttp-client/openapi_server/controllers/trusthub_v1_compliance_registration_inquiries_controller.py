from typing import List, Dict
from aiohttp import web

from openapi_server.models.compliance_registration_enum_business_identity_type import ComplianceRegistrationEnumBusinessIdentityType
from openapi_server.models.compliance_registration_enum_business_registration_authority import ComplianceRegistrationEnumBusinessRegistrationAuthority
from openapi_server.models.compliance_registration_enum_end_user_type import ComplianceRegistrationEnumEndUserType
from openapi_server.models.compliance_registration_enum_phone_number_type import ComplianceRegistrationEnumPhoneNumberType
from openapi_server.models.trusthub_v1_compliance_registration import TrusthubV1ComplianceRegistration
from openapi_server import util


async def create_compliance_registration(request: web.Request, end_user_type, phone_number_type, accepted_notification_receipt=None, address_city=None, address_country_code=None, address_postal_code=None, address_street=None, address_street_secondary=None, address_subdivision=None, authorized_representative1_date_of_birth=None, authorized_representative1_email=None, authorized_representative1_first_name=None, authorized_representative1_last_name=None, authorized_representative1_phone=None, business_identity_type=None, business_legal_name=None, business_registration_authority=None, business_registration_number=None, business_website_url=None, date_of_birth=None, emergency_address_city=None, emergency_address_country_code=None, emergency_address_postal_code=None, emergency_address_street=None, emergency_address_street_secondary=None, emergency_address_subdivision=None, file=None, file_name=None, first_name=None, friendly_name=None, individual_email=None, individual_phone=None, is_isv_embed=None, last_name=None, notification_email=None, use_address_as_emergency_address=None) -> web.Response:
    """create_compliance_registration

    Create a new Compliance Registration Inquiry for the authenticated account. This is necessary to start a new embedded session.

    :param end_user_type: 
    :type end_user_type: str
    :param phone_number_type: 
    :type phone_number_type: str
    :param accepted_notification_receipt: The email address to receive the notification about the verification result.
    :type accepted_notification_receipt: bool
    :param address_city: City of the business
    :type address_city: str
    :param address_country_code: Country code of the business
    :type address_country_code: str
    :param address_postal_code: Postal code of the business
    :type address_postal_code: str
    :param address_street: Street address of the business
    :type address_street: str
    :param address_street_secondary: Street address of the business
    :type address_street_secondary: str
    :param address_subdivision: State or province of the business
    :type address_subdivision: str
    :param authorized_representative1_date_of_birth: Birthdate of the authorized representative
    :type authorized_representative1_date_of_birth: str
    :param authorized_representative1_email: Email address of the authorized representative
    :type authorized_representative1_email: str
    :param authorized_representative1_first_name: First name of the authorized representative
    :type authorized_representative1_first_name: str
    :param authorized_representative1_last_name: Last name of the authorized representative
    :type authorized_representative1_last_name: str
    :param authorized_representative1_phone: Phone number of the authorized representative
    :type authorized_representative1_phone: str
    :param business_identity_type: 
    :type business_identity_type: str
    :param business_legal_name: he name of the business or organization using the Tollfree number.
    :type business_legal_name: str
    :param business_registration_authority: 
    :type business_registration_authority: str
    :param business_registration_number: Business registration number of the business
    :type business_registration_number: str
    :param business_website_url: The URL of the business website
    :type business_website_url: str
    :param date_of_birth: The date of birth of the Individual User.
    :type date_of_birth: str
    :param emergency_address_city: City of the business
    :type emergency_address_city: str
    :param emergency_address_country_code: Country code of the business
    :type emergency_address_country_code: str
    :param emergency_address_postal_code: Postal code of the business
    :type emergency_address_postal_code: str
    :param emergency_address_street: Street address of the business
    :type emergency_address_street: str
    :param emergency_address_street_secondary: Street address of the business
    :type emergency_address_street_secondary: str
    :param emergency_address_subdivision: State or province of the business
    :type emergency_address_subdivision: str
    :param file: The verification document to upload
    :type file: str
    :param file_name: The name of the verification document to upload
    :type file_name: str
    :param first_name: The first name of the Individual User.
    :type first_name: str
    :param friendly_name: Friendly name for your business information
    :type friendly_name: str
    :param individual_email: The email address of the Individual User.
    :type individual_email: str
    :param individual_phone: The phone number of the Individual User.
    :type individual_phone: str
    :param is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
    :type is_isv_embed: bool
    :param last_name: The last name of the Individual User.
    :type last_name: str
    :param notification_email: he email address to receive the notification about the verification result.
    :type notification_email: str
    :param use_address_as_emergency_address: Use the business address as the emergency address
    :type use_address_as_emergency_address: bool

    """
    return web.Response(status=200)
