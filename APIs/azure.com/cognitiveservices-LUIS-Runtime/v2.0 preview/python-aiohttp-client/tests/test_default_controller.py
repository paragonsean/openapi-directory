# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.luis_result import LuisResult


pytestmark = pytest.mark.asyncio

async def test_prediction_resolve(client):
    """Test case for prediction_resolve

    
    """
    q = 'q_example'
    params = [('timezoneOffset', 3.4),
                    ('verbose', True),
                    ('staging', True),
                    ('spellCheck', True),
                    ('bing-spell-check-subscription-key', 'bing_spell_check_subscription_key_example'),
                    ('log', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/luis/v2.0/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        json=q,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prediction_resolve2(client):
    """Test case for prediction_resolve2

    
    """
    params = [('q', 'q_example'),
                    ('timezoneOffset', 3.4),
                    ('verbose', True),
                    ('staging', True),
                    ('spellCheck', True),
                    ('bing-spell-check-subscription-key', 'bing_spell_check_subscription_key_example'),
                    ('log', True)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/luis/v2.0/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

