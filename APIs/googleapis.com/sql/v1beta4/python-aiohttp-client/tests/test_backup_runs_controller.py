# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_run import BackupRun
from openapi_server.models.backup_runs_list_response import BackupRunsListResponse
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_sql_backup_runs_delete(client):
    """Test case for sql_backup_runs_delete

    
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
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/backupRuns/{id}'.format(project='project_example', instance='instance_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_backup_runs_get(client):
    """Test case for sql_backup_runs_get

    
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
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/backupRuns/{id}'.format(project='project_example', instance='instance_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_backup_runs_insert(client):
    """Test case for sql_backup_runs_insert

    
    """
    body = {"instance":"instance","windowStartTime":"windowStartTime","kind":"kind","description":"description","timeZone":"timeZone","diskEncryptionConfiguration":{"kind":"kind","kmsKeyName":"kmsKeyName"},"diskEncryptionStatus":{"kind":"kind","kmsKeyVersionName":"kmsKeyVersionName"},"error":{"code":"code","kind":"kind","message":"message"},"type":"SQL_BACKUP_RUN_TYPE_UNSPECIFIED","selfLink":"selfLink","enqueuedTime":"enqueuedTime","backupKind":"SQL_BACKUP_KIND_UNSPECIFIED","location":"location","startTime":"startTime","endTime":"endTime","id":"id","status":"SQL_BACKUP_RUN_STATUS_UNSPECIFIED"}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/backupRuns'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_backup_runs_list(client):
    """Test case for sql_backup_runs_list

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/backupRuns'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

