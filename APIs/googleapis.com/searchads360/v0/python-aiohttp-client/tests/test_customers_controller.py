# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_ads_searchads360_v0_services_list_accessible_customers_response import GoogleAdsSearchads360V0ServicesListAccessibleCustomersResponse
from openapi_server.models.google_ads_searchads360_v0_services_list_custom_columns_response import GoogleAdsSearchads360V0ServicesListCustomColumnsResponse
from openapi_server.models.google_ads_searchads360_v0_services_search_search_ads360_request import GoogleAdsSearchads360V0ServicesSearchSearchAds360Request
from openapi_server.models.google_ads_searchads360_v0_services_search_search_ads360_response import GoogleAdsSearchads360V0ServicesSearchSearchAds360Response


pytestmark = pytest.mark.asyncio

async def test_searchads360_customers_custom_columns_list(client):
    """Test case for searchads360_customers_custom_columns_list

    
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
        path='/v0/customers/{customer_id}/customColumns'.format(customer_id='customer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchads360_customers_list_accessible_customers(client):
    """Test case for searchads360_customers_list_accessible_customers

    
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
        path='/v0/customers:listAccessibleCustomers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchads360_customers_search_ads360_search(client):
    """Test case for searchads360_customers_search_ads360_search

    
    """
    body = openapi_server.GoogleAdsSearchads360V0ServicesSearchSearchAds360Request()
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
        path='/v0/customers/{customer_id}/searchAds360:search'.format(customer_id='customer_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

