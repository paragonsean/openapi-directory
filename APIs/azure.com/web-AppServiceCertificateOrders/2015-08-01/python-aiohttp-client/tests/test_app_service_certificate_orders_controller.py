# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_create_or_update(client):
    """Test case for app_service_certificate_orders_create_or_update

    Create or update a certificate purchase order.
    """
    certificate_distinguished_name = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=certificate_distinguished_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_create_or_update_certificate(client):
    """Test case for app_service_certificate_orders_create_or_update_certificate

    Creates or updates a certificate and associates with key vault secret.
    """
    key_vault_certificate = {"properties":{"keyVaultSecretName":"keyVaultSecretName","provisioningState":"Initialized","keyVaultId":"keyVaultId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/certificates/{name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=key_vault_certificate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_delete(client):
    """Test case for app_service_certificate_orders_delete

    Delete an existing certificate order.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_delete_certificate(client):
    """Test case for app_service_certificate_orders_delete_certificate

    Delete the certificate associated with a certificate order.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/certificates/{name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_get(client):
    """Test case for app_service_certificate_orders_get

    Get a certificate order.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_get_certificate(client):
    """Test case for app_service_certificate_orders_get_certificate

    Get the certificate associated with a certificate order.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/certificates/{name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_list(client):
    """Test case for app_service_certificate_orders_list

    List all certificate orders in a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CertificateRegistration/certificateOrders'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_list_by_resource_group(client):
    """Test case for app_service_certificate_orders_list_by_resource_group

    Get certificate orders in a resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_list_certificates(client):
    """Test case for app_service_certificate_orders_list_certificates

    List all certificates associated with a certificate order.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/certificates'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_reissue(client):
    """Test case for app_service_certificate_orders_reissue

    Reissue an existing certificate order.
    """
    reissue_certificate_order_request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/reissue'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=reissue_certificate_order_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_renew(client):
    """Test case for app_service_certificate_orders_renew

    Renew an existing certificate order.
    """
    renew_certificate_order_request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/renew'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=renew_certificate_order_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_resend_email(client):
    """Test case for app_service_certificate_orders_resend_email

    Resend certificate email.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/resendEmail'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_resend_request_emails(client):
    """Test case for app_service_certificate_orders_resend_request_emails

    Verify domain ownership for this certificate order.
    """
    name_identifier = openapi_server.AppServiceCertificateOrdersResendRequestEmailsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/resendRequestEmails'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=name_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_retrieve_certificate_actions(client):
    """Test case for app_service_certificate_orders_retrieve_certificate_actions

    Retrieve the list of certificate actions.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveCertificateActions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_retrieve_certificate_email_history(client):
    """Test case for app_service_certificate_orders_retrieve_certificate_email_history

    Retrieve email history.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveEmailHistory'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_retrieve_site_seal(client):
    """Test case for app_service_certificate_orders_retrieve_site_seal

    Verify domain ownership for this certificate order.
    """
    site_seal_request = {"lightTheme":True,"locale":"locale"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/retrieveSiteSeal'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_seal_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_update(client):
    """Test case for app_service_certificate_orders_update

    Create or update a certificate purchase order.
    """
    certificate_distinguished_name = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=certificate_distinguished_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_update_certificate(client):
    """Test case for app_service_certificate_orders_update_certificate

    Creates or updates a certificate and associates with key vault secret.
    """
    key_vault_certificate = {"properties":{"keyVaultSecretName":"keyVaultSecretName","provisioningState":"Initialized","keyVaultId":"keyVaultId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/certificates/{name}'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=key_vault_certificate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_validate_purchase_information(client):
    """Test case for app_service_certificate_orders_validate_purchase_information

    Validate information for a certificate order.
    """
    app_service_certificate_order = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CertificateRegistration/validateCertificateRegistrationInformation'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=app_service_certificate_order,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_service_certificate_orders_verify_domain_ownership(client):
    """Test case for app_service_certificate_orders_verify_domain_ownership

    Verify domain ownership for this certificate order.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificate_order_name}/verifyDomainOwnership'.format(resource_group_name='resource_group_name_example', certificate_order_name='certificate_order_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

