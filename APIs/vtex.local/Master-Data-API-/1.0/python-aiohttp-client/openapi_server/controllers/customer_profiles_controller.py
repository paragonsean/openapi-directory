from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_update_profile_requests import CreateUpdateProfileRequests
from openapi_server.models.document_response import DocumentResponse
from openapi_server import util


async def create_new_customer_profilev2(request: web.Request, content_type, accept, body, _schema=None) -> web.Response:
    """Create new customer profile

    Creates new customer profile.    &gt; You can use this request to create customer profiles according to any &#x60;CL&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str

    """
    body = CreateUpdateProfileRequests.from_dict(body)
    return web.Response(status=200)


async def delete_customer_profile(request: web.Request, content_type, accept, id) -> web.Response:
    """Delete customer profile

    Deletes a customer profile.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str

    """
    return web.Response(status=200)


async def update_customer_profile(request: web.Request, content_type, accept, id, body, _schema=None) -> web.Response:
    """Update customer profile

    Partially updates a customer profile.    &gt; You can use this request to update customer profiles according to any &#x60;CL&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str

    """
    body = CreateUpdateProfileRequests.from_dict(body)
    return web.Response(status=200)
