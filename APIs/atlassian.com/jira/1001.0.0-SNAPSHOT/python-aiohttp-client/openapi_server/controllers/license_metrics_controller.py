from typing import List, Dict
from aiohttp import web

from openapi_server.models.license_metric import LicenseMetric
from openapi_server import util


async def get_approximate_application_license_count(request: web.Request, application_key) -> web.Response:
    """Get approximate application license count

    Returns the total approximate user account for a specific &#x60;jira licence application key&#x60;. Please note this information is cached with a 7-day lifecycle and could be stale at the time of call.  #### Application Key ####  An application key represents a specific version of Jira. See \\{@link ApplicationKey\\} for details  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param application_key: 
    :type application_key: str

    """
    return web.Response(status=200)


async def get_approximate_license_count(request: web.Request, ) -> web.Response:
    """Get approximate license count

    Returns the total approximate user account across all jira licenced application keys. Please note this information is cached with a 7-day lifecycle and could be stale at the time of call.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).


    """
    return web.Response(status=200)
