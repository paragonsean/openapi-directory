from typing import List, Dict
from aiohttp import web

from openapi_server.models.execution import Execution
from openapi_server.models.execution_list import ExecutionList
from openapi_server.models.functions_create_execution_request import FunctionsCreateExecutionRequest
from openapi_server import util


async def functions_create_execution(request: web.Request, function_id, body=None) -> web.Response:
    """Create Execution

    Trigger a function execution. The returned object will return you the current execution status. You can ping the &#x60;Get Execution&#x60; endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

    :param function_id: Function unique ID.
    :type function_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FunctionsCreateExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def functions_get_execution(request: web.Request, function_id, execution_id) -> web.Response:
    """Get Execution

    Get a function execution log by its unique ID.

    :param function_id: Function unique ID.
    :type function_id: str
    :param execution_id: Execution unique ID.
    :type execution_id: str

    """
    return web.Response(status=200)


async def functions_list_executions(request: web.Request, function_id, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """List Executions

    Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s executions. [Learn more about different API modes](/docs/admin).

    :param function_id: Function unique ID.
    :type function_id: str
    :param search: Search term to filter your list results. Max length: 256 chars.
    :type search: str
    :param limit: Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    :type limit: int
    :param offset: Results offset. The default value is 0. Use this param to manage pagination.
    :type offset: int
    :param order_type: Order result by ASC or DESC order.
    :type order_type: str

    """
    return web.Response(status=200)
