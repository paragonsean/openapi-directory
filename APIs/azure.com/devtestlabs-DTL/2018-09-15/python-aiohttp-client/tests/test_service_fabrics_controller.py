# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.applicable_schedule import ApplicableSchedule
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.service_fabric import ServiceFabric
from openapi_server.models.service_fabric_fragment import ServiceFabricFragment
from openapi_server.models.service_fabric_list import ServiceFabricList


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_create_or_update(client):
    """Test case for service_fabrics_create_or_update

    
    """
    service_fabric = {"properties":{"applicableSchedule":{"properties":{"labVmsStartup":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"notificationLocale":"notificationLocale","emailRecipient":"emailRecipient","webhookUrl":"webhookUrl","status":"Enabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}},"labVmsShutdown":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"notificationLocale":"notificationLocale","emailRecipient":"emailRecipient","webhookUrl":"webhookUrl","status":"Enabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}}}},"environmentId":"environmentId","externalServiceFabricId":"externalServiceFabricId","provisioningState":"provisioningState","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=service_fabric,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_delete(client):
    """Test case for service_fabrics_delete

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_get(client):
    """Test case for service_fabrics_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_list(client):
    """Test case for service_fabrics_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_list_applicable_schedules(client):
    """Test case for service_fabrics_list_applicable_schedules

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics/{name}/listApplicableSchedules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_start(client):
    """Test case for service_fabrics_start

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics/{name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_stop(client):
    """Test case for service_fabrics_stop

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics/{name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_fabrics_update(client):
    """Test case for service_fabrics_update

    
    """
    service_fabric = {"properties":{"environmentId":"environmentId","externalServiceFabricId":"externalServiceFabricId"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/servicefabrics/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=service_fabric,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

