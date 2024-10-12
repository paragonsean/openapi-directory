# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.campaign import Campaign
from openapi_server.models.campaign_paged_collection_response import CampaignPagedCollectionResponse
from openapi_server.models.campaigns import Campaigns
from openapi_server.models.clone_campaign_request import CloneCampaignRequest
from openapi_server.models.create_campaign_request import CreateCampaignRequest
from openapi_server.models.targeted_ads_paged_collection import TargetedAdsPagedCollection
from openapi_server.models.update_adrate_strategy_request import UpdateAdrateStrategyRequest
from openapi_server.models.update_campaign_budget_request import UpdateCampaignBudgetRequest
from openapi_server.models.update_campaign_identification_request import UpdateCampaignIdentificationRequest


pytestmark = pytest.mark.asyncio

async def test_clone_campaign(client):
    """Test case for clone_campaign

    
    """
    body = {"endDate":"endDate","fundingStrategy":{"adRateStrategy":"adRateStrategy","dynamicAdRatePreferences":[{"adRateAdjustmentPercent":"adRateAdjustmentPercent","adRateCapPercent":"adRateCapPercent"},{"adRateAdjustmentPercent":"adRateAdjustmentPercent","adRateCapPercent":"adRateCapPercent"}],"fundingModel":"fundingModel","bidPercentage":"bidPercentage"},"campaignName":"campaignName","startDate":"startDate"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/clone'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_campaign(client):
    """Test case for create_campaign

    
    """
    body = {"marketplaceId":"marketplaceId","campaignCriterion":{"criterionType":"criterionType","autoSelectFutureInventory":True,"selectionRules":[{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]},{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]}]},"endDate":"endDate","fundingStrategy":{"adRateStrategy":"adRateStrategy","dynamicAdRatePreferences":[{"adRateAdjustmentPercent":"adRateAdjustmentPercent","adRateCapPercent":"adRateCapPercent"},{"adRateAdjustmentPercent":"adRateAdjustmentPercent","adRateCapPercent":"adRateCapPercent"}],"fundingModel":"fundingModel","bidPercentage":"bidPercentage"},"campaignName":"campaignName","startDate":"startDate","budget":{"daily":{"amount":{"currency":"currency","value":"value"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_campaign(client):
    """Test case for delete_campaign

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}'.format(campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_end_campaign(client):
    """Test case for end_campaign

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/end'.format(campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_campaign_by_ad_reference(client):
    """Test case for find_campaign_by_ad_reference

    
    """
    params = [('inventory_reference_id', 'inventory_reference_id_example'),
                    ('inventory_reference_type', 'inventory_reference_type_example'),
                    ('listing_id', 'listing_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/find_campaign_by_ad_reference',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign(client):
    """Test case for get_campaign

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}'.format(campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_by_name(client):
    """Test case for get_campaign_by_name

    
    """
    params = [('campaign_name', 'campaign_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/get_campaign_by_name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaigns(client):
    """Test case for get_campaigns

    
    """
    params = [('campaign_name', 'campaign_name_example'),
                    ('campaign_status', 'campaign_status_example'),
                    ('end_date_range', 'end_date_range_example'),
                    ('funding_strategy', 'funding_strategy_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('start_date_range', 'start_date_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pause_campaign(client):
    """Test case for pause_campaign

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/pause'.format(campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resume_campaign(client):
    """Test case for resume_campaign

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/resume'.format(campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggest_items(client):
    """Test case for suggest_items

    
    """
    params = [('category_ids', 'category_ids_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/suggest_items'.format(campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ad_rate_strategy(client):
    """Test case for update_ad_rate_strategy

    
    """
    body = {"adRateStrategy":"adRateStrategy","dynamicAdRatePreferences":[{"adRateAdjustmentPercent":"adRateAdjustmentPercent","adRateCapPercent":"adRateCapPercent"},{"adRateAdjustmentPercent":"adRateAdjustmentPercent","adRateCapPercent":"adRateCapPercent"}],"bidPercentage":"bidPercentage"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/update_ad_rate_strategy'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_campaign_budget(client):
    """Test case for update_campaign_budget

    
    """
    body = {"daily":{"amount":{"currency":"currency","value":"value"}}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_budget'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_campaign_identification(client):
    """Test case for update_campaign_identification

    
    """
    body = {"endDate":"endDate","campaignName":"campaignName","startDate":"startDate"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_identification'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

