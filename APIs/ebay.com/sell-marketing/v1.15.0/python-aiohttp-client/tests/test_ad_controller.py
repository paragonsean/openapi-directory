# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ad import Ad
from openapi_server.models.ad_ids import AdIds
from openapi_server.models.ad_paged_collection_response import AdPagedCollectionResponse
from openapi_server.models.ad_references import AdReferences
from openapi_server.models.ads import Ads
from openapi_server.models.bulk_ad_response import BulkAdResponse
from openapi_server.models.bulk_ad_update_response import BulkAdUpdateResponse
from openapi_server.models.bulk_ad_update_status_by_listing_id_response import BulkAdUpdateStatusByListingIdResponse
from openapi_server.models.bulk_ad_update_status_response import BulkAdUpdateStatusResponse
from openapi_server.models.bulk_create_ad_request import BulkCreateAdRequest
from openapi_server.models.bulk_create_ads_by_inventory_reference_request import BulkCreateAdsByInventoryReferenceRequest
from openapi_server.models.bulk_create_ads_by_inventory_reference_response import BulkCreateAdsByInventoryReferenceResponse
from openapi_server.models.bulk_delete_ad_request import BulkDeleteAdRequest
from openapi_server.models.bulk_delete_ad_response import BulkDeleteAdResponse
from openapi_server.models.bulk_delete_ads_by_inventory_reference_request import BulkDeleteAdsByInventoryReferenceRequest
from openapi_server.models.bulk_delete_ads_by_inventory_reference_response import BulkDeleteAdsByInventoryReferenceResponse
from openapi_server.models.bulk_update_ad_status_by_listing_id_request import BulkUpdateAdStatusByListingIdRequest
from openapi_server.models.bulk_update_ad_status_request import BulkUpdateAdStatusRequest
from openapi_server.models.bulk_update_ads_by_inventory_reference_response import BulkUpdateAdsByInventoryReferenceResponse
from openapi_server.models.create_ad_request import CreateAdRequest
from openapi_server.models.create_ads_by_inventory_reference_request import CreateAdsByInventoryReferenceRequest
from openapi_server.models.delete_ads_by_inventory_reference_request import DeleteAdsByInventoryReferenceRequest
from openapi_server.models.update_bid_percentage_request import UpdateBidPercentageRequest


pytestmark = pytest.mark.asyncio

async def test_bulk_create_ads_by_inventory_reference(client):
    """Test case for bulk_create_ads_by_inventory_reference

    
    """
    body = {"requests":[{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType","bidPercentage":"bidPercentage","adGroupId":"adGroupId"},{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType","bidPercentage":"bidPercentage","adGroupId":"adGroupId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_create_ads_by_listing_id(client):
    """Test case for bulk_create_ads_by_listing_id

    
    """
    body = {"requests":[{"listingId":"listingId","bidPercentage":"bidPercentage","adGroupId":"adGroupId"},{"listingId":"listingId","bidPercentage":"bidPercentage","adGroupId":"adGroupId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_ads_by_inventory_reference(client):
    """Test case for bulk_delete_ads_by_inventory_reference

    
    """
    body = {"requests":[{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType"},{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_ads_by_listing_id(client):
    """Test case for bulk_delete_ads_by_listing_id

    
    """
    body = {"requests":[{"listingId":"listingId"},{"listingId":"listingId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_ads_bid_by_inventory_reference(client):
    """Test case for bulk_update_ads_bid_by_inventory_reference

    
    """
    body = {"requests":[{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType","bidPercentage":"bidPercentage","adGroupId":"adGroupId"},{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType","bidPercentage":"bidPercentage","adGroupId":"adGroupId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_ads_bid_by_listing_id(client):
    """Test case for bulk_update_ads_bid_by_listing_id

    
    """
    body = {"requests":[{"listingId":"listingId","bidPercentage":"bidPercentage","adGroupId":"adGroupId"},{"listingId":"listingId","bidPercentage":"bidPercentage","adGroupId":"adGroupId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_ads_status(client):
    """Test case for bulk_update_ads_status

    
    """
    body = {"requests":[{"adId":"adId","adStatus":"adStatus"},{"adId":"adId","adStatus":"adStatus"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_ads_status_by_listing_id(client):
    """Test case for bulk_update_ads_status_by_listing_id

    
    """
    body = {"requests":[{"adStatus":"adStatus","listingId":"listingId","adGroupId":"adGroupId"},{"adStatus":"adStatus","listingId":"listingId","adGroupId":"adGroupId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_ad_by_listing_id(client):
    """Test case for create_ad_by_listing_id

    
    """
    body = {"listingId":"listingId","bidPercentage":"bidPercentage","adGroupId":"adGroupId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_ads_by_inventory_reference(client):
    """Test case for create_ads_by_inventory_reference

    
    """
    body = {"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType","bidPercentage":"bidPercentage","adGroupId":"adGroupId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/create_ads_by_inventory_reference'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ad(client):
    """Test case for delete_ad

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}'.format(ad_id='ad_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ads_by_inventory_reference(client):
    """Test case for delete_ads_by_inventory_reference

    
    """
    body = {"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/delete_ads_by_inventory_reference'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ad(client):
    """Test case for get_ad

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}'.format(ad_id='ad_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ads(client):
    """Test case for get_ads

    
    """
    params = [('ad_group_ids', 'ad_group_ids_example'),
                    ('ad_status', 'ad_status_example'),
                    ('limit', 'limit_example'),
                    ('listing_ids', 'listing_ids_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad'.format(campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ads_by_inventory_reference(client):
    """Test case for get_ads_by_inventory_reference

    
    """
    params = [('inventory_reference_id', 'inventory_reference_id_example'),
                    ('inventory_reference_type', 'inventory_reference_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/get_ads_by_inventory_reference'.format(campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_bid(client):
    """Test case for update_bid

    
    """
    body = {"bidPercentage":"bidPercentage"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid'.format(ad_id='ad_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

