# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversion_source import ConversionSource
from openapi_server.models.list_conversion_sources_response import ListConversionSourcesResponse


pytestmark = pytest.mark.asyncio

async def test_content_conversionsources_create(client):
    """Test case for content_conversionsources_create

    
    """
    body = {"expireTime":"expireTime","merchantCenterDestination":{"attributionSettings":{"attributionModel":"ATTRIBUTION_MODEL_UNSPECIFIED","conversionType":[{"includeInReporting":True,"name":"name"},{"includeInReporting":True,"name":"name"}],"attributionLookbackWindowInDays":0},"displayName":"displayName","destinationId":"destinationId","currencyCode":"currencyCode"},"conversionSourceId":"conversionSourceId","googleAnalyticsLink":{"attributionSettings":{"attributionModel":"ATTRIBUTION_MODEL_UNSPECIFIED","conversionType":[{"includeInReporting":True,"name":"name"},{"includeInReporting":True,"name":"name"}],"attributionLookbackWindowInDays":0},"propertyName":"propertyName","propertyId":"propertyId"},"state":"STATE_UNSPECIFIED"}
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
        path='/content/v2.1/{merchant_id}/conversionsources'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_conversionsources_delete(client):
    """Test case for content_conversionsources_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/content/v2.1/{merchant_id}/conversionsources/{conversion_source_id}'.format(merchant_id='merchant_id_example', conversion_source_id='conversion_source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_conversionsources_get(client):
    """Test case for content_conversionsources_get

    
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
        path='/content/v2.1/{merchant_id}/conversionsources/{conversion_source_id}'.format(merchant_id='merchant_id_example', conversion_source_id='conversion_source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_conversionsources_list(client):
    """Test case for content_conversionsources_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/conversionsources'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_conversionsources_patch(client):
    """Test case for content_conversionsources_patch

    
    """
    body = {"expireTime":"expireTime","merchantCenterDestination":{"attributionSettings":{"attributionModel":"ATTRIBUTION_MODEL_UNSPECIFIED","conversionType":[{"includeInReporting":True,"name":"name"},{"includeInReporting":True,"name":"name"}],"attributionLookbackWindowInDays":0},"displayName":"displayName","destinationId":"destinationId","currencyCode":"currencyCode"},"conversionSourceId":"conversionSourceId","googleAnalyticsLink":{"attributionSettings":{"attributionModel":"ATTRIBUTION_MODEL_UNSPECIFIED","conversionType":[{"includeInReporting":True,"name":"name"},{"includeInReporting":True,"name":"name"}],"attributionLookbackWindowInDays":0},"propertyName":"propertyName","propertyId":"propertyId"},"state":"STATE_UNSPECIFIED"}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/content/v2.1/{merchant_id}/conversionsources/{conversion_source_id}'.format(merchant_id='merchant_id_example', conversion_source_id='conversion_source_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_conversionsources_undelete(client):
    """Test case for content_conversionsources_undelete

    
    """
    body = None
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/conversionsources/{conversion_source_idundelet}'.format(merchant_id='merchant_id_example', conversion_source_id='conversion_source_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

