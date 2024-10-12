from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_media_processor_response import ListMediaProcessorResponse
from openapi_server.models.media_processor_enum_order import MediaProcessorEnumOrder
from openapi_server.models.media_processor_enum_status import MediaProcessorEnumStatus
from openapi_server.models.media_processor_enum_update_status import MediaProcessorEnumUpdateStatus
from openapi_server.models.media_v1_media_processor import MediaV1MediaProcessor
from openapi_server import util


async def create_media_processor(request: web.Request, extension, extension_context, extension_environment=None, max_duration=None, status_callback=None, status_callback_method=None) -> web.Response:
    """create_media_processor

    

    :param extension: The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: &#x60;video-composer-v2&#x60;
    :type extension: str
    :param extension_context: The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send.
    :type extension_context: str
    :param extension_environment: User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about whether you need to provide this.
    :type extension_environment: dict | bytes
    :param max_duration: The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.
    :type max_duration: int
    :param status_callback: The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details.
    :type status_callback: str
    :param status_callback_method: The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;.
    :type status_callback_method: str

    """
    extension_environment = object.from_dict(extension_environment)
    return web.Response(status=200)


async def fetch_media_processor(request: web.Request, sid) -> web.Response:
    """fetch_media_processor

    Returns a single MediaProcessor resource identified by a SID.

    :param sid: The SID of the MediaProcessor resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_media_processor(request: web.Request, order=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_media_processor

    Returns a list of MediaProcessors.

    :param order: The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default.
    :type order: str
    :param status: Status to filter by, with possible values &#x60;started&#x60;, &#x60;ended&#x60; or &#x60;failed&#x60;.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_media_processor(request: web.Request, sid, status) -> web.Response:
    """update_media_processor

    Updates a MediaProcessor resource identified by a SID.

    :param sid: The SID of the MediaProcessor resource to update.
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
