# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_health_policy import ApplicationHealthPolicy
from openapi_server.models.deployed_service_replica_detail_info import DeployedServiceReplicaDetailInfo
from openapi_server.models.deployed_service_replica_info import DeployedServiceReplicaInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.paged_replica_info_list import PagedReplicaInfoList
from openapi_server.models.replica_health import ReplicaHealth
from openapi_server.models.replica_info import ReplicaInfo


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_replica_detail_info(client):
    """Test case for get_deployed_service_replica_detail_info

    Gets the details of replica deployed on a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetPartitions/{partition_id}/$/GetReplicas/{replica_id}/$/GetDetail'.format(node_name='node_name_example', partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_replica_detail_info_by_partition_id(client):
    """Test case for get_deployed_service_replica_detail_info_by_partition_id

    Gets the details of replica deployed on a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetPartitions/{partition_id}/$/GetReplicas'.format(node_name='node_name_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_replica_info_list(client):
    """Test case for get_deployed_service_replica_info_list

    Gets the list of replicas deployed on a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('PartitionId', 'partition_id_example'),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetReplicas'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replica_health(client):
    """Test case for get_replica_health

    Gets the health of a Service Fabric stateful service replica or stateless service instance.
    """
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}/$/GetHealth'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_replica_health_using_policy(client):
    """Test case for get_replica_health_using_policy

    Gets the health of a Service Fabric stateful service replica or stateless service instance using the specified policy.
    """
    application_health_policy = openapi_server.ApplicationHealthPolicy()
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}/$/GetHealth'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        json=application_health_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replica_info(client):
    """Test case for get_replica_info

    Gets the information about a replica of a Service Fabric partition.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replica_info_list(client):
    """Test case for get_replica_info_list

    Gets the information about replicas of a Service Fabric service partition.
    """
    params = [('api-version', 6.0),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetReplicas'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_replica(client):
    """Test case for remove_replica

    Removes a service replica running on a node.
    """
    params = [('api-version', 6.0),
                    ('ForceRemove', True),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetPartitions/{partition_id}/$/GetReplicas/{replica_id}/$/Delete'.format(node_name='node_name_example', partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_replica_health(client):
    """Test case for report_replica_health

    Sends a health report on the Service Fabric replica.
    """
    health_information = openapi_server.HealthInformation()
    params = [('api-version', 6.0),
                    ('ReplicaHealthReportServiceKind', Stateful),
                    ('Immediate', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}/$/ReportHealth'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restart_replica(client):
    """Test case for restart_replica

    Restarts a service replica of a persisted service running on a node.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetPartitions/{partition_id}/$/GetReplicas/{replica_id}/$/Restart'.format(node_name='node_name_example', partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

