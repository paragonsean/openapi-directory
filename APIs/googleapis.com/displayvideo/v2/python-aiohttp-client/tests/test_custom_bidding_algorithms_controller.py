# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_bidding_algorithm import CustomBiddingAlgorithm
from openapi_server.models.custom_bidding_script import CustomBiddingScript
from openapi_server.models.custom_bidding_script_ref import CustomBiddingScriptRef
from openapi_server.models.list_custom_bidding_algorithms_response import ListCustomBiddingAlgorithmsResponse
from openapi_server.models.list_custom_bidding_scripts_response import ListCustomBiddingScriptsResponse


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_create(client):
    """Test case for displayvideo_custom_bidding_algorithms_create

    
    """
    body = {"customBiddingAlgorithmId":"customBiddingAlgorithmId","customBiddingAlgorithmType":"CUSTOM_BIDDING_ALGORITHM_TYPE_UNSPECIFIED","modelDetails":[{"suspensionState":"SUSPENSION_STATE_UNSPECIFIED","readinessState":"READINESS_STATE_UNSPECIFIED","advertiserId":"advertiserId"},{"suspensionState":"SUSPENSION_STATE_UNSPECIFIED","readinessState":"READINESS_STATE_UNSPECIFIED","advertiserId":"advertiserId"}],"entityStatus":"ENTITY_STATUS_UNSPECIFIED","displayName":"displayName","name":"name","sharedAdvertiserIds":["sharedAdvertiserIds","sharedAdvertiserIds"],"partnerId":"partnerId","advertiserId":"advertiserId"}
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
        path='/v2/customBiddingAlgorithms',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_get(client):
    """Test case for displayvideo_custom_bidding_algorithms_get

    
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customBiddingAlgorithms/{custom_bidding_algorithm_id}'.format(custom_bidding_algorithm_id='custom_bidding_algorithm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_list(client):
    """Test case for displayvideo_custom_bidding_algorithms_list

    
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customBiddingAlgorithms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_patch(client):
    """Test case for displayvideo_custom_bidding_algorithms_patch

    
    """
    body = {"customBiddingAlgorithmId":"customBiddingAlgorithmId","customBiddingAlgorithmType":"CUSTOM_BIDDING_ALGORITHM_TYPE_UNSPECIFIED","modelDetails":[{"suspensionState":"SUSPENSION_STATE_UNSPECIFIED","readinessState":"READINESS_STATE_UNSPECIFIED","advertiserId":"advertiserId"},{"suspensionState":"SUSPENSION_STATE_UNSPECIFIED","readinessState":"READINESS_STATE_UNSPECIFIED","advertiserId":"advertiserId"}],"entityStatus":"ENTITY_STATUS_UNSPECIFIED","displayName":"displayName","name":"name","sharedAdvertiserIds":["sharedAdvertiserIds","sharedAdvertiserIds"],"partnerId":"partnerId","advertiserId":"advertiserId"}
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
        path='/v2/customBiddingAlgorithms/{custom_bidding_algorithm_id}'.format(custom_bidding_algorithm_id='custom_bidding_algorithm_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_scripts_create(client):
    """Test case for displayvideo_custom_bidding_algorithms_scripts_create

    
    """
    body = {"customBiddingAlgorithmId":"customBiddingAlgorithmId","createTime":"createTime","customBiddingScriptId":"customBiddingScriptId","name":"name","active":True,"state":"STATE_UNSPECIFIED","errors":[{"line":"line","column":"column","errorMessage":"errorMessage","errorCode":"ERROR_CODE_UNSPECIFIED"},{"line":"line","column":"column","errorMessage":"errorMessage","errorCode":"ERROR_CODE_UNSPECIFIED"}],"script":{"resourceName":"resourceName"}}
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/customBiddingAlgorithms/{custom_bidding_algorithm_id}/scripts'.format(custom_bidding_algorithm_id='custom_bidding_algorithm_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_scripts_get(client):
    """Test case for displayvideo_custom_bidding_algorithms_scripts_get

    
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customBiddingAlgorithms/{custom_bidding_algorithm_id}/scripts/{custom_bidding_script_id}'.format(custom_bidding_algorithm_id='custom_bidding_algorithm_id_example', custom_bidding_script_id='custom_bidding_script_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_scripts_list(client):
    """Test case for displayvideo_custom_bidding_algorithms_scripts_list

    
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customBiddingAlgorithms/{custom_bidding_algorithm_id}/scripts'.format(custom_bidding_algorithm_id='custom_bidding_algorithm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_custom_bidding_algorithms_upload_script(client):
    """Test case for displayvideo_custom_bidding_algorithms_upload_script

    
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customBiddingAlgorithms/{custom_bidding_algorithm_idupload_scrip}'.format(custom_bidding_algorithm_id='custom_bidding_algorithm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

