# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.compute_node import ComputeNode
from openapi_server.models.compute_node_get_remote_login_settings_result import ComputeNodeGetRemoteLoginSettingsResult
from openapi_server.models.compute_node_list_result import ComputeNodeListResult
from openapi_server.models.compute_node_user import ComputeNodeUser
from openapi_server.models.node_disable_scheduling_parameter import NodeDisableSchedulingParameter
from openapi_server.models.node_reboot_parameter import NodeRebootParameter
from openapi_server.models.node_reimage_parameter import NodeReimageParameter
from openapi_server.models.node_remove_parameter import NodeRemoveParameter
from openapi_server.models.node_update_user_parameter import NodeUpdateUserParameter
from openapi_server.models.upload_batch_service_logs_configuration import UploadBatchServiceLogsConfiguration
from openapi_server.models.upload_batch_service_logs_result import UploadBatchServiceLogsResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_add_user(client):
    """Test case for compute_node_add_user

    Adds a user account to the specified compute node.
    """
    user = openapi_server.ComputeNodeUser()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/users'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=user,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_delete_user(client):
    """Test case for compute_node_delete_user

    Deletes a user account from the specified compute node.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='DELETE',
        path='/pools/{pool_id}/nodes/{node_id}/users/{user_name}'.format(pool_id='pool_id_example', node_id='node_id_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_disable_scheduling(client):
    """Test case for compute_node_disable_scheduling

    Disables task scheduling on the specified compute node.
    """
    node_disable_scheduling_parameter = openapi_server.NodeDisableSchedulingParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/disablescheduling'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=node_disable_scheduling_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_enable_scheduling(client):
    """Test case for compute_node_enable_scheduling

    Enables task scheduling on the specified compute node.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/enablescheduling'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_get(client):
    """Test case for compute_node_get

    Gets information about the specified compute node.
    """
    params = [('$select', 'select_example'),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}/nodes/{node_id}'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_get_remote_desktop(client):
    """Test case for compute_node_get_remote_desktop

    Gets the Remote Desktop Protocol file for the specified compute node.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}/nodes/{node_id}/rdp'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_get_remote_login_settings(client):
    """Test case for compute_node_get_remote_login_settings

    Gets the settings required for remote login to a compute node.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}/nodes/{node_id}/remoteloginsettings'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_list(client):
    """Test case for compute_node_list

    Lists the compute nodes in the specified pool.
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('maxresults', 1000),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}/nodes'.format(pool_id='pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_reboot(client):
    """Test case for compute_node_reboot

    Restarts the specified compute node.
    """
    node_reboot_parameter = openapi_server.NodeRebootParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/reboot'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=node_reboot_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_reimage(client):
    """Test case for compute_node_reimage

    Reinstalls the operating system on the specified compute node.
    """
    node_reimage_parameter = openapi_server.NodeReimageParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/reimage'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=node_reimage_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_update_user(client):
    """Test case for compute_node_update_user

    Updates the password and expiration time of a user account on the specified compute node.
    """
    node_update_user_parameter = openapi_server.NodeUpdateUserParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='PUT',
        path='/pools/{pool_id}/nodes/{node_id}/users/{user_name}'.format(pool_id='pool_id_example', node_id='node_id_example', user_name='user_name_example'),
        headers=headers,
        json=node_update_user_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_upload_batch_service_logs(client):
    """Test case for compute_node_upload_batch_service_logs

    Upload Azure Batch service log files from the specified compute node to Azure Blob Storage.
    """
    upload_batch_service_logs_configuration = openapi_server.UploadBatchServiceLogsConfiguration()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/uploadbatchservicelogs'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=upload_batch_service_logs_configuration,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_remove_nodes(client):
    """Test case for pool_remove_nodes

    Removes compute nodes from the specified pool.
    """
    node_remove_parameter = openapi_server.NodeRemoveParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/removenodes'.format(pool_id='pool_id_example'),
        headers=headers,
        json=node_remove_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

