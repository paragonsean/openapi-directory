from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation_item import ConversationItem
from openapi_server.models.v2_distributed_client_info import V2DistributedClientInfo
from openapi_server import util


async def get_journal_entries(request: web.Request, telephony_conversation_id, timestamp=None, number_of_entries=None, direction=None, journal_filter=None) -> web.Response:
    """Get journal

    Get telephony journal OauthScopes: READ_CONVERSATIONS

    :param telephony_conversation_id: The id of the telephony conversation
    :type telephony_conversation_id: str
    :param timestamp: A timestamp, default &#x3D; 0
    :type timestamp: 
    :param number_of_entries: The number of entries, between 1 and 100, default &#x3D; 25
    :type number_of_entries: 
    :param direction: The direction (BEFORE||AFTER||BOTH), default &#x3D; AFTER
    :type direction: str
    :param journal_filter: The filter, ALL||MISSED||DIALED||RECEIVED||DIVERTED||VOICEMAILS||UNHERAD_VOICEMAILS. default &#x3D; ALL
    :type journal_filter: str

    """
    return web.Response(status=200)


async def v2_get_device_infos(request: web.Request, ) -> web.Response:
    """Get devices infos

    Get the device infos of the requesting user OauthScopes: READ_USER_PROFILE


    """
    return web.Response(status=200)


async def v2_get_telephony_conversation_id(request: web.Request, ) -> web.Response:
    """Get telephony conversation id

    Get telephony conversation id for requesting client OauthScopes: READ_CONVERSATIONS


    """
    return web.Response(status=200)
