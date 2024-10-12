# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sso_strategy_entity import SsoStrategyEntity


pytestmark = pytest.mark.asyncio

async def test_get_sso_strategies(client):
    """Test case for get_sso_strategies

    List Sso Strategies
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/sso_strategies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sso_strategies_id(client):
    """Test case for get_sso_strategies_id

    Show Sso Strategy
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/sso_strategies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_sso_strategies_id_sync(client):
    """Test case for post_sso_strategies_id_sync

    Synchronize provisioning data with the SSO remote server.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/sso_strategies/{id}/sync'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

