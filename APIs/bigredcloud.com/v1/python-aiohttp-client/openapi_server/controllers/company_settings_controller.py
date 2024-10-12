from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_company_setting_dto import PageResultCompanySettingDto
from openapi_server import util


async def company_settings_get(request: web.Request, ) -> web.Response:
    """Returns a list of company settings. Supports OData querying protocol.  Filtering is forbidden.

    


    """
    return web.Response(status=200)
