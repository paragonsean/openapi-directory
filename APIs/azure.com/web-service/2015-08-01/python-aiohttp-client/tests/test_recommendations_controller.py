# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recommendation import Recommendation
from openapi_server.models.recommendation_rule import RecommendationRule


pytestmark = pytest.mark.asyncio

async def test_recommendations_get_recommendation_by_subscription(client):
    """Test case for recommendations_get_recommendation_by_subscription

    Gets a list of recommendations associated with the specified subscription.
    """
    params = [('featured', True),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/recommendations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_get_recommendation_history_for_site(client):
    """Test case for recommendations_get_recommendation_history_for_site

    Gets the list of past recommendations optionally specified by the time range.
    """
    params = [('startTime', 'start_time_example'),
                    ('endTime', 'end_time_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/recommendationHistory'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_get_recommended_rules_for_site(client):
    """Test case for recommendations_get_recommended_rules_for_site

    Gets a list of recommendations associated with the specified web site.
    """
    params = [('featured', True),
                    ('siteSku', 'site_sku_example'),
                    ('numSlots', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/recommendations'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_get_rule_details_by_site_name(client):
    """Test case for recommendations_get_rule_details_by_site_name

    Gets the detailed properties of the recommendation object for the specified web site.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/recommendations/{name}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

