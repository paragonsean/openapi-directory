# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.three_d_secure import ThreeDSecure


pytestmark = pytest.mark.asyncio

async def test_get3_d_secure(client):
    """Test case for get3_d_secure

    Retrieve a ThreeDSecure entry
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/3dsecure/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get3_d_secure_collection(client):
    """Test case for get3_d_secure_collection

    Retrieve a list of ThreeDSecure entries
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/3dsecure',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post3_d_secure(client):
    """Test case for post3_d_secure

    Create a ThreeDSecure entry
    """
    body = {"amount":0.8008281904610115,"payerAuthResponseStatus":"Y","paymentCardId":"","signatureVerification":"Y","_links":[{"rel":"self"},{"rel":"self"}],"gatewayAccountId":"","eci":6,"cavv":"cavv","websiteId":"","xid":"xid","customerId":"","createdTime":"","currency":"","id":"","enrolled":"Y","enrollmentEci":"enrollmentEci"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/3dsecure',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

