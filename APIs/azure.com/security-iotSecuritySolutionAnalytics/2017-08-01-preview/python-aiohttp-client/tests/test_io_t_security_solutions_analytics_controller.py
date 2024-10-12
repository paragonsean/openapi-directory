# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.io_t_security_aggregated_alert import IoTSecurityAggregatedAlert
from openapi_server.models.io_t_security_aggregated_alert_list import IoTSecurityAggregatedAlertList
from openapi_server.models.io_t_security_aggregated_recommendation import IoTSecurityAggregatedRecommendation
from openapi_server.models.io_t_security_aggregated_recommendation_list import IoTSecurityAggregatedRecommendationList
from openapi_server.models.io_t_security_solution_analytics_model import IoTSecuritySolutionAnalyticsModel
from openapi_server.models.io_t_security_solution_analytics_model_list import IoTSecuritySolutionAnalyticsModelList
from openapi_server.models.io_t_security_solutions_analytics_get_all_default_response import IoTSecuritySolutionsAnalyticsGetAllDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_io_t_security_solutions_analytics_aggregated_alert_dismiss(client):
    """Test case for io_t_security_solutions_analytics_aggregated_alert_dismiss

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels/default/aggregatedAlerts/{aggregated_alert_name}/dismiss'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example', aggregated_alert_name='aggregated_alert_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_security_solutions_analytics_aggregated_alert_get(client):
    """Test case for io_t_security_solutions_analytics_aggregated_alert_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels/default/aggregatedAlerts/{aggregated_alert_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example', aggregated_alert_name='aggregated_alert_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_security_solutions_analytics_aggregated_alerts_list(client):
    """Test case for io_t_security_solutions_analytics_aggregated_alerts_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels/default/aggregatedAlerts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_security_solutions_analytics_get_all(client):
    """Test case for io_t_security_solutions_analytics_get_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_security_solutions_analytics_get_default(client):
    """Test case for io_t_security_solutions_analytics_get_default

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_security_solutions_analytics_recommendation_get(client):
    """Test case for io_t_security_solutions_analytics_recommendation_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels/default/aggregatedRecommendations/{aggregated_recommendation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example', aggregated_recommendation_name='aggregated_recommendation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_security_solutions_analytics_recommendations_list(client):
    """Test case for io_t_security_solutions_analytics_recommendations_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels/default/aggregatedRecommendations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

