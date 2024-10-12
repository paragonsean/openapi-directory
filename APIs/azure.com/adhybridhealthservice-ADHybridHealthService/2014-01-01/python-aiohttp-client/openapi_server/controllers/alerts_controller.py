from typing import List, Dict
from aiohttp import web

from openapi_server.models.alerts import Alerts
from openapi_server import util


async def service_members_list_alerts(request: web.Request, service_member_id, service_name, api_version, filter=None, state=None, _from=None, to=None) -> web.Response:
    """service_members_list_alerts

    Gets the details of an alert for a given service and server combination.

    :param service_member_id: The server Id for which the alert details needs to be queried.
    :type service_member_id: str
    :type service_member_id: str
    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The alert property filter to apply.
    :type filter: str
    :param state: The alert state to query for.
    :type state: str
    :param _from: The start date to query for.
    :type _from: str
    :param to: The end date till when to query for.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def services_list_alerts(request: web.Request, service_name, api_version, filter=None, state=None, _from=None, to=None) -> web.Response:
    """services_list_alerts

    Gets the alerts for a given service.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The alert property filter to apply.
    :type filter: str
    :param state: The alert state to query for.
    :type state: str
    :param _from: The start date to query for.
    :type _from: str
    :param to: The end date till when to query for.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
