from typing import List, Dict
from aiohttp import web

from openapi_server.models.pmjay400_response import Pmjay400Response
from openapi_server.models.pmjay401_response import Pmjay401Response
from openapi_server.models.pmjay404_response import Pmjay404Response
from openapi_server.models.pmjay500_response import Pmjay500Response
from openapi_server.models.pmjay502_response import Pmjay502Response
from openapi_server.models.pmjay503_response import Pmjay503Response
from openapi_server.models.pmjay504_response import Pmjay504Response
from openapi_server.models.pmjay_request import PmjayRequest
from openapi_server import util


async def pmjay(request: web.Request, body=None) -> web.Response:
    """Pradhan Mantri Jan Arogya Yojana

    API to verify Pradhan Mantri Jan Arogya Yojana.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PmjayRequest.from_dict(body)
    return web.Response(status=200)
