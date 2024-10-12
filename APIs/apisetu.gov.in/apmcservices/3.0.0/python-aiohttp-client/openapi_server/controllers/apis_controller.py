from typing import List, Dict
from aiohttp import web

from openapi_server.models.apmcl400_response import Apmcl400Response
from openapi_server.models.apmcl401_response import Apmcl401Response
from openapi_server.models.apmcl404_response import Apmcl404Response
from openapi_server.models.apmcl500_response import Apmcl500Response
from openapi_server.models.apmcl502_response import Apmcl502Response
from openapi_server.models.apmcl503_response import Apmcl503Response
from openapi_server.models.apmcl504_response import Apmcl504Response
from openapi_server.models.apmcl_request import ApmclRequest
from openapi_server import util


async def apmcl(request: web.Request, body=None) -> web.Response:
    """Agriculture Produce Market Committee License

    API to verify Agriculture Produce Market Committee License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ApmclRequest.from_dict(body)
    return web.Response(status=200)
