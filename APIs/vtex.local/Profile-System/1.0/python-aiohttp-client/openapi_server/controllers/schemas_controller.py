from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_schema import ModelSchema
from openapi_server import util


async def create_or_update_profile_schema(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create or update profile schema

    Creates or updates profile schema.    &gt; Each account has one profile schema. Updating it with this request will substitute the previous version.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModelSchema.from_dict(body)
    return web.Response(status=200)
