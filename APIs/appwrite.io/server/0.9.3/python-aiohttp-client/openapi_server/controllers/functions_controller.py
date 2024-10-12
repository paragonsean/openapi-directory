from typing import List, Dict
from aiohttp import web

from openapi_server.models.execution import Execution
from openapi_server.models.execution_list import ExecutionList
from openapi_server.models.function import Function
from openapi_server.models.function_list import FunctionList
from openapi_server.models.functions_create_execution_request import FunctionsCreateExecutionRequest
from openapi_server.models.functions_create_request import FunctionsCreateRequest
from openapi_server.models.functions_update_request import FunctionsUpdateRequest
from openapi_server.models.functions_update_tag_request import FunctionsUpdateTagRequest
from openapi_server.models.tag import Tag
from openapi_server.models.tag_list import TagList
from openapi_server import util


async def functions_create(request: web.Request, body=None) -> web.Response:
    """Create Function

    Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different project users or team with access to execute the function using the client API.

    :param body: 
    :type body: dict | bytes

    """
    body = FunctionsCreateRequest.from_dict(body)
    return web.Response(status=200)


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


async def functions_create_tag(request: web.Request, function_id, code, command) -> web.Response:
    """Create Tag

    Create a new function code tag. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you&#39;ll need to update the function&#39;s tag to use your new tag UID.  This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](/docs/functions).  Use the \&quot;command\&quot; param to set the entry point used to execute your code.

    :param function_id: Function unique ID.
    :type function_id: str
    :param code: Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
    :type code: str
    :param command: Code execution command.
    :type command: str

    """
    return web.Response(status=200)


async def functions_delete(request: web.Request, function_id) -> web.Response:
    """Delete Function

    Delete a function by its unique ID.

    :param function_id: Function unique ID.
    :type function_id: str

    """
    return web.Response(status=200)


async def functions_delete_tag(request: web.Request, function_id, tag_id) -> web.Response:
    """Delete Tag

    Delete a code tag by its unique ID.

    :param function_id: Function unique ID.
    :type function_id: str
    :param tag_id: Tag unique ID.
    :type tag_id: str

    """
    return web.Response(status=200)


async def functions_get(request: web.Request, function_id) -> web.Response:
    """Get Function

    Get a function by its unique ID.

    :param function_id: Function unique ID.
    :type function_id: str

    """
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


async def functions_get_tag(request: web.Request, function_id, tag_id) -> web.Response:
    """Get Tag

    Get a code tag by its unique ID.

    :param function_id: Function unique ID.
    :type function_id: str
    :param tag_id: Tag unique ID.
    :type tag_id: str

    """
    return web.Response(status=200)


async def functions_list(request: web.Request, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """List Functions

    Get a list of all the project&#39;s functions. You can use the query params to filter your results.

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


async def functions_list_tags(request: web.Request, function_id, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """List Tags

    Get a list of all the project&#39;s code tags. You can use the query params to filter your results.

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


async def functions_update(request: web.Request, function_id, body=None) -> web.Response:
    """Update Function

    Update function by its unique ID.

    :param function_id: Function unique ID.
    :type function_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FunctionsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def functions_update_tag(request: web.Request, function_id, body=None) -> web.Response:
    """Update Function Tag

    Update the function code tag ID using the unique function ID. Use this endpoint to switch the code tag that should be executed by the execution endpoint.

    :param function_id: Function unique ID.
    :type function_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FunctionsUpdateTagRequest.from_dict(body)
    return web.Response(status=200)
