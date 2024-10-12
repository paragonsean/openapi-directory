from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_collection import CertificateCollection
from openapi_server.models.certificate_patch_resource import CertificatePatchResource
from openapi_server import util


async def certificates_create_or_update(request: web.Request, resource_group_name, name, subscription_id, api_version, certificate_envelope) -> web.Response:
    """Create or update a certificate.

    Create or update a certificate.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_envelope: Details of certificate, if it exists already.
    :type certificate_envelope: dict | bytes

    """
    certificate_envelope = Certificate.from_dict(certificate_envelope)
    return web.Response(status=200)


async def certificates_delete(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Delete a certificate.

    Delete a certificate.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_get(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get a certificate.

    Get a certificate.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all certificates for a subscription.

    Get all certificates for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get all certificates in a resource group.

    Get all certificates in a resource group.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_update(request: web.Request, resource_group_name, name, subscription_id, api_version, certificate_envelope) -> web.Response:
    """Create or update a certificate.

    Create or update a certificate.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_envelope: Details of certificate, if it exists already.
    :type certificate_envelope: dict | bytes

    """
    certificate_envelope = CertificatePatchResource.from_dict(certificate_envelope)
    return web.Response(status=200)
