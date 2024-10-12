from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specificationvalue_specification_value_id_get200_response import ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response
from openapi_server.models.get_spec_field_value import GetSpecFieldValue
from openapi_server.models.specifications_insert_field_value_request import SpecificationsInsertFieldValueRequest
from openapi_server.models.specifications_update_field_value_request import SpecificationsUpdateFieldValueRequest
from openapi_server import util


async def specifications_get_field_value(request: web.Request, content_type, accept, field_value_id) -> web.Response:
    """Get Specification Field Value

    Retrieves details from a specification field&#39;s value by this value&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-value-id) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;TesteInsert\&quot;,      \&quot;Text\&quot;: \&quot;Value Description\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param field_value_id: 
    :type field_value_id: str

    """
    return web.Response(status=200)


async def specifications_insert_field_value(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Specification Field Value

    Creates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SpecificationsInsertFieldValueRequest.from_dict(body)
    return web.Response(status=200)


async def specifications_update_field_value(request: web.Request, content_type, accept, body) -> web.Response:
    """Update Specification Field Value

    Updates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification Field Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification-value-id) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 1,      \&quot;FieldValueId\&quot;: 143,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example (200 OK)    &#x60;&#x60;&#x60;json  \&quot;Field Value Updated\&quot;  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SpecificationsUpdateFieldValueRequest.from_dict(body)
    return web.Response(status=200)


async def specifications_values_by_field_id(request: web.Request, content_type, accept, field_id) -> web.Response:
    """Get Specification Values By Field ID

    Gets a list of all specification values from a Specification Field by this field&#39;s ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;FieldValueId\&quot;: 52,          \&quot;Value\&quot;: \&quot;0 a 6 meses\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 1      },      {          \&quot;FieldValueId\&quot;: 53,          \&quot;Value\&quot;: \&quot;1 a 2 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 4      },      {          \&quot;FieldValueId\&quot;: 54,          \&quot;Value\&quot;: \&quot;3 a 4 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 3      },      {          \&quot;FieldValueId\&quot;: 55,          \&quot;Value\&quot;: \&quot;5 a 6 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 2      },      {          \&quot;FieldValueId\&quot;: 56,          \&quot;Value\&quot;: \&quot;7 a 8 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 5      },      {          \&quot;FieldValueId\&quot;: 57,          \&quot;Value\&quot;: \&quot;9 a 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 6      },      {          \&quot;FieldValueId\&quot;: 58,          \&quot;Value\&quot;: \&quot;Acima de 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 7      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param field_id: Specification Field ID.
    :type field_id: int

    """
    return web.Response(status=200)
