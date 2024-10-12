# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_order import CertificateOrder
from openapi_server.models.certificate_order_collection import CertificateOrderCollection


pytestmark = pytest.mark.asyncio

async def test_global_certificate_order_get_all_certificate_orders(client):
    """Test case for global_certificate_order_get_all_certificate_orders

    Lists all domains in a subscription
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_certificate_order_validate_certificate_purchase_information(client):
    """Test case for global_certificate_order_validate_certificate_purchase_information

    Validate certificate purchase information
    """
    certificate_order = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CertificateRegistration/validateCertificateRegistrationInformation'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=certificate_order,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

