# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_email import CertificateEmail
from openapi_server.models.certificate_order import CertificateOrder
from openapi_server.models.certificate_order_action import CertificateOrderAction
from openapi_server.models.certificate_order_certificate import CertificateOrderCertificate
from openapi_server.models.certificate_order_certificate_collection import CertificateOrderCertificateCollection
from openapi_server.models.certificate_order_collection import CertificateOrderCollection
from openapi_server.models.reissue_certificate_order_request import ReissueCertificateOrderRequest
from openapi_server.models.renew_certificate_order_request import RenewCertificateOrderRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_certificate_orders_create_or_update_certificate(client):
    """Test case for certificate_orders_create_or_update_certificate

    Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it's ready
    """
    key_vault_certificate = {"properties":"{}"}
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_certificate_orders_create_or_update_certificate_order(client):
    """Test case for certificate_orders_create_or_update_certificate_order

    Create or update a certificate purchase order
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=certificate_distinguished_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_orders_delete_certificate(client):
    """Test case for certificate_orders_delete_certificate

    Deletes the certificate associated with the certificate order
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
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

async def test_certificate_orders_delete_certificate_order(client):
    """Test case for certificate_orders_delete_certificate_order

    Delete an existing certificate order
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_orders_get_certificate(client):
    """Test case for certificate_orders_get_certificate

    Get certificate associated with the certificate order
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

async def test_certificate_orders_get_certificate_order(client):
    """Test case for certificate_orders_get_certificate_order

    Get a certificate order
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_orders_get_certificate_orders(client):
    """Test case for certificate_orders_get_certificate_orders

    Get certificate orders in a resource group
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

async def test_certificate_orders_get_certificates(client):
    """Test case for certificate_orders_get_certificates

    List all certificates associated with a certificate order (only one certificate can be associated with an order at a time)
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_certificate_orders_reissue_certificate_order(client):
    """Test case for certificate_orders_reissue_certificate_order

    Reissue an existing certificate order
    """
    reissue_certificate_order_request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/reissue'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=reissue_certificate_order_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_certificate_orders_renew_certificate_order(client):
    """Test case for certificate_orders_renew_certificate_order

    Renew an existing certificate order
    """
    renew_certificate_order_request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/renew'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=renew_certificate_order_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_orders_resend_certificate_email(client):
    """Test case for certificate_orders_resend_certificate_email

    Resend certificate email
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/resendEmail'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_orders_retrieve_certificate_actions(client):
    """Test case for certificate_orders_retrieve_certificate_actions

    Retrieve the list of certificate actions
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

async def test_certificate_orders_retrieve_certificate_email_history(client):
    """Test case for certificate_orders_retrieve_certificate_email_history

    Retrieve email history
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_certificate_orders_update_certificate(client):
    """Test case for certificate_orders_update_certificate

    Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it's ready
    """
    key_vault_certificate = {"properties":"{}"}
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_certificate_orders_update_certificate_order(client):
    """Test case for certificate_orders_update_certificate_order

    Create or update a certificate purchase order
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=certificate_distinguished_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_orders_verify_domain_ownership(client):
    """Test case for certificate_orders_verify_domain_ownership

    Verify domain ownership for this certificate order
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/verifyDomainOwnership'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

