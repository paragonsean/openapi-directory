# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_kms_inventory_v1_search_protected_resources_response import GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse


pytestmark = pytest.mark.asyncio

async def test_kmsinventory_organizations_protected_resources_search(client):
    """Test case for kmsinventory_organizations_protected_resources_search

    
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
                    ('cryptoKey', 'crypto_key_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('resourceTypes', ['resource_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{scope}/protectedResources:search'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

