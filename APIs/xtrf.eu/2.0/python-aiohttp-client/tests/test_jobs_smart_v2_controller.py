# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.external_file_dto import ExternalFileDto
from openapi_server.models.file_categorizations_dto import FileCategorizationsDto
from openapi_server.models.file_dto import FileDto
from openapi_server.models.file_link_categorizations_dto import FileLinkCategorizationsDto
from openapi_server.models.files_dto import FilesDto
from openapi_server.models.files_share_status_dto import FilesShareStatusDto
from openapi_server.models.job_dates_dto import JobDatesDto
from openapi_server.models.job_status_dto import JobStatusDTO
from openapi_server.models.project_file_dto import ProjectFileDto
from openapi_server.models.string_dto import StringDTO
from openapi_server.models.vendor_price_profile_dto import VendorPriceProfileDTO


pytestmark = pytest.mark.asyncio

async def test_add_external_file_link(client):
    """Test case for add_external_file_link

    
    """
    body = {"filename":"filename","languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"externalInfo":{"key":"externalInfo"},"languageIds":[0,0],"category":"category"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/jobs/{job_id}/files/addExternalLink'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_file_links(client):
    """Test case for add_file_links

    Adds file link to the project as a link delivered in the job.
    """
    body = {"fileLinks":[{"filename":"filename","toBeGenerated":True,"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"externalInfo":{"key":"externalInfo"},"languageIds":[0,0],"category":"category","url":"url"},{"filename":"filename","toBeGenerated":True,"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"externalInfo":{"key":"externalInfo"},"languageIds":[0,0],"category":"category","url":"url"}]}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/jobs/{job_id}/files/delivered/addLink'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_files(client):
    """Test case for add_files

    Adds files to the project as delivered in the job.
    """
    body = {"files":[{"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"languageIds":[0,0],"category":"category","fileId":"fileId"},{"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"languageIds":[0,0],"category":"category","fileId":"fileId"}]}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/files/delivered/add'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assign_vendor1(client):
    """Test case for assign_vendor1

    Assigns vendor to a job in a project.
    """
    body = {"vendorPriceProfileId":0}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/vendor'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_dates(client):
    """Test case for change_dates

    Updates dates of a given job.
    """
    body = {"actualEndDate":0,"actualStartDate":6,"deadline":1,"startDate":5}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/dates'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status1(client):
    """Test case for change_status1

    Changes job status if possible (400 Bad Request is returned otherwise).
    """
    body = {"externalId":"externalId","status":"status"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/status'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_external_id(client):
    """Test case for get_by_external_id

    
    """
    params = [('externalProjectId', 'external_project_id_example'),
                    ('externalId', 'external_id_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/jobs/for-external-id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_delivered_files(client):
    """Test case for get_delivered_files

    Returns list of files delivered in the job.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/jobs/{job_id}/files/delivered'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_by_id1(client):
    """Test case for get_file_by_id1

    Returns details for a job.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shared_reference_files(client):
    """Test case for get_shared_reference_files

    Returns list of files shared with the job as Reference Files.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/jobs/{job_id}/files/sharedReferenceFiles'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shared_work_files(client):
    """Test case for get_shared_work_files

    Returns list of files shared with the job as Work Files.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/jobs/{job_id}/files/sharedWorkFiles'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_share_as_reference_files(client):
    """Test case for share_as_reference_files

    Shares selected files as Reference Files with a job in a project.
    """
    body = /home-api/assets/examples/v2/jobs/shareAsReferenceFiles.json#requestBody
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/files/sharedReferenceFiles/share'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_share_as_work_files(client):
    """Test case for share_as_work_files

    Shares selected files as Work Files with a job in a project.
    """
    body = /home-api/assets/examples/v2/jobs/shareAsWorkFiles.json#requestBody
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/files/sharedWorkFiles/share'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_stop_sharing(client):
    """Test case for stop_sharing

    Stops sharing selected files with a job in a project.
    """
    body = /home-api/assets/examples/v2/jobs/stopSharing.json#requestBody
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/files/stopSharing'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_instructions4(client):
    """Test case for update_instructions4

    Updates instructions for a job.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/jobs/{job_id}/instructions'.format(job_id='job_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file1(client):
    """Test case for upload_file1

    Uploads file to the project as a file delivered in the job.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'multipart/form-data',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/home-api/v2/jobs/{job_id}/files/delivered/upload'.format(job_id='job_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

