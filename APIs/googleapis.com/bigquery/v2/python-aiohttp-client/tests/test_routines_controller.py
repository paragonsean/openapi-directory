# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_routines_response import ListRoutinesResponse
from openapi_server.models.routine import Routine


pytestmark = pytest.mark.asyncio

async def test_bigquery_routines_delete(client):
    """Test case for bigquery_routines_delete

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/routines/{routine_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example', routine_id='routine_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_routines_get(client):
    """Test case for bigquery_routines_get

    
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
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/routines/{routine_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example', routine_id='routine_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_routines_insert(client):
    """Test case for bigquery_routines_insert

    
    """
    body = {"dataGovernanceType":"DATA_GOVERNANCE_TYPE_UNSPECIFIED","importedLibraries":["importedLibraries","importedLibraries"],"lastModifiedTime":"lastModifiedTime","creationTime":"creationTime","sparkOptions":{"pyFileUris":["pyFileUris","pyFileUris"],"runtimeVersion":"runtimeVersion","mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"connection":"connection","fileUris":["fileUris","fileUris"],"jarUris":["jarUris","jarUris"],"containerImage":"containerImage","properties":{"key":"properties"},"mainFileUri":"mainFileUri"},"routineType":"ROUTINE_TYPE_UNSPECIFIED","strictMode":True,"description":"description","language":"LANGUAGE_UNSPECIFIED","securityMode":"SECURITY_MODE_UNSPECIFIED","definitionBody":"definitionBody","returnTableType":{"columns":[{"name":"name","type":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}}},{"name":"name","type":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}}}]},"remoteFunctionOptions":{"userDefinedContext":{"key":"userDefinedContext"},"endpoint":"endpoint","maxBatchingRows":"maxBatchingRows","connection":"connection"},"determinismLevel":"DETERMINISM_LEVEL_UNSPECIFIED","arguments":[{"mode":"MODE_UNSPECIFIED","dataType":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}},"name":"name","argumentKind":"ARGUMENT_KIND_UNSPECIFIED","isAggregate":True},{"mode":"MODE_UNSPECIFIED","dataType":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}},"name":"name","argumentKind":"ARGUMENT_KIND_UNSPECIFIED","isAggregate":True}],"etag":"etag","routineReference":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"returnType":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}}}
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
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/routines'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_routines_list(client):
    """Test case for bigquery_routines_list

    
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
                    ('filter', 'filter_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/routines'.format(project_id='project_id_example', dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_routines_update(client):
    """Test case for bigquery_routines_update

    
    """
    body = {"dataGovernanceType":"DATA_GOVERNANCE_TYPE_UNSPECIFIED","importedLibraries":["importedLibraries","importedLibraries"],"lastModifiedTime":"lastModifiedTime","creationTime":"creationTime","sparkOptions":{"pyFileUris":["pyFileUris","pyFileUris"],"runtimeVersion":"runtimeVersion","mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"connection":"connection","fileUris":["fileUris","fileUris"],"jarUris":["jarUris","jarUris"],"containerImage":"containerImage","properties":{"key":"properties"},"mainFileUri":"mainFileUri"},"routineType":"ROUTINE_TYPE_UNSPECIFIED","strictMode":True,"description":"description","language":"LANGUAGE_UNSPECIFIED","securityMode":"SECURITY_MODE_UNSPECIFIED","definitionBody":"definitionBody","returnTableType":{"columns":[{"name":"name","type":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}}},{"name":"name","type":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}}}]},"remoteFunctionOptions":{"userDefinedContext":{"key":"userDefinedContext"},"endpoint":"endpoint","maxBatchingRows":"maxBatchingRows","connection":"connection"},"determinismLevel":"DETERMINISM_LEVEL_UNSPECIFIED","arguments":[{"mode":"MODE_UNSPECIFIED","dataType":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}},"name":"name","argumentKind":"ARGUMENT_KIND_UNSPECIFIED","isAggregate":True},{"mode":"MODE_UNSPECIFIED","dataType":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}},"name":"name","argumentKind":"ARGUMENT_KIND_UNSPECIFIED","isAggregate":True}],"etag":"etag","routineReference":{"datasetId":"datasetId","projectId":"projectId","routineId":"routineId"},"returnType":{"typeKind":"TYPE_KIND_UNSPECIFIED","structType":{"fields":[null,null]}}}
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
        method='PUT',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/routines/{routine_id}'.format(project_id='project_id_example', dataset_id='dataset_id_example', routine_id='routine_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

