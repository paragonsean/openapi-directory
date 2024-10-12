from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_or_replace_documents_request_inner import AddOrReplaceDocumentsRequestInner
from openapi_server.models.add_or_update_documents_request_inner import AddOrUpdateDocumentsRequestInner
from openapi_server import util


async def add_or_replace_documents(request: web.Request, primary_key=None, csv_delimiter=None, body=None) -> web.Response:
    """Add or replace documents

    Add or replace documents

    :param primary_key: 
    :type primary_key: str
    :param csv_delimiter: 
    :type csv_delimiter: str
    :param body: 
    :type body: list | bytes

    """
    body = [AddOrReplaceDocumentsRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def add_or_update_documents(request: web.Request, primary_key=None, csv_delimiter=None, body=None) -> web.Response:
    """Add or update documents

    Add or update documents

    :param primary_key: 
    :type primary_key: str
    :param csv_delimiter: 
    :type csv_delimiter: str
    :param body: 
    :type body: list | bytes

    """
    body = [AddOrUpdateDocumentsRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_all_documents(request: web.Request, ) -> web.Response:
    """Delete all documents

    Delete all documents


    """
    return web.Response(status=200)


async def delete_documents(request: web.Request, body=None) -> web.Response:
    """Delete documents

    Delete documents

    :param body: 
    :type body: List[]

    """
    return web.Response(status=200)


async def delete_one_document(request: web.Request, ) -> web.Response:
    """Delete one document

    Delete one document


    """
    return web.Response(status=200)


async def get_documents(request: web.Request, limit=None, offset=None, fields=None) -> web.Response:
    """Get documents

    Get documents

    :param limit: 
    :type limit: str
    :param offset: 
    :type offset: str
    :param fields: 
    :type fields: str

    """
    return web.Response(status=200)


async def get_one_document(request: web.Request, fields=None) -> web.Response:
    """Get one document

    Get one document

    :param fields: 
    :type fields: str

    """
    return web.Response(status=200)
