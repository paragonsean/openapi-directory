from typing import List, Dict
from aiohttp import web

from openapi_server.models.buckets import Buckets
from openapi_server.models.error import Error
from openapi_server.models.health_check import HealthCheck
from openapi_server.models.source import Source
from openapi_server.models.sources import Sources
from openapi_server import util


async def delete_sources_id(request: web.Request, source_id, zap_trace_span=None) -> web.Response:
    """Delete a source

    

    :param source_id: The source ID.
    :type source_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_sources(request: web.Request, zap_trace_span=None, org=None) -> web.Response:
    """List all sources

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org: The name of the organization.
    :type org: str

    """
    return web.Response(status=200)


async def get_sources_id(request: web.Request, source_id, zap_trace_span=None) -> web.Response:
    """Retrieve a source

    

    :param source_id: The source ID.
    :type source_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_sources_id_buckets(request: web.Request, source_id, zap_trace_span=None, org=None) -> web.Response:
    """Get buckets in a source

    

    :param source_id: The source ID.
    :type source_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org: The name of the organization.
    :type org: str

    """
    return web.Response(status=200)


async def get_sources_id_health(request: web.Request, source_id, zap_trace_span=None) -> web.Response:
    """Get the health of a source

    

    :param source_id: The source ID.
    :type source_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_sources_id(request: web.Request, source_id, body, zap_trace_span=None) -> web.Response:
    """Update a Source

    

    :param source_id: The source ID.
    :type source_id: str
    :param body: Source update
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = Source.from_dict(body)
    return web.Response(status=200)


async def post_sources(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a source

    

    :param body: Source to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = Source.from_dict(body)
    return web.Response(status=200)
