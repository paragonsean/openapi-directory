# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_ads_searchads360_v0_resources_search_ads360_field import GoogleAdsSearchads360V0ResourcesSearchAds360Field
from openapi_server.models.google_ads_searchads360_v0_services_search_search_ads360_fields_request import GoogleAdsSearchads360V0ServicesSearchSearchAds360FieldsRequest
from openapi_server.models.google_ads_searchads360_v0_services_search_search_ads360_fields_response import GoogleAdsSearchads360V0ServicesSearchSearchAds360FieldsResponse


pytestmark = pytest.mark.asyncio

async def test_searchads360_search_ads360_fields_get(client):
    """Test case for searchads360_search_ads360_fields_get

    
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
        path='/v0/{resource_name}'.format(resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchads360_search_ads360_fields_search(client):
    """Test case for searchads360_search_ads360_fields_search

    
    """
    body = openapi_server.GoogleAdsSearchads360V0ServicesSearchSearchAds360FieldsRequest()
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
        path='/v0/searchAds360Fields:search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

