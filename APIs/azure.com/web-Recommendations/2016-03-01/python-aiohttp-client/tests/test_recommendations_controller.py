# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recommendation_collection import RecommendationCollection
from openapi_server.models.recommendation_rule import RecommendationRule


pytestmark = pytest.mark.asyncio

async def test_recommendations_disable_all_for_web_app(client):
    """Test case for recommendations_disable_all_for_web_app

    Disable all recommendations for an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/recommendations/disable'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_disable_recommendation_for_site(client):
    """Test case for recommendations_disable_recommendation_for_site

    Disables the specific rule for a web site permanently.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/recommendations/{name}/disable'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_disable_recommendation_for_subscription(client):
    """Test case for recommendations_disable_recommendation_for_subscription

    Disables the specified rule so it will not apply to a subscription in the future.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/recommendations/{name}/disable'.format(name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_get_rule_details_by_web_app(client):
    """Test case for recommendations_get_rule_details_by_web_app

    Get a recommendation rule for an app.
    """
    params = [('updateSeen', True),
                    ('recommendationId', 'recommendation_id_example'),
                    ('api-version', 'api_version_example')]
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


pytestmark = pytest.mark.asyncio

async def test_recommendations_list(client):
    """Test case for recommendations_list

    List all recommendations for a subscription.
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

async def test_recommendations_list_history_for_web_app(client):
    """Test case for recommendations_list_history_for_web_app

    Get past recommendations for an app, optionally specified by the time range.
    """
    params = [('$filter', 'filter_example'),
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

async def test_recommendations_list_recommended_rules_for_web_app(client):
    """Test case for recommendations_list_recommended_rules_for_web_app

    Get all recommendations for an app.
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/recommendations'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_reset_all_filters(client):
    """Test case for recommendations_reset_all_filters

    Reset all recommendation opt-out settings for a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/recommendations/reset'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendations_reset_all_filters_for_web_app(client):
    """Test case for recommendations_reset_all_filters_for_web_app

    Reset all recommendation opt-out settings for an app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/recommendations/reset'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

