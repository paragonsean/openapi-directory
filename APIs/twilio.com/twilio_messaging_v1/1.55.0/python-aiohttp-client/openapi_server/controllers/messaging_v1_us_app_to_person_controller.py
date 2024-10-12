from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_us_app_to_person_response import ListUsAppToPersonResponse
from openapi_server.models.messaging_v1_service_us_app_to_person import MessagingV1ServiceUsAppToPerson
from openapi_server import util


async def create_us_app_to_person(request: web.Request, messaging_service_sid, brand_registration_sid, description, has_embedded_links, has_embedded_phone, message_flow, message_samples, us_app_to_person_usecase, age_gated=None, direct_lending=None, help_keywords=None, help_message=None, opt_in_keywords=None, opt_in_message=None, opt_out_keywords=None, opt_out_message=None, subscriber_opt_in=None) -> web.Response:
    """create_us_app_to_person

    

    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to create the resources from.
    :type messaging_service_sid: str
    :param brand_registration_sid: A2P Brand Registration SID
    :type brand_registration_sid: str
    :param description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
    :type description: str
    :param has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
    :type has_embedded_links: bool
    :param has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
    :type has_embedded_phone: bool
    :param message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
    :type message_flow: str
    :param message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.
    :type message_samples: List[str]
    :param us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
    :type us_app_to_person_usecase: str
    :param age_gated: A boolean that specifies whether campaign is age gated or not.
    :type age_gated: bool
    :param direct_lending: A boolean that specifies whether campaign allows direct lending or not.
    :type direct_lending: bool
    :param help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    :type help_keywords: List[str]
    :param help_message: When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    :type help_message: str
    :param opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
    :type opt_in_keywords: List[str]
    :param opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
    :type opt_in_message: str
    :param opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    :type opt_out_keywords: List[str]
    :param opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    :type opt_out_message: str
    :param subscriber_opt_in: A boolean that specifies whether campaign has Subscriber Optin or not.
    :type subscriber_opt_in: bool

    """
    return web.Response(status=200)


async def delete_us_app_to_person(request: web.Request, messaging_service_sid, sid) -> web.Response:
    """delete_us_app_to_person

    

    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to delete the resource from.
    :type messaging_service_sid: str
    :param sid: The SID of the US A2P Compliance resource to delete &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_us_app_to_person(request: web.Request, messaging_service_sid, sid) -> web.Response:
    """fetch_us_app_to_person

    

    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
    :type messaging_service_sid: str
    :param sid: The SID of the US A2P Compliance resource to fetch &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;.
    :type sid: str

    """
    return web.Response(status=200)


async def list_us_app_to_person(request: web.Request, messaging_service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_us_app_to_person

    

    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
    :type messaging_service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_us_app_to_person(request: web.Request, messaging_service_sid, sid, age_gated, description, direct_lending, has_embedded_links, has_embedded_phone, message_flow, message_samples) -> web.Response:
    """update_us_app_to_person

    

    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to update the resource from.
    :type messaging_service_sid: str
    :param sid: The SID of the US A2P Compliance resource to update &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;.
    :type sid: str
    :param age_gated: A boolean that specifies whether campaign requires age gate for federally legal content.
    :type age_gated: bool
    :param description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
    :type description: str
    :param direct_lending: A boolean that specifies whether campaign allows direct lending or not.
    :type direct_lending: bool
    :param has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
    :type has_embedded_links: bool
    :param has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
    :type has_embedded_phone: bool
    :param message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
    :type message_flow: str
    :param message_samples: An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.
    :type message_samples: List[str]

    """
    return web.Response(status=200)
