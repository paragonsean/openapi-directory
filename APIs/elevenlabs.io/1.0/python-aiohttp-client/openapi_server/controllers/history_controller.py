from typing import List, Dict
from aiohttp import web

from openapi_server.models.body_delete_history_items_v1_history_delete_post import BodyDeleteHistoryItemsV1HistoryDeletePost
from openapi_server.models.body_download_history_items_v1_history_download_post import BodyDownloadHistoryItemsV1HistoryDownloadPost
from openapi_server.models.get_history_response_model import GetHistoryResponseModel
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def delete_history_item_v1_history_history_item_id_delete(request: web.Request, history_item_id, xi_api_key=None) -> web.Response:
    """Delete History Item

    Delete a history item by its ID

    :param history_item_id: History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
    :type history_item_id: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)


async def delete_history_items_v1_history_delete_post(request: web.Request, body, xi_api_key=None) -> web.Response:
    """Delete History Items

    Delete a number of history items by their IDs.

    :param body: 
    :type body: dict | bytes
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    body = BodyDeleteHistoryItemsV1HistoryDeletePost.from_dict(body)
    return web.Response(status=200)


async def download_history_items_v1_history_download_post(request: web.Request, body, xi_api_key=None) -> web.Response:
    """Download History Items

    Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file.

    :param body: 
    :type body: dict | bytes
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    body = BodyDownloadHistoryItemsV1HistoryDownloadPost.from_dict(body)
    return web.Response(status=200)


async def get_audio_from_history_item_v1_history_history_item_id_audio_get(request: web.Request, history_item_id, xi_api_key=None) -> web.Response:
    """Get Audio From History Item

    Returns the audio of an history item.

    :param history_item_id: History item ID to be used, you can use GET https://api.elevenlabs.io/v1/history to receive a list of history items and their IDs.
    :type history_item_id: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)


async def get_generated_items_v1_history_get(request: web.Request, xi_api_key=None) -> web.Response:
    """Get Generated Items

    Returns metadata about all your generated audio.

    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)
