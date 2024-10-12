# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_resource import ApplicationResource
from openapi_server.models.application_resource_list import ApplicationResourceList
from openapi_server.models.application_resource_update import ApplicationResourceUpdate
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_applications_create(client):
    """Test case for applications_create

    Creates or updates a Service Fabric application resource.
    """
    parameters = {"properties":{"typeName":"typeName","provisioningState":"provisioningState"}}
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_delete(client):
    """Test case for applications_delete

    Deletes a Service Fabric application resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_get(client):
    """Test case for applications_get

    Gets a Service Fabric application resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list(client):
    """Test case for applications_list

    Gets the list of application resources created in the specified Service Fabric cluster resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_update(client):
    """Test case for applications_update

    Updates a Service Fabric application resource.
    """
    parameters = {"properties":{"upgradePolicy":{"upgradeReplicaSetCheckTimeout":"upgradeReplicaSetCheckTimeout","forceRestart":False,"applicationHealthPolicy":{"DefaultServiceTypeHealthPolicy":{"maxPercentUnhealthyServices":93,"maxPercentUnhealthyReplicasPerPartition":70,"maxPercentUnhealthyPartitionsPerService":23},"ConsiderWarningAsError":False,"MaxPercentUnhealthyDeployedApplications":3,"ServiceTypeHealthPolicyMap":{"key":{"maxPercentUnhealthyServices":93,"maxPercentUnhealthyReplicasPerPartition":70,"maxPercentUnhealthyPartitionsPerService":23}}},"rollingUpgradeMonitoringPolicy":{"healthCheckRetryTimeout":"PT0H10M0S","healthCheckWaitDuration":"0","failureAction":"Rollback","healthCheckStableDuration":"PT0H2M0S","upgradeDomainTimeout":"P10675199DT02H48M05.4775807S","upgradeTimeout":"P10675199DT02H48M05.4775807S"}},"typeVersion":"typeVersion","maximumNodes":0,"minimumNodes":0,"metrics":[{"MaximumCapacity":6,"ReservationCapacity":1,"TotalApplicationCapacity":5,"Name":"Name"},{"MaximumCapacity":6,"ReservationCapacity":1,"TotalApplicationCapacity":5,"Name":"Name"}],"parameters":{"key":"parameters"},"removeApplicationCapacity":True}}
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

