# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_description import ApplicationDescription
from openapi_server.models.application_health import ApplicationHealth
from openapi_server.models.application_health_policy import ApplicationHealthPolicy
from openapi_server.models.application_info import ApplicationInfo
from openapi_server.models.application_load_info import ApplicationLoadInfo
from openapi_server.models.application_upgrade_description import ApplicationUpgradeDescription
from openapi_server.models.application_upgrade_progress_info import ApplicationUpgradeProgressInfo
from openapi_server.models.application_upgrade_update_description import ApplicationUpgradeUpdateDescription
from openapi_server.models.deployed_application_health import DeployedApplicationHealth
from openapi_server.models.deployed_application_info import DeployedApplicationInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.paged_application_info_list import PagedApplicationInfoList
from openapi_server.models.paged_deployed_application_info_list import PagedDeployedApplicationInfoList
from openapi_server.models.resume_application_upgrade_description import ResumeApplicationUpgradeDescription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_application(client):
    """Test case for create_application

    Creates a Service Fabric application.
    """
    application_description = openapi_server.ApplicationDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/$/Create',
        headers=headers,
        json=application_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_application(client):
    """Test case for delete_application

    Deletes an existing Service Fabric application.
    """
    params = [('api-version', 6.0),
                    ('ForceRemove', True),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/Delete'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_health(client):
    """Test case for get_application_health

    Gets the health of the service fabric application.
    """
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('DeployedApplicationsHealthStateFilter', 0),
                    ('ServicesHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}/$/GetHealth'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_application_health_using_policy(client):
    """Test case for get_application_health_using_policy

    Gets the health of a Service Fabric application using the specified policy.
    """
    application_health_policy = openapi_server.ApplicationHealthPolicy()
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('DeployedApplicationsHealthStateFilter', 0),
                    ('ServicesHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/GetHealth'.format(application_id='application_id_example'),
        headers=headers,
        json=application_health_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_info(client):
    """Test case for get_application_info

    Gets information about a Service Fabric application.
    """
    params = [('api-version', 6.0),
                    ('ExcludeApplicationParameters', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_info_list(client):
    """Test case for get_application_info_list

    Gets the list of applications created in the Service Fabric cluster that match the specified filters.
    """
    params = [('api-version', 6.1),
                    ('ApplicationDefinitionKindFilter', 0),
                    ('ApplicationTypeName', 'application_type_name_example'),
                    ('ExcludeApplicationParameters', False),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_load_info(client):
    """Test case for get_application_load_info

    Gets load information about a Service Fabric application.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}/$/GetLoadInformation'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_upgrade(client):
    """Test case for get_application_upgrade

    Gets details for the latest upgrade performed on this application.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}/$/GetUpgradeProgress'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_application_health(client):
    """Test case for get_deployed_application_health

    Gets the information about health of an application deployed on a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('DeployedServicePackagesHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetHealth'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_deployed_application_health_using_policy(client):
    """Test case for get_deployed_application_health_using_policy

    Gets the information about health of an application deployed on a Service Fabric node. using the specified policy.
    """
    application_health_policy = openapi_server.ApplicationHealthPolicy()
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('DeployedServicePackagesHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/GetHealth'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        json=application_health_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_application_info(client):
    """Test case for get_deployed_application_info

    Gets the information about an application deployed on a Service Fabric node.
    """
    params = [('api-version', 6.1),
                    ('timeout', 60),
                    ('IncludeHealthState', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_id}'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployed_application_info_list(client):
    """Test case for get_deployed_application_info_list

    Gets the list of applications deployed on a Service Fabric node.
    """
    params = [('api-version', 6.1),
                    ('timeout', 60),
                    ('IncludeHealthState', False),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_application_health(client):
    """Test case for report_application_health

    Sends a health report on the Service Fabric application.
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
        path='/Applications/{application_id}/$/ReportHealth'.format(application_id='application_id_example'),
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_deployed_application_health(client):
    """Test case for report_deployed_application_health

    Sends a health report on the Service Fabric application deployed on a Service Fabric node.
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
        path='/Nodes/{node_name}/$/GetApplications/{application_id}/$/ReportHealth'.format(node_name='node_name_example', application_id='application_id_example'),
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_resume_application_upgrade(client):
    """Test case for resume_application_upgrade

    Resumes upgrading an application in the Service Fabric cluster.
    """
    resume_application_upgrade_description = openapi_server.ResumeApplicationUpgradeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/MoveToNextUpgradeDomain'.format(application_id='application_id_example'),
        headers=headers,
        json=resume_application_upgrade_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rollback_application_upgrade(client):
    """Test case for rollback_application_upgrade

    Starts rolling back the currently on-going upgrade of an application in the Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/RollbackUpgrade'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_start_application_upgrade(client):
    """Test case for start_application_upgrade

    Starts upgrading an application in the Service Fabric cluster.
    """
    application_upgrade_description = openapi_server.ApplicationUpgradeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/Upgrade'.format(application_id='application_id_example'),
        headers=headers,
        json=application_upgrade_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_application_upgrade(client):
    """Test case for update_application_upgrade

    Updates an ongoing application upgrade in the Service Fabric cluster.
    """
    application_upgrade_update_description = openapi_server.ApplicationUpgradeUpdateDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/UpdateUpgrade'.format(application_id='application_id_example'),
        headers=headers,
        json=application_upgrade_update_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

