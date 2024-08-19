from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_started_dto import ActionStartedDTO
from openapi_server.models.macro_request_dto import MacroRequestDTO
from openapi_server import util


async def run(request: web.Request, macro_id, body) -> web.Response:
    """Executes a macro.

    Runs a specified macro on a specified list of items (\&quot;list\&quot; variable in the macro code). The list of items can be empty if the macro doesn&#39;t use it. Additional custom parameters can be provided to the macro when necessary (\&quot;params\&quot; variable in the macro code).   &lt;BR&gt;Note: Macros that support parameters can be also run from GUI (Views in Home Portal),so they should also handle the empty parameters map (e.g. by defining default values when parameters are not provided).

    :param macro_id: macro internal identifier
    :type macro_id: int
    :param body: Generated client invoices documents.
    :type body: dict | bytes

    """
    body = MacroRequestDTO.from_dict(body)
    return web.Response(status=200)
