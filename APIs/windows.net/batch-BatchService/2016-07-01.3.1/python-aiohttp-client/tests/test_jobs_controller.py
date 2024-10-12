# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.cloud_job import CloudJob
from openapi_server.models.cloud_job_list_preparation_and_release_task_status_result import CloudJobListPreparationAndReleaseTaskStatusResult
from openapi_server.models.cloud_job_list_result import CloudJobListResult
from openapi_server.models.job_add_parameter import JobAddParameter
from openapi_server.models.job_disable_parameter import JobDisableParameter
from openapi_server.models.job_patch_parameter import JobPatchParameter
from openapi_server.models.job_statistics import JobStatistics
from openapi_server.models.job_terminate_parameter import JobTerminateParameter
from openapi_server.models.job_update_parameter import JobUpdateParameter


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_add(client):
    """Test case for job_add

    Adds a job to the specified account.
    """
    job = openapi_server.JobAddParameter()
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
        path='/jobs',
        headers=headers,
        json=job,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_delete(client):
    """Test case for job_delete

    Deletes a job.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='DELETE',
        path='/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_disable(client):
    """Test case for job_disable

    Disables the specified job, preventing new tasks from running.
    """
    job_disable_parameter = openapi_server.JobDisableParameter()
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
        path='/jobs/{job_id}/disable'.format(job_id='job_id_example'),
        headers=headers,
        json=job_disable_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_enable(client):
    """Test case for job_enable

    Enables the specified job, allowing new tasks to run.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
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
        path='/jobs/{job_id}/enable'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get(client):
    """Test case for job_get

    Gets information about the specified job.
    """
    params = [('$select', 'select_example'),
                    ('$expand', 'expand_example'),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get_all_jobs_lifetime_statistics(client):
    """Test case for job_get_all_jobs_lifetime_statistics

    Gets lifetime summary statistics for all of the jobs in the specified account.
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
        path='/lifetimejobstats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list(client):
    """Test case for job_list

    Lists all of the jobs in the specified account.
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
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
        path='/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list_from_job_schedule(client):
    """Test case for job_list_from_job_schedule

    Lists the jobs that have been created under the specified job schedule.
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
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
        path='/jobschedules/{job_schedule_id}/jobs'.format(job_schedule_id='job_schedule_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list_preparation_and_release_task_status(client):
    """Test case for job_list_preparation_and_release_task_status

    Lists the execution status of the Job Preparation and Job Release task for the specified job across the compute nodes where the job has run.
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
        path='/jobs/{job_id}/jobpreparationandreleasetaskstatus'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_patch(client):
    """Test case for job_patch

    Updates the properties of the specified job.
    """
    job_patch_parameter = openapi_server.JobPatchParameter()
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
        method='PATCH',
        path='/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        json=job_patch_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_terminate(client):
    """Test case for job_terminate

    Terminates the specified job, marking it as completed.
    """
    job_terminate_parameter = openapi_server.JobTerminateParameter()
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
        path='/jobs/{job_id}/terminate'.format(job_id='job_id_example'),
        headers=headers,
        json=job_terminate_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_update(client):
    """Test case for job_update

    Updates the properties of the specified job.
    """
    job_update_parameter = openapi_server.JobUpdateParameter()
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
        method='PUT',
        path='/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        json=job_update_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

