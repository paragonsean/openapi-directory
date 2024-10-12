# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.table_data_insert_all_request import TableDataInsertAllRequest
from openapi_server.models.table_data_insert_all_response import TableDataInsertAllResponse
from openapi_server.models.table_data_list import TableDataList


pytestmark = pytest.mark.asyncio

async def test_bigquery_tabledata_insert_all(client):
    """Test case for bigquery_tabledata_insert_all

    
    """
    body = {"traceId":"traceId","skipInvalidRows":True,"kind":"bigquery#tableDataInsertAllRequest","templateSuffix":"templateSuffix","ignoreUnknownValues":True,"rows":[{"json":{},"insertId":"insertId"},{"json":{},"insertId":"insertId"}]}
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
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}/insertAll'.format(project_id='project_id_example', dataset_id='dataset_id_example', table_id='table_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bigquery_tabledata_list(client):
    """Test case for bigquery_tabledata_list

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startIndex', 'start_index_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}/data'.format(project_id='project_id_example', dataset_id='dataset_id_example', table_id='table_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

