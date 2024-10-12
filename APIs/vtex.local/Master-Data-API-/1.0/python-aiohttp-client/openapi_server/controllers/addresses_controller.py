from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_update_address_requests import CreateUpdateAddressRequests
from openapi_server.models.document_response import DocumentResponse
from openapi_server import util


async def create_new_customer_address(request: web.Request, content_type, accept, body, _schema=None) -> web.Response:
    """Create new customer address

    Creates new customer address.     &gt; You can use this request to create customer addresses according to any &#x60;AD&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str

    """
    body = CreateUpdateAddressRequests.from_dict(body)
    return web.Response(status=200)


async def delete_customer_address(request: web.Request, content_type, accept, id) -> web.Response:
    """Delete customer address

    Deletes a customer address.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str

    """
    return web.Response(status=200)


async def update_customer_address(request: web.Request, content_type, accept, id, body, _schema=None) -> web.Response:
    """Update customer address

    Partially updates a customer address.    &gt; You can use this request to update customer addresses according to any &#x60;AD&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

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
    body = CreateUpdateAddressRequests.from_dict(body)
    return web.Response(status=200)
