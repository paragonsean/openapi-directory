# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_id_offer_post_request import ConversationsIdOfferPostRequest
from openapi_server.models.listings_listing_id_conversations_post_request import ListingsListingIdConversationsPostRequest
from openapi_server.models.listings_post_request import ListingsPostRequest
from openapi_server.models.listings_slug_flag_post_request import ListingsSlugFlagPostRequest


pytestmark = pytest.mark.asyncio

async def test_listings_all_get(client):
    """Test case for listings_all_get

    All listings including used, handmade, and brand new
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
        path='/api/listings/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_facets_seller_location_get(client):
    """Test case for listings_facets_seller_location_get

    Individual facets
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/listings/facets/seller_location',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_get(client):
    """Test case for listings_get

    Default search of listings includes only used & handmade. Add a filter to view all listings or use the /listings/all endpoint.
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
        path='/api/listings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_id_negotiation_get(client):
    """Test case for listings_id_negotiation_get

    Returns the latest negotiation for the requesting user given a listing id
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{id}/negotiation'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_id_offer_post(client):
    """Test case for listings_id_offer_post

    Make an offer to the seller of a listing
    """
    body = openapi_server.ConversationsIdOfferPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/listings/{id}/offer'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_listing_id_bump_budget_type_post(client):
    """Test case for listings_listing_id_bump_budget_type_post

    Bump a listing
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/listings/{listing_id}/bump/{budget_type}'.format(listing_id='listing_id_example', budget_type='budget_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_listing_id_bump_get(client):
    """Test case for listings_listing_id_bump_get

    View available bump tiers and stats for a listing
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{listing_id}/bump'.format(listing_id='listing_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_listing_id_conversations_post(client):
    """Test case for listings_listing_id_conversations_post

    Start a conversation with a seller
    """
    body = openapi_server.ListingsListingIdConversationsPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/listings/{listing_id}/conversations'.format(listing_id='listing_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_listing_id_images_get(client):
    """Test case for listings_listing_id_images_get

    View the images associated with a particular listing
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{listing_id}/images'.format(listing_id='listing_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_listing_id_images_image_id_delete(client):
    """Test case for listings_listing_id_images_image_id_delete

    Delete an image from a listing
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/listings/{listing_id}/images/{image_id}'.format(listing_id='listing_id_example', image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_listing_id_sales_get(client):
    """Test case for listings_listing_id_sales_get

    See all sales that include a listing.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{listing_id}/sales'.format(listing_id='listing_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_post(client):
    """Test case for listings_post

    Create a listing
    """
    body = openapi_server.ListingsPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/listings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_delete(client):
    """Test case for listings_slug_delete

    Delete a draft listing. Cannot be used on non-drafts.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/listings/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_edit_get(client):
    """Test case for listings_slug_edit_get

    Edit listing.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{slug}/edit'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_flag_post(client):
    """Test case for listings_slug_flag_post

    Flag a listing for inappropriate content or fraud
    """
    body = openapi_server.ListingsSlugFlagPostRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/listings/{slug}/flag'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_get(client):
    """Test case for listings_slug_get

    Listing details
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_put(client):
    """Test case for listings_slug_put

    Update a listing
    """
    body = openapi_server.ListingsPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/listings/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_reviews_get(client):
    """Test case for listings_slug_reviews_get

    View reviews of a listing
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{slug}/reviews'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_reviews_post(client):
    """Test case for listings_slug_reviews_post

    Create a review for a listing
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/listings/{slug}/reviews'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_slug_similar_listings_get(client):
    """Test case for listings_slug_similar_listings_get

    Listing details
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/listings/{slug}/similar_listings'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

