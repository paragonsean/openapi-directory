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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_add_user(client):
    """Test case for compute_node_add_user

    
    """
    body = openapi_server.ComputeNodeUser()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/users'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_delete_user(client):
    """Test case for compute_node_delete_user

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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

    
    """
    body = openapi_server.NodeDisableSchedulingParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/disablescheduling'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_node_enable_scheduling(client):
    """Test case for compute_node_enable_scheduling

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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

    
    """
    params = [('$select', 'select_example'),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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

    
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('maxresults', 56),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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

    
    """
    body = openapi_server.NodeRebootParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/reboot'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_reimage(client):
    """Test case for compute_node_reimage

    
    """
    body = openapi_server.NodeReimageParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/nodes/{node_id}/reimage'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_compute_node_update_user(client):
    """Test case for compute_node_update_user

    
    """
    body = openapi_server.NodeUpdateUserParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='PUT',
        path='/pools/{pool_id}/nodes/{node_id}/users/{user_name}'.format(pool_id='pool_id_example', node_id='node_id_example', user_name='user_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_remove_nodes(client):
    """Test case for pool_remove_nodes

    
    """
    body = openapi_server.NodeRemoveParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

