from typing import List, Dict
from aiohttp import web

from openapi_server.models.scim_resource_type import ScimResourceType
from openapi_server.models.scim_schema import ScimSchema
from openapi_server.models.scim_service_provider_config import ScimServiceProviderConfig
from openapi_server.models.scim_user import ScimUser
from openapi_server.models.v2_scim20_resource_types_get200_response import V2Scim20ResourceTypesGet200Response
from openapi_server.models.v2_scim20_resource_types_get401_response import V2Scim20ResourceTypesGet401Response
from openapi_server.models.v2_scim20_resource_types_get500_response import V2Scim20ResourceTypesGet500Response
from openapi_server.models.v2_scim20_resource_types_name_get404_response import V2Scim20ResourceTypesNameGet404Response
from openapi_server.models.v2_scim20_schemas_get200_response import V2Scim20SchemasGet200Response
from openapi_server.models.v2_scim20_users_get200_response import V2Scim20UsersGet200Response
from openapi_server.models.v2_scim20_users_get400_response import V2Scim20UsersGet400Response
from openapi_server.models.v2_scim20_users_get403_response import V2Scim20UsersGet403Response
from openapi_server.models.v2_scim20_users_id_put_request import V2Scim20UsersIdPutRequest
from openapi_server.models.v2_scim20_users_post409_response import V2Scim20UsersPost409Response
from openapi_server.models.v2_scim20_users_post_request import V2Scim20UsersPostRequest
from openapi_server import util


async def v2_scim20_resource_types_get(request: web.Request, ) -> web.Response:
    """List resource types

    Returns all resource types supported for the SCIM configuration. 


    """
    return web.Response(status=200)


async def v2_scim20_resource_types_name_get(request: web.Request, name) -> web.Response:
    """Get a resource type

    Returns a resource type by name. 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def v2_scim20_schemas_get(request: web.Request, ) -> web.Response:
    """List schemas

    Returns all schemas supported for the SCIM configuration. 


    """
    return web.Response(status=200)


async def v2_scim20_schemas_id_get(request: web.Request, id) -> web.Response:
    """Get a schema

    Returns a schema by ID. 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def v2_scim20_service_provider_config_get(request: web.Request, ) -> web.Response:
    """Get service provider config

    Returns a service provider config for Docker&#39;s configuration. 


    """
    return web.Response(status=200)


async def v2_scim20_users_get(request: web.Request, start_index=None, count=None, filter=None, attributes=None, sort_order=None, sort_by=None) -> web.Response:
    """List users

    List users, returns paginated users for an organization. Use &#x60;startIndex&#x60; and &#x60;count&#x60; query parameters to receive paginated results.  **Sorting:**&lt;br&gt; Sorting lets you to specify the order of returned resources by specifying a combination of &#x60;sortBy&#x60; and &#x60;sortOrder&#x60; query parameters.  The &#x60;sortBy&#x60; parameter specifies the attribute whose value will be used to order the returned responses. The &#x60;sortOrder&#x60; parameter defines the order in which the &#x60;sortBy&#x60; parameter is applied. Allowed values are \&quot;ascending\&quot; and \&quot;descending\&quot;.  **Filtering:**&lt;br&gt; You can request a subset of resources by specifying the &#x60;filter&#x60; query parameter containing a filter expression. Attribute names and attribute operators used in filters are case insensitive. The filter parameter must contain at least one valid expression. Each expression must contain an attribute name followed by an attribute operator and an optional value.  Supported operators are listed below.  - &#x60;eq&#x60; equal - &#x60;ne&#x60; not equal - &#x60;co&#x60; contains - &#x60;sw&#x60; starts with - &#x60;and&#x60; Logical \&quot;and\&quot; - &#x60;or&#x60; Logical \&quot;or\&quot; - &#x60;not&#x60; \&quot;Not\&quot; function - &#x60;()&#x60; Precedence grouping 

    :param start_index: 
    :type start_index: int
    :param count: 
    :type count: int
    :param filter: 
    :type filter: str
    :param attributes: Comma delimited list of attributes to limit to in the response.
    :type attributes: str
    :param sort_order: 
    :type sort_order: str
    :param sort_by: User attribute to sort by.
    :type sort_by: str

    """
    return web.Response(status=200)


async def v2_scim20_users_id_get(request: web.Request, id) -> web.Response:
    """Get a user

    Returns a user by ID. 

    :param id: The user ID.
    :type id: str

    """
    return web.Response(status=200)


async def v2_scim20_users_id_put(request: web.Request, id, body) -> web.Response:
    """Update a user

    Updates a user. Use this route to change the user&#39;s name, activate, and deactivate the user. 

    :param id: The user ID.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = V2Scim20UsersIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def v2_scim20_users_post(request: web.Request, body) -> web.Response:
    """Create user

    Creates a user. If the user already exists by email, they are assigned to the organization on the \&quot;company\&quot; team. 

    :param body: 
    :type body: dict | bytes

    """
    body = V2Scim20UsersPostRequest.from_dict(body)
    return web.Response(status=200)
