# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_handpicked_slug_get(client):
    """Test case for handpicked_slug_get

    Get results from a handpicked collection
    """
    params = [('query', 'query_example'),
                    ('auction_price_max', 3.4),
                    ('category', 'category_example'),
                    ('product_type', 'product_type_example'),
                    ('conditions', ['conditions_example']),
                    ('decade', 'decade_example'),
                    ('finish', 'finish_example'),
                    ('handmade', True),
                    ('item_city', 'item_city_example'),
                    ('item_country', 'item_country_example'),
                    ('item_region', 'item_region_example'),
                    ('item_state', 'item_state_example'),
                    ('make', ['make_example']),
                    ('model', 'model_example'),
                    ('must_not', 'must_not_example'),
                    ('price_max', 3.4),
                    ('price_min', 3.4),
                    ('currency', 'currency_example'),
                    ('year_max', 56),
                    ('year_min', 56),
                    ('accepts_gift_cards', True),
                    ('preferred_seller', True),
                    ('shop', 'shop_example'),
                    ('shop_id', 'shop_id_example'),
                    ('listing_type', 'listing_type_example'),
                    ('ships_to', 'ships_to_example'),
                    ('exclude_auctions', True),
                    ('accepts_payment_plans', True),
                    ('watchers_count_min', 56),
                    ('not_ids', ['not_ids_example']),
                    ('local_pickup', True),
                    ('page', 1),
                    ('per_page', 24),
                    ('offset', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/handpicked/{slug}'.format(slug='slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

