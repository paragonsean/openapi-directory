from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_collection import CertificateCollection
from openapi_server.models.csr import Csr
from openapi_server import util


async def certificates_create_or_update_certificate(request: web.Request, resource_group_name, name, subscription_id, api_version, certificate_envelope) -> web.Response:
    """Creates or modifies an existing certificate.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_envelope: Details of certificate if it exists already.
    :type certificate_envelope: dict | bytes

    """
    certificate_envelope = Certificate.from_dict(certificate_envelope)
    return web.Response(status=200)


async def certificates_create_or_update_csr(request: web.Request, resource_group_name, name, subscription_id, api_version, csr_envelope) -> web.Response:
    """Creates or modifies an existing certificate signing request.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param csr_envelope: Details of certificate signing request if it exists already.
    :type csr_envelope: dict | bytes

    """
    csr_envelope = Csr.from_dict(csr_envelope)
    return web.Response(status=200)


async def certificates_delete_certificate(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Delete a certificate by name in a specified subscription and resourcegroup.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate to be deleted.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_delete_csr(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Delete the certificate signing request.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate signing request.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_get_certificate(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get a certificate by certificate name for a subscription in the specified resource group.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_get_certificates(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get certificates for a subscription in the specified resource group.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_get_csr(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets a certificate signing request by certificate name for a subscription in the specified resource group

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_get_csrs(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Gets the certificate signing requests for a subscription in the specified resource group

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificates_update_certificate(request: web.Request, resource_group_name, name, subscription_id, api_version, certificate_envelope) -> web.Response:
    """Creates or modifies an existing certificate.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_envelope: Details of certificate if it exists already.
    :type certificate_envelope: dict | bytes

    """
    certificate_envelope = Certificate.from_dict(certificate_envelope)
    return web.Response(status=200)


async def certificates_update_csr(request: web.Request, resource_group_name, name, subscription_id, api_version, csr_envelope) -> web.Response:
    """Creates or modifies an existing certificate signing request.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param csr_envelope: Details of certificate signing request if it exists already.
    :type csr_envelope: dict | bytes

    """
    csr_envelope = Csr.from_dict(csr_envelope)
    return web.Response(status=200)
