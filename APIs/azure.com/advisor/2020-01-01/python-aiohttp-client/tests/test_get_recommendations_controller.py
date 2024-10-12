# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_recommendation_base import ResourceRecommendationBase
from openapi_server.models.resource_recommendation_base_list_result import ResourceRecommendationBaseListResult


pytestmark = pytest.mark.asyncio

async def test_recommendations_get(client):
    """Test case for recommendations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/Microsoft.Advisor/recommendations/{recommendation_id}'.format(resource_uri='resource_uri_example', recommendation_id='recommendation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_list(client):
    """Test case for recommendations_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Advisor/recommendations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

