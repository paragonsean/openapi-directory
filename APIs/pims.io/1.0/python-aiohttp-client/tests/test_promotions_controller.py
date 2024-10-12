# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.promotions_entity import PromotionsEntity


pytestmark = pytest.mark.asyncio

async def test_fetch_all_events_promotions(client):
    """Test case for fetch_all_events_promotions

    Find all promotions for one event
    """
    params = [('label', 'label_example'),
                    ('from_date', '2013-10-20'),
                    ('to_date', '2013-10-20'),
                    ('type', 'type_example'),
                    ('family', 'family_example'),
                    ('sort', date),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/promotions'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_all_promotions(client):
    """Test case for fetch_all_promotions

    Find all promotions
    """
    params = [('label', 'label_example'),
                    ('from_date', '2013-10-20'),
                    ('to_date', '2013-10-20'),
                    ('type', 'type_example'),
                    ('family', 'family_example'),
                    ('sort', date),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/promotions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_all_series_promotions(client):
    """Test case for fetch_all_series_promotions

    Find all promotions for one series
    """
    params = [('label', 'label_example'),
                    ('from_date', '2013-10-20'),
                    ('to_date', '2013-10-20'),
                    ('type', 'type_example'),
                    ('family', 'family_example'),
                    ('sort', date),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/series/{series_id}/promotions'.format(series_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_promotion(client):
    """Test case for fetch_one_promotion

    Get one promotion by ID
    """
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/promotions/{promotion_id}'.format(promotion_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

