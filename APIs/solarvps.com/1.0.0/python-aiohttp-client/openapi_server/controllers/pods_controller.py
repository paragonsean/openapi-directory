from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def pods_get(request: web.Request, ) -> web.Response:
    """View all your pods

    Shows all your pods


    """
    return web.Response(status=200)


async def pods_pod_id_action_get(request: web.Request, pod_id, action) -> web.Response:
    """Perform action on a specific pod

    Allowed actions are reboot, shutdown, boot

    :param pod_id: Id of the pod you want to perform actions on
    :type pod_id: 
    :param action: Action to perform on selected pod
    :type action: str

    """
    return web.Response(status=200)


async def pods_pod_id_get(request: web.Request, pod_id) -> web.Response:
    """View information on a specific pod

    Shows details of a specific pod. Enter 1 below to see an example

    :param pod_id: Id of the pod you want to perform actions on
    :type pod_id: 

    """
    return web.Response(status=200)


async def pods_pod_id_ping_get(request: web.Request, pod_id) -> web.Response:
    """Ping your specified pod

    Returns the ping response from your server.

    :param pod_id: Id of the pod you want to ping check
    :type pod_id: 

    """
    return web.Response(status=200)
