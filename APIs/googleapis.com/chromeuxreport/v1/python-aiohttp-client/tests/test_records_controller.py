# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_history_request import QueryHistoryRequest
from openapi_server.models.query_history_response import QueryHistoryResponse
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse


pytestmark = pytest.mark.asyncio

async def test_chromeuxreport_records_query_history_record(client):
    """Test case for chromeuxreport_records_query_history_record

    
    """
    body = {"formFactor":"ALL_FORM_FACTORS","origin":"origin","metrics":["metrics","metrics"],"url":"url"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/records:queryHistoryRecord',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromeuxreport_records_query_record(client):
    """Test case for chromeuxreport_records_query_record

    
    """
    body = {"effectiveConnectionType":"effectiveConnectionType","formFactor":"ALL_FORM_FACTORS","origin":"origin","metrics":["metrics","metrics"],"url":"url"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/records:queryRecord',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

