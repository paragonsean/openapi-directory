from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_program_activation_request import CreateRewardProgramActivationRequest
from openapi_server.models.create_reward_program_activation_response import CreateRewardProgramActivationResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_program_activation_response import FetchRewardProgramActivationResponse
from openapi_server.models.fetch_reward_program_activations_response import FetchRewardProgramActivationsResponse
from openapi_server import util


async def create_reward_program_activation(request: web.Request, body) -> web.Response:
    """Create a reward program activation

    Create a reward program activation for a patient. There can only be one activation for a patient for a given reward program.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRewardProgramActivationRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_reward_program_activation(request: web.Request, id) -> web.Response:
    """Get a reward program activation

    Get a reward program activationrecord by id.

    :param id: Reward program activation identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_reward_program_activations(request: web.Request, filter_patient=None, filter_groups=None, filter_organization=None) -> web.Response:
    """List reward program activations

    Get a list of reward program activations matching the specified filters.

    :param filter_patient: Patient identifier. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_patient: str
    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_organization: str

    """
    return web.Response(status=200)
