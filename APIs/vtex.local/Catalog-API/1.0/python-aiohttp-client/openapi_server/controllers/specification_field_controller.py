from typing import List, Dict
from aiohttp import web

from openapi_server.models.specifications_field200_response import SpecificationsField200Response
from openapi_server.models.specifications_insert_field_request import SpecificationsInsertFieldRequest
from openapi_server.models.specifications_insert_field_update_request import SpecificationsInsertFieldUpdateRequest
from openapi_server import util


async def specifications_field(request: web.Request, content_type, accept, field_id) -> web.Response:
    """Get Specification Field

    Retrieves details from a specification field by this field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-specification-specificationid) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldId\&quot;: 88,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;FieldTypeName\&quot;: \&quot;Texto\&quot;,      \&quot;FieldValueId\&quot;: null,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: null,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param field_id: Specification Field ID.
    :type field_id: int

    """
    return web.Response(status=200)


async def specifications_insert_field(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Specification Field

    Creates a specification field in a category.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification) instead.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldId\&quot;: 88,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;FieldValueId\&quot;: 1,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: true,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: null,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  89  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SpecificationsInsertFieldRequest.from_dict(body)
    return web.Response(status=200)


async def specifications_insert_field_update(request: web.Request, content_type, accept, body) -> web.Response:
    """Update Specification Field

    Updates a specification field in a category.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification) instead.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 89,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: true,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: false,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  89  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SpecificationsInsertFieldUpdateRequest.from_dict(body)
    return web.Response(status=200)
