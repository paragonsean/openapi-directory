from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_tollfree_verification_response import ListTollfreeVerificationResponse
from openapi_server.models.messaging_v1_tollfree_verification import MessagingV1TollfreeVerification
from openapi_server.models.tollfree_verification_enum_opt_in_type import TollfreeVerificationEnumOptInType
from openapi_server.models.tollfree_verification_enum_status import TollfreeVerificationEnumStatus
from openapi_server import util


async def create_tollfree_verification(request: web.Request, business_name, business_website, message_volume, notification_email, opt_in_image_urls, opt_in_type, production_message_sample, tollfree_phone_number_sid, use_case_categories, use_case_summary, additional_information=None, business_city=None, business_contact_email=None, business_contact_first_name=None, business_contact_last_name=None, business_contact_phone=None, business_country=None, business_postal_code=None, business_state_province_region=None, business_street_address=None, business_street_address2=None, customer_profile_sid=None, external_reference_id=None) -> web.Response:
    """create_tollfree_verification

    

    :param business_name: The name of the business or organization using the Tollfree number.
    :type business_name: str
    :param business_website: The website of the business or organization using the Tollfree number.
    :type business_website: str
    :param message_volume: Estimate monthly volume of messages from the Tollfree Number.
    :type message_volume: str
    :param notification_email: The email address to receive the notification about the verification result. .
    :type notification_email: str
    :param opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    :type opt_in_image_urls: List[str]
    :param opt_in_type: 
    :type opt_in_type: str
    :param production_message_sample: An example of message content, i.e. a sample message.
    :type production_message_sample: str
    :param tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
    :type tollfree_phone_number_sid: str
    :param use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
    :type use_case_categories: List[str]
    :param use_case_summary: Use this to further explain how messaging is used by the business or organization.
    :type use_case_summary: str
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
    :param business_contact_phone: The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.
    :type business_contact_phone: str
    :param business_country: The country of the business or organization using the Tollfree number.
    :type business_country: str
    :param business_postal_code: The postal code of the business or organization using the Tollfree number.
    :type business_postal_code: str
    :param business_state_province_region: The state/province/region of the business or organization using the Tollfree number.
    :type business_state_province_region: str
    :param business_street_address: The address of the business or organization using the Tollfree number.
    :type business_street_address: str
    :param business_street_address2: The address of the business or organization using the Tollfree number.
    :type business_street_address2: str
    :param customer_profile_sid: Customer&#39;s Profile Bundle BundleSid.
    :type customer_profile_sid: str
    :param external_reference_id: An optional external reference ID supplied by customer and echoed back on status retrieval.
    :type external_reference_id: str

    """
    return web.Response(status=200)


async def delete_tollfree_verification(request: web.Request, sid) -> web.Response:
    """delete_tollfree_verification

    

    :param sid: The unique string to identify Tollfree Verification.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_tollfree_verification(request: web.Request, sid) -> web.Response:
    """fetch_tollfree_verification

    

    :param sid: The unique string to identify Tollfree Verification.
    :type sid: str

    """
    return web.Response(status=200)


async def list_tollfree_verification(request: web.Request, tollfree_phone_number_sid=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_tollfree_verification

    

    :param tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
    :type tollfree_phone_number_sid: str
    :param status: The compliance status of the Tollfree Verification record.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_tollfree_verification(request: web.Request, sid, additional_information=None, business_city=None, business_contact_email=None, business_contact_first_name=None, business_contact_last_name=None, business_contact_phone=None, business_country=None, business_name=None, business_postal_code=None, business_state_province_region=None, business_street_address=None, business_street_address2=None, business_website=None, edit_reason=None, message_volume=None, notification_email=None, opt_in_image_urls=None, opt_in_type=None, production_message_sample=None, use_case_categories=None, use_case_summary=None) -> web.Response:
    """update_tollfree_verification

    

    :param sid: The unique string to identify Tollfree Verification.
    :type sid: str
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
    :param business_contact_phone: The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.
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
    :param edit_reason: Describe why the verification is being edited. If the verification was rejected because of a technical issue, such as the website being down, and the issue has been resolved this parameter should be set to something similar to &#39;Website fixed&#39;.
    :type edit_reason: str
    :param message_volume: Estimate monthly volume of messages from the Tollfree Number.
    :type message_volume: str
    :param notification_email: The email address to receive the notification about the verification result. .
    :type notification_email: str
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
