from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_token_request import CreateTokenRequest
from openapi_server.models.create_token_response import CreateTokenResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse
from openapi_server.models.fetch_organization_response import FetchOrganizationResponse
from openapi_server import util


async def create_token(request: web.Request, body, include=None) -> web.Response:
    """Create an oauth token

    Create an OAuth 2.0 Bearer token. A valid bearer token is required for all other API requests.  Be sure to set the header &#x60;Content-Type: \&quot;application/vnd.api+json\&quot;&#x60;. Otherwise, you will get an error 403 Forbidden. Using &#x60;Content-Type: \&quot;application/json\&quot;&#x60; is permitted (to support older oauth clients) but when using &#x60;application/json&#x60; the body should have a body in the following format instead of nesting under &#x60;data.attributes&#x60;: &#x60;&#x60;&#x60; {   \&quot;grant_type\&quot;: \&quot;client_credentials\&quot;,   \&quot;client_id\&quot;: \&quot;95c78ab2-167f-40b8-8bec-8398d4b87454\&quot;,   \&quot;client_secret\&quot;: \&quot;35d18dc9-a3dd-4948-b787-063a490b9354\&quot; } &#x60;&#x60;&#x60; 

    :param body: 
    :type body: dict | bytes
    :param include: List of related resources to include in the response
    :type include: str

    """
    body = CreateTokenRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_token_groups(request: web.Request, id) -> web.Response:
    """Get the groups for a token

    Get the list of groups a token can be used to access.

    :param id: Token identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_token_organization(request: web.Request, id) -> web.Response:
    """Get the organization for a token

    Get the organization a token can be used to access.

    :param id: Token identifier
    :type id: str

    """
    return web.Response(status=200)
