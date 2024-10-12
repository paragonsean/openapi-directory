# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deployed_service_type_info import DeployedServiceTypeInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.service_type_info import ServiceTypeInfo
from openapi_server.models.service_type_manifest import ServiceTypeManifest


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_type_info_by_name(client):
    """Test case for get_deployed_service_type_info_by_name

    Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetServiceTypes/{service_type_name}'.format(node_name='node_name_example', application_id='application_id_example', service_type_name='service_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_type_info_list(client):
    """Test case for get_deployed_service_type_info_list

    Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetServiceTypes'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_manifest(client):
    """Test case for get_service_manifest

    Gets the manifest describing a service type.
    """
    params = [('api-version', 6.0),
                    ('ApplicationTypeVersion', 'application_type_version_example'),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}/$/GetServiceManifest'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_type_info_by_name(client):
    """Test case for get_service_type_info_by_name

    Gets the information about a specific service type that is supported by a provisioned application type in a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('ApplicationTypeVersion', 'application_type_version_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}/$/GetServiceTypes/{service_type_name}'.format(application_type_name='application_type_name_example', service_type_name='service_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_type_info_list(client):
    """Test case for get_service_type_info_list

    Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('ApplicationTypeVersion', 'application_type_version_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}/$/GetServiceTypes'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

