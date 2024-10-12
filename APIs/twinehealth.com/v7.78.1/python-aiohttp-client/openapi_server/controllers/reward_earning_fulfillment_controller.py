from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_earning_fulfillment_request import CreateRewardEarningFulfillmentRequest
from openapi_server.models.create_reward_earning_fulfillment_response import CreateRewardEarningFulfillmentResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_earning_fulfillment_response import FetchRewardEarningFulfillmentResponse
from openapi_server.models.fetch_reward_earning_fulfillments_response import FetchRewardEarningFulfillmentsResponse
from openapi_server import util


async def create_reward_earning_fulfillment(request: web.Request, body) -> web.Response:
    """Create a reward earning fulfillment

    Create a reward earning fulfillment for a reward earning. There can only be one fulfillment for each earning.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRewardEarningFulfillmentRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_reward_earning_fulfillment(request: web.Request, id) -> web.Response:
    """Get a reward earning fulfillment

    Get a reward earning fulfillment record by id.

    :param id: Reward earning fulfillment identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_reward_earning_fulfillments(request: web.Request, filter_patient) -> web.Response:
    """List reward earning fulfillments

    Get a list of reward earning fulfillments matching the specified filters.

    :param filter_patient: Patient identifier
    :type filter_patient: str

    """
    return web.Response(status=200)
