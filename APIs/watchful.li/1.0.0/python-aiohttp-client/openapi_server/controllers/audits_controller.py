from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit import Audit
from openapi_server import util


async def delete_audit_by_id(request: web.Request, id) -> web.Response:
    """Delete a specific audit

    Delete a specific audit

    :param id: ID of audit that needs to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def get_audit_by_id(request: web.Request, id, fields=None) -> web.Response:
    """Find audit by ID

    Returns a audit based on ID

    :param id: ID of audit that needs to be fetched
    :type id: int
    :param fields: Fields to return separate by comas: name,id
    :type fields: str

    """
    return web.Response(status=200)


async def get_audits(request: web.Request, limit=None, limitstart=None, order=None) -> web.Response:
    """Get a list of audits

    Returns a list of audits

    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    :type order: str

    """
    return web.Response(status=200)


async def get_fields_audits(request: web.Request, ) -> web.Response:
    """Get the list of fields

    Returns a list of fields


    """
    return web.Response(status=200)
