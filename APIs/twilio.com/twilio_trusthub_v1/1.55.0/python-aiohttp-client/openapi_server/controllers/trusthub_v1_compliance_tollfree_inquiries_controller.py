from typing import List, Dict
from aiohttp import web

from openapi_server.models.compliance_tollfree_inquiry_enum_opt_in_type import ComplianceTollfreeInquiryEnumOptInType
from openapi_server.models.trusthub_v1_compliance_tollfree_inquiry import TrusthubV1ComplianceTollfreeInquiry
from openapi_server import util


async def create_compliance_tollfree_inquiry(request: web.Request, notification_email, tollfree_phone_number, additional_information=None, business_city=None, business_contact_email=None, business_contact_first_name=None, business_contact_last_name=None, business_contact_phone=None, business_country=None, business_name=None, business_postal_code=None, business_state_province_region=None, business_street_address=None, business_street_address2=None, business_website=None, message_volume=None, opt_in_image_urls=None, opt_in_type=None, production_message_sample=None, use_case_categories=None, use_case_summary=None) -> web.Response:
    """create_compliance_tollfree_inquiry

    Create a new Compliance Tollfree Verification Inquiry for the authenticated account. This is necessary to start a new embedded session.

    :param notification_email: The email address to receive the notification about the verification result.
    :type notification_email: str
    :param tollfree_phone_number: The Tollfree phone number to be verified
    :type tollfree_phone_number: str
    :param additional_information: Additional information to be provided for verification.
    :type additional_information: str
    :param business_city: The city of the business or organization using the Tollfree number.
    :type business_city: str
    :param business_contact_email: The email address of the contact for the business or organization using the Tollfree number.
    :type business_contact_email: str
    :param business_contact_first_name: The first name of the contact for the business or organization using the Tollfree number.
    :type business_contact_first_name: str
    :param business_contact_last_name: The last name of the contact for the business or organization using the Tollfree number.
    :type business_contact_last_name: str
    :param business_contact_phone: The phone number of the contact for the business or organization using the Tollfree number.
    :type business_contact_phone: str
    :param business_country: The country of the business or organization using the Tollfree number.
    :type business_country: str
    :param business_name: The name of the business or organization using the Tollfree number.
    :type business_name: str
    :param business_postal_code: The postal code of the business or organization using the Tollfree number.
    :type business_postal_code: str
    :param business_state_province_region: The state/province/region of the business or organization using the Tollfree number.
    :type business_state_province_region: str
    :param business_street_address: The address of the business or organization using the Tollfree number.
    :type business_street_address: str
    :param business_street_address2: The address of the business or organization using the Tollfree number.
    :type business_street_address2: str
    :param business_website: The website of the business or organization using the Tollfree number.
    :type business_website: str
    :param message_volume: Estimate monthly volume of messages from the Tollfree Number.
    :type message_volume: str
    :param opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    :type opt_in_image_urls: List[str]
    :param opt_in_type: 
    :type opt_in_type: str
    :param production_message_sample: An example of message content, i.e. a sample message.
    :type production_message_sample: str
    :param use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
    :type use_case_categories: List[str]
    :param use_case_summary: Use this to further explain how messaging is used by the business or organization.
    :type use_case_summary: str

    """
    return web.Response(status=200)
