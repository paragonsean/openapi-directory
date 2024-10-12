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

    
    """
    body = openapi_server.JobAddParameter()
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
        path='/jobs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_delete(client):
    """Test case for job_delete

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
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

    
    """
    body = openapi_server.JobDisableParameter()
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
        path='/jobs/{job_id}/disable'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_enable(client):
    """Test case for job_enable

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
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
        path='/jobs/{job_id}/enable'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get(client):
    """Test case for job_get

    
    """
    params = [('$select', 'select_example'),
                    ('$expand', 'expand_example'),
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
        path='/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get_all_jobs_lifetime_statistics(client):
    """Test case for job_get_all_jobs_lifetime_statistics

    
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
        path='/lifetimejobstats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list(client):
    """Test case for job_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
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
        path='/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list_from_job_schedule(client):
    """Test case for job_list_from_job_schedule

    
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
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
        path='/jobschedules/{job_schedule_id}/jobs'.format(job_schedule_id='job_schedule_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list_preparation_and_release_task_status(client):
    """Test case for job_list_preparation_and_release_task_status

    
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
        path='/jobs/{job_id}/jobpreparationandreleasetaskstatus'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_patch(client):
    """Test case for job_patch

    
    """
    body = openapi_server.JobPatchParameter()
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
        method='PATCH',
        path='/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_terminate(client):
    """Test case for job_terminate

    
    """
    body = openapi_server.JobTerminateParameter()
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
        path='/jobs/{job_id}/terminate'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_job_update(client):
    """Test case for job_update

    
    """
    body = openapi_server.JobUpdateParameter()
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
        method='PUT',
        path='/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

