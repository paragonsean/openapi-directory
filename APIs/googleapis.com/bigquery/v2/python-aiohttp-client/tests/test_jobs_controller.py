# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_query_results_response import GetQueryResultsResponse
from openapi_server.models.job import Job
from openapi_server.models.job_cancel_response import JobCancelResponse
from openapi_server.models.job_list import JobList
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse


pytestmark = pytest.mark.asyncio

async def test_bigquery_jobs_cancel(client):
    """Test case for bigquery_jobs_cancel

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('location', 'location_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bigquery/v2/projects/{project_id}/jobs/{job_id}/cancel'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_jobs_delete(client):
    """Test case for bigquery_jobs_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('location', 'location_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bigquery/v2/projects/{project_id}/jobs/{job_id}/delete'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_jobs_get(client):
    """Test case for bigquery_jobs_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('location', 'location_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/jobs/{job_id}'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_jobs_get_query_results(client):
    """Test case for bigquery_jobs_get_query_results

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('formatOptions.useInt64Timestamp', True),
                    ('location', 'location_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('startIndex', 'start_index_example'),
                    ('timeoutMs', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/queries/{job_id}'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_bigquery_jobs_insert(client):
    """Test case for bigquery_jobs_insert

    
    """
    body = openapi_server.Job()
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bigquery/v2/projects/{project_id}/jobs'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_jobs_list(client):
    """Test case for bigquery_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('allUsers', True),
                    ('maxCreationTime', 'max_creation_time_example'),
                    ('maxResults', 56),
                    ('minCreationTime', 'min_creation_time_example'),
                    ('pageToken', 'page_token_example'),
                    ('parentJobId', 'parent_job_id_example'),
                    ('projection', 'projection_example'),
                    ('stateFilter', ['state_filter_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/jobs'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_jobs_query(client):
    """Test case for bigquery_jobs_query

    
    """
    body = {"connectionProperties":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"jobCreationMode":"JOB_CREATION_MODE_UNSPECIFIED","dryRun":True,"useQueryCache":True,"kind":"bigquery#queryRequest","preserveNulls":True,"query":"query","maximumBytesBilled":"maximumBytesBilled","formatOptions":{"useInt64Timestamp":True},"createSession":True,"defaultDataset":{"datasetId":"datasetId","projectId":"projectId"},"labels":{"key":"labels"},"parameterMode":"parameterMode","queryParameters":[{"parameterType":{"type":"type","structTypes":[{"name":"name","description":"description"},{"name":"name","description":"description"}]},"name":"name","parameterValue":{"rangeValue":{},"structValues":{},"value":"value","arrayValues":[null,null]}},{"parameterType":{"type":"type","structTypes":[{"name":"name","description":"description"},{"name":"name","description":"description"}]},"name":"name","parameterValue":{"rangeValue":{},"structValues":{},"value":"value","arrayValues":[null,null]}}],"maxResults":0,"requestId":"requestId","timeoutMs":6,"continuous":True,"location":"location","useLegacySql":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bigquery/v2/projects/{project_id}/queries'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

