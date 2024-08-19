from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_request import CertificateRequest
from openapi_server.models.vault_certificate_response import VaultCertificateResponse
from openapi_server import util


async def vault_certificates_create(request: web.Request, subscription_id, api_version, resource_group_name, vault_name, certificate_name, certificate_request) -> web.Response:
    """vault_certificates_create

    Uploads a certificate for a resource.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param certificate_name: Certificate friendly name.
    :type certificate_name: str
    :param certificate_request: Input parameters for uploading the vault certificate.
    :type certificate_request: dict | bytes

    """
    certificate_request = CertificateRequest.from_dict(certificate_request)
    return web.Response(status=200)
