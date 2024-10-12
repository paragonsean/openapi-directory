# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.counter import Counter
from openapi_server.models.import_job import ImportJob


pytestmark = pytest.mark.asyncio

async def test_activate_import_job(client):
    """Test case for activate_import_job

    Activate an ImportJob
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/jobs/{id}/activate'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_import_job(client):
    """Test case for create_import_job

    Create ImportJob
    """
    body = {"metadata":{"lastUpdate":6,"annotations":{"key":"annotations"},"createdOn":0,"labels":{"key":"labels"}},"mainArtifact":True,"repositoryDisableSSLValidation":True,"secretRef":"{\n    \"secretId\": \"5be58fb51ed744d1b87481bd\",\n    \"name\": \"Gogs internal\"\n}","active":True,"frequency":"frequency","repositoryUrl":"repositoryUrl","createdDate":"2000-01-23T04:56:07.000+00:00","lastImportError":"lastImportError","lastImportDate":"2000-01-23T04:56:07.000+00:00","name":"name","etag":"etag","id":"id","serviceRefs":[{"name":"name","serviceId":"serviceId","version":"version"},{"name":"name","serviceId":"serviceId","version":"version"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/jobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_import_job(client):
    """Test case for delete_import_job

    Delete ImportJob
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/jobs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_import_job_counter(client):
    """Test case for get_import_job_counter

    Get the ImportJobs counter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/jobs/count',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_import_jobs(client):
    """Test case for get_import_jobs

    Get ImportJobs
    """
    params = [('page', 56),
                    ('size', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_id_get(client):
    """Test case for jobs_id_get

    Get ImportJob
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_id_post(client):
    """Test case for jobs_id_post

    Update ImportJob
    """
    body = {"metadata":{"lastUpdate":6,"annotations":{"key":"annotations"},"createdOn":0,"labels":{"key":"labels"}},"mainArtifact":True,"repositoryDisableSSLValidation":True,"secretRef":"{\n    \"secretId\": \"5be58fb51ed744d1b87481bd\",\n    \"name\": \"Gogs internal\"\n}","active":True,"frequency":"frequency","repositoryUrl":"repositoryUrl","createdDate":"2000-01-23T04:56:07.000+00:00","lastImportError":"lastImportError","lastImportDate":"2000-01-23T04:56:07.000+00:00","name":"name","etag":"etag","id":"id","serviceRefs":[{"name":"name","serviceId":"serviceId","version":"version"},{"name":"name","serviceId":"serviceId","version":"version"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/jobs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_import_job(client):
    """Test case for start_import_job

    Start an ImportJob
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/jobs/{id}/start'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_import_job(client):
    """Test case for stop_import_job

    Stop an ImportJob
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/jobs/{id}/stop'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_artifact(client):
    """Test case for upload_artifact

    Upload an artifact
    """
    params = [('mainArtifact', True)]
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/artifact/upload',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

