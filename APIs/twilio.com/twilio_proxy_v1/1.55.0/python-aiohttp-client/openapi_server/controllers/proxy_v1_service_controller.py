from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.proxy_v1_service import ProxyV1Service
from openapi_server.models.service_enum_geo_match_level import ServiceEnumGeoMatchLevel
from openapi_server.models.service_enum_number_selection_behavior import ServiceEnumNumberSelectionBehavior
from openapi_server import util


async def create_service(request: web.Request, unique_name, callback_url=None, chat_instance_sid=None, default_ttl=None, geo_match_level=None, intercept_callback_url=None, number_selection_behavior=None, out_of_session_callback_url=None) -> web.Response:
    """create_service

    Create a new Service for Twilio Proxy

    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
    :type unique_name: str
    :param callback_url: The URL we should call when the interaction status changes.
    :type callback_url: str
    :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
    :type chat_instance_sid: str
    :param default_ttl: The default &#x60;ttl&#x60; value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session&#39;s last create or last Interaction. The default value of &#x60;0&#x60; indicates an unlimited Session length. You can override a Session&#39;s default TTL value by setting its &#x60;ttl&#x60; value.
    :type default_ttl: int
    :param geo_match_level: 
    :type geo_match_level: str
    :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
    :type intercept_callback_url: str
    :param number_selection_behavior: 
    :type number_selection_behavior: str
    :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
    :type out_of_session_callback_url: str

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    Delete a specific Service.

    :param sid: The Twilio-provided string that uniquely identifies the Service resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    Fetch a specific Service.

    :param sid: The Twilio-provided string that uniquely identifies the Service resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will be returned per page.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, sid, callback_url=None, chat_instance_sid=None, default_ttl=None, geo_match_level=None, intercept_callback_url=None, number_selection_behavior=None, out_of_session_callback_url=None, unique_name=None) -> web.Response:
    """update_service

    Update a specific Service.

    :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
    :type sid: str
    :param callback_url: The URL we should call when the interaction status changes.
    :type callback_url: str
    :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
    :type chat_instance_sid: str
    :param default_ttl: The default &#x60;ttl&#x60; value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session&#39;s last create or last Interaction. The default value of &#x60;0&#x60; indicates an unlimited Session length. You can override a Session&#39;s default TTL value by setting its &#x60;ttl&#x60; value.
    :type default_ttl: int
    :param geo_match_level: 
    :type geo_match_level: str
    :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
    :type intercept_callback_url: str
    :param number_selection_behavior: 
    :type number_selection_behavior: str
    :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
    :type out_of_session_callback_url: str
    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
    :type unique_name: str

    """
    return web.Response(status=200)
