# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.datafeed import Datafeed
from openapi_server.models.datafeeds_custom_batch_request import DatafeedsCustomBatchRequest
from openapi_server.models.datafeeds_custom_batch_response import DatafeedsCustomBatchResponse
from openapi_server.models.datafeeds_fetch_now_response import DatafeedsFetchNowResponse
from openapi_server.models.datafeeds_list_response import DatafeedsListResponse


pytestmark = pytest.mark.asyncio

async def test_content_datafeeds_custombatch(client):
    """Test case for content_datafeeds_custombatch

    
    """
    body = {"entries":[{"datafeed":{"fetchSchedule":{"password":"password","paused":True,"hour":1,"dayOfMonth":6,"fetchUrl":"fetchUrl","weekday":"weekday","timeZone":"timeZone","minuteOfHour":5,"username":"username"},"fileName":"fileName","kind":"kind","format":{"fileEncoding":"fileEncoding","quotingMode":"quotingMode","columnDelimiter":"columnDelimiter"},"name":"name","attributeLanguage":"attributeLanguage","id":"id","contentType":"contentType","targets":[{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"},{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"}]},"datafeedId":"datafeedId","method":"method","merchantId":"merchantId","batchId":0},{"datafeed":{"fetchSchedule":{"password":"password","paused":True,"hour":1,"dayOfMonth":6,"fetchUrl":"fetchUrl","weekday":"weekday","timeZone":"timeZone","minuteOfHour":5,"username":"username"},"fileName":"fileName","kind":"kind","format":{"fileEncoding":"fileEncoding","quotingMode":"quotingMode","columnDelimiter":"columnDelimiter"},"name":"name","attributeLanguage":"attributeLanguage","id":"id","contentType":"contentType","targets":[{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"},{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"}]},"datafeedId":"datafeedId","method":"method","merchantId":"merchantId","batchId":0}]}
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
        path='/content/v2.1/datafeeds/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_datafeeds_delete(client):
    """Test case for content_datafeeds_delete

    
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
        path='/content/v2.1/{merchant_id}/datafeeds/{datafeed_id}'.format(merchant_id='merchant_id_example', datafeed_id='datafeed_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_datafeeds_fetchnow(client):
    """Test case for content_datafeeds_fetchnow

    
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
        method='POST',
        path='/content/v2.1/{merchant_id}/datafeeds/{datafeed_id}/fetchNow'.format(merchant_id='merchant_id_example', datafeed_id='datafeed_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_datafeeds_get(client):
    """Test case for content_datafeeds_get

    
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
        path='/content/v2.1/{merchant_id}/datafeeds/{datafeed_id}'.format(merchant_id='merchant_id_example', datafeed_id='datafeed_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_datafeeds_insert(client):
    """Test case for content_datafeeds_insert

    
    """
    body = {"fetchSchedule":{"password":"password","paused":True,"hour":1,"dayOfMonth":6,"fetchUrl":"fetchUrl","weekday":"weekday","timeZone":"timeZone","minuteOfHour":5,"username":"username"},"fileName":"fileName","kind":"kind","format":{"fileEncoding":"fileEncoding","quotingMode":"quotingMode","columnDelimiter":"columnDelimiter"},"name":"name","attributeLanguage":"attributeLanguage","id":"id","contentType":"contentType","targets":[{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"},{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"}]}
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
        path='/content/v2.1/{merchant_id}/datafeeds'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_datafeeds_list(client):
    """Test case for content_datafeeds_list

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/datafeeds'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_datafeeds_update(client):
    """Test case for content_datafeeds_update

    
    """
    body = {"fetchSchedule":{"password":"password","paused":True,"hour":1,"dayOfMonth":6,"fetchUrl":"fetchUrl","weekday":"weekday","timeZone":"timeZone","minuteOfHour":5,"username":"username"},"fileName":"fileName","kind":"kind","format":{"fileEncoding":"fileEncoding","quotingMode":"quotingMode","columnDelimiter":"columnDelimiter"},"name":"name","attributeLanguage":"attributeLanguage","id":"id","contentType":"contentType","targets":[{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"},{"country":"country","includedDestinations":["includedDestinations","includedDestinations"],"excludedDestinations":["excludedDestinations","excludedDestinations"],"feedLabel":"feedLabel","targetCountries":["targetCountries","targetCountries"],"language":"language"}]}
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
        method='PUT',
        path='/content/v2.1/{merchant_id}/datafeeds/{datafeed_id}'.format(merchant_id='merchant_id_example', datafeed_id='datafeed_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

