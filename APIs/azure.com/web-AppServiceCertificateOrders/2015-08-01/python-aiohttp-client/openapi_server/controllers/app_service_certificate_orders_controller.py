from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_service_certificate_collection import AppServiceCertificateCollection
from openapi_server.models.app_service_certificate_order import AppServiceCertificateOrder
from openapi_server.models.app_service_certificate_order_collection import AppServiceCertificateOrderCollection
from openapi_server.models.app_service_certificate_order_patch_resource import AppServiceCertificateOrderPatchResource
from openapi_server.models.app_service_certificate_orders_resend_request_emails_request import AppServiceCertificateOrdersResendRequestEmailsRequest
from openapi_server.models.app_service_certificate_patch_resource import AppServiceCertificatePatchResource
from openapi_server.models.app_service_certificate_resource import AppServiceCertificateResource
from openapi_server.models.certificate_email import CertificateEmail
from openapi_server.models.certificate_order_action import CertificateOrderAction
from openapi_server.models.reissue_certificate_order_request import ReissueCertificateOrderRequest
from openapi_server.models.renew_certificate_order_request import RenewCertificateOrderRequest
from openapi_server.models.site_seal import SiteSeal
from openapi_server.models.site_seal_request import SiteSealRequest
from openapi_server import util


async def app_service_certificate_orders_create_or_update(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version, certificate_distinguished_name) -> web.Response:
    """Create or update a certificate purchase order.

    Create or update a certificate purchase order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_distinguished_name: Distinguished name to use for the certificate order.
    :type certificate_distinguished_name: dict | bytes

    """
    certificate_distinguished_name = AppServiceCertificateOrder.from_dict(certificate_distinguished_name)
    return web.Response(status=200)


async def app_service_certificate_orders_create_or_update_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version, key_vault_certificate) -> web.Response:
    """Creates or updates a certificate and associates with key vault secret.

    Creates or updates a certificate and associates with key vault secret.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param key_vault_certificate: Key vault certificate resource Id.
    :type key_vault_certificate: dict | bytes

    """
    key_vault_certificate = AppServiceCertificateResource.from_dict(key_vault_certificate)
    return web.Response(status=200)


async def app_service_certificate_orders_delete(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version) -> web.Response:
    """Delete an existing certificate order.

    Delete an existing certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_delete_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version) -> web.Response:
    """Delete the certificate associated with a certificate order.

    Delete the certificate associated with a certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_get(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version) -> web.Response:
    """Get a certificate order.

    Get a certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order..
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_get_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version) -> web.Response:
    """Get the certificate associated with a certificate order.

    Get the certificate associated with a certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """List all certificate orders in a subscription.

    List all certificate orders in a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get certificate orders in a resource group.

    Get certificate orders in a resource group.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_list_certificates(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version) -> web.Response:
    """List all certificates associated with a certificate order.

    List all certificates associated with a certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_reissue(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version, reissue_certificate_order_request) -> web.Response:
    """Reissue an existing certificate order.

    Reissue an existing certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param reissue_certificate_order_request: Parameters for the reissue.
    :type reissue_certificate_order_request: dict | bytes

    """
    reissue_certificate_order_request = ReissueCertificateOrderRequest.from_dict(reissue_certificate_order_request)
    return web.Response(status=200)


async def app_service_certificate_orders_renew(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version, renew_certificate_order_request) -> web.Response:
    """Renew an existing certificate order.

    Renew an existing certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param renew_certificate_order_request: Renew parameters
    :type renew_certificate_order_request: dict | bytes

    """
    renew_certificate_order_request = RenewCertificateOrderRequest.from_dict(renew_certificate_order_request)
    return web.Response(status=200)


async def app_service_certificate_orders_resend_email(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version) -> web.Response:
    """Resend certificate email.

    Resend certificate email.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_resend_request_emails(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version, name_identifier) -> web.Response:
    """Verify domain ownership for this certificate order.

    Verify domain ownership for this certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param name_identifier: Email address
    :type name_identifier: dict | bytes

    """
    name_identifier = AppServiceCertificateOrdersResendRequestEmailsRequest.from_dict(name_identifier)
    return web.Response(status=200)


async def app_service_certificate_orders_retrieve_certificate_actions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieve the list of certificate actions.

    Retrieve the list of certificate actions.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the certificate order.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_retrieve_certificate_email_history(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieve email history.

    Retrieve email history.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the certificate order.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_certificate_orders_retrieve_site_seal(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version, site_seal_request) -> web.Response:
    """Verify domain ownership for this certificate order.

    Verify domain ownership for this certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_seal_request: Site seal request.
    :type site_seal_request: dict | bytes

    """
    site_seal_request = SiteSealRequest.from_dict(site_seal_request)
    return web.Response(status=200)


async def app_service_certificate_orders_update(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version, certificate_distinguished_name) -> web.Response:
    """Create or update a certificate purchase order.

    Create or update a certificate purchase order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_distinguished_name: Distinguished name to use for the certificate order.
    :type certificate_distinguished_name: dict | bytes

    """
    certificate_distinguished_name = AppServiceCertificateOrderPatchResource.from_dict(certificate_distinguished_name)
    return web.Response(status=200)


async def app_service_certificate_orders_update_certificate(request: web.Request, resource_group_name, certificate_order_name, name, subscription_id, api_version, key_vault_certificate) -> web.Response:
    """Creates or updates a certificate and associates with key vault secret.

    Creates or updates a certificate and associates with key vault secret.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param name: Name of the certificate.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param key_vault_certificate: Key vault certificate resource Id.
    :type key_vault_certificate: dict | bytes

    """
    key_vault_certificate = AppServiceCertificatePatchResource.from_dict(key_vault_certificate)
    return web.Response(status=200)


async def app_service_certificate_orders_validate_purchase_information(request: web.Request, subscription_id, api_version, app_service_certificate_order) -> web.Response:
    """Validate information for a certificate order.

    Validate information for a certificate order.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param app_service_certificate_order: Information for a certificate order.
    :type app_service_certificate_order: dict | bytes

    """
    app_service_certificate_order = AppServiceCertificateOrder.from_dict(app_service_certificate_order)
    return web.Response(status=200)


async def app_service_certificate_orders_verify_domain_ownership(request: web.Request, resource_group_name, certificate_order_name, subscription_id, api_version) -> web.Response:
    """Verify domain ownership for this certificate order.

    Verify domain ownership for this certificate order.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param certificate_order_name: Name of the certificate order.
    :type certificate_order_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
