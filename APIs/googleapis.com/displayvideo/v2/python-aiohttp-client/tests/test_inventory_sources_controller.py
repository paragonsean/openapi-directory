# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_inventory_source_read_write_accessors_request import EditInventorySourceReadWriteAccessorsRequest
from openapi_server.models.inventory_source import InventorySource
from openapi_server.models.inventory_source_accessors import InventorySourceAccessors
from openapi_server.models.list_inventory_sources_response import ListInventorySourcesResponse


pytestmark = pytest.mark.asyncio

async def test_displayvideo_inventory_sources_create(client):
    """Test case for displayvideo_inventory_sources_create

    
    """
    body = {"inventorySourceProductType":"INVENTORY_SOURCE_PRODUCT_TYPE_UNSPECIFIED","readAdvertiserIds":["readAdvertiserIds","readAdvertiserIds"],"inventorySourceId":"inventorySourceId","readWriteAccessors":{"partner":{"partnerId":"partnerId"},"advertisers":{"advertiserIds":["advertiserIds","advertiserIds"]}},"deliveryMethod":"INVENTORY_SOURCE_DELIVERY_METHOD_UNSPECIFIED","dealId":"dealId","displayName":"displayName","creativeConfigs":[{"displayCreativeConfig":{"creativeSize":{"heightPixels":0,"widthPixels":6}},"creativeType":"CREATIVE_TYPE_UNSPECIFIED","videoCreativeConfig":{"duration":"duration"}},{"displayCreativeConfig":{"creativeSize":{"heightPixels":0,"widthPixels":6}},"creativeType":"CREATIVE_TYPE_UNSPECIFIED","videoCreativeConfig":{"duration":"duration"}}],"readPartnerIds":["readPartnerIds","readPartnerIds"],"commitment":"INVENTORY_SOURCE_COMMITMENT_UNSPECIFIED","updateTime":"updateTime","guaranteedOrderId":"guaranteedOrderId","rateDetails":{"minimumSpend":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"rate":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"inventorySourceRateType":"INVENTORY_SOURCE_RATE_TYPE_UNSPECIFIED","unitsPurchased":"unitsPurchased"},"inventorySourceType":"INVENTORY_SOURCE_TYPE_UNSPECIFIED","publisherName":"publisherName","name":"name","exchange":"EXCHANGE_UNSPECIFIED","status":{"entityPauseReason":"entityPauseReason","sellerStatus":"ENTITY_STATUS_UNSPECIFIED","entityStatus":"ENTITY_STATUS_UNSPECIFIED","sellerPauseReason":"sellerPauseReason","configStatus":"INVENTORY_SOURCE_CONFIG_STATUS_UNSPECIFIED"},"timeRange":{"startTime":"startTime","endTime":"endTime"}}
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
        path='/v2/inventorySources',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_inventory_sources_edit_inventory_source_read_write_accessors(client):
    """Test case for displayvideo_inventory_sources_edit_inventory_source_read_write_accessors

    
    """
    body = {"advertisersUpdate":{"addedAdvertisers":["addedAdvertisers","addedAdvertisers"],"removedAdvertisers":["removedAdvertisers","removedAdvertisers"]},"assignPartner":True,"partnerId":"partnerId"}
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
        path='/v2/inventorySources/{inventory_source_idedit_inventory_source_read_write_accessor}'.format(inventory_source_id='inventory_source_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_inventory_sources_get(client):
    """Test case for displayvideo_inventory_sources_get

    
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
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventorySources/{inventory_source_id}'.format(inventory_source_id='inventory_source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_inventory_sources_list(client):
    """Test case for displayvideo_inventory_sources_list

    
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
        path='/v2/inventorySources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_inventory_sources_patch(client):
    """Test case for displayvideo_inventory_sources_patch

    
    """
    body = {"inventorySourceProductType":"INVENTORY_SOURCE_PRODUCT_TYPE_UNSPECIFIED","readAdvertiserIds":["readAdvertiserIds","readAdvertiserIds"],"inventorySourceId":"inventorySourceId","readWriteAccessors":{"partner":{"partnerId":"partnerId"},"advertisers":{"advertiserIds":["advertiserIds","advertiserIds"]}},"deliveryMethod":"INVENTORY_SOURCE_DELIVERY_METHOD_UNSPECIFIED","dealId":"dealId","displayName":"displayName","creativeConfigs":[{"displayCreativeConfig":{"creativeSize":{"heightPixels":0,"widthPixels":6}},"creativeType":"CREATIVE_TYPE_UNSPECIFIED","videoCreativeConfig":{"duration":"duration"}},{"displayCreativeConfig":{"creativeSize":{"heightPixels":0,"widthPixels":6}},"creativeType":"CREATIVE_TYPE_UNSPECIFIED","videoCreativeConfig":{"duration":"duration"}}],"readPartnerIds":["readPartnerIds","readPartnerIds"],"commitment":"INVENTORY_SOURCE_COMMITMENT_UNSPECIFIED","updateTime":"updateTime","guaranteedOrderId":"guaranteedOrderId","rateDetails":{"minimumSpend":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"rate":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"inventorySourceRateType":"INVENTORY_SOURCE_RATE_TYPE_UNSPECIFIED","unitsPurchased":"unitsPurchased"},"inventorySourceType":"INVENTORY_SOURCE_TYPE_UNSPECIFIED","publisherName":"publisherName","name":"name","exchange":"EXCHANGE_UNSPECIFIED","status":{"entityPauseReason":"entityPauseReason","sellerStatus":"ENTITY_STATUS_UNSPECIFIED","entityStatus":"ENTITY_STATUS_UNSPECIFIED","sellerPauseReason":"sellerPauseReason","configStatus":"INVENTORY_SOURCE_CONFIG_STATUS_UNSPECIFIED"},"timeRange":{"startTime":"startTime","endTime":"endTime"}}
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
        path='/v2/inventorySources/{inventory_source_id}'.format(inventory_source_id='inventory_source_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

