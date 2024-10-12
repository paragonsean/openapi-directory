# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_result_object import EntityResultObject
from openapi_server.models.error_object import ErrorObject


pytestmark = pytest.mark.asyncio

async def test_blacklist_entity(client):
    """Test case for blacklist_entity

    Set Entity Blacklist State.
    """
    params = [('set', True),
                    ('reason', 'reason_example'),
                    ('blockedBy', 'blocked_by_example'),
                    ('attribute', 'attribute_example'),
                    ('originalId', 'original_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/flag/blacklist'.format(entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_entity_monitoring(client):
    """Test case for entity_monitoring

    Set Entity Ongoing AML Monitoring Status.
    """
    params = [('set', True)]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/flag/monitor'.format(entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flag_duplicate_entity(client):
    """Test case for flag_duplicate_entity

    Resolve Duplicate States.
    """
    params = [('set', True)]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/flag/duplicate/{other_id}'.format(entity_id='entity_id_example', other_id='other_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watchlist_entity(client):
    """Test case for watchlist_entity

    Set Entity Watchlist State.
    """
    params = [('set', True),
                    ('reason', 'reason_example'),
                    ('comment', 'comment_example')]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/flag/watchlist'.format(entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

