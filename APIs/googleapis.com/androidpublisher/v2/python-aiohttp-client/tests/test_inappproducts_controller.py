# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.in_app_product import InAppProduct
from openapi_server.models.inappproducts_list_response import InappproductsListResponse


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_delete(client):
    """Test case for androidpublisher_inappproducts_delete

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v2/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_get(client):
    """Test case for androidpublisher_inappproducts_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_insert(client):
    """Test case for androidpublisher_inappproducts_insert

    
    """
    body = {"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","listings":{"key":{"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","purchaseType":"purchaseType","status":"status"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('autoConvertMissingPrices', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/inappproducts'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_list(client):
    """Test case for androidpublisher_inappproducts_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('startIndex', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/inappproducts'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_patch(client):
    """Test case for androidpublisher_inappproducts_patch

    
    """
    body = {"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","listings":{"key":{"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","purchaseType":"purchaseType","status":"status"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('autoConvertMissingPrices', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v2/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_update(client):
    """Test case for androidpublisher_inappproducts_update

    
    """
    body = {"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","listings":{"key":{"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","purchaseType":"purchaseType","status":"status"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('autoConvertMissingPrices', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v2/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

