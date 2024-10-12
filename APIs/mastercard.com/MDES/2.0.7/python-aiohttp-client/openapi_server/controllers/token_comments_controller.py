from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_comments_request_schema import TokenCommentsRequestSchema
from openapi_server.models.token_comments_response_schema import TokenCommentsResponseSchema
from openapi_server import util


async def token_comments_post(request: web.Request, token_comments_request_schema=None) -> web.Response:
    """token_comments_post

    Used to retrieve all comments associated with a token. Typically the response includes comments created earlier by Issuer Customer Service representatives detailing additional information about a particular inquiry or event. There may also be comments with warnings of potential fraud. These comments are created automatically by the MDES system when a Token requestor indicates a high risk of fraud during digitization. 

    :param token_comments_request_schema: Contains the details of the request message.
    :type token_comments_request_schema: dict | bytes

    """
    token_comments_request_schema = TokenCommentsRequestSchema.from_dict(token_comments_request_schema)
    return web.Response(status=200)
