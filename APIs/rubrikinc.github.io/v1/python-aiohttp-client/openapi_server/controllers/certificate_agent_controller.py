from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_secondary_certificate_info import AgentSecondaryCertificateInfo
from openapi_server.models.agent_secondary_certificate_info_list_response import AgentSecondaryCertificateInfoListResponse
from openapi_server import util


async def mark_agent_secondary_certificate(request: web.Request, body) -> web.Response:
    """Mark a certificate to be added to agents

    Mark a secondary cluster certificate to be asynchronously synced to all Rubrik Backup Service instances for which this cluster is the primary.

    :param body: ID of certificate to add.
    :type body: str

    """
    return web.Response(status=200)


async def query_agent_secondary_certificate(request: web.Request, is_agent_enabled=None) -> web.Response:
    """Get all potential agent secondary cluster certificates

    Get all certificates that have been added to the cluster and qualify to be secondary cluster certificates for the Rubrik Backup Service. This call retrieves any certificates that are detected to be Rubrik cluster certificates.

    :param is_agent_enabled: Filter based on whether or not certificates have been marked for use by agents.
    :type is_agent_enabled: bool

    """
    return web.Response(status=200)


async def unmark_agent_secondary_certificate(request: web.Request, id) -> web.Response:
    """Unmark a certificate that was previously marked

    Unmark a previously marked secondary cluster certificate to be asynchronously removed from all Rubrik Backup Service instances for which this cluster is the primary.

    :param id: ID of certificate to remove.
    :type id: str

    """
    return web.Response(status=200)
