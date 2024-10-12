# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.prediction_list_result import PredictionListResult
from openapi_server.models.prediction_model_status import PredictionModelStatus
from openapi_server.models.prediction_resource_format import PredictionResourceFormat
from openapi_server.models.prediction_training_results import PredictionTrainingResults


pytestmark = pytest.mark.asyncio

async def test_predictions_create_or_update(client):
    """Test case for predictions_create_or_update

    
    """
    parameters = {"properties":{"involvedRelationships":["involvedRelationships","involvedRelationships"],"displayName":{"key":"displayName"},"positiveOutcomeExpression":"positiveOutcomeExpression","description":{"key":"description"},"scopeExpression":"scopeExpression","grades":[{"gradeName":"gradeName","minScoreThreshold":6,"maxScoreThreshold":0},{"gradeName":"gradeName","minScoreThreshold":6,"maxScoreThreshold":0}],"provisioningState":"Provisioning","autoAnalyze":True,"predictionName":"predictionName","scoreLabel":"scoreLabel","involvedInteractionTypes":["involvedInteractionTypes","involvedInteractionTypes"],"involvedKpiTypes":["involvedKpiTypes","involvedKpiTypes"],"mappings":{"reason":"reason","score":"score","grade":"grade"},"primaryProfileType":"primaryProfileType","tenantId":"tenantId","negativeOutcomeExpression":"negativeOutcomeExpression","systemGeneratedEntities":{"generatedInteractionTypes":["generatedInteractionTypes","generatedInteractionTypes"],"generatedKpis":{"key":"generatedKpis"},"generatedLinks":["generatedLinks","generatedLinks"]}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/predictions/{prediction_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', prediction_name='prediction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_delete(client):
    """Test case for predictions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/predictions/{prediction_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', prediction_name='prediction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_get(client):
    """Test case for predictions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/predictions/{prediction_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', prediction_name='prediction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_get_model_status(client):
    """Test case for predictions_get_model_status

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/predictions/{prediction_name}/getModelStatus'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', prediction_name='prediction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_get_training_results(client):
    """Test case for predictions_get_training_results

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/predictions/{prediction_name}/getTrainingResults'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', prediction_name='prediction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_list_by_hub(client):
    """Test case for predictions_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/predictions'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_predictions_model_status(client):
    """Test case for predictions_model_status

    
    """
    parameters = {"signalsUsed":0,"validationSetCount":5,"predictionGuidId":"predictionGuidId","modelVersion":"modelVersion","tenantId":"tenantId","testSetCount":6,"trainingAccuracy":1,"trainingSetCount":5,"message":"message","predictionName":"predictionName","status":"New"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/predictions/{prediction_name}/modelStatus'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', prediction_name='prediction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

