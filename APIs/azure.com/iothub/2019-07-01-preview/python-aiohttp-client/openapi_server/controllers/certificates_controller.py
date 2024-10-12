from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_body_description import CertificateBodyDescription
from openapi_server.models.certificate_description import CertificateDescription
from openapi_server.models.certificate_list_description import CertificateListDescription
from openapi_server.models.certificate_verification_description import CertificateVerificationDescription
from openapi_server.models.certificate_with_nonce_description import CertificateWithNonceDescription
from openapi_server.models.error_details import ErrorDetails
from openapi_server import util


async def certificates_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, certificate_name, certificate_description, if_match=None) -> web.Response:
    """Upload the certificate to the IoT hub.

    Adds new or replaces existing certificate.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param certificate_name: The name of the certificate
    :type certificate_name: str
    :param certificate_description: The certificate body.
    :type certificate_description: dict | bytes
    :param if_match: ETag of the Certificate. Do not specify for creating a brand new certificate. Required to update an existing certificate.
    :type if_match: str

    """
    certificate_description = CertificateBodyDescription.from_dict(certificate_description)
    return web.Response(status=200)


async def certificates_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, certificate_name, if_match) -> web.Response:
    """Delete an X509 certificate.

    Deletes an existing X509 certificate or does nothing if it does not exist.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param certificate_name: The name of the certificate
    :type certificate_name: str
    :param if_match: ETag of the Certificate.
    :type if_match: str

    """
    return web.Response(status=200)


async def certificates_generate_verification_code(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, certificate_name, if_match) -> web.Response:
    """Generate verification code for proof of possession flow.

    Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param certificate_name: The name of the certificate
    :type certificate_name: str
    :param if_match: ETag of the Certificate.
    :type if_match: str

    """
    return web.Response(status=200)


async def certificates_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, certificate_name) -> web.Response:
    """Get the certificate.

    Returns the certificate.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param certificate_name: The name of the certificate
    :type certificate_name: str

    """
    return web.Response(status=200)


async def certificates_list_by_iot_hub(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Get the certificate list.

    Returns the list of certificates.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def certificates_verify(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, certificate_name, if_match, certificate_verification_body) -> web.Response:
    """Verify certificate&#39;s private key possession.

    Verifies the certificate&#39;s private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param certificate_name: The name of the certificate
    :type certificate_name: str
    :param if_match: ETag of the Certificate.
    :type if_match: str
    :param certificate_verification_body: The name of the certificate
    :type certificate_verification_body: dict | bytes

    """
    certificate_verification_body = CertificateVerificationDescription.from_dict(certificate_verification_body)
    return web.Response(status=200)
