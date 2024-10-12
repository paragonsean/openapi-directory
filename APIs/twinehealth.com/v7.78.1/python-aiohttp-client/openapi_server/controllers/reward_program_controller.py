from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_program_request import CreateRewardProgramRequest
from openapi_server.models.create_reward_program_response import CreateRewardProgramResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse
from openapi_server.models.fetch_reward_program_response import FetchRewardProgramResponse
from openapi_server.models.fetch_reward_programs_response import FetchRewardProgramsResponse
from openapi_server import util


async def create_reward_program(request: web.Request, body) -> web.Response:
    """Create a reward program

    Create a reward program for a group.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRewardProgramRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_reward_program(request: web.Request, id) -> web.Response:
    """Get a reward program

    Get a reward program record by id.

    :param id: Reward program identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_reward_program_group(request: web.Request, id) -> web.Response:
    """Get group for a reward program

    Get the group related to a reward program.

    :param id: Reward program identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_reward_programs(request: web.Request, filter_groups=None, filter_organization=None) -> web.Response:
    """List reward programs

    Get a list of reward programs matching the specified filters.

    :param filter_groups: Comma-separated list of group identifiers. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_organization: str

    """
    return web.Response(status=200)
