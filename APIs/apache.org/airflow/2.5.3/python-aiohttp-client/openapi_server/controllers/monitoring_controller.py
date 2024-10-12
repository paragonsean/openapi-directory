from typing import List, Dict
from aiohttp import web

from openapi_server.models.health_info import HealthInfo
from openapi_server.models.version_info import VersionInfo
from openapi_server import util


async def get_health(request: web.Request, ) -> web.Response:
    """Get instance status

    Get the status of Airflow&#39;s metadatabase and scheduler. It includes info about metadatabase and last heartbeat of scheduler. 


    """
    return web.Response(status=200)


async def get_version(request: web.Request, ) -> web.Response:
    """Get version information

    


    """
    return web.Response(status=200)
