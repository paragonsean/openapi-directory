# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.lab_cost import LabCost


pytestmark = pytest.mark.asyncio

async def test_costs_create_or_update(client):
    """Test case for costs_create_or_update

    
    """
    lab_cost = {"properties":{"createdDate":"2000-01-23T04:56:07.000+00:00","startDateTime":"2000-01-23T04:56:07.000+00:00","targetCost":{"cycleType":"CalendarMonth","cycleEndDateTime":"2000-01-23T04:56:07.000+00:00","costThresholds":[{"percentageThreshold":{"thresholdValue":5.962133916683182},"sendNotificationWhenExceeded":"Enabled","displayOnChart":"Enabled","thresholdId":"thresholdId","notificationSent":"notificationSent"},{"percentageThreshold":{"thresholdValue":5.962133916683182},"sendNotificationWhenExceeded":"Enabled","displayOnChart":"Enabled","thresholdId":"thresholdId","notificationSent":"notificationSent"}],"cycleStartDateTime":"2000-01-23T04:56:07.000+00:00","status":"Enabled","target":5},"labCostDetails":[{"date":"2000-01-23T04:56:07.000+00:00","cost":0.8008281904610115,"costType":"Unavailable"},{"date":"2000-01-23T04:56:07.000+00:00","cost":0.8008281904610115,"costType":"Unavailable"}],"provisioningState":"provisioningState","endDateTime":"2000-01-23T04:56:07.000+00:00","labCostSummary":{"estimatedLabCost":6.027456183070403},"currencyCode":"currencyCode","resourceCosts":[{"resourceId":"resourceId","resourceStatus":"resourceStatus","externalResourceId":"externalResourceId","resourceCost":1.4658129805029452,"resourceOwner":"resourceOwner","resourceUId":"resourceUId","resourcePricingTier":"resourcePricingTier","resourcename":"resourcename","resourceType":"resourceType"},{"resourceId":"resourceId","resourceStatus":"resourceStatus","externalResourceId":"externalResourceId","resourceCost":1.4658129805029452,"resourceOwner":"resourceOwner","resourceUId":"resourceUId","resourcePricingTier":"resourcePricingTier","resourcename":"resourcename","resourceType":"resourceType"}],"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/costs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=lab_cost,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_costs_get(client):
    """Test case for costs_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/costs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

