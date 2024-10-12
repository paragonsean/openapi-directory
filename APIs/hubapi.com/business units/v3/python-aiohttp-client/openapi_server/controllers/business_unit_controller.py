from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_public_business_unit_no_paging import CollectionResponsePublicBusinessUnitNoPaging
from openapi_server.models.error import Error
from openapi_server import util


async def get_business_units_v3_business_units_user_user_id_get_by_user_id(request: web.Request, user_id, properties=None, name=None) -> web.Response:
    """Get Business Units for a user

    Get Business Units identified by &#x60;userId&#x60;. The &#x60;userId&#x60; refers to the user’s ID.

    :param user_id: Identifier of user to retrieve.
    :type user_id: str
    :param properties: The names of properties to optionally include in the response body. The only valid value is &#x60;logoMetadata&#x60;.
    :type properties: List[str]
    :param name: The names of Business Units to retrieve. If empty or not provided, then all associated Business Units will be returned.
    :type name: List[str]

    """
    return web.Response(status=200)
