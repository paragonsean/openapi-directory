from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specificationgroup_group_id_put200_response import ApiCatalogPvtSpecificationgroupGroupIdPut200Response
from openapi_server.models.request_body8 import RequestBody8
from openapi_server.models.specification_group_insert2200_response import SpecificationGroupInsert2200Response
from openapi_server.models.specification_group_insert_request import SpecificationGroupInsertRequest
from openapi_server.models.specifications_group import SpecificationsGroup
from openapi_server import util


async def api_catalog_pvt_specificationgroup_group_id_put(request: web.Request, content_type, accept, group_id, body=None) -> web.Response:
    """Update Specification Group

    Update a specification group.   &gt;⚠️ It is also possible to update a Specification Group by using an alternative legacy route: &#x60;/api/catalog_system/pvt/specification/group&#x60;.    ## Request and response body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1,      \&quot;Id\&quot;: 17,      \&quot;Name\&quot;: \&quot;NewGroupName\&quot;,      \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group’s unique numerical identifier.
    :type group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody8.from_dict(body)
    return web.Response(status=200)


async def specification_group_insert2(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Specification Group

    Create a specification group.   &gt;⚠️ It is also possible to create a Specification Group by using an alternative legacy route: &#x60;/api/catalog_system/pvt/specification/group&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1,      \&quot;Name\&quot;: \&quot;Sizes\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 6,    \&quot;CategoryId\&quot;: 1,    \&quot;Name\&quot;: \&quot;Sizes\&quot;,    \&quot;Position\&quot;: 3  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SpecificationGroupInsertRequest.from_dict(body)
    return web.Response(status=200)


async def specifications_group_get(request: web.Request, content_type, accept, group_id) -> web.Response:
    """Get Specification Group

    Retrieves details from a specification group by the ID of the group.   ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;CategoryId\&quot;: 1,    \&quot;Id\&quot;: 6,    \&quot;Name\&quot;: \&quot;Sizes\&quot;,    \&quot;Position\&quot;: 3  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Specification Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def specifications_group_listby_category(request: web.Request, content_type, accept, category_id) -> web.Response:
    """List Specification Group by Category

    Retrieves a list of specification groups by the category ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {        \&quot;CategoryId\&quot;: 1,        \&quot;Id\&quot;: 5,        \&quot;Name\&quot;: \&quot;Materials\&quot;,        \&quot;Position\&quot;: 2      },      {        \&quot;CategoryId\&quot;: 1,        \&quot;Id\&quot;: 6,        \&quot;Name\&quot;: \&quot;Sizes\&quot;,        \&quot;Position\&quot;: 3      }    ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param category_id: 
    :type category_id: str

    """
    return web.Response(status=200)
