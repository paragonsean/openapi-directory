from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.public_channel_index import PublicChannelIndex
from openapi_server.models.public_channel_info_list import PublicChannelInfoList
from openapi_server import util


async def get_channels(request: web.Request, country_iso_code, accept_encoding, if_none_match=None) -> web.Response:
    """The channel list for one country

    

    :param country_iso_code: The country iso code alpha 3 based on this: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Decoding_table \\ To know which country are available you have to use the operation: GetChannelsByCountry 
    :type country_iso_code: str
    :param accept_encoding: Allows the client to indicate whether it accepts a compressed encoding to reduce traffic size.
    :type accept_encoding: List[str]
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_channels_index(request: web.Request, if_none_match=None) -> web.Response:
    """Get public channel index

    Use this operation to get the correct link to the channels and to the list of values

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)
