from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server import util


async def virtual_meter_calculate_formula_get(request: web.Request, formula) -> web.Response:
    """Calculates a virtual meter from a formula.               A meter is coded as ID(\&quot;METERID\&quot;)

    Calculates a virtual meter from a formula.                            A meter is coded as ID(\&quot;METERID\&quot;)              Ariphmetical operators:               ()  parentheses;                 +   plus (a + b);                -  minus (a - b);                *  multiplycation symbol (a * b);                /  divide symbol (a / b);               Example: (ID(\&quot;63ac09cb-4e5f-4f3e-bd27-ad8c30bdfc0c\&quot;) + ID(\&quot;0209555e-9dc4-4e84-a166-a864488b4b12\&quot;)) * 2

    :param formula: 
    :type formula: str

    """
    return web.Response(status=200)
