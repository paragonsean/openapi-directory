# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_conversation_id_offer_post_request import ConversationsConversationIdOfferPostRequest
from openapi_server.models.listings_listing_id_conversations_post_request import ListingsListingIdConversationsPostRequest
from openapi_server.models.my_account_put_request import MyAccountPutRequest
from openapi_server.models.my_conversations_id_put_request import MyConversationsIdPutRequest
from openapi_server.models.my_conversations_post_request import MyConversationsPostRequest
from openapi_server.models.my_follows_articles_post_request import MyFollowsArticlesPostRequest
from openapi_server.models.my_follows_search_post_request import MyFollowsSearchPostRequest
from openapi_server.models.my_listings_slug_state_end_put_request import MyListingsSlugStateEndPutRequest
from openapi_server.models.my_negotiations_id_accept_post_request import MyNegotiationsIdAcceptPostRequest
from openapi_server.models.my_orders_selling_id_mark_picked_up_post_request import MyOrdersSellingIdMarkPickedUpPostRequest
from openapi_server.models.my_orders_selling_id_ship_post_request import MyOrdersSellingIdShipPostRequest


pytestmark = pytest.mark.asyncio

async def test_my_account_get(client):
    """Test case for my_account_get

    Get account details
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_account_put(client):
    """Test case for my_account_put

    Update account details
    """
    body = openapi_server.MyAccountPutRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/my/account',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_addresses_address_id_delete(client):
    """Test case for my_addresses_address_id_delete

    Delete an existing address in your address book
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/addresses/{address_id}'.format(address_id='address_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_addresses_address_id_put(client):
    """Test case for my_addresses_address_id_put

    Update an existing address in your address book
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/my/addresses/{address_id}'.format(address_id='address_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_addresses_get(client):
    """Test case for my_addresses_get

    See all addresses in your address book
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/addresses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_addresses_post(client):
    """Test case for my_addresses_post

    Create a new address in your address book
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/addresses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_conversations_conversation_id_messages_post(client):
    """Test case for my_conversations_conversation_id_messages_post

    Send a message
    """
    body = openapi_server.ListingsListingIdConversationsPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/conversations/{conversation_id}/messages'.format(conversation_id='conversation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_conversations_get(client):
    """Test case for my_conversations_get

    Get a list of your conversations
    """
    params = [('search', 'search_example'),
                    ('unread_only', True),
                    ('page', 1),
                    ('per_page', 24),
                    ('offset', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/conversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_conversations_id_get(client):
    """Test case for my_conversations_id_get

    Display conversation details with messages in natural time order (oldest to newest)
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/conversations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_conversations_id_put(client):
    """Test case for my_conversations_id_put

    Mark a conversation read/unread
    """
    body = openapi_server.MyConversationsIdPutRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/my/conversations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_conversations_post(client):
    """Test case for my_conversations_post

    Start a conversation
    """
    body = openapi_server.MyConversationsPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/conversations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_counts_get(client):
    """Test case for my_counts_get

    Get your actionable status counts
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/counts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_curated_set_product_product_id_delete(client):
    """Test case for my_curated_set_product_product_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/curated_set/product/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_curated_set_product_product_id_post(client):
    """Test case for my_curated_set_product_product_id_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/my/curated_set/product/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_feed_customize_get(client):
    """Test case for my_feed_customize_get

    get your feed customization options
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/feed/customize',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_feed_get(client):
    """Test case for my_feed_get

    Get listings from your feed
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/feed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_feed_grid_get(client):
    """Test case for my_feed_grid_get

    get your feed
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/feed/grid',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_feedback_received_get(client):
    """Test case for my_feedback_received_get

    List of received feedback
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/feedback/received',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_feedback_sent_get(client):
    """Test case for my_feedback_sent_get

    List of sent feedback
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/feedback/sent',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_articles_get(client):
    """Test case for my_follows_articles_get

    Returns a user's ArticleCategoryFollows
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/articles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_articles_post(client):
    """Test case for my_follows_articles_post

    Set a user's ArticleCategoryFollows
    """
    body = openapi_server.MyFollowsArticlesPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/articles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_brands_slug_delete(client):
    """Test case for my_follows_brands_slug_delete

    Unfollow a brand
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/brands/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_brands_slug_get(client):
    """Test case for my_follows_brands_slug_get

    Follow status for a brand
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/brands/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_brands_slug_post(client):
    """Test case for my_follows_brands_slug_post

    Follow a brand
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/brands/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_categories_category_subcategory_delete(client):
    """Test case for my_follows_categories_category_subcategory_delete

    Unfollow a subcategory
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/categories/{category}/{subcategory}'.format(category='category_example', subcategory='subcategory_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_categories_category_subcategory_get(client):
    """Test case for my_follows_categories_category_subcategory_get

    Follow status for a subcategory
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/categories/{category}/{subcategory}'.format(category='category_example', subcategory='subcategory_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_categories_category_subcategory_post(client):
    """Test case for my_follows_categories_category_subcategory_post

    Follow a subcategory
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/categories/{category}/{subcategory}'.format(category='category_example', subcategory='subcategory_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_categories_identifier_delete(client):
    """Test case for my_follows_categories_identifier_delete

    Unfollow a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/categories/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_categories_identifier_get(client):
    """Test case for my_follows_categories_identifier_get

    Follow status for a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/categories/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_categories_identifier_post(client):
    """Test case for my_follows_categories_identifier_post

    Follow a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/categories/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_categories_uuid_post(client):
    """Test case for my_follows_categories_uuid_post

    Follow a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/categories/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_collections_slug_delete(client):
    """Test case for my_follows_collections_slug_delete

    Unfollow a collection
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/collections/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_collections_slug_get(client):
    """Test case for my_follows_collections_slug_get

    Follow status for a collection
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/collections/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_collections_slug_post(client):
    """Test case for my_follows_collections_slug_post

    Follow a collection
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/collections/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_follow_id_alert_delete(client):
    """Test case for my_follows_follow_id_alert_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/{follow_id}/alert'.format(follow_id='follow_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_follow_id_alert_post(client):
    """Test case for my_follows_follow_id_alert_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/{follow_id}/alert'.format(follow_id='follow_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_follow_id_delete(client):
    """Test case for my_follows_follow_id_delete

    Delete a follow
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/{follow_id}'.format(follow_id='follow_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_get(client):
    """Test case for my_follows_get

    See what the user is following
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_handpicked_slug_delete(client):
    """Test case for my_follows_handpicked_slug_delete

    Unfollow a handpicked collection
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/handpicked/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_handpicked_slug_get(client):
    """Test case for my_follows_handpicked_slug_get

    Follow status for a handpicked collection
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/handpicked/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_handpicked_slug_post(client):
    """Test case for my_follows_handpicked_slug_post

    Follow a handpicked collection
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/handpicked/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_search_get(client):
    """Test case for my_follows_search_get

    Follow status for a search
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/search',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_search_post(client):
    """Test case for my_follows_search_post

    Follow a search
    """
    body = openapi_server.MyFollowsSearchPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_shops_slug_delete(client):
    """Test case for my_follows_shops_slug_delete

    Unfollow a shop
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/follows/shops/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_shops_slug_get(client):
    """Test case for my_follows_shops_slug_get

    Follow status for a shop
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/follows/shops/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_follows_shops_slug_post(client):
    """Test case for my_follows_shops_slug_post

    Follow a shop
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/follows/shops/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_listings_drafts_get(client):
    """Test case for my_listings_drafts_get

    Retrieve a list your draft listings
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
                    ('local_pickup', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/listings/drafts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_listings_get(client):
    """Test case for my_listings_get

    Retrieve a list of live listings for the seller. To search all listings specify state=all
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
                    ('state', 'live'),
                    ('sku', 'sku_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/listings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_listings_negotiations_get(client):
    """Test case for my_listings_negotiations_get

    Get a list of active negotiations as a seller
    """
    params = [('page', 1),
                    ('per_page', 24),
                    ('offset', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/listings/negotiations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_listings_slug_state_end_put(client):
    """Test case for my_listings_slug_state_end_put

    End a listing
    """
    body = openapi_server.MyListingsSlugStateEndPutRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/my/listings/{slug}/state/end'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_lists_get(client):
    """Test case for my_lists_get

    Get a list of your lists (wishlist, watch list, etc)
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/lists',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_negotiations_buying_get(client):
    """Test case for my_negotiations_buying_get

    Get a list of active negotiations as a buyer
    """
    params = [('page', 1),
                    ('per_page', 24),
                    ('offset', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/negotiations/buying',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_negotiations_id_accept_post(client):
    """Test case for my_negotiations_id_accept_post

    Accept an offer
    """
    body = openapi_server.MyNegotiationsIdAcceptPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/negotiations/{id}/accept'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_negotiations_id_counter_post(client):
    """Test case for my_negotiations_id_counter_post

    Counter an offer
    """
    body = openapi_server.ConversationsConversationIdOfferPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/negotiations/{id}/counter'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_negotiations_id_decline_post(client):
    """Test case for my_negotiations_id_decline_post

    Decline an offer
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/negotiations/{id}/decline'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_negotiations_id_get(client):
    """Test case for my_negotiations_id_get

    Get offer details
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/negotiations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_awaiting_feedback_get(client):
    """Test case for my_orders_awaiting_feedback_get

    List of orders that need feedback
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/awaiting_feedback',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_buying_all_get(client):
    """Test case for my_orders_buying_all_get

    Returns all orders, newest first.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/buying/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_buying_by_uuid_uuid_get(client):
    """Test case for my_orders_buying_by_uuid_uuid_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/buying/by_uuid/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_buying_id_get(client):
    """Test case for my_orders_buying_id_get

    Returns order details for a buyer
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/buying/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_buying_id_mark_received_post(client):
    """Test case for my_orders_buying_id_mark_received_post

    Marks an order as received by the buyer
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/orders/buying/{id}/mark_received'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_buying_unpaid_get(client):
    """Test case for my_orders_buying_unpaid_get

    Returns unpaid orders, newest first.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/buying/unpaid',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_all_get(client):
    """Test case for my_orders_selling_all_get

    Get all seller orders, newest first.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/selling/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_awaiting_shipment_get(client):
    """Test case for my_orders_selling_awaiting_shipment_get

    Get unpaid seller orders, newest first.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/selling/awaiting_shipment',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_buyer_history_buyer_id_get(client):
    """Test case for my_orders_selling_buyer_history_buyer_id_get

    See previous orders from buyer
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/selling/buyer_history/{buyer_id}'.format(buyer_id='buyer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_by_uuid_uuid_get(client):
    """Test case for my_orders_selling_by_uuid_uuid_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/selling/by_uuid/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_id_get(client):
    """Test case for my_orders_selling_id_get

    Returns order details for a seller
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/selling/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_id_mark_picked_up_post(client):
    """Test case for my_orders_selling_id_mark_picked_up_post

    Marks an order as picked up
    """
    body = openapi_server.MyOrdersSellingIdMarkPickedUpPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/orders/selling/{id}/mark_picked_up'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_id_ship_post(client):
    """Test case for my_orders_selling_id_ship_post

    Marks an order as shipped
    """
    body = openapi_server.MyOrdersSellingIdShipPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/orders/selling/{id}/ship'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_order_id_refund_requests_post(client):
    """Test case for my_orders_selling_order_id_refund_requests_post

    Initiate a refund for a sold order
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/my/orders/selling/{order_id}/refund_requests'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_orders_selling_unpaid_get(client):
    """Test case for my_orders_selling_unpaid_get

    Get unpaid seller orders, newest first.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/orders/selling/unpaid',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_payments_selling_get(client):
    """Test case for my_payments_selling_get

    Get payments
    """
    params = [('page', 1),
                    ('per_page', 24),
                    ('offset', 56),
                    ('created_start_date', 'created_start_date_example'),
                    ('created_end_date', 'created_end_date_example'),
                    ('updated_start_date', 'updated_start_date_example'),
                    ('updated_end_date', 'updated_end_date_example'),
                    ('order_id', 'order_id_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/payments/selling',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_payments_selling_id_get(client):
    """Test case for my_payments_selling_id_get

    Get payment
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/payments/selling/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_payouts_get(client):
    """Test case for my_payouts_get

    Get a list of payouts
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/payouts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_payouts_id_line_items_get(client):
    """Test case for my_payouts_id_line_items_get

    Read the line items of a payout
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/payouts/{id}/line_items'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_refund_requests_selling_get(client):
    """Test case for my_refund_requests_selling_get

    Get a list of refund requests as a seller
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/refund_requests/selling',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_refund_requests_selling_id_put(client):
    """Test case for my_refund_requests_selling_id_put

    Update a refund request for a sold order
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/my/refund_requests/selling/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_viewed_listings_get(client):
    """Test case for my_viewed_listings_get

    Get a list of your recently viewed listings.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/viewed_listings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_wishlist_get(client):
    """Test case for my_wishlist_get

    Get a list of wishlisted items
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/my/wishlist',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_wishlist_id_delete(client):
    """Test case for my_wishlist_id_delete

    Remove a listing from your wishlist
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/my/wishlist/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_wishlist_id_put(client):
    """Test case for my_wishlist_id_put

    Add a listing to your wishlist
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/my/wishlist/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

