from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.secret_keys import SecretKeys
from openapi_server.models.secret_keys_response import SecretKeysResponse
from openapi_server import util


async def get_orgs_id_secrets(request: web.Request, org_id, zap_trace_span=None) -> web.Response:
    """List all secret keys for an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_orgs_id_secrets(request: web.Request, org_id, body, zap_trace_span=None) -> web.Response:
    """Update secrets in an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param body: Secret key value pairs to update/add
    :type body: Dict[str, str]
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def post_orgs_id_secrets(request: web.Request, org_id, body, zap_trace_span=None) -> web.Response:
    """Delete secrets from an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param body: Secret key to delete
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = SecretKeys.from_dict(body)
    return web.Response(status=200)
