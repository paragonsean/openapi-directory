from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_bundle import CertificateBundle
from openapi_server.models.deleted_certificate_bundle import DeletedCertificateBundle
from openapi_server.models.deleted_certificate_list_result import DeletedCertificateListResult
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server import util


async def get_deleted_certificate(request: web.Request, certificate_name, api_version) -> web.Response:
    """Retrieves information about the specified deleted certificate.

    The GetDeletedCertificate operation retrieves the deleted certificate information plus its attributes, such as retention interval, scheduled permanent deletion and the current deletion recovery level. This operation requires the certificates/get permission.

    :param certificate_name: The name of the certificate
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_deleted_certificates(request: web.Request, api_version, maxresults=None, include_pending=None) -> web.Response:
    """Lists the deleted certificates in the specified vault currently available for recovery.

    The GetDeletedCertificates operation retrieves the certificates in the current vault which are in a deleted state and ready for recovery or purging. This operation includes deletion-specific information. This operation requires the certificates/get/list permission. This operation can only be enabled on soft-delete enabled vaults.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int
    :param include_pending: Specifies whether to include certificates which are not completely provisioned.
    :type include_pending: bool

    """
    return web.Response(status=200)


async def purge_deleted_certificate(request: web.Request, certificate_name, api_version) -> web.Response:
    """Permanently deletes the specified deleted certificate.

    The PurgeDeletedCertificate operation performs an irreversible deletion of the specified certificate, without possibility for recovery. The operation is not available if the recovery level does not specify &#39;Purgeable&#39;. This operation requires the certificate/purge permission.

    :param certificate_name: The name of the certificate
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def recover_deleted_certificate(request: web.Request, certificate_name, api_version) -> web.Response:
    """Recovers the deleted certificate back to its current version under /certificates.

    The RecoverDeletedCertificate operation performs the reversal of the Delete operation. The operation is applicable in vaults enabled for soft-delete, and must be issued during the retention interval (available in the deleted certificate&#39;s attributes). This operation requires the certificates/recover permission.

    :param certificate_name: The name of the deleted certificate
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
