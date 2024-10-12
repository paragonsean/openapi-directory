from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_agent import APIPagedResponseBuildSystemSharedDTOAgent
from openapi_server.models.build_system_shared_dto_activity_run import BuildSystemSharedDTOActivityRun
from openapi_server.models.build_system_shared_dto_agent import BuildSystemSharedDTOAgent
from openapi_server.models.build_system_shared_dto_agent_status import BuildSystemSharedDTOAgentStatus
from openapi_server import util


async def agents_delete_agent(request: web.Request, agent_id) -> web.Response:
    """Delete an Agent

    Deletes an Agent. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param agent_id: The id of the Agent to delete.
    :type agent_id: int

    """
    return web.Response(status=200)


async def agents_get_agent_activity_run(request: web.Request, agent_id) -> web.Response:
    """Get an Agent&#39;s ActivityRun

    Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

    :param agent_id: The id of the Agent to get.
    :type agent_id: int

    """
    return web.Response(status=200)


async def agents_get_agent_async(request: web.Request, agent_id) -> web.Response:
    """Get Agent

    Gets an Agent by ID. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.

    :param agent_id: The id of the Agent to get.
    :type agent_id: int

    """
    return web.Response(status=200)


async def agents_get_agents(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get Agents

    Gets a collection of Agents. When successful, the response is a PagedResponse of Agents.                If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def agents_get_current_agent_activity_run(request: web.Request, ) -> web.Response:
    """Get the ActivityRun of Agent associated with the current user

    Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.


    """
    return web.Response(status=200)


async def agents_get_current_agent_async(request: web.Request, ) -> web.Response:
    """Get Agent associated with the current user

    Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.


    """
    return web.Response(status=200)


async def agents_post_agent(request: web.Request, body) -> web.Response:
    """Create an Agent

    Creates an Agent.  The body of the POST is the Agent to create.  The AgentID will be assigned              on creation of the Agent.  When successful, the response is the AgentID.  If unsuccessful, an              appropriate ApiError is returned.

    :param body: The Agent to create.  The AgentID will be assigned on creation of the Agent.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOAgent.from_dict(body)
    return web.Response(status=200)


async def agents_put_agent(request: web.Request, agent_id, body) -> web.Response:
    """Update an Agent

    Updates an Agent.  The body of the PUT is the updated Agent.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

    :param agent_id: The id of the Agent to update.
    :type agent_id: int
    :param body: The updated Agent
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOAgent.from_dict(body)
    return web.Response(status=200)


async def agents_put_agent_activity_run(request: web.Request, agent_id, body) -> web.Response:
    """Update the ActivityRun assigned to the Agent.

    No Documentation Found.

    :param agent_id: The id of the Agent to update.
    :type agent_id: int
    :param body: The ActivityRun assigned to the agent.  Only the ActivityRunID is used.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOActivityRun.from_dict(body)
    return web.Response(status=200)


async def agents_put_agent_status(request: web.Request, agent_id, body) -> web.Response:
    """Update an Agent

    Updates the status of an Agent.The body of the PUT is the updated Agent status.  When successful,              the response is empty.If unsuccessful, an appropriate ApiError is returned.

    :param agent_id: The id of the Agent to update.
    :type agent_id: int
    :param body: The updated AgentStatus.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOAgentStatus.from_dict(body)
    return web.Response(status=200)
