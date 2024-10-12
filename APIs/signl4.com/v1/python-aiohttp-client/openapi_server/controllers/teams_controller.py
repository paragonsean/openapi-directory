from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_settings import AlertSettings
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.event_source_endpoint_info import EventSourceEndpointInfo
from openapi_server.models.team_info import TeamInfo
from openapi_server.models.team_profile import TeamProfile
from openapi_server.models.team_setup_progress import TeamSetupProgress
from openapi_server import util


async def subscriptions_subscription_id_teams_get(request: web.Request, subscription_id) -> web.Response:
    """Get infos for all teams of the subscription.

    

    :param subscription_id: 
    :type subscription_id: str

    """
    return web.Response(status=200)


async def teams_get(request: web.Request, ) -> web.Response:
    """Get infos of all teams.

    


    """
    return web.Response(status=200)


async def teams_team_id_alert_reports_file_name_get(request: web.Request, team_id, file_name) -> web.Response:
    """Returns Alert Report

    

    :param team_id: ID of team you want to get the duty report file infos for.
    :type team_id: str
    :param file_name: File name of file you want to download.
    :type file_name: str

    """
    return web.Response(status=200)


async def teams_team_id_alert_reports_get(request: web.Request, team_id) -> web.Response:
    """Get information about downloadable alert reports

    

    :param team_id: ID of team you want to download reports from.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_alert_settings_get(request: web.Request, team_id) -> web.Response:
    """Gets alert settings of a specific team.

    

    :param team_id: ID of the team the settings should be retrieved for.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_alert_settings_post(request: web.Request, team_id, body=None) -> web.Response:
    """Sets alert settings of a specific team.

    

    :param team_id: ID of the team the settings should be set for.
    :type team_id: str
    :param body: Alert settings to be set
    :type body: dict | bytes

    """
    body = AlertSettings.from_dict(body)
    return web.Response(status=200)


async def teams_team_id_event_sources_get(request: web.Request, team_id) -> web.Response:
    """Gets event sources of a specific team.

    

    :param team_id: ID of the team the sources should be retrieved for.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_get(request: web.Request, team_id) -> web.Response:
    """Gets infos of a specific team.

    

    :param team_id: ID of the team that should be retrieved.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_profile_put(request: web.Request, team_id, body=None) -> web.Response:
    """Updates team profile of a team

    

    :param team_id: Team ID of team which should be updated.
    :type team_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamProfile.from_dict(body)
    return web.Response(status=200)


async def teams_team_id_setup_progress_get(request: web.Request, team_id) -> web.Response:
    """Gets setup progress of a specific team.

    

    :param team_id: ID of the team the progress should be retrieved for.
    :type team_id: str

    """
    return web.Response(status=200)
