from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_request import CreateRewardRequest
from openapi_server.models.create_reward_response import CreateRewardResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_response import FetchRewardResponse
from openapi_server.models.fetch_rewards_response import FetchRewardsResponse
from openapi_server import util


async def create_reward(request: web.Request, body) -> web.Response:
    """Create a reward

    Create a reward for a patient.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRewardRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_reward(request: web.Request, id) -> web.Response:
    """Get a reward

    Get a reward record by id.

    :param id: Reward identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_rewards(request: web.Request, filter_patient=None, filter_reward_program_activation=None, filter_thread=None, filter_groups=None, filter_organization=None) -> web.Response:
    """List rewards

    Get a list of rewards matching the specified filters.

    :param filter_patient: Patient identifier. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_patient: str
    :param filter_reward_program_activation: Reward program activation identifier
    :type filter_reward_program_activation: str
    :param filter_thread: Thread identifier
    :type filter_thread: str
    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_organization: str

    """
    return web.Response(status=200)
