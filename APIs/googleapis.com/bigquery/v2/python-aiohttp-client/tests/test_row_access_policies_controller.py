# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_row_access_policies_response import ListRowAccessPoliciesResponse


pytestmark = pytest.mark.asyncio

async def test_bigquery_row_access_policies_list(client):
    """Test case for bigquery_row_access_policies_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}/rowAccessPolicies'.format(project_id='project_id_example', dataset_id='dataset_id_example', table_id='table_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

