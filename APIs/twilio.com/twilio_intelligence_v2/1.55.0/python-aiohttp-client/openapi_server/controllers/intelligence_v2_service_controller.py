from typing import List, Dict
from aiohttp import web

from openapi_server.models.intelligence_v2_service import IntelligenceV2Service
from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.service_enum_http_method import ServiceEnumHttpMethod
from openapi_server import util


async def create_service(request: web.Request, unique_name, auto_redaction=None, auto_transcribe=None, data_logging=None, friendly_name=None, language_code=None, media_redaction=None, webhook_http_method=None, webhook_url=None) -> web.Response:
    """create_service

    Create a new Service for the given Account

    :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
    :type unique_name: str
    :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
    :type auto_redaction: bool
    :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
    :type auto_transcribe: bool
    :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
    :type data_logging: bool
    :param friendly_name: A human readable description of this resource, up to 64 characters.
    :type friendly_name: str
    :param language_code: The default language code of the audio.
    :type language_code: str
    :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
    :type media_redaction: bool
    :param webhook_http_method: 
    :type webhook_http_method: str
    :param webhook_url: The URL Twilio will request when executing the Webhook.
    :type webhook_url: str

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    Delete a specific Service.

    :param sid: A 34 character string that uniquely identifies this Service.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    Fetch a specific Service.

    :param sid: A 34 character string that uniquely identifies this Service.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    Retrieves a list of all Services for an account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, sid, if_match=None, auto_redaction=None, auto_transcribe=None, data_logging=None, friendly_name=None, language_code=None, media_redaction=None, unique_name=None, webhook_http_method=None, webhook_url=None) -> web.Response:
    """update_service

    Update a specific Service.

    :param sid: A 34 character string that uniquely identifies this Service.
    :type sid: str
    :param if_match: The If-Match HTTP request header
    :type if_match: str
    :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
    :type auto_redaction: bool
    :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
    :type auto_transcribe: bool
    :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
    :type data_logging: bool
    :param friendly_name: A human readable description of this resource, up to 64 characters.
    :type friendly_name: str
    :param language_code: The default language code of the audio.
    :type language_code: str
    :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
    :type media_redaction: bool
    :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
    :type unique_name: str
    :param webhook_http_method: 
    :type webhook_http_method: str
    :param webhook_url: The URL Twilio will request when executing the Webhook.
    :type webhook_url: str

    """
    return web.Response(status=200)
