from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_document_response import ListDocumentResponse
from openapi_server.models.sync_v1_service_document import SyncV1ServiceDocument
from openapi_server import util


async def create_document(request: web.Request, service_sid, data=None, ttl=None, unique_name=None) -> web.Response:
    """create_document

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Document resource in.
    :type service_sid: str
    :param data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be up to 16 KiB in length.
    :type data: dict | bytes
    :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Document expires and is deleted (the Sync Document&#39;s time-to-live).
    :type ttl: int
    :param unique_name: An application-defined string that uniquely identifies the Sync Document
    :type unique_name: str

    """
    data = object.from_dict(data)
    return web.Response(status=200)


async def delete_document(request: web.Request, service_sid, sid) -> web.Response:
    """delete_document

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document resource to delete.
    :type service_sid: str
    :param sid: The SID of the Document resource to delete. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_document(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_document

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document resource to fetch.
    :type service_sid: str
    :param sid: The SID of the Document resource to fetch. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type sid: str

    """
    return web.Response(status=200)


async def list_document(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_document

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document resources to read.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_document(request: web.Request, service_sid, sid, if_match=None, data=None, ttl=None) -> web.Response:
    """update_document

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document resource to update.
    :type service_sid: str
    :param sid: The SID of the Document resource to update. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type sid: str
    :param if_match: The If-Match HTTP request header
    :type if_match: str
    :param data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be up to 16 KiB in length.
    :type data: dict | bytes
    :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Document expires and is deleted (time-to-live).
    :type ttl: int

    """
    data = object.from_dict(data)
    return web.Response(status=200)
