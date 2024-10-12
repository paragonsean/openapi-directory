from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.search_request_schema import SearchRequestSchema
from openapi_server.models.search_response_schema import SearchResponseSchema
from openapi_server import util


async def search_post(request: web.Request, search_request_schema=None) -> web.Response:
    """search_post

    Provides the ability to search for tokens based on Account PAN, Alternate Account Identifier, Token Unique Reference, Token, Payment App Instance Id or Comment Id. Returns all of the tokens associated with an account according to the scope of the indicated search request criteria. The response includes key state and informational data for each token, including the Token Unique Reference which is needed for subsequent token lifecycle management activities.&lt;br&gt;&lt;br&gt;_Notes:_ The Search API request MUST include only one of the available search methods Account PAN, Token Unique Reference, Token, Payment App Instance Id, Comment Id, or Alternate Account Identifier. They cannot be used together in a single request.&lt;br&gt; Moreover, this function only retrieves results if the search criteria matches a current value from the token vault. In other words, if the search criteria is a PAN that has been replaced, the system will not retrieve any data.  

    :param search_request_schema: Contains the details of the request message.
    :type search_request_schema: dict | bytes

    """
    search_request_schema = SearchRequestSchema.from_dict(search_request_schema)
    return web.Response(status=200)
