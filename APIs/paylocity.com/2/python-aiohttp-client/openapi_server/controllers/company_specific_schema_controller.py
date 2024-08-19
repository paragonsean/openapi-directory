from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def get_company_specific_open_api_documentation(request: web.Request, authorization, company_id) -> web.Response:
    """Get Company-Specific Open API Documentation

    The company-specific Open API endpoint allows the client to GET an Open API document for the Paylocity API that is customized with company-specific resource schemas. These customized resource schemas define certain properties as enumerations of pre-defined values that correspond to the company&#39;s setup with Web Pay. The customized schemas also indicate which properties are required by the company within Web Pay.&lt;br  /&gt;To learn more about Open API, click [here](https://www.openapis.org/)

    :param authorization: Bearer + JWT
    :type authorization: str
    :param company_id: Company Id
    :type company_id: str

    """
    return web.Response(status=200)
