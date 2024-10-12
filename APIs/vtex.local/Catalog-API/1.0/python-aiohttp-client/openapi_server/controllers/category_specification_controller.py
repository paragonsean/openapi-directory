from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_specification_inner import CategorySpecificationInner
from openapi_server import util


async def specifications_by_category_id(request: web.Request, content_type, accept, category_id) -> web.Response:
    """Get Specifications By Category ID

    Retrieves all specifications from a category by its ID.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Name\&quot;: \&quot;Specification A\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification B\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification C\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 35,          \&quot;IsActive\&quot;: false,          \&quot;IsStockKeepingUnit\&quot;: false      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param category_id: Category ID.
    :type category_id: int

    """
    return web.Response(status=200)


async def specifications_tree_by_category_id(request: web.Request, content_type, accept, category_id) -> web.Response:
    """Get Specifications Tree By Category ID

    Lists all specifications including the current category and the level zero specifications from a category by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Name\&quot;: \&quot;Specification A\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification B\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification C\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 35,          \&quot;IsActive\&quot;: false,          \&quot;IsStockKeepingUnit\&quot;: false      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param category_id: Category ID.
    :type category_id: int

    """
    return web.Response(status=200)
