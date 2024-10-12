from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.user_friend_info import UserFriendInfo
from openapi_server import util


async def get_friend_info(request: web.Request, user_id, if_none_match=None) -> web.Response:
    """Get friend information

    

    :param user_id: Your friend user id
    :type user_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)
