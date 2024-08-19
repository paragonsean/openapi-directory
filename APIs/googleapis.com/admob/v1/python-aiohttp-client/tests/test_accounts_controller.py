# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_mediation_report_request import GenerateMediationReportRequest
from openapi_server.models.generate_mediation_report_response import GenerateMediationReportResponse
from openapi_server.models.generate_network_report_request import GenerateNetworkReportRequest
from openapi_server.models.generate_network_report_response import GenerateNetworkReportResponse
from openapi_server.models.list_ad_units_response import ListAdUnitsResponse
from openapi_server.models.list_apps_response import ListAppsResponse
from openapi_server.models.list_publisher_accounts_response import ListPublisherAccountsResponse
from openapi_server.models.publisher_account import PublisherAccount


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_units_list(client):
    """Test case for admob_accounts_ad_units_list

    
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
        path='/v1/{parent}/adUnits'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_apps_list(client):
    """Test case for admob_accounts_apps_list

    
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
        path='/v1/{parent}/apps'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_get(client):
    """Test case for admob_accounts_get

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_list(client):
    """Test case for admob_accounts_list

    
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
        path='/v1/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_mediation_report_generate(client):
    """Test case for admob_accounts_mediation_report_generate

    
    """
    body = {"reportSpec":{"sortConditions":[{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"},{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"}],"dimensionFilters":[{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"},{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"}],"dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"timeZone":"timeZone","localizationSettings":{"languageCode":"languageCode","currencyCode":"currencyCode"},"metrics":["METRIC_UNSPECIFIED","METRIC_UNSPECIFIED"],"maxReportRows":0,"dimensions":["DIMENSION_UNSPECIFIED","DIMENSION_UNSPECIFIED"]}}
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
        path='/v1/{parent}/mediationReport:generate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_network_report_generate(client):
    """Test case for admob_accounts_network_report_generate

    
    """
    body = {"reportSpec":{"sortConditions":[{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"},{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"}],"dimensionFilters":[{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"},{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"}],"dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"timeZone":"timeZone","localizationSettings":{"languageCode":"languageCode","currencyCode":"currencyCode"},"metrics":["METRIC_UNSPECIFIED","METRIC_UNSPECIFIED"],"maxReportRows":0,"dimensions":["DIMENSION_UNSPECIFIED","DIMENSION_UNSPECIFIED"]}}
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
        path='/v1/{parent}/networkReport:generate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

