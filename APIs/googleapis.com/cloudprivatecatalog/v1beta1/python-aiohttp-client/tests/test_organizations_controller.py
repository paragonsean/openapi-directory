# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_privatecatalog_v1beta1_search_catalogs_response import GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse
from openapi_server.models.google_cloud_privatecatalog_v1beta1_search_products_response import GoogleCloudPrivatecatalogV1beta1SearchProductsResponse
from openapi_server.models.google_cloud_privatecatalog_v1beta1_search_versions_response import GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalog_organizations_catalogs_search(client):
    """Test case for cloudprivatecatalog_organizations_catalogs_search

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{resource}/catalogs:search'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalog_organizations_products_search(client):
    """Test case for cloudprivatecatalog_organizations_products_search

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{resource}/products:search'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudprivatecatalog_organizations_versions_search(client):
    """Test case for cloudprivatecatalog_organizations_versions_search

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{resource}/versions:search'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

