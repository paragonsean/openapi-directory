# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_datacatalog_v1_search_catalog_request import GoogleCloudDatacatalogV1SearchCatalogRequest
from openapi_server.models.google_cloud_datacatalog_v1_search_catalog_response import GoogleCloudDatacatalogV1SearchCatalogResponse


pytestmark = pytest.mark.asyncio

async def test_datacatalog_catalog_search(client):
    """Test case for datacatalog_catalog_search

    
    """
    body = {"adminSearch":True,"query":"query","scope":{"starredOnly":True,"includeGcpPublicDatasets":True,"includeOrgIds":["includeOrgIds","includeOrgIds"],"includeProjectIds":["includeProjectIds","includeProjectIds"],"restrictedLocations":["restrictedLocations","restrictedLocations"],"includePublicTagTemplates":True},"orderBy":"orderBy","pageSize":0,"pageToken":"pageToken"}
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
        path='/v1/catalog:search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

