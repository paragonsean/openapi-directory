# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_collection import SubscriptionCollection
from openapi_server.models.subscription_contract import SubscriptionContract
from openapi_server.models.subscription_create_parameters import SubscriptionCreateParameters
from openapi_server.models.subscription_list_default_response import SubscriptionListDefaultResponse
from openapi_server.models.subscription_update_parameters import SubscriptionUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_subscription_create_or_update(client):
    """Test case for subscription_create_or_update

    
    """
    parameters = {"productId":"productId","secondaryKey":"secondaryKey","name":"name","state":"suspended","userId":"userId","primaryKey":"primaryKey"}
    params = [('notify', False),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{sid}'.format(sid='sid_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_delete(client):
    """Test case for subscription_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{sid}'.format(sid='sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_get(client):
    """Test case for subscription_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{sid}'.format(sid='sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_list(client):
    """Test case for subscription_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_regenerate_primary_key(client):
    """Test case for subscription_regenerate_primary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{sid}/regeneratePrimaryKey'.format(sid='sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_regenerate_secondary_key(client):
    """Test case for subscription_regenerate_secondary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{sid}/regenerateSecondaryKey'.format(sid='sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_update(client):
    """Test case for subscription_update

    
    """
    parameters = {"productId":"productId","secondaryKey":"secondaryKey","stateComment":"stateComment","name":"name","state":"suspended","userId":"userId","expirationDate":"2000-01-23T04:56:07.000+00:00","primaryKey":"primaryKey"}
    params = [('notify', False),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{sid}'.format(sid='sid_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

