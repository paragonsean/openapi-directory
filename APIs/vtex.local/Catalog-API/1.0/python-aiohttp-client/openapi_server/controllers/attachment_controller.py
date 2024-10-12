from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_attachments_get200_response import ApiCatalogPvtAttachmentsGet200Response
from openapi_server.models.attachment_request import AttachmentRequest
from openapi_server.models.attachment_response import AttachmentResponse
from openapi_server import util


async def api_catalog_pvt_attachment_attachmentid_delete(request: web.Request, attachmentid, content_type, accept) -> web.Response:
    """Delete attachment

    Deletes a previously existing SKU attachment.

    :param attachmentid: Attachment ID.
    :type attachmentid: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_catalog_pvt_attachment_attachmentid_get(request: web.Request, attachmentid, content_type, accept) -> web.Response:
    """Get attachment

    Gets information about a registered attachment.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

    :param attachmentid: Attachment ID.
    :type attachmentid: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_catalog_pvt_attachment_attachmentid_put(request: web.Request, attachmentid, content_type, accept, body=None) -> web.Response:
    """Update attachment

    Updates a previously existing SKU attachment with new information.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

    :param attachmentid: Attachment ID.
    :type attachmentid: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = AttachmentRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_attachment_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create attachment

    Creates a new SKU attachment.   &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = AttachmentRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_attachments_get(request: web.Request, content_type, accept) -> web.Response:
    """Get all attachments

    Retrieves information about all registered attachments.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Page\&quot;: 1,      \&quot;Size\&quot;: 11,      \&quot;TotalRows\&quot;: 11,      \&quot;TotalPage\&quot;: 1,      \&quot;Data\&quot;: [          {              \&quot;Id\&quot;: 1,              \&quot;Name\&quot;: \&quot;Acessórios do bicho\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;extra\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-3]#1[1-2][1]pricetable1;#3[0-2][0]pricetable2;#5[0-2][0]pricetable3\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 2,              \&quot;Name\&quot;: \&quot;Sobrenome\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Assinatura Teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot; vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 day, 7 day, 1 month, 6 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.begin\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.end\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;31\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1, 2, 20, 31\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 5,              \&quot;Name\&quot;: \&quot;teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 6,              \&quot;Name\&quot;: \&quot;teste2\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 7,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste3\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 8,              \&quot;Name\&quot;: \&quot;teste api nova\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;Basic teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 9,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 10,              \&quot;Name\&quot;: \&quot;Montagens\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 11,              \&quot;Name\&quot;: \&quot;vtex.subscription.subscription\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1,15,28\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 12,              \&quot;Name\&quot;: \&quot;T-Shirt Customization\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;T-Shirt Name\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[]\&quot;                  }              ]          }      ]  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
