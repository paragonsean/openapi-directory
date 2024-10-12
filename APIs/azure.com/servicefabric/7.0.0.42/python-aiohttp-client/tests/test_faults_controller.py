# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.node_transition_progress import NodeTransitionProgress
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.partition_data_loss_progress import PartitionDataLossProgress
from openapi_server.models.partition_quorum_loss_progress import PartitionQuorumLossProgress
from openapi_server.models.partition_restart_progress import PartitionRestartProgress


pytestmark = pytest.mark.asyncio

async def test_cancel_operation(client):
    """Test case for cancel_operation

    Cancels a user-induced fault operation.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('Force', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Faults/$/Cancel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_loss_progress(client):
    """Test case for get_data_loss_progress

    Gets the progress of a partition data loss operation started using the StartDataLoss API.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Faults/Services/{service_id}/$/GetPartitions/{partition_id}/$/GetDataLossProgress'.format(service_id='service_id_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fault_operation_list(client):
    """Test case for get_fault_operation_list

    Gets a list of user-induced fault operations filtered by provided input.
    """
    params = [('api-version', 6.0),
                    ('TypeFilter', 65535),
                    ('StateFilter', 65535),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Faults/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_transition_progress(client):
    """Test case for get_node_transition_progress

    Gets the progress of an operation started using StartNodeTransition.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Faults/Nodes/{node_name}/$/GetTransitionProgress'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_restart_progress(client):
    """Test case for get_partition_restart_progress

    Gets the progress of a PartitionRestart operation started using StartPartitionRestart.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Faults/Services/{service_id}/$/GetPartitions/{partition_id}/$/GetRestartProgress'.format(service_id='service_id_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quorum_loss_progress(client):
    """Test case for get_quorum_loss_progress

    Gets the progress of a quorum loss operation on a partition started using the StartQuorumLoss API.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Faults/Services/{service_id}/$/GetPartitions/{partition_id}/$/GetQuorumLossProgress'.format(service_id='service_id_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_data_loss(client):
    """Test case for start_data_loss

    This API will induce data loss for the specified partition. It will trigger a call to the OnDataLossAsync API of the partition.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('DataLossMode', 'data_loss_mode_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Faults/Services/{service_id}/$/GetPartitions/{partition_id}/$/StartDataLoss'.format(service_id='service_id_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_node_transition(client):
    """Test case for start_node_transition

    Starts or stops a cluster node.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('NodeTransitionType', 'node_transition_type_example'),
                    ('NodeInstanceId', 'node_instance_id_example'),
                    ('StopDurationInSeconds', 56),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Faults/Nodes/{node_name}/$/StartTransition'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_partition_restart(client):
    """Test case for start_partition_restart

    This API will restart some or all replicas or instances of the specified partition.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('RestartPartitionMode', 'restart_partition_mode_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Faults/Services/{service_id}/$/GetPartitions/{partition_id}/$/StartRestart'.format(service_id='service_id_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_quorum_loss(client):
    """Test case for start_quorum_loss

    Induces quorum loss for a given stateful service partition.
    """
    params = [('api-version', 6.0),
                    ('OperationId', 'operation_id_example'),
                    ('QuorumLossMode', 'quorum_loss_mode_example'),
                    ('QuorumLossDuration', 56),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Faults/Services/{service_id}/$/GetPartitions/{partition_id}/$/StartQuorumLoss'.format(service_id='service_id_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

