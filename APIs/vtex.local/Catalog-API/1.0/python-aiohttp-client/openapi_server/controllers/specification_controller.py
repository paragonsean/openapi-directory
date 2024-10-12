from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specification_post200_response import ApiCatalogPvtSpecificationPost200Response
from openapi_server.models.api_catalog_pvt_specification_post_request import ApiCatalogPvtSpecificationPostRequest
from openapi_server.models.request_body6 import RequestBody6
from openapi_server.models.request_body7 import RequestBody7
from openapi_server import util


async def api_catalog_pvt_specification_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Specification

    Creates a new Product or SKU Specification.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;  

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtSpecificationPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_specification_specification_id_get(request: web.Request, content_type, accept, specification_id) -> web.Response:
    """Get Specification

    Retrieves information of a Product or SKU Specification.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;  

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param specification_id: Specification’s unique numerical identifier.
    :type specification_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_specification_specification_id_put(request: web.Request, content_type, accept, specification_id, body=None) -> web.Response:
    """Update Specification

    Updates a Product or SKU Specification.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Leather\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Leather\&quot;  }  &#x60;&#x60;&#x60;  

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param specification_id: Specification’s unique numerical identifier.
    :type specification_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody7.from_dict(body)
    return web.Response(status=200)
