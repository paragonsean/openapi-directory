# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_event import ApplicationEvent
from openapi_server.models.cluster_event import ClusterEvent
from openapi_server.models.container_instance_event import ContainerInstanceEvent
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.fabric_event import FabricEvent
from openapi_server.models.node_event import NodeEvent
from openapi_server.models.partition_event import PartitionEvent
from openapi_server.models.replica_event import ReplicaEvent
from openapi_server.models.service_event import ServiceEvent


pytestmark = pytest.mark.asyncio

async def test_get_application_event_list(client):
    """Test case for get_application_event_list

    Gets an Application-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Applications/{application_id}/$/Events'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_applications_event_list(client):
    """Test case for get_applications_event_list

    Gets all Applications-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Applications/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_event_list(client):
    """Test case for get_cluster_event_list

    Gets all Cluster-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Cluster/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_containers_event_list(client):
    """Test case for get_containers_event_list

    Gets all Containers-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Containers/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_correlated_event_list(client):
    """Test case for get_correlated_event_list

    Gets all correlated events for a given event.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/CorrelatedEvents/{event_instance_id}/$/Events'.format(event_instance_id='event_instance_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_event_list(client):
    """Test case for get_node_event_list

    Gets a Node-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Nodes/{node_name}/$/Events'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nodes_event_list(client):
    """Test case for get_nodes_event_list

    Gets all Nodes-related Events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Nodes/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_event_list(client):
    """Test case for get_partition_event_list

    Gets a Partition-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Partitions/{partition_id}/$/Events'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_replica_event_list(client):
    """Test case for get_partition_replica_event_list

    Gets a Partition Replica-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Partitions/{partition_id}/$/Replicas/{replica_id}/$/Events'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_replicas_event_list(client):
    """Test case for get_partition_replicas_event_list

    Gets all Replicas-related events for a Partition.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Partitions/{partition_id}/$/Replicas/Events'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partitions_event_list(client):
    """Test case for get_partitions_event_list

    Gets all Partitions-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Partitions/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_event_list(client):
    """Test case for get_service_event_list

    Gets a Service-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Services/{service_id}/$/Events'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services_event_list(client):
    """Test case for get_services_event_list

    Gets all Services-related events.
    """
    params = [('api-version', 6.2-preview),
                    ('timeout', 60),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('EventsTypesFilter', 'events_types_filter_example'),
                    ('ExcludeAnalysisEvents', True),
                    ('SkipCorrelationLookup', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EventsStore/Services/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

