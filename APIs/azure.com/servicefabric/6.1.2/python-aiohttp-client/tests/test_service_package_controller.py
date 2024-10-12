# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_health_policy import ApplicationHealthPolicy
from openapi_server.models.deploy_service_package_to_node_description import DeployServicePackageToNodeDescription
from openapi_server.models.deployed_service_package_health import DeployedServicePackageHealth
from openapi_server.models.deployed_service_package_info import DeployedServicePackageInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_deployed_service_package_to_node(client):
    """Test case for deployed_service_package_to_node

    Downloads all of the code packagesassociated with specified service manifest on the specified node.
    """
    deploy_service_package_to_node_description = openapi_server.DeployServicePackageToNodeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/DeployServicePackage'.format(node_name='node_name_example'),
        headers=headers,
        json=deploy_service_package_to_node_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_package_health(client):
    """Test case for get_deployed_service_package_health

    Gets the information about health of an service package for a specific application deployed for a Service Fabric node and application.
    """
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetServicePackages/{service_package_name}/$/GetHealth'.format(node_name='node_name_example', application_id='application_id_example', service_package_name='service_package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_deployed_service_package_health_using_policy(client):
    """Test case for get_deployed_service_package_health_using_policy

    Gets the information about health of service package for a specific application deployed on a Service Fabric node using the specified policy.
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
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetServicePackages/{service_package_name}/$/GetHealth'.format(node_name='node_name_example', application_id='application_id_example', service_package_name='service_package_name_example'),
        headers=headers,
        json=application_health_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_package_info_list(client):
    """Test case for get_deployed_service_package_info_list

    Gets the list of service packages deployed on a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetServicePackages'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_service_package_info_list_by_name(client):
    """Test case for get_deployed_service_package_info_list_by_name

    Gets the list of service packages deployed on a Service Fabric node matching exactly the specified name.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetServicePackages/{service_package_name}'.format(node_name='node_name_example', application_id='application_id_example', service_package_name='service_package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_deployed_service_package_health(client):
    """Test case for report_deployed_service_package_health

    Sends a health report on the Service Fabric deployed service package.
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
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetServicePackages/{service_package_name}/$/ReportHealth'.format(node_name='node_name_example', application_id='application_id_example', service_package_name='service_package_name_example'),
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

