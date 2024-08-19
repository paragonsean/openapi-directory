# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assessed_machine import AssessedMachine
from openapi_server.models.assessed_machine_result_list import AssessedMachineResultList
from openapi_server.models.assessment import Assessment
from openapi_server.models.assessment_options import AssessmentOptions
from openapi_server.models.assessment_options_result_list import AssessmentOptionsResultList
from openapi_server.models.assessment_result_list import AssessmentResultList
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.download_url import DownloadUrl
from openapi_server.models.group import Group
from openapi_server.models.group_result_list import GroupResultList
from openapi_server.models.hyper_v_collector import HyperVCollector
from openapi_server.models.hyper_v_collector_list import HyperVCollectorList
from openapi_server.models.machine import Machine
from openapi_server.models.machine_result_list import MachineResultList
from openapi_server.models.operation_result_list import OperationResultList
from openapi_server.models.project import Project
from openapi_server.models.project_result_list import ProjectResultList
from openapi_server.models.update_group_body import UpdateGroupBody
from openapi_server.models.v_mware_collector import VMwareCollector
from openapi_server.models.v_mware_collector_list import VMwareCollectorList


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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/assessments/{assessment_name}/assessedMachines/{assessed_machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example', assessed_machine_name='assessed_machine_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/assessments/{assessment_name}/assessedMachines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_create(client):
    """Test case for assessments_create

    Create or Update assessment.
    """
    assessment = {"name":"name","eTag":"eTag","id":"id","type":"type","properties":{"vmUptime":{"daysPerMonth":2.027123023002322,"hoursPerDay":4.145608029883936},"monthlyStandardSSDStorageCost":2.3021358869347655,"pricesTimestamp":"2000-01-23T04:56:07.000+00:00","updatedTimestamp":"2000-01-23T04:56:07.000+00:00","eaSubscriptionId":"eaSubscriptionId","azureStorageRedundancy":"Unknown","discountPercentage":6.027456183070403,"azurePricingTier":"Standard","azureOfferCode":"Unknown","numberOfMachines":9,"azureLocation":"Unknown","perfDataStartTime":"2000-01-23T04:56:07.000+00:00","reservedInstance":"None","currency":"Unknown","monthlyBandwidthCost":1.4658129805029452,"azureHybridUseBenefit":"Unknown","monthlyStorageCost":7.061401241503109,"timeRange":"Day","monthlyPremiumStorageCost":5.637376656633329,"perfDataEndTime":"2000-01-23T04:56:07.000+00:00","createdTimestamp":"2000-01-23T04:56:07.000+00:00","azureDiskType":"Unknown","scalingFactor":3.616076749251911,"confidenceRatingInPercentage":0.8008281904610115,"azureVmFamilies":["Unknown","Unknown"],"percentile":"Percentile50","stage":"InProgress","sizingCriterion":"PerformanceBased","monthlyComputeCost":5.962133916683182,"status":"Created"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/assessments/{assessment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/assessments/{assessment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/assessments/{assessment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/assessments/{assessment_name}/downloadUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example', assessment_name='assessment_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/assessments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/assessments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_create(client):
    """Test case for groups_create

    Create a new group with specified settings.
    """
    group = {"name":"name","eTag":"eTag","id":"id","type":"type","properties":{"assessments":["assessments","assessments"],"createdTimestamp":"2000-01-23T04:56:07.000+00:00","areAssessmentsRunning":True,"groupStatus":"Created","machineCount":0,"updatedTimestamp":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_update_machines(client):
    """Test case for groups_update_machines

    Update machines in group.
    """
    group_update_properties = {"eTag":"eTag","properties":{"operationType":"Add","machines":["machines","machines"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/groups/{group_name}/updateMachines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', group_name='group_name_example'),
        headers=headers,
        json=group_update_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hyper_v_collectors_create(client):
    """Test case for hyper_v_collectors_create

    Create or Update Hyper-V collector.
    """
    collector_body = {"name":"name","eTag":"eTag","id":"id","type":"type","properties":{"discoverySiteId":"discoverySiteId","createdTimestamp":"createdTimestamp","updatedTimestamp":"updatedTimestamp","agentProperties":{"spnDetails":{"audience":"audience","authority":"authority","tenantId":"tenantId","applicationId":"applicationId","objectId":"objectId"},"lastHeartbeatUtc":"2000-01-23T04:56:07.000+00:00","id":"id","version":"version"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/hypervcollectors/{hyper_v_collector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', hyper_v_collector_name='hyper_v_collector_name_example'),
        headers=headers,
        json=collector_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hyper_v_collectors_delete(client):
    """Test case for hyper_v_collectors_delete

    Deletes Hyper-V collector from the project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/hypervcollectors/{hyper_v_collector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', hyper_v_collector_name='hyper_v_collector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hyper_v_collectors_get(client):
    """Test case for hyper_v_collectors_get

    Get a Hyper-V collector.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/hypervcollectors/{hyper_v_collector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', hyper_v_collector_name='hyper_v_collector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hyper_v_collectors_list_by_project(client):
    """Test case for hyper_v_collectors_list_by_project

    Get a list of Hyper-V collector.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/hypervcollectors'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/machines/{machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', machine_name='machine_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/machines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
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

async def test_project_assessment_options(client):
    """Test case for project_assessment_options

    Get all available options for the properties of an assessment on a project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/assessmentOptions/{assessment_options_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', assessment_options_name='assessment_options_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_assessment_options_list(client):
    """Test case for project_assessment_options_list

    Gets list of all available options for the properties of an assessment on a project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/assessmentOptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create(client):
    """Test case for projects_create

    Create or update project.
    """
    project = {"name":"name","eTag":"eTag","location":"location","id":"id","type":"type","properties":{"customerWorkspaceLocation":"customerWorkspaceLocation","projectStatus":"Active","numberOfAssessments":0,"numberOfMachines":1,"createdTimestamp":"2000-01-23T04:56:07.000+00:00","numberOfGroups":6,"lastAssessmentTimestamp":"2000-01-23T04:56:07.000+00:00","provisioningState":"Accepted","serviceEndpoint":"serviceEndpoint","customerWorkspaceId":"customerWorkspaceId","updatedTimestamp":"2000-01-23T04:56:07.000+00:00","assessmentSolutionId":"assessmentSolutionId"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
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
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
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
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list(client):
    """Test case for projects_list

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
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Migrate/assessmentProjects'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update(client):
    """Test case for projects_update

    Update project.
    """
    project = {"name":"name","eTag":"eTag","location":"location","id":"id","type":"type","properties":{"customerWorkspaceLocation":"customerWorkspaceLocation","projectStatus":"Active","numberOfAssessments":0,"numberOfMachines":1,"createdTimestamp":"2000-01-23T04:56:07.000+00:00","numberOfGroups":6,"lastAssessmentTimestamp":"2000-01-23T04:56:07.000+00:00","provisioningState":"Accepted","serviceEndpoint":"serviceEndpoint","customerWorkspaceId":"customerWorkspaceId","updatedTimestamp":"2000-01-23T04:56:07.000+00:00","assessmentSolutionId":"assessmentSolutionId"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        json=project,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_mware_collectors_create(client):
    """Test case for v_mware_collectors_create

    Create or Update VMware collector.
    """
    collector_body = {"name":"name","eTag":"eTag","id":"id","type":"type","properties":{"discoverySiteId":"discoverySiteId","createdTimestamp":"createdTimestamp","updatedTimestamp":"updatedTimestamp","agentProperties":{"spnDetails":{"audience":"audience","authority":"authority","tenantId":"tenantId","applicationId":"applicationId","objectId":"objectId"},"lastHeartbeatUtc":"2000-01-23T04:56:07.000+00:00","id":"id","version":"version"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/vmwarecollectors/{vm_ware_collector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', vm_ware_collector_name='vm_ware_collector_name_example'),
        headers=headers,
        json=collector_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_mware_collectors_delete(client):
    """Test case for v_mware_collectors_delete

    Deletes VMware collector from the project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/vmwarecollectors/{vm_ware_collector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', vm_ware_collector_name='vm_ware_collector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_mware_collectors_get(client):
    """Test case for v_mware_collectors_get

    Get a VMware collector.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/vmwarecollectors/{vm_ware_collector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example', vm_ware_collector_name='vm_ware_collector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_mware_collectors_list_by_project(client):
    """Test case for v_mware_collectors_list_by_project

    Get a list of VMware collector.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/assessmentProjects/{project_name}/vmwarecollectors'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

