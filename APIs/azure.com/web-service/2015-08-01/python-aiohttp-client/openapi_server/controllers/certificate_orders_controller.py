from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_email import CertificateEmail
from openapi_server.models.certificate_order import CertificateOrder
from openapi_server.models.certificate_order_action import CertificateOrderAction
from openapi_server.models.certificate_order_certificate import CertificateOrderCertificate
from openapi_server.models.certificate_order_certificate_collection import CertificateOrderCertificateCollection
from openapi_server.models.certificate_order_collection import CertificateOrderCollection
from openapi_server.models.reissue_certificate_order_request import ReissueCertificateOrderRequest
from openapi_server.models.renew_certificate_order_request import RenewCertificateOrderRequest
from openapi_server import util


async def certificate_orders_create_or_update_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version, key_vault_certificate) -> web.Response:
    """Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param certificate_order_name: Certificate name
    :type certificate_order_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param key_vault_certificate: Key Vault secret csm Id
    :type key_vault_certificate: dict | bytes

    """
    key_vault_certificate = CertificateOrderCertificate.from_dict(key_vault_certificate)
    return web.Response(status=200)


async def certificate_orders_create_or_update_certificate_order(request: web.Request, resource_group_name, name, subscription_id, api_version, certificate_distinguished_name) -> web.Response:
    """Create or update a certificate purchase order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_distinguished_name: Distinguished name to be used for purchasing certificate
    :type certificate_distinguished_name: dict | bytes

    """
    certificate_distinguished_name = CertificateOrder.from_dict(certificate_distinguished_name)
    return web.Response(status=200)


async def certificate_orders_delete_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version) -> web.Response:
    """Deletes the certificate associated with the certificate order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param certificate_order_name: Certificate name
    :type certificate_order_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_delete_certificate_order(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Delete an existing certificate order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_get_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version) -> web.Response:
    """Get certificate associated with the certificate order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param certificate_order_name: Certificate name
    :type certificate_order_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_get_certificate_order(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get a certificate order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_get_certificate_orders(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get certificate orders in a resource group

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_get_certificates(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version) -> web.Response:
    """List all certificates associated with a certificate order (only one certificate can be associated with an order at a time)

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param certificate_order_name: Certificate name
    :type certificate_order_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_reissue_certificate_order(request: web.Request, resource_group_name, name, subscription_id, api_version, reissue_certificate_order_request) -> web.Response:
    """Reissue an existing certificate order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param reissue_certificate_order_request: Reissue parameters
    :type reissue_certificate_order_request: dict | bytes

    """
    reissue_certificate_order_request = ReissueCertificateOrderRequest.from_dict(reissue_certificate_order_request)
    return web.Response(status=200)


async def certificate_orders_renew_certificate_order(request: web.Request, resource_group_name, name, subscription_id, api_version, renew_certificate_order_request) -> web.Response:
    """Renew an existing certificate order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param renew_certificate_order_request: Renew parameters
    :type renew_certificate_order_request: dict | bytes

    """
    renew_certificate_order_request = RenewCertificateOrderRequest.from_dict(renew_certificate_order_request)
    return web.Response(status=200)


async def certificate_orders_resend_certificate_email(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Resend certificate email

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate order name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_retrieve_certificate_actions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieve the list of certificate actions

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate order name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_retrieve_certificate_email_history(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieve email history

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate order name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_orders_update_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version, key_vault_certificate) -> web.Response:
    """Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param certificate_order_name: Certificate name
    :type certificate_order_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param key_vault_certificate: Key Vault secret csm Id
    :type key_vault_certificate: dict | bytes

    """
    key_vault_certificate = CertificateOrderCertificate.from_dict(key_vault_certificate)
    return web.Response(status=200)


async def certificate_orders_update_certificate_order(request: web.Request, resource_group_name, name, subscription_id, api_version, certificate_distinguished_name) -> web.Response:
    """Create or update a certificate purchase order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_distinguished_name: Distinguished name to be used for purchasing certificate
    :type certificate_distinguished_name: dict | bytes

    """
    certificate_distinguished_name = CertificateOrder.from_dict(certificate_distinguished_name)
    return web.Response(status=200)


async def certificate_orders_verify_domain_ownership(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Verify domain ownership for this certificate order

    

    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param name: Certificate order name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
