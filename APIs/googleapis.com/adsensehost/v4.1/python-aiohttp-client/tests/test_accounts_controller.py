# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts import Accounts
from openapi_server.models.ad_client import AdClient
from openapi_server.models.ad_clients import AdClients
from openapi_server.models.ad_code import AdCode
from openapi_server.models.ad_unit import AdUnit
from openapi_server.models.ad_units import AdUnits
from openapi_server.models.report import Report


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adclients_get(client):
    """Test case for adsensehost_accounts_adclients_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}'.format(account_id='account_id_example', ad_client_id='ad_client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adclients_list(client):
    """Test case for adsensehost_accounts_adclients_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adunits_delete(client):
    """Test case for adsensehost_accounts_adunits_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}/adunits/{ad_unit_id}'.format(account_id='account_id_example', ad_client_id='ad_client_id_example', ad_unit_id='ad_unit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adunits_get(client):
    """Test case for adsensehost_accounts_adunits_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}/adunits/{ad_unit_id}'.format(account_id='account_id_example', ad_client_id='ad_client_id_example', ad_unit_id='ad_unit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adunits_get_ad_code(client):
    """Test case for adsensehost_accounts_adunits_get_ad_code

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('hostCustomChannelId', ['host_custom_channel_id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}/adunits/{ad_unit_id}/adcode'.format(account_id='account_id_example', ad_client_id='ad_client_id_example', ad_unit_id='ad_unit_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adunits_insert(client):
    """Test case for adsensehost_accounts_adunits_insert

    
    """
    body = {"code":"code","customStyle":{"corners":"corners","kind":"adsensehost#adStyle","colors":{"border":"border","background":"background","text":"text","title":"title","url":"url"},"font":{"size":"size","family":"family"}},"kind":"adsensehost#adUnit","name":"name","id":"id","mobileContentAdsSettings":{"markupLanguage":"markupLanguage","size":"size","scriptingLanguage":"scriptingLanguage","type":"type"},"contentAdsSettings":{"size":"size","backupOption":{"color":"color","type":"type","url":"url"},"type":"type"},"status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}/adunits'.format(account_id='account_id_example', ad_client_id='ad_client_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adunits_list(client):
    """Test case for adsensehost_accounts_adunits_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('includeInactive', True),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}/adunits'.format(account_id='account_id_example', ad_client_id='ad_client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adunits_patch(client):
    """Test case for adsensehost_accounts_adunits_patch

    
    """
    body = {"code":"code","customStyle":{"corners":"corners","kind":"adsensehost#adStyle","colors":{"border":"border","background":"background","text":"text","title":"title","url":"url"},"font":{"size":"size","family":"family"}},"kind":"adsensehost#adUnit","name":"name","id":"id","mobileContentAdsSettings":{"markupLanguage":"markupLanguage","size":"size","scriptingLanguage":"scriptingLanguage","type":"type"},"contentAdsSettings":{"size":"size","backupOption":{"color":"color","type":"type","url":"url"},"type":"type"},"status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('adUnitId', 'ad_unit_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}/adunits'.format(account_id='account_id_example', ad_client_id='ad_client_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_adunits_update(client):
    """Test case for adsensehost_accounts_adunits_update

    
    """
    body = {"code":"code","customStyle":{"corners":"corners","kind":"adsensehost#adStyle","colors":{"border":"border","background":"background","text":"text","title":"title","url":"url"},"font":{"size":"size","family":"family"}},"kind":"adsensehost#adUnit","name":"name","id":"id","mobileContentAdsSettings":{"markupLanguage":"markupLanguage","size":"size","scriptingLanguage":"scriptingLanguage","type":"type"},"contentAdsSettings":{"size":"size","backupOption":{"color":"color","type":"type","url":"url"},"type":"type"},"status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/adsensehost/v4.1/accounts/{account_id}/adclients/{ad_client_id}/adunits'.format(account_id='account_id_example', ad_client_id='ad_client_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_get(client):
    """Test case for adsensehost_accounts_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_list(client):
    """Test case for adsensehost_accounts_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('filterAdClientId', ['filter_ad_client_id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_accounts_reports_generate(client):
    """Test case for adsensehost_accounts_reports_generate

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('dimension', ['dimension_example']),
                    ('filter', ['filter_example']),
                    ('locale', 'locale_example'),
                    ('maxResults', 56),
                    ('metric', ['metric_example']),
                    ('sort', ['sort_example']),
                    ('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/accounts/{account_id}/reports'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

