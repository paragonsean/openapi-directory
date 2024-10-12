# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_health_policy import ApplicationHealthPolicy
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.paged_service_partition_info_list import PagedServicePartitionInfoList
from openapi_server.models.partition_health import PartitionHealth
from openapi_server.models.partition_load_information import PartitionLoadInformation
from openapi_server.models.service_name_info import ServiceNameInfo
from openapi_server.models.service_partition_info import ServicePartitionInfo


pytestmark = pytest.mark.asyncio

async def test_get_partition_health(client):
    """Test case for get_partition_health

    Gets the health of the specified Service Fabric partition.
    """
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('ReplicasHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetHealth'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_partition_health_using_policy(client):
    """Test case for get_partition_health_using_policy

    Gets the health of the specified Service Fabric partition, by using the specified health policy.
    """
    application_health_policy = openapi_server.ApplicationHealthPolicy()
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('ReplicasHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/GetHealth'.format(partition_id='partition_id_example'),
        headers=headers,
        json=application_health_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_info(client):
    """Test case for get_partition_info

    Gets the information about a Service Fabric partition.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_info_list(client):
    """Test case for get_partition_info_list

    Gets the list of partitions of a Service Fabric service.
    """
    params = [('api-version', 6.4),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_id}/$/GetPartitions'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_load_information(client):
    """Test case for get_partition_load_information

    Gets the load information of the specified Service Fabric partition.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetLoadInformation'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_name_info(client):
    """Test case for get_service_name_info

    Gets the name of the Service Fabric service for a partition.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetServiceName'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_primary_replica(client):
    """Test case for move_primary_replica

    Moves the primary replica of a partition of a stateful service.
    """
    params = [('api-version', 6.5),
                    ('NodeName', 'node_name_example'),
                    ('IgnoreConstraints', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/MovePrimaryReplica'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_secondary_replica(client):
    """Test case for move_secondary_replica

    Moves the secondary replica of a partition of a stateful service.
    """
    params = [('api-version', 6.5),
                    ('CurrentNodeName', 'current_node_name_example'),
                    ('NewNodeName', 'new_node_name_example'),
                    ('IgnoreConstraints', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/MoveSecondaryReplica'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_all_partitions(client):
    """Test case for recover_all_partitions

    Indicates to the Service Fabric cluster that it should attempt to recover any services (including system services) which are currently stuck in quorum loss.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/RecoverAllPartitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_partition(client):
    """Test case for recover_partition

    Indicates to the Service Fabric cluster that it should attempt to recover a specific partition that is currently stuck in quorum loss.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/Recover'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_service_partitions(client):
    """Test case for recover_service_partitions

    Indicates to the Service Fabric cluster that it should attempt to recover the specified service that is currently stuck in quorum loss.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/$/{service_id}/$/GetPartitions/$/Recover'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_system_partitions(client):
    """Test case for recover_system_partitions

    Indicates to the Service Fabric cluster that it should attempt to recover the system services that are currently stuck in quorum loss.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/RecoverSystemPartitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_partition_health(client):
    """Test case for report_partition_health

    Sends a health report on the Service Fabric partition.
    """
    health_information = openapi_server.HealthInformation()
    params = [('api-version', 6.0),
                    ('Immediate', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/ReportHealth'.format(partition_id='partition_id_example'),
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_partition_load(client):
    """Test case for reset_partition_load

    Resets the current load of a Service Fabric partition.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/ResetLoad'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

