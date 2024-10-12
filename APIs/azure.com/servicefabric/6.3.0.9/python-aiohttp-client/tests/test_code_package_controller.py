# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_api_request_body import ContainerApiRequestBody
from openapi_server.models.container_api_response import ContainerApiResponse
from openapi_server.models.container_logs import ContainerLogs
from openapi_server.models.deployed_code_package_info import DeployedCodePackageInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.restart_deployed_code_package_description import RestartDeployedCodePackageDescription


pytestmark = pytest.mark.asyncio

async def test_get_container_logs_deployed_on_node(client):
    """Test case for get_container_logs_deployed_on_node

    Gets the container logs for container deployed on a Service Fabric node.
    """
    params = [('api-version', 6.2),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('CodePackageName', 'code_package_name_example'),
                    ('Tail', 'tail_example'),
                    ('Previous', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetCodePackages/$/ContainerLogs'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_code_package_info_list(client):
    """Test case for get_deployed_code_package_info_list

    Gets the list of code packages deployed on a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('CodePackageName', 'code_package_name_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetCodePackages'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_invoke_container_api(client):
    """Test case for invoke_container_api

    Invoke container API on a container deployed on a Service Fabric node.
    """
    container_api_request_body = openapi_server.ContainerApiRequestBody()
    params = [('api-version', 6.2),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('CodePackageName', 'code_package_name_example'),
                    ('CodePackageInstanceId', 'code_package_instance_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetCodePackages/$/ContainerApi'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        json=container_api_request_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_restart_deployed_code_package(client):
    """Test case for restart_deployed_code_package

    Restarts a code package deployed on a Service Fabric node in a cluster.
    """
    restart_deployed_code_package_description = openapi_server.RestartDeployedCodePackageDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetCodePackages/$/Restart'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        json=restart_deployed_code_package_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

