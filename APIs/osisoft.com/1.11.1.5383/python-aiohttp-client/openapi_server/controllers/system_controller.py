from typing import List, Dict
from aiohttp import web

from openapi_server.models.items_cache_instance import ItemsCacheInstance
from openapi_server.models.system_landing import SystemLanding
from openapi_server.models.system_status import SystemStatus
from openapi_server.models.user_info import UserInfo
from openapi_server.models.version import Version
from openapi_server import util


async def system_cache_instances(request: web.Request, ) -> web.Response:
    """Get AF cache instances currently in use by the system. These are caches from which user requests are serviced. The number of instances depends on the number of users connected to the service, the service&#39;s authentication method, and the cache instance configuration.

    


    """
    return web.Response(status=200)


async def system_landing(request: web.Request, ) -> web.Response:
    """Get system links for this PI System Web API instance.

    


    """
    return web.Response(status=200)


async def system_status(request: web.Request, ) -> web.Response:
    """Get information about this PI Web API instance. Examples of information returned include the system uptime, the number of cache instances for this PI System Web API instance, and the system run state.

    


    """
    return web.Response(status=200)


async def system_user_info(request: web.Request, ) -> web.Response:
    """Get information about the Windows identity used to fulfill the request. This depends on the service&#39;s authentication method and the credentials passed by the client. The impersonation level of the Windows identity is included.

    


    """
    return web.Response(status=200)


async def system_versions(request: web.Request, ) -> web.Response:
    """Get the current versions of the PI Web API instance and all external plugins.

    


    """
    return web.Response(status=200)
