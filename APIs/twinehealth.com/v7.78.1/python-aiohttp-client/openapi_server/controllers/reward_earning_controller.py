from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_earning_request import CreateRewardEarningRequest
from openapi_server.models.create_reward_earning_response import CreateRewardEarningResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_earning_response import FetchRewardEarningResponse
from openapi_server.models.fetch_reward_earnings_response import FetchRewardEarningsResponse
from openapi_server import util


async def create_reward_earning(request: web.Request, body) -> web.Response:
    """Create a reward earning

    Create a reward earning for a reward. There can only be one earning for a reward. It is possilble to create multiple reward earnings simultaneously by providing and array of reward earnings in the data property.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRewardEarningRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_reward_earning(request: web.Request, id) -> web.Response:
    """Get a reward earning

    Get a reward earning record by id.

    :param id: Reward earning identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_reward_earnings(request: web.Request, filter_groups, filter_patient, filter_ready_for_fulfillment=None) -> web.Response:
    """List reward earnings

    Get a list of reward earnings matching the specified filters.

    :param filter_groups: Group identifiers
    :type filter_groups: str
    :param filter_patient: Patient identifier
    :type filter_patient: str
    :param filter_ready_for_fulfillment: If true, only returns those reward earnings for which ready_for_fulfillment is true and fulfilled_at is null. If false, only returns those reward earnings for which ready_for_fulfillment is false and fulfilled_at is null.
    :type filter_ready_for_fulfillment: bool

    """
    return web.Response(status=200)
