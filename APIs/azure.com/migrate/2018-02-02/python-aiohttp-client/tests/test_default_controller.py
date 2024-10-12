# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assessed_machine import AssessedMachine
from openapi_server.models.assessed_machine_result_list import AssessedMachineResultList
from openapi_server.models.assessment import Assessment
from openapi_server.models.assessment_options_result_list import AssessmentOptionsResultList
from openapi_server.models.assessment_result_list import AssessmentResultList
from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.download_url import DownloadUrl
from openapi_server.models.group import Group
from openapi_server.models.group_result_list import GroupResultList
from openapi_server.models.machine import Machine
from openapi_server.models.machine_result_list import MachineResultList
from openapi_server.models.operation_result_list import OperationResultList
from openapi_server.models.project import Project
from openapi_server.models.project_key import ProjectKey
from openapi_server.models.project_result_list import ProjectResultList


pytestmark = pytest.mark.asyncio

async def test_assessed_machines_get(client):
    """Test case for assessed_machines_get

    Get an assessed machine.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}/assessments/{assessment_name}/assessedMachines/{assessed_machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example', assessed_machine_name='assessed_machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessed_machines_list_by_assessment(client):
    """Test case for assessed_machines_list_by_assessment

    Get assessed machines for assessment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}/assessments/{assessment_name}/assessedMachines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessment_options_get(client):
    """Test case for assessment_options_get

    Get the assessment options.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Migrate/locations/{location_name}/assessmentOptions'.format(subscription_id='subscription_id_example', location_name='location_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_create(client):
    """Test case for assessments_create

    Create or Update assessment.
    """
    assessment = {"name":"name","eTag":"eTag","id":"id","type":"type","properties":{"createdTimestamp":"2000-01-23T04:56:07.000+00:00","scalingFactor":7.061401241503109,"pricesTimestamp":"2000-01-23T04:56:07.000+00:00","confidenceRatingInPercentage":0.8008281904610115,"updatedTimestamp":"2000-01-23T04:56:07.000+00:00","azureStorageRedundancy":"Unknown","discountPercentage":6.027456183070403,"azurePricingTier":"Standard","percentile":"Percentile50","azureOfferCode":"Unknown","stage":"InProgress","numberOfMachines":2,"azureLocation":"Unknown","sizingCriterion":"PerformanceBased","currency":"Unknown","monthlyBandwidthCost":1.4658129805029452,"azureHybridUseBenefit":"Unknown","monthlyComputeCost":5.962133916683182,"monthlyStorageCost":5.637376656633329,"status":"Created","timeRange":"Day"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}/assessments/{assessment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
        headers=headers,
        json=assessment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_delete(client):
    """Test case for assessments_delete

    Deletes an assessment from the project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}/assessments/{assessment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_get(client):
    """Test case for assessments_get

    Get an assessment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}/assessments/{assessment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_get_report_download_url(client):
    """Test case for assessments_get_report_download_url

    Get download URL for the assessment report.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}/assessments/{assessment_name}/downloadUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_list_by_group(client):
    """Test case for assessments_list_by_group

    Get all assessments created for the specified group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}/assessments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_list_by_project(client):
    """Test case for assessments_list_by_project

    Get all assessments created in the project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/assessments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_create(client):
    """Test case for groups_create

    Create a new group with specified settings. If group with the name provided already exists, then the existing group is updated.
    """
    group = {"name":"name","eTag":"eTag","id":"id","type":"type","properties":{"assessments":["assessments","assessments"],"createdTimestamp":"2000-01-23T04:56:07.000+00:00","machines":["machines","machines"],"updatedTimestamp":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
        headers=headers,
        json=group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_delete(client):
    """Test case for groups_delete

    Delete the group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get(client):
    """Test case for groups_get

    Get a specific group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups/{group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_list_by_project(client):
    """Test case for groups_list_by_project

    Get all groups
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/groups'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_location_check_name_availability(client):
    """Test case for location_check_name_availability

    
    """
    parameters = {"name":"name","type":"Microsoft.Migrate/projects"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Migrate/locations/{location_name}/checkNameAvailability'.format(location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machines_get(client):
    """Test case for machines_get

    Get a specific machine.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/machines/{machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', machine_name='machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machines_list_by_project(client):
    """Test case for machines_list_by_project

    Get all machines in the project
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/machines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    Get list of operations supported in the API.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Migrate/operations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create(client):
    """Test case for projects_create

    Create or update project.
    """
    project = {"name":"name","eTag":"eTag","location":"location","id":"id","type":"type","properties":{"customerWorkspaceLocation":"customerWorkspaceLocation","lastDiscoverySessionId":"lastDiscoverySessionId","numberOfAssessments":0,"numberOfMachines":1,"createdTimestamp":"2000-01-23T04:56:07.000+00:00","discoveryStatus":"Unknown","numberOfGroups":6,"lastAssessmentTimestamp":"2000-01-23T04:56:07.000+00:00","provisioningState":"Accepted","customerWorkspaceId":"customerWorkspaceId","updatedTimestamp":"2000-01-23T04:56:07.000+00:00","lastDiscoveryTimestamp":"2000-01-23T04:56:07.000+00:00"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        json=project,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_delete(client):
    """Test case for projects_delete

    Delete the project
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get(client):
    """Test case for projects_get

    Get the specified project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_keys(client):
    """Test case for projects_get_keys

    Get shared keys for the project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}/keys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_by_resource_group(client):
    """Test case for projects_list_by_resource_group

    Get all projects.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/projects'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_by_subscription(client):
    """Test case for projects_list_by_subscription

    Get all projects.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Migrate/projects'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update(client):
    """Test case for projects_update

    Update project.
    """
    project = {"name":"name","eTag":"eTag","location":"location","id":"id","type":"type","properties":{"customerWorkspaceLocation":"customerWorkspaceLocation","lastDiscoverySessionId":"lastDiscoverySessionId","numberOfAssessments":0,"numberOfMachines":1,"createdTimestamp":"2000-01-23T04:56:07.000+00:00","discoveryStatus":"Unknown","numberOfGroups":6,"lastAssessmentTimestamp":"2000-01-23T04:56:07.000+00:00","provisioningState":"Accepted","customerWorkspaceId":"customerWorkspaceId","updatedTimestamp":"2000-01-23T04:56:07.000+00:00","lastDiscoveryTimestamp":"2000-01-23T04:56:07.000+00:00"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        json=project,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

