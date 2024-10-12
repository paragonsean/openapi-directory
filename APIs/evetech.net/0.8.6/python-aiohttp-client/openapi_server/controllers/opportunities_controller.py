from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_opportunities200_ok import GetCharactersCharacterIdOpportunities200Ok
from openapi_server.models.get_opportunities_groups_group_id_ok import GetOpportunitiesGroupsGroupIdOk
from openapi_server.models.get_opportunities_tasks_task_id_ok import GetOpportunitiesTasksTaskIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_opportunities(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get a character&#39;s completed tasks

    Return a list of tasks finished by a character  --- Alternate route: &#x60;/dev/characters/{character_id}/opportunities/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/opportunities/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/opportunities/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_opportunities_groups(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get opportunities groups

    Return a list of opportunities groups  --- Alternate route: &#x60;/dev/opportunities/groups/&#x60;  Alternate route: &#x60;/legacy/opportunities/groups/&#x60;  Alternate route: &#x60;/v1/opportunities/groups/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_opportunities_groups_group_id(request: web.Request, group_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get opportunities group

    Return information of an opportunities group  --- Alternate route: &#x60;/dev/opportunities/groups/{group_id}/&#x60;  Alternate route: &#x60;/legacy/opportunities/groups/{group_id}/&#x60;  Alternate route: &#x60;/v1/opportunities/groups/{group_id}/&#x60;  --- This route expires daily at 11:05

    :param group_id: ID of an opportunities group
    :type group_id: int
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str

    """
    return web.Response(status=200)


async def get_opportunities_tasks(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get opportunities tasks

    Return a list of opportunities tasks  --- Alternate route: &#x60;/dev/opportunities/tasks/&#x60;  Alternate route: &#x60;/legacy/opportunities/tasks/&#x60;  Alternate route: &#x60;/v1/opportunities/tasks/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_opportunities_tasks_task_id(request: web.Request, task_id, datasource=None, if_none_match=None) -> web.Response:
    """Get opportunities task

    Return information of an opportunities task  --- Alternate route: &#x60;/dev/opportunities/tasks/{task_id}/&#x60;  Alternate route: &#x60;/legacy/opportunities/tasks/{task_id}/&#x60;  Alternate route: &#x60;/v1/opportunities/tasks/{task_id}/&#x60;  --- This route expires daily at 11:05

    :param task_id: ID of an opportunities task
    :type task_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
