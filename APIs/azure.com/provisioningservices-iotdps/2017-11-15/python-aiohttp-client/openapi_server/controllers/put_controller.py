from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_body_description import CertificateBodyDescription
from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.provisioning_service_description import ProvisioningServiceDescription
from openapi_server import util


async def dps_certificate_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, provisioning_service_name, certificate_name, certificate_description, if_match=None) -> web.Response:
    """Upload the certificate to the provisioning service.

    Add new certificate or update an existing certificate.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param provisioning_service_name: The name of the provisioning service.
    :type provisioning_service_name: str
    :param certificate_name: The name of the certificate create or update.
    :type certificate_name: str
    :param certificate_description: The certificate body.
    :type certificate_description: dict | bytes
    :param if_match: ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate.
    :type if_match: str

    """
    certificate_description = CertificateBodyDescription.from_dict(certificate_description)
    return web.Response(status=200)


async def iot_dps_resource_create_or_update(request: web.Request, subscription_id, resource_group_name, provisioning_service_name, api_version, iot_dps_description) -> web.Response:
    """Create or update the metadata of the provisioning service.

    Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param provisioning_service_name: Name of provisioning service to create or update.
    :type provisioning_service_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param iot_dps_description: Description of the provisioning service to create or update.
    :type iot_dps_description: dict | bytes

    """
    iot_dps_description = ProvisioningServiceDescription.from_dict(iot_dps_description)
    return web.Response(status=200)
