# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.items_paged_collection import ItemsPagedCollection
from openapi_server.models.promotions_paged_collection import PromotionsPagedCollection


pytestmark = pytest.mark.asyncio

async def test_get_listing_set(client):
    """Test case for get_listing_set

    
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/promotion/{promotion_id}/get_listing_set'.format(promotion_id='promotion_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_promotions(client):
    """Test case for get_promotions

    
    """
    params = [('limit', 'limit_example'),
                    ('marketplace_id', 'marketplace_id_example'),
                    ('offset', 'offset_example'),
                    ('promotion_status', 'promotion_status_example'),
                    ('promotion_type', 'promotion_type_example'),
                    ('q', 'q_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/promotion',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pause_promotion(client):
    """Test case for pause_promotion

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/promotion/{promotion_id}/pause'.format(promotion_id='promotion_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resume_promotion(client):
    """Test case for resume_promotion

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/promotion/{promotion_id}/resume'.format(promotion_id='promotion_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

