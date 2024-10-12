# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_authenticators200_response import GetAuthenticators200Response
from openapi_server.models.get_service_authenticator_status200_response import GetServiceAuthenticatorStatus200Response
from openapi_server.models.info200_response import Info200Response
from openapi_server.models.who_am_i200_response import WhoAmI200Response


pytestmark = pytest.mark.asyncio

async def test_get_authenticators(client):
    """Test case for get_authenticators

    Details about which authenticators are on the Conjur Server
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': 'test-id',
        'Authorization': 'BasicZm9vOmJhcg==',
        
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/authenticators',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gcp_authenticator_status(client):
    """Test case for get_gcp_authenticator_status

    Details whether an authentication service has been configured properly
    """
    headers = { 
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/authn-gcp/{account}/status'.format(account='dev'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_authenticator_status(client):
    """Test case for get_service_authenticator_status

    Details whether an authentication service has been configured properly
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{authenticator}/{service_id}/{account}/status'.format(authenticator='authn-oidc', service_id='prod%2fgke', account='dev'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health(client):
    """Test case for health

    Health info about conjur
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_info(client):
    """Test case for info

    Basic information about the Conjur Enterprise server
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remote_health(client):
    """Test case for remote_health

    Health info about a given Conjur Enterprise server
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/remote_health/{remote}'.format(remote='conjur.myorg.com'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_who_am_i(client):
    """Test case for who_am_i

    Provides information about the client making an API request.
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/whoami',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

