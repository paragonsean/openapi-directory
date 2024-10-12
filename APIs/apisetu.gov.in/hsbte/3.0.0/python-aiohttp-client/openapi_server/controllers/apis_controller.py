from typing import List, Dict
from aiohttp import web

from openapi_server.models.dgmst400_response import Dgmst400Response
from openapi_server.models.dgmst401_response import Dgmst401Response
from openapi_server.models.dgmst404_response import Dgmst404Response
from openapi_server.models.dgmst500_response import Dgmst500Response
from openapi_server.models.dgmst502_response import Dgmst502Response
from openapi_server.models.dgmst503_response import Dgmst503Response
from openapi_server.models.dgmst504_response import Dgmst504Response
from openapi_server.models.dgmst_request import DgmstRequest
from openapi_server import util


async def dgmst(request: web.Request, body=None) -> web.Response:
    """Degree/ Diploma Marksheet

    API to verify Degree/ Diploma Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DgmstRequest.from_dict(body)
    return web.Response(status=200)
