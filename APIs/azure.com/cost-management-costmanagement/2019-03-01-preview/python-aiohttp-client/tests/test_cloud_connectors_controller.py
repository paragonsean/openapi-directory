# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connector_definition import ConnectorDefinition
from openapi_server.models.connector_definition_list_result import ConnectorDefinitionListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_cloud_connector_create_or_update(client):
    """Test case for cloud_connector_create_or_update

    
    """
    connector = {"kind":"kind","name":"name","id":"id","type":"type","properties":{"reportId":"reportId","displayName":"displayName","billingModel":"trial","collectionInfo":{"lastUpdated":"2000-01-23T04:56:07.000+00:00","sourceLastUpdated":"2000-01-23T04:56:07.000+00:00","error":{"errorMessage":"errorMessage","errorCode":"errorCode","errorStartTime":"2000-01-23T04:56:07.000+00:00","errorInnerMessage":"errorInnerMessage"},"lastChecked":"2000-01-23T04:56:07.000+00:00"},"externalBillingAccountId":"externalBillingAccountId","credentialsKey":"credentialsKey","createdOn":"2000-01-23T04:56:07.000+00:00","defaultManagementGroupId":"defaultManagementGroupId","daysTrialRemaining":0,"providerBillingAccountDisplayName":"providerBillingAccountDisplayName","providerBillingAccountId":"providerBillingAccountId","modifiedOn":"2000-01-23T04:56:07.000+00:00","credentialsSecret":"credentialsSecret","subscriptionId":"subscriptionId","status":"active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.CostManagement/cloudConnectors/{connector_name}'.format(connector_name='connector_name_example'),
        headers=headers,
        json=connector,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connector_delete(client):
    """Test case for cloud_connector_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.CostManagement/cloudConnectors/{connector_name}'.format(connector_name='connector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connector_get(client):
    """Test case for cloud_connector_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/cloudConnectors/{connector_name}'.format(connector_name='connector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connector_list(client):
    """Test case for cloud_connector_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/cloudConnectors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connector_update(client):
    """Test case for cloud_connector_update

    
    """
    connector = {"kind":"kind","name":"name","id":"id","type":"type","properties":{"reportId":"reportId","displayName":"displayName","billingModel":"trial","collectionInfo":{"lastUpdated":"2000-01-23T04:56:07.000+00:00","sourceLastUpdated":"2000-01-23T04:56:07.000+00:00","error":{"errorMessage":"errorMessage","errorCode":"errorCode","errorStartTime":"2000-01-23T04:56:07.000+00:00","errorInnerMessage":"errorInnerMessage"},"lastChecked":"2000-01-23T04:56:07.000+00:00"},"externalBillingAccountId":"externalBillingAccountId","credentialsKey":"credentialsKey","createdOn":"2000-01-23T04:56:07.000+00:00","defaultManagementGroupId":"defaultManagementGroupId","daysTrialRemaining":0,"providerBillingAccountDisplayName":"providerBillingAccountDisplayName","providerBillingAccountId":"providerBillingAccountId","modifiedOn":"2000-01-23T04:56:07.000+00:00","credentialsSecret":"credentialsSecret","subscriptionId":"subscriptionId","status":"active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.CostManagement/cloudConnectors/{connector_name}'.format(connector_name='connector_name_example'),
        headers=headers,
        json=connector,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

