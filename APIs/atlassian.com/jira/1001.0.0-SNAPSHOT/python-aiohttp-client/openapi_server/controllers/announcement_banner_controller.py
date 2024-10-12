from typing import List, Dict
from aiohttp import web

from openapi_server.models.announcement_banner_configuration import AnnouncementBannerConfiguration
from openapi_server.models.announcement_banner_configuration_update import AnnouncementBannerConfigurationUpdate
from openapi_server.models.error_collection import ErrorCollection
from openapi_server import util


async def get_banner(request: web.Request, ) -> web.Response:
    """Get announcement banner configuration

    Returns the current announcement banner configuration.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).


    """
    return web.Response(status=200)


async def set_banner(request: web.Request, body) -> web.Response:
    """Update announcement banner configuration

    Updates the announcement banner configuration.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = AnnouncementBannerConfigurationUpdate.from_dict(body)
    return web.Response(status=200)
