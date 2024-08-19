# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assign_vendor_dto import AssignVendorDTO
from openapi_server.models.file_metadata_dto import FileMetadataDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.job_dates_dto import JobDatesDto
from openapi_server.models.job_dto import JobDto
from openapi_server.models.job_files_dto import JobFilesDTO
from openapi_server.models.job_status_dto import JobStatusDTO
from openapi_server.models.task_file_dto import TaskFileDTO


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_assign_file_to_job_output(client):
    """Test case for assign_file_to_job_output

    
    """
    body = /home-api/assets/examples/v1/jobs/assignFileToJobOutput.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/jobs/{job_id}/files/output'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assign_vendor(client):
    """Test case for assign_vendor

    Assigns vendor to a job in a project.
    """
    body = {"recalculateRates":True,"vendorPriceProfileId":0}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/jobs/{job_id}/vendor'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status(client):
    """Test case for change_status

    Changes job status if possible (400 Bad Request is returned otherwise).
    """
    body = {"externalId":"externalId","status":"status"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/jobs/{job_id}/status'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_details(client):
    """Test case for get_job_details

    Returns job details by jobId.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_files(client):
    """Test case for get_job_files

    Returns list of input and output files of a job.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/jobs/{job_id}/files'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_files1(client):
    """Test case for get_job_files1

    Returns file metadata.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/jobs/{job_id}/files/{file_id}'.format(job_id='job_id_example', file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_dates(client):
    """Test case for update_dates

    Updates dates of a given job.
    """
    body = {"actualEndDate":0,"actualStartDate":6,"deadline":1,"startDate":5}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/jobs/{job_id}/dates'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_instructions(client):
    """Test case for update_instructions

    Updates instructions for a job.
    """
    body = {"internal":"internal","notes":"notes","forProvider":"forProvider","paymentNoteForCustomer":"paymentNoteForCustomer","fromCustomer":"fromCustomer","paymentNoteForVendor":"paymentNoteForVendor"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/jobs/{job_id}/instructions'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

