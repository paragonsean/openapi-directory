# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_guaranteed_order_read_accessors_request import EditGuaranteedOrderReadAccessorsRequest
from openapi_server.models.edit_guaranteed_order_read_accessors_response import EditGuaranteedOrderReadAccessorsResponse
from openapi_server.models.guaranteed_order import GuaranteedOrder
from openapi_server.models.list_guaranteed_orders_response import ListGuaranteedOrdersResponse


pytestmark = pytest.mark.asyncio

async def test_displayvideo_guaranteed_orders_create(client):
    """Test case for displayvideo_guaranteed_orders_create

    
    """
    body = {"readAdvertiserIds":["readAdvertiserIds","readAdvertiserIds"],"displayName":"displayName","legacyGuaranteedOrderId":"legacyGuaranteedOrderId","readWritePartnerId":"readWritePartnerId","updateTime":"updateTime","guaranteedOrderId":"guaranteedOrderId","publisherName":"publisherName","name":"name","exchange":"EXCHANGE_UNSPECIFIED","readAccessInherited":True,"readWriteAdvertiserId":"readWriteAdvertiserId","defaultAdvertiserId":"defaultAdvertiserId","defaultCampaignId":"defaultCampaignId","status":{"entityPauseReason":"entityPauseReason","entityStatus":"ENTITY_STATUS_UNSPECIFIED","configStatus":"GUARANTEED_ORDER_CONFIG_STATUS_UNSPECIFIED"}}
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
        path='/v2/guaranteedOrders',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_guaranteed_orders_edit_guaranteed_order_read_accessors(client):
    """Test case for displayvideo_guaranteed_orders_edit_guaranteed_order_read_accessors

    
    """
    body = {"addedAdvertisers":["addedAdvertisers","addedAdvertisers"],"readAccessInherited":True,"partnerId":"partnerId","removedAdvertisers":["removedAdvertisers","removedAdvertisers"]}
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
        path='/v2/guaranteedOrders/{guaranteed_order_idedit_guaranteed_order_read_accessor}'.format(guaranteed_order_id='guaranteed_order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_guaranteed_orders_get(client):
    """Test case for displayvideo_guaranteed_orders_get

    
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
        path='/v2/guaranteedOrders/{guaranteed_order_id}'.format(guaranteed_order_id='guaranteed_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_guaranteed_orders_list(client):
    """Test case for displayvideo_guaranteed_orders_list

    
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
        path='/v2/guaranteedOrders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_guaranteed_orders_patch(client):
    """Test case for displayvideo_guaranteed_orders_patch

    
    """
    body = {"readAdvertiserIds":["readAdvertiserIds","readAdvertiserIds"],"displayName":"displayName","legacyGuaranteedOrderId":"legacyGuaranteedOrderId","readWritePartnerId":"readWritePartnerId","updateTime":"updateTime","guaranteedOrderId":"guaranteedOrderId","publisherName":"publisherName","name":"name","exchange":"EXCHANGE_UNSPECIFIED","readAccessInherited":True,"readWriteAdvertiserId":"readWriteAdvertiserId","defaultAdvertiserId":"defaultAdvertiserId","defaultCampaignId":"defaultCampaignId","status":{"entityPauseReason":"entityPauseReason","entityStatus":"ENTITY_STATUS_UNSPECIFIED","configStatus":"GUARANTEED_ORDER_CONFIG_STATUS_UNSPECIFIED"}}
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
                    ('partnerId', 'partner_id_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/guaranteedOrders/{guaranteed_order_id}'.format(guaranteed_order_id='guaranteed_order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

