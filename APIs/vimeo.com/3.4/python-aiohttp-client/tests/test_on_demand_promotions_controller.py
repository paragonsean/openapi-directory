# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_vod_promotion_request import CreateVodPromotionRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_promotion import OnDemandPromotion
from openapi_server.models.on_demand_promotion_code import OnDemandPromotionCode


pytestmark = pytest.mark.asyncio

async def test_create_vod_promotion(client):
    """Test case for create_vod_promotion

    Add a promotion to an On Demand page
    """
    body = openapi_server.CreateVodPromotionRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.promotion+json',
        'Content-Type': 'application/vnd.vimeo.ondemand.promotion+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ondemand/pages/{ondemand_id}/promotions'.format(ondemand_id=61326),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vod_promotion(client):
    """Test case for delete_vod_promotion

    Remove a promotion from an On Demand page
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ondemand/pages/{ondemand_id}/promotions/{promotion_id}'.format(ondemand_id=61326, promotion_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_promotion(client):
    """Test case for get_vod_promotion

    Get a specific promotion on an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.promotion+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/promotions/{promotion_id}'.format(ondemand_id=61326, promotion_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_promotion_codes(client):
    """Test case for get_vod_promotion_codes

    Get all the codes of a promotion on an On Demand page
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.promocode+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes'.format(ondemand_id=61326, promotion_id=12345),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_promotions(client):
    """Test case for get_vod_promotions

    Get all the promotions on an On Demand page
    """
    params = [('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.promotion+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/promotions'.format(ondemand_id=61326),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

