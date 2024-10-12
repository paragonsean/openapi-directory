# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_traffic_manager_relative_dns_name_availability_parameters import CheckTrafficManagerRelativeDnsNameAvailabilityParameters
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.delete_operation_result import DeleteOperationResult
from openapi_server.models.profile import Profile
from openapi_server.models.profile_list_result import ProfileListResult
from openapi_server.models.traffic_manager_name_availability import TrafficManagerNameAvailability


pytestmark = pytest.mark.asyncio

async def test_profiles_check_traffic_manager_relative_dns_name_availability(client):
    """Test case for profiles_check_traffic_manager_relative_dns_name_availability

    
    """
    parameters = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Network/checkTrafficManagerNameAvailability',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_create_or_update(client):
    """Test case for profiles_create_or_update

    
    """
    parameters = {"properties":{"endpoints":[{"properties":{"targetResourceId":"targetResourceId","endpointLocation":"endpointLocation","endpointStatus":"Enabled","minChildEndpoints":6,"weight":5,"priority":1,"geoMapping":["geoMapping","geoMapping"],"endpointMonitorStatus":"CheckingEndpoint","target":"target"}},{"properties":{"targetResourceId":"targetResourceId","endpointLocation":"endpointLocation","endpointStatus":"Enabled","minChildEndpoints":6,"weight":5,"priority":1,"geoMapping":["geoMapping","geoMapping"],"endpointMonitorStatus":"CheckingEndpoint","target":"target"}}],"trafficViewEnrollmentStatus":"Enabled","dnsConfig":{"relativeName":"relativeName","fqdn":"fqdn","ttl":0},"monitorConfig":{"profileMonitorStatus":"CheckingEndpoints","path":"path","protocol":"HTTP","port":2,"toleratedNumberOfFailures":9,"intervalInSeconds":5,"timeoutInSeconds":7},"profileStatus":"Enabled","trafficRoutingMethod":"Performance"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_delete(client):
    """Test case for profiles_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_get(client):
    """Test case for profiles_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_list_by_resource_group(client):
    """Test case for profiles_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_list_by_subscription(client):
    """Test case for profiles_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/trafficmanagerprofiles'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_update(client):
    """Test case for profiles_update

    
    """
    parameters = {"properties":{"endpoints":[{"properties":{"targetResourceId":"targetResourceId","endpointLocation":"endpointLocation","endpointStatus":"Enabled","minChildEndpoints":6,"weight":5,"priority":1,"geoMapping":["geoMapping","geoMapping"],"endpointMonitorStatus":"CheckingEndpoint","target":"target"}},{"properties":{"targetResourceId":"targetResourceId","endpointLocation":"endpointLocation","endpointStatus":"Enabled","minChildEndpoints":6,"weight":5,"priority":1,"geoMapping":["geoMapping","geoMapping"],"endpointMonitorStatus":"CheckingEndpoint","target":"target"}}],"trafficViewEnrollmentStatus":"Enabled","dnsConfig":{"relativeName":"relativeName","fqdn":"fqdn","ttl":0},"monitorConfig":{"profileMonitorStatus":"CheckingEndpoints","path":"path","protocol":"HTTP","port":2,"toleratedNumberOfFailures":9,"intervalInSeconds":5,"timeoutInSeconds":7},"profileStatus":"Enabled","trafficRoutingMethod":"Performance"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

