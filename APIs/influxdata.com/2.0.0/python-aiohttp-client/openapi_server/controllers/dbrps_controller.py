from typing import List, Dict
from aiohttp import web

from openapi_server.models.dbrp import DBRP
from openapi_server.models.dbrp_update import DBRPUpdate
from openapi_server.models.dbrps import DBRPs
from openapi_server.models.error import Error
from openapi_server import util


async def delete_dbrpid(request: web.Request, org_id, dbrp_id, zap_trace_span=None) -> web.Response:
    """Delete a database retention policy

    

    :param org_id: Specifies the organization ID of the mapping
    :type org_id: str
    :param dbrp_id: The database retention policy mapping
    :type dbrp_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_dbrps(request: web.Request, org_id, zap_trace_span=None, id=None, bucket_id=None, default=None, db=None, rp=None) -> web.Response:
    """List all database retention policy mappings

    

    :param org_id: Specifies the organization ID to filter on
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param id: Specifies the mapping ID to filter on
    :type id: str
    :param bucket_id: Specifies the bucket ID to filter on
    :type bucket_id: str
    :param default: Specifies filtering on default
    :type default: bool
    :param db: Specifies the database to filter on
    :type db: str
    :param rp: Specifies the retention policy to filter on
    :type rp: str

    """
    return web.Response(status=200)


async def get_dbrps_id(request: web.Request, org_id, dbrp_id, zap_trace_span=None) -> web.Response:
    """Retrieve a database retention policy mapping

    

    :param org_id: Specifies the organization ID of the mapping
    :type org_id: str
    :param dbrp_id: The database retention policy mapping ID
    :type dbrp_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_dbrpid(request: web.Request, org_id, dbrp_id, body, zap_trace_span=None) -> web.Response:
    """Update a database retention policy mapping

    

    :param org_id: Specifies the organization ID of the mapping
    :type org_id: str
    :param dbrp_id: The database retention policy mapping.
    :type dbrp_id: str
    :param body: Database retention policy update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = DBRPUpdate.from_dict(body)
    return web.Response(status=200)


async def post_dbrp(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Add a database retention policy mapping

    

    :param body: The database retention policy mapping to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = DBRP.from_dict(body)
    return web.Response(status=200)
