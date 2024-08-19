# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.farm import Farm
from openapi_server.models.farm_creation_properties import FarmCreationProperties
from openapi_server.models.farm_list import FarmList
from openapi_server.models.farms_list_metric_definitions200_response import FarmsListMetricDefinitions200Response
from openapi_server.models.farms_list_metrics200_response import FarmsListMetrics200Response


pytestmark = pytest.mark.asyncio

async def test_farms_create(client):
    """Test case for farms_create

    
    """
    farm_object = {"properties":{"settingAccessString":"settingAccessString"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example'),
        headers=headers,
        json=farm_object,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_farms_get(client):
    """Test case for farms_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_farms_list(client):
    """Test case for farms_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_farms_list_metric_definitions(client):
    """Test case for farms_list_metric_definitions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/metricdefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_farms_list_metrics(client):
    """Test case for farms_list_metrics

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_farms_start_garbage_collection(client):
    """Test case for farms_start_garbage_collection

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/ondemandgc'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_farms_update(client):
    """Test case for farms_update

    
    """
    farm_object = {"properties":{"settings":{"minimumRequestThresholdInTps":1.1730742,"minimumTotalIngressThresholdInGbps":5.025005,"gracePeriodForFullThrottlingInRefreshIntervals":2,"toleranceFactorForTotalEgress":3.3531933,"minimumTotalEgressThresholdInGbps":4.9652185,"minimumEgressThresholdInGbps":1.0246457,"minimumIntranetIngressThresholdInGbps":7.4577446,"feedbackRefreshIntervalInSeconds":3,"corsAllowedOriginsList":"corsAllowedOriginsList","defaultIntranetEgressThresholdInGbps":1.4658129,"defaultTotalEgressThresholdInGbps":7.0614014,"overallEgressThresholdInGbps":9.36931,"toleranceFactorForEgress":6.778325,"toleranceFactorForIngress":6.878052,"toleranceFactorForIntranetIngress":6.704019,"numberOfAccountsToSync":9,"toleranceFactorForIntranetEgress":5.9448957,"defaultRequestThresholdInTps":5.637377,"defaultIntranetIngressThresholdInGbps":5.962134,"defaultIngressThresholdInGbps":6.0274563,"overallTotalEgressThresholdInGbps":3.5571952,"hostStyleHttpsPort":1,"overallIntranetIngressThresholdInGbps":9.018348,"overallRequestThresholdInTps":6.4384236,"defaultEgressThresholdInGbps":0.8008282,"defaultTotalIngressThresholdInGbps":9.301444,"dataCenterUriHostSuffixes":"dataCenterUriHostSuffixes","toleranceFactorForTps":7.143538,"overallIngressThresholdInGbps":6.6835623,"defaultThrottleProbabilityDecayIntervalInSeconds":2,"overallTotalIngressThresholdInGbps":6.965118,"usageCollectionIntervalInSeconds":0,"minimumIngressThresholdInGbps":1.4894159,"bandwidthThrottleIsEnabled":True,"gracePeriodMaxThrottleProbability":4.145608,"minimumIntranetEgressThresholdInGbps":6.846853,"hostStyleHttpPort":7,"overallIntranetEgressThresholdInGbps":8.762042,"retentionPeriodForDeletedStorageAccountsInDays":1,"toleranceFactorForTotalIngress":3.0937452,"settingsPollingIntervalInSecond":2},"settingsStore":"settingsStore","farmId":"farmId","version":"version"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example'),
        headers=headers,
        json=farm_object,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

