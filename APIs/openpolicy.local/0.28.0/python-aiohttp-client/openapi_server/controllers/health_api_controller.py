from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_health(request: web.Request, bundles=None, plugins=None) -> web.Response:
    """Health

    This API endpoint verifies that the server is operational.  The response from the server is either 200 or 500: - **200** - OPA service is healthy. If &#x60;bundles&#x60; is true, then all configured bundles have been activated. If &#x60;plugins&#x60; is true, then all plugins are in an &#39;OK&#39; state. - **500** - OPA service is *not* healthy. If &#x60;bundles&#x60; is true, at least one of configured bundles has not yet been activated. If &#x60;plugins&#x60; is true, at least one plugins is in a &#39;not OK&#39; state.  --- **Note** This check is only for initial bundle activation. Subsequent downloads will not affect the health check.  Use the **status** endpoint (in the (management API)[management.html]) for more fine-grained bundle status monitoring.  ---

    :param bundles: Reports on bundle activation status (useful for &#39;ready&#39; checks at startup).  This includes any discovery bundles or bundles defined in the loaded discovery configuration.
    :type bundles: bool
    :param plugins: Reports on plugin status
    :type plugins: bool

    """
    return web.Response(status=200)
