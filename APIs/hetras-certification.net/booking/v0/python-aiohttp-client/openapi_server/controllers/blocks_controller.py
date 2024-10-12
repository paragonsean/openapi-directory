from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancellation_token import CancellationToken
from openapi_server.models.total_count_response import TotalCountResponse
from openapi_server import util


async def blocks_get_blocks_async(request: web.Request, app_id, app_key, token, hotel_id=None, group_code=None, _from=None, to=None, status=None, rate_plan_codes=None, count_details=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Gets a list of blocks.

    With this endpoint you can request a list of blocks for the hotel chain. Currently we only support to optionally              filter by the group code linked to the block. Additional filters will be available soon.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param token: 
    :type token: dict | bytes
    :param hotel_id: Only return blocks for this specific hotel.
    :type hotel_id: int
    :param group_code: Filter the blocks by the specified group code
    :type group_code: str
    :param _from: Return all blocks where the block&#39;s last_departure is greater than specified date.
    :type _from: str
    :param to: Return all blocks where the block&#39;s last_departure is less than specified date.
    :type to: str
    :param status: Return all blocks where the block status is one of the specified values.
    :type status: str
    :param rate_plan_codes: Return all blocks that have related the specified comma-separated rate plans.
    :type rate_plan_codes: List[str]
    :param count_details: If true it will include also details of block count per each room type.
    :type count_details: bool
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    token = CancellationToken.from_dict(token)
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def blocks_get_blocks_count_async(request: web.Request, app_id, app_key, token, hotel_id=None, group_code=None, _from=None, to=None, status=None, rate_plan_codes=None, count_details=None) -> web.Response:
    """Get total blocks count that match the given filter criteria.

    

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param token: 
    :type token: dict | bytes
    :param hotel_id: Only return blocks for this specific hotel.
    :type hotel_id: int
    :param group_code: Filter the blocks by the specified group code
    :type group_code: str
    :param _from: Return all blocks where the block&#39;s last_departure is greater than specified date.
    :type _from: str
    :param to: Return all blocks where the block&#39;s last_departure is less than specified date.
    :type to: str
    :param status: Return all blocks where the block status is one of the specified values.
    :type status: str
    :param rate_plan_codes: Return all blocks that have related the specified comma-separated rate plans.
    :type rate_plan_codes: List[str]
    :param count_details: If true it will include also details of block count per each room type.
    :type count_details: bool

    """
    token = CancellationToken.from_dict(token)
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def blocks_get_single_block_async(request: web.Request, app_id, app_key, block_code, token) -> web.Response:
    """Gets the details for a specific block.

    Read all informationen about a block including the numbers of blocked rooms per room type and business day.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param block_code: Specifies the block code. The block code is composed of the hotel code, a dash and the block code               as shown in the hetras UI.
    :type block_code: str
    :param token: 
    :type token: dict | bytes

    """
    token = CancellationToken.from_dict(token)
    return web.Response(status=200)
