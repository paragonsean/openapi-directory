# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autofollow_strategies_post200_response import AutofollowStrategiesPost200Response
from openapi_server.models.autofollow_strategies_post_request import AutofollowStrategiesPostRequest
from openapi_server.models.autofollow_strategies_strategyid_content_put200_response import AutofollowStrategiesStrategyidContentPut200Response
from openapi_server.models.autofollow_strategies_strategyid_content_put_request import AutofollowStrategiesStrategyidContentPutRequest
from openapi_server.models.autofollow_strategies_strategyid_put200_response import AutofollowStrategiesStrategyidPut200Response
from openapi_server.models.autofollow_strategies_strategyid_put_request import AutofollowStrategiesStrategyidPutRequest
from openapi_server.models.autofollow_strategies_strategyid_signals_post200_response import AutofollowStrategiesStrategyidSignalsPost200Response
from openapi_server.models.autofollow_strategies_strategyid_signals_post_request import AutofollowStrategiesStrategyidSignalsPostRequest
from openapi_server.models.error import Error
from openapi_server.models.signal import Signal
from openapi_server.models.strategy import Strategy
from openapi_server.models.strategy_position import StrategyPosition


pytestmark = pytest.mark.asyncio

async def test_autofollow_strategies_get(client):
    """Test case for autofollow_strategies_get

    Get autofollow strategies list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/autofollow/strategies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_autofollow_strategies_post(client):
    """Test case for autofollow_strategies_post

    Create new autofollow strategy
    """
    body = openapi_server.AutofollowStrategiesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/autofollow/strategies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_autofollow_strategies_strategyid_content_put(client):
    """Test case for autofollow_strategies_strategyid_content_put

    Update rules for strategy that was created with strategy builder
    """
    body = openapi_server.AutofollowStrategiesStrategyidContentPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/autofollow/strategies/{strategyid}/content'.format(strategyid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autofollow_strategies_strategyid_get(client):
    """Test case for autofollow_strategies_strategyid_get

    Get autofollow strategy by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/autofollow/strategies/{strategyid}'.format(strategyid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autofollow_strategies_strategyid_positions_get(client):
    """Test case for autofollow_strategies_strategyid_positions_get

    Get positions for strategy
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/autofollow/strategies/{strategyid}/positions'.format(strategyid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_autofollow_strategies_strategyid_put(client):
    """Test case for autofollow_strategies_strategyid_put

    Update autofollow strategy
    """
    body = openapi_server.AutofollowStrategiesStrategyidPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/autofollow/strategies/{strategyid}'.format(strategyid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autofollow_strategies_strategyid_signals_get(client):
    """Test case for autofollow_strategies_strategyid_signals_get

    Get trading signals for strategy
    """
    params = [('count', 56)]
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/autofollow/strategies/{strategyid}/signals'.format(strategyid=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_autofollow_strategies_strategyid_signals_post(client):
    """Test case for autofollow_strategies_strategyid_signals_post

    Send a new signal for autofollow strategy
    """
    body = openapi_server.AutofollowStrategiesStrategyidSignalsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/autofollow/strategies/{strategyid}/signals'.format(strategyid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

