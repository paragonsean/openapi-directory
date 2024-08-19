# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.bulk_download_request import BulkDownloadRequest
from openapi_server.models.bulk_job_list import BulkJobList
from openapi_server.models.bulk_query import BulkQuery
from openapi_server.models.bulk_status import BulkStatus
from openapi_server.models.bulk_upload_response import BulkUploadResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_bulk_by_object_name(client):
    """Test case for create_bulk_by_object_name

    Upload a file of objects to be bulk uploaded to the provider.
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'authorization': 'authorization_example',
        'elements_async_callback_url': 'elements_async_callback_url_example',
    }
    data = FormData()
    data.add_field('meta_data', 'meta_data_example')
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/elements/api-v2/bulk/{object_name}'.format(object_name='object_name_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_bulk_download(client):
    """Test case for create_bulk_download

    Create a new bulk download job (asynchronous)
    """
    body = openapi_server.BulkDownloadRequest()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/elements/api-v2/bulk/download',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_bulk_query(client):
    """Test case for create_bulk_query

    Create an asynchronous bulk query job.
    """
    params = [('q', 'q_example'),
                    ('lastRunDate', 'last_run_date_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'authorization': 'authorization_example',
        'elements_async_callback_url': 'elements_async_callback_url_example',
    }
    data = FormData()
    data.add_field('meta_data', 'meta_data_example')
    response = await client.request(
        method='POST',
        path='/elements/api-v2/bulk/query',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bulk_by_object_name(client):
    """Test case for get_bulk_by_object_name

    Retrieve the results of an asynchronous bulk query.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/bulk/{id}/{object_name}'.format(id='id_example', object_name='object_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bulk_errors(client):
    """Test case for get_bulk_errors

    Retrieve the errors of a bulk job.
    """
    params = [('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/bulk/{id}/errors'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bulk_jobs(client):
    """Test case for get_bulk_jobs

    Fetch all the bulk jobs for an instance
    """
    params = [('where', 'where_example'),
                    ('nextPage', 'next_page_example'),
                    ('pageSize', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/bulk/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bulk_status(client):
    """Test case for get_bulk_status

    Retrieve the status of a bulk job.
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/bulk/{id}/status'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_bulk_cancel(client):
    """Test case for replace_bulk_cancel

    Cancel an asynchronous bulk query job.
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/elements/api-v2/bulk/{id}/cancel'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

