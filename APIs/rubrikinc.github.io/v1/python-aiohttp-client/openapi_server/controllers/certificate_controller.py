from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_import_request import CertificateImportRequest
from openapi_server.models.certificate_patch_request import CertificatePatchRequest
from openapi_server.models.certificate_summary import CertificateSummary
from openapi_server.models.certificate_summary_list_response import CertificateSummaryListResponse
from openapi_server import util


async def delete_certificate(request: web.Request, id) -> web.Response:
    """Delete imported certificate object

    Deletes an imported certificate.

    :param id: The certificate ID.
    :type id: str

    """
    return web.Response(status=200)


async def export_certificate(request: web.Request, id) -> web.Response:
    """Get a certificate summary to export

    Get a certificate summary.

    :param id: ID of certificate to export.
    :type id: str

    """
    return web.Response(status=200)


async def import_certificate(request: web.Request, body) -> web.Response:
    """Import a certificate

    Import a certificate.

    :param body: Request to import a certificate.
    :type body: dict | bytes

    """
    body = CertificateImportRequest.from_dict(body)
    return web.Response(status=200)


async def query_certificates(request: web.Request, name=None, has_key=None, description=None, expiration=None, include_expired=None, sort_by=None, sort_order=None) -> web.Response:
    """Get all certificates

    Get all certificates.

    :param name: Search by certificate name.
    :type name: str
    :param has_key: Search certificates by whether or not they contain a private key. 
    :type has_key: bool
    :param description: Search certificates by description.
    :type description: str
    :param expiration: Search certificates by expiration.
    :type expiration: str
    :param include_expired: Specifies whether to include expired certificates. The default is false.
    :type include_expired: bool
    :param sort_by: Attribute by which the list of certificates is sorted.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def update_certificate(request: web.Request, id, body) -> web.Response:
    """Update a certificate entry

    Provide updated information for a certificate object.

    :param id: ID of certificate object to update.
    :type id: str
    :param body: Patch request to update a certificate object.
    :type body: dict | bytes

    """
    body = CertificatePatchRequest.from_dict(body)
    return web.Response(status=200)
