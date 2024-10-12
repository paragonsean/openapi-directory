from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_batch_request200_response import CreateBatchRequest200Response
from openapi_server.models.create_batch_request_request import CreateBatchRequestRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def create_batch_request(request: web.Request, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Submit parallel requests

    Make multiple requests in parallel to Asana&#39;s API.

    :param body: The requests to batch together via the Batch API.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateBatchRequestRequest.from_dict(body)
    return web.Response(status=200)
