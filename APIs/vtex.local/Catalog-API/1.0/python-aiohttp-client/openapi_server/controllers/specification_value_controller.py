from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specificationvalue_post200_response import ApiCatalogPvtSpecificationvaluePost200Response
from openapi_server.models.api_catalog_pvt_specificationvalue_post_request import ApiCatalogPvtSpecificationvaluePostRequest
from openapi_server.models.api_catalog_pvt_specificationvalue_specification_value_id_get200_response import ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response
from openapi_server import util


async def api_catalog_pvt_specificationvalue_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Specification Value

    Creates a new Specification Value for a Category.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 193,      \&quot;Name\&quot;: \&quot;Metal\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 1    }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;FieldValueId\&quot;: 360,    \&quot;FieldId\&quot;: 193,    \&quot;Name\&quot;: \&quot;Metal\&quot;,    \&quot;Text\&quot;: null,    \&quot;IsActive\&quot;: true,    \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtSpecificationvaluePostRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_specificationvalue_specification_value_id_get(request: web.Request, content_type, accept, specification_value_id) -> web.Response:
    """Get Specification Value

    Retrieves general information about a Specification Value.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param specification_value_id: Specification Value’s unique numerical identifier.
    :type specification_value_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_specificationvalue_specification_value_id_put(request: web.Request, content_type, accept, specification_value_id, body=None) -> web.Response:
    """Update Specification Value

    Updates a new Specification Value for a Category.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 193,      \&quot;Name\&quot;: \&quot;Metal\&quot;,      \&quot;Text\&quot;: null,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 1    }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;FieldValueId\&quot;: 360,    \&quot;FieldId\&quot;: 193,    \&quot;Name\&quot;: \&quot;Metal\&quot;,    \&quot;Text\&quot;: null,    \&quot;IsActive\&quot;: true,    \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param specification_value_id:  Specification Value’s unique numerical identifier.
    :type specification_value_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtSpecificationvaluePostRequest.from_dict(body)
    return web.Response(status=200)
