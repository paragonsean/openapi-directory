# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_operations_cancel(client):
    """Test case for cloudprivatecatalogproducer_operations_cancel

    
    """
    body = None
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalogproducer_operations_list(client):
    """Test case for cloudprivatecatalogproducer_operations_list

    
    """
    params = [('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('filter', 'filter_example'),
                    ('name', 'name_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

