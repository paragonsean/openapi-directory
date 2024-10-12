# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verify_check200_response import VerifyCheck200Response
from openapi_server.models.verify_control200_response import VerifyControl200Response
from openapi_server.models.verify_request_with_psd2200_response import VerifyRequestWithPSD2200Response
from openapi_server.models.verify_search200_response import VerifySearch200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_verify_check(client):
    """Test case for verify_check

    Verify Check
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'code': 'code_example',
        'ip_address': 'ip_address_example',
        'request_id': 'request_id_example'
        }
    response = await client.request(
        method='POST',
        path='/verify/check/{format}'.format(format='json'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_verify_control(client):
    """Test case for verify_control

    Verify Control
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'cmd': 'cmd_example',
        'request_id': 'request_id_example'
        }
    response = await client.request(
        method='POST',
        path='/verify/control/{format}'.format(format='json'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_verify_request_with_psd2(client):
    """Test case for verify_request_with_psd2

    PSD2 (Payment Services Directive 2) Request
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'amount': 3.4,
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'code_length': 4,
        'country': 'country_example',
        'lg': en-gb,
        'next_event_wait': 300,
        'number': 'number_example',
        'payee': 'payee_example',
        'pin_expiry': 300,
        'workflow_id': 1
        }
    response = await client.request(
        method='POST',
        path='/verify/psd2/{format}'.format(format='json'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_search(client):
    """Test case for verify_search

    Verify Search
    """
    params = [('api_key', 'api_key_example'),
                    ('api_secret', 'api_secret_example'),
                    ('request_id', 'abcdef0123456789abcdef0123456789'),
                    ('request_ids', ['request_ids_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/verify/search/{format}'.format(format='json'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

