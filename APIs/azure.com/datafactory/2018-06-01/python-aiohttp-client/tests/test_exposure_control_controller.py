# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.exposure_control_request import ExposureControlRequest
from openapi_server.models.exposure_control_response import ExposureControlResponse


pytestmark = pytest.mark.asyncio

async def test_exposure_control_get_feature_value(client):
    """Test case for exposure_control_get_feature_value

    
    """
    exposure_control_request = {"featureName":"featureName","featureType":"featureType"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataFactory/locations/{location_id}/getFeatureValue'.format(subscription_id='subscription_id_example', location_id='location_id_example'),
        headers=headers,
        json=exposure_control_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exposure_control_get_feature_value_by_factory(client):
    """Test case for exposure_control_get_feature_value_by_factory

    
    """
    exposure_control_request = {"featureName":"featureName","featureType":"featureType"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/getFeatureValue'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=exposure_control_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

