from typing import List, Dict
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
from openapi_server import util


async def my_account_get(request: web.Request, ) -> web.Response:
    """Get account details

    Get account details


    """
    return web.Response(status=200)


async def my_account_put(request: web.Request, body=None) -> web.Response:
    """Update account details

    Update account details

    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyAccountPutRequest.from_dict(body)
    return web.Response(status=200)


async def my_addresses_address_id_delete(request: web.Request, address_id) -> web.Response:
    """Delete an existing address in your address book

    Delete an existing address in your address book

    :param address_id: 
    :type address_id: str

    """
    return web.Response(status=200)


async def my_addresses_address_id_put(request: web.Request, address_id) -> web.Response:
    """Update an existing address in your address book

    Update an existing address in your address book

    :param address_id: 
    :type address_id: str

    """
    return web.Response(status=200)


async def my_addresses_get(request: web.Request, ) -> web.Response:
    """See all addresses in your address book

    See all addresses in your address book


    """
    return web.Response(status=200)


async def my_addresses_post(request: web.Request, ) -> web.Response:
    """Create a new address in your address book

    Create a new address in your address book


    """
    return web.Response(status=200)


async def my_conversations_conversation_id_messages_post(request: web.Request, conversation_id, body=None) -> web.Response:
    """Send a message

    Send a message

    :param conversation_id: 
    :type conversation_id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ListingsListingIdConversationsPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_conversations_get(request: web.Request, search=None, unread_only=None, page=None, per_page=None, offset=None) -> web.Response:
    """Get a list of your conversations

    Get a list of your conversations

    :param search: Query string to search conversations by
    :type search: str
    :param unread_only: Show unread conversations only
    :type unread_only: bool
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def my_conversations_id_get(request: web.Request, id) -> web.Response:
    """Display conversation details with messages in natural time order (oldest to newest)

    Display conversation details with messages in natural time order (oldest to newest)

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_conversations_id_put(request: web.Request, id, body=None) -> web.Response:
    """Mark a conversation read/unread

    Mark a conversation read/unread

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyConversationsIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def my_conversations_post(request: web.Request, body=None) -> web.Response:
    """Start a conversation

    Start a conversation

    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyConversationsPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_counts_get(request: web.Request, ) -> web.Response:
    """Get your actionable status counts

    Get your actionable status counts


    """
    return web.Response(status=200)


async def my_curated_set_product_product_id_delete(request: web.Request, product_id) -> web.Response:
    """my_curated_set_product_product_id_delete

    

    :param product_id: 
    :type product_id: str

    """
    return web.Response(status=200)


async def my_curated_set_product_product_id_post(request: web.Request, product_id) -> web.Response:
    """my_curated_set_product_product_id_post

    

    :param product_id: 
    :type product_id: str

    """
    return web.Response(status=200)


async def my_feed_customize_get(request: web.Request, ) -> web.Response:
    """get your feed customization options

    get your feed customization options


    """
    return web.Response(status=200)


async def my_feed_get(request: web.Request, ) -> web.Response:
    """Get listings from your feed

    Get listings from your feed


    """
    return web.Response(status=200)


async def my_feed_grid_get(request: web.Request, ) -> web.Response:
    """get your feed

    get your feed


    """
    return web.Response(status=200)


async def my_feedback_received_get(request: web.Request, ) -> web.Response:
    """List of received feedback

    List of received feedback


    """
    return web.Response(status=200)


async def my_feedback_sent_get(request: web.Request, ) -> web.Response:
    """List of sent feedback

    List of sent feedback


    """
    return web.Response(status=200)


async def my_follows_articles_get(request: web.Request, ) -> web.Response:
    """Returns a user&#39;s ArticleCategoryFollows

    Returns a user&#39;s ArticleCategoryFollows


    """
    return web.Response(status=200)


async def my_follows_articles_post(request: web.Request, body=None) -> web.Response:
    """Set a user&#39;s ArticleCategoryFollows

    Set a user&#39;s ArticleCategoryFollows

    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyFollowsArticlesPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_follows_brands_slug_delete(request: web.Request, slug) -> web.Response:
    """Unfollow a brand

    Unfollow a brand

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_brands_slug_get(request: web.Request, slug) -> web.Response:
    """Follow status for a brand

    Follow status for a brand

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_brands_slug_post(request: web.Request, slug) -> web.Response:
    """Follow a brand

    Follow a brand

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_categories_category_subcategory_delete(request: web.Request, category, subcategory) -> web.Response:
    """Unfollow a subcategory

    Unfollow a subcategory

    :param category: 
    :type category: str
    :param subcategory: 
    :type subcategory: str

    """
    return web.Response(status=200)


async def my_follows_categories_category_subcategory_get(request: web.Request, category, subcategory) -> web.Response:
    """Follow status for a subcategory

    Follow status for a subcategory

    :param category: 
    :type category: str
    :param subcategory: 
    :type subcategory: str

    """
    return web.Response(status=200)


async def my_follows_categories_category_subcategory_post(request: web.Request, category, subcategory) -> web.Response:
    """Follow a subcategory

    Follow a subcategory

    :param category: 
    :type category: str
    :param subcategory: 
    :type subcategory: str

    """
    return web.Response(status=200)


async def my_follows_categories_identifier_delete(request: web.Request, identifier) -> web.Response:
    """Unfollow a category

    Unfollow a category

    :param identifier: 
    :type identifier: str

    """
    return web.Response(status=200)


async def my_follows_categories_identifier_get(request: web.Request, identifier) -> web.Response:
    """Follow status for a category

    Follow status for a category

    :param identifier: 
    :type identifier: str

    """
    return web.Response(status=200)


async def my_follows_categories_identifier_post(request: web.Request, identifier) -> web.Response:
    """Follow a category

    Follow a category

    :param identifier: 
    :type identifier: str

    """
    return web.Response(status=200)


async def my_follows_categories_uuid_post(request: web.Request, uuid) -> web.Response:
    """Follow a category

    Follow a category

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def my_follows_collections_slug_delete(request: web.Request, slug) -> web.Response:
    """Unfollow a collection

    Unfollow a collection

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_collections_slug_get(request: web.Request, slug) -> web.Response:
    """Follow status for a collection

    Follow status for a collection

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_collections_slug_post(request: web.Request, slug) -> web.Response:
    """Follow a collection

    Follow a collection

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_follow_id_alert_delete(request: web.Request, follow_id) -> web.Response:
    """my_follows_follow_id_alert_delete

    

    :param follow_id: 
    :type follow_id: str

    """
    return web.Response(status=200)


async def my_follows_follow_id_alert_post(request: web.Request, follow_id) -> web.Response:
    """my_follows_follow_id_alert_post

    

    :param follow_id: 
    :type follow_id: str

    """
    return web.Response(status=200)


async def my_follows_follow_id_delete(request: web.Request, follow_id) -> web.Response:
    """Delete a follow

    Delete a follow

    :param follow_id: 
    :type follow_id: str

    """
    return web.Response(status=200)


async def my_follows_get(request: web.Request, ) -> web.Response:
    """See what the user is following

    See what the user is following


    """
    return web.Response(status=200)


async def my_follows_handpicked_slug_delete(request: web.Request, slug) -> web.Response:
    """Unfollow a handpicked collection

    Unfollow a handpicked collection

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_handpicked_slug_get(request: web.Request, slug) -> web.Response:
    """Follow status for a handpicked collection

    Follow status for a handpicked collection

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_handpicked_slug_post(request: web.Request, slug) -> web.Response:
    """Follow a handpicked collection

    Follow a handpicked collection

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_search_get(request: web.Request, ) -> web.Response:
    """Follow status for a search

    Follow status for a search


    """
    return web.Response(status=200)


async def my_follows_search_post(request: web.Request, body=None) -> web.Response:
    """Follow a search

    Follow a search

    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyFollowsSearchPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_follows_shops_slug_delete(request: web.Request, slug) -> web.Response:
    """Unfollow a shop

    Unfollow a shop

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_shops_slug_get(request: web.Request, slug) -> web.Response:
    """Follow status for a shop

    Follow status for a shop

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_follows_shops_slug_post(request: web.Request, slug) -> web.Response:
    """Follow a shop

    Follow a shop

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def my_listings_drafts_get(request: web.Request, query=None, auction_price_max=None, category=None, product_type=None, conditions=None, decade=None, finish=None, handmade=None, item_city=None, item_country=None, item_region=None, item_state=None, make=None, model=None, must_not=None, price_max=None, price_min=None, currency=None, year_max=None, year_min=None, accepts_gift_cards=None, preferred_seller=None, shop=None, shop_id=None, listing_type=None, ships_to=None, exclude_auctions=None, accepts_payment_plans=None, watchers_count_min=None, not_ids=None, local_pickup=None) -> web.Response:
    """Retrieve a list your draft listings

    Retrieve a list your draft listings

    :param query: Search query.
    :type query: str
    :param auction_price_max: Maximum current auction price
    :type auction_price_max: float
    :param category: Category slug from /api/categories
    :type category: str
    :param product_type: Product type slug from /api/categories
    :type product_type: str
    :param conditions: Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    :type conditions: List[str]
    :param decade: Decade: e.g. 1970s, early 70s
    :type decade: str
    :param finish: Visual finish of the item, common for guitars
    :type finish: str
    :param handmade: Handmade items only
    :type handmade: bool
    :param item_city: City where item is located
    :type item_city: str
    :param item_country: DEPRECATED - Country code where item is located
    :type item_country: str
    :param item_region: Country code where item is located
    :type item_region: str
    :param item_state: State or region code where item is located
    :type item_state: str
    :param make: Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    :type make: List[str]
    :param model: Model of item (e.g. Stratocaster)
    :type model: str
    :param must_not: Search term negation. If you want to exclude a term, add it here
    :type must_not: str
    :param price_max: Maximum price of search results (USD)
    :type price_max: float
    :param price_min: Minimum price of search results (USD)
    :type price_min: float
    :param currency: The currency to be used for the price filters
    :type currency: str
    :param year_max: Maximum year of manufacture
    :type year_max: int
    :param year_min: Minumum year of manufacture
    :type year_min: int
    :param accepts_gift_cards: If true, include only items that accept gift cards
    :type accepts_gift_cards: bool
    :param preferred_seller: If true, include only items by Reverb Preferred Sellers
    :type preferred_seller: bool
    :param shop: Slug of shop to search
    :type shop: str
    :param shop_id: ID of shop to search
    :type shop_id: str
    :param listing_type: Type of listing: auctions,offers
    :type listing_type: str
    :param ships_to: Limit search to items that ship to this country code
    :type ships_to: str
    :param exclude_auctions: If true, exclude auctions
    :type exclude_auctions: bool
    :param accepts_payment_plans: If true, only show items that can be purchased with a payment plan
    :type accepts_payment_plans: bool
    :param watchers_count_min: Minimum number of watchers (used to find popular items)
    :type watchers_count_min: int
    :param not_ids: Listing ID negation. If you want to exclude a listing, add it here.
    :type not_ids: List[str]
    :param local_pickup: Only items that offer local pickup
    :type local_pickup: bool

    """
    return web.Response(status=200)


async def my_listings_get(request: web.Request, query=None, auction_price_max=None, category=None, product_type=None, conditions=None, decade=None, finish=None, handmade=None, item_city=None, item_country=None, item_region=None, item_state=None, make=None, model=None, must_not=None, price_max=None, price_min=None, currency=None, year_max=None, year_min=None, accepts_gift_cards=None, preferred_seller=None, shop=None, shop_id=None, listing_type=None, ships_to=None, exclude_auctions=None, accepts_payment_plans=None, watchers_count_min=None, not_ids=None, local_pickup=None, state=None, sku=None) -> web.Response:
    """Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all

    Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all

    :param query: Search query.
    :type query: str
    :param auction_price_max: Maximum current auction price
    :type auction_price_max: float
    :param category: Category slug from /api/categories
    :type category: str
    :param product_type: Product type slug from /api/categories
    :type product_type: str
    :param conditions: Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    :type conditions: List[str]
    :param decade: Decade: e.g. 1970s, early 70s
    :type decade: str
    :param finish: Visual finish of the item, common for guitars
    :type finish: str
    :param handmade: Handmade items only
    :type handmade: bool
    :param item_city: City where item is located
    :type item_city: str
    :param item_country: DEPRECATED - Country code where item is located
    :type item_country: str
    :param item_region: Country code where item is located
    :type item_region: str
    :param item_state: State or region code where item is located
    :type item_state: str
    :param make: Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    :type make: List[str]
    :param model: Model of item (e.g. Stratocaster)
    :type model: str
    :param must_not: Search term negation. If you want to exclude a term, add it here
    :type must_not: str
    :param price_max: Maximum price of search results (USD)
    :type price_max: float
    :param price_min: Minimum price of search results (USD)
    :type price_min: float
    :param currency: The currency to be used for the price filters
    :type currency: str
    :param year_max: Maximum year of manufacture
    :type year_max: int
    :param year_min: Minumum year of manufacture
    :type year_min: int
    :param accepts_gift_cards: If true, include only items that accept gift cards
    :type accepts_gift_cards: bool
    :param preferred_seller: If true, include only items by Reverb Preferred Sellers
    :type preferred_seller: bool
    :param shop: Slug of shop to search
    :type shop: str
    :param shop_id: ID of shop to search
    :type shop_id: str
    :param listing_type: Type of listing: auctions,offers
    :type listing_type: str
    :param ships_to: Limit search to items that ship to this country code
    :type ships_to: str
    :param exclude_auctions: If true, exclude auctions
    :type exclude_auctions: bool
    :param accepts_payment_plans: If true, only show items that can be purchased with a payment plan
    :type accepts_payment_plans: bool
    :param watchers_count_min: Minimum number of watchers (used to find popular items)
    :type watchers_count_min: int
    :param not_ids: Listing ID negation. If you want to exclude a listing, add it here.
    :type not_ids: List[str]
    :param local_pickup: Only items that offer local pickup
    :type local_pickup: bool
    :param state: Available: [\&quot;all\&quot;, \&quot;draft\&quot;, \&quot;ended\&quot;, \&quot;live\&quot;, \&quot;ordered\&quot;, \&quot;sold_out\&quot;, \&quot;suspended\&quot;, \&quot;seller_unavailable\&quot;]. Defaults to &#39;live&#39;
    :type state: str
    :param sku: Find a listing by sku
    :type sku: str

    """
    return web.Response(status=200)


async def my_listings_negotiations_get(request: web.Request, page=None, per_page=None, offset=None) -> web.Response:
    """Get a list of active negotiations as a seller

    Get a list of active negotiations as a seller

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def my_listings_slug_state_end_put(request: web.Request, slug, body=None) -> web.Response:
    """End a listing

    End a listing

    :param slug: 
    :type slug: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyListingsSlugStateEndPutRequest.from_dict(body)
    return web.Response(status=200)


async def my_lists_get(request: web.Request, ) -> web.Response:
    """Get a list of your lists (wishlist, watch list, etc)

    Get a list of your lists (wishlist, watch list, etc)


    """
    return web.Response(status=200)


async def my_negotiations_buying_get(request: web.Request, page=None, per_page=None, offset=None) -> web.Response:
    """Get a list of active negotiations as a buyer

    Get a list of active negotiations as a buyer

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def my_negotiations_id_accept_post(request: web.Request, id, body=None) -> web.Response:
    """Accept an offer

    Accept an offer

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyNegotiationsIdAcceptPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_negotiations_id_counter_post(request: web.Request, id, body=None) -> web.Response:
    """Counter an offer

    Counter an offer

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ConversationsConversationIdOfferPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_negotiations_id_decline_post(request: web.Request, id) -> web.Response:
    """Decline an offer

    Decline an offer

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_negotiations_id_get(request: web.Request, id) -> web.Response:
    """Get offer details

    Get offer details

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_orders_awaiting_feedback_get(request: web.Request, ) -> web.Response:
    """List of orders that need feedback

    List of orders that need feedback


    """
    return web.Response(status=200)


async def my_orders_buying_all_get(request: web.Request, ) -> web.Response:
    """Returns all orders, newest first.

    Returns all orders, newest first.


    """
    return web.Response(status=200)


async def my_orders_buying_by_uuid_uuid_get(request: web.Request, uuid) -> web.Response:
    """my_orders_buying_by_uuid_uuid_get

    

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def my_orders_buying_id_get(request: web.Request, id) -> web.Response:
    """Returns order details for a buyer

    Returns order details for a buyer

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_orders_buying_id_mark_received_post(request: web.Request, id) -> web.Response:
    """Marks an order as received by the buyer

    Marks an order as received by the buyer

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_orders_buying_unpaid_get(request: web.Request, ) -> web.Response:
    """Returns unpaid orders, newest first.

    Returns unpaid orders, newest first.


    """
    return web.Response(status=200)


async def my_orders_selling_all_get(request: web.Request, ) -> web.Response:
    """Get all seller orders, newest first.

    Get all seller orders, newest first.


    """
    return web.Response(status=200)


async def my_orders_selling_awaiting_shipment_get(request: web.Request, ) -> web.Response:
    """Get unpaid seller orders, newest first.

    Get unpaid seller orders, newest first.


    """
    return web.Response(status=200)


async def my_orders_selling_buyer_history_buyer_id_get(request: web.Request, buyer_id) -> web.Response:
    """See previous orders from buyer

    See previous orders from buyer

    :param buyer_id: 
    :type buyer_id: str

    """
    return web.Response(status=200)


async def my_orders_selling_by_uuid_uuid_get(request: web.Request, uuid) -> web.Response:
    """my_orders_selling_by_uuid_uuid_get

    

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def my_orders_selling_id_get(request: web.Request, id) -> web.Response:
    """Returns order details for a seller

    Returns order details for a seller

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_orders_selling_id_mark_picked_up_post(request: web.Request, id, body=None) -> web.Response:
    """Marks an order as picked up

    Marks an order as picked up

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyOrdersSellingIdMarkPickedUpPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_orders_selling_id_ship_post(request: web.Request, id, body=None) -> web.Response:
    """Marks an order as shipped

    Marks an order as shipped

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = MyOrdersSellingIdShipPostRequest.from_dict(body)
    return web.Response(status=200)


async def my_orders_selling_order_id_refund_requests_post(request: web.Request, order_id) -> web.Response:
    """Initiate a refund for a sold order

    Initiate a refund for a sold order

    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def my_orders_selling_unpaid_get(request: web.Request, ) -> web.Response:
    """Get unpaid seller orders, newest first.

    Get unpaid seller orders, newest first.


    """
    return web.Response(status=200)


async def my_payments_selling_get(request: web.Request, page=None, per_page=None, offset=None, created_start_date=None, created_end_date=None, updated_start_date=None, updated_end_date=None, order_id=None) -> web.Response:
    """Get payments

    Get payments

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int
    :param created_start_date: Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    :type created_start_date: str
    :param created_end_date: Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    :type created_end_date: str
    :param updated_start_date: Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    :type updated_start_date: str
    :param updated_end_date: Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    :type updated_end_date: str
    :param order_id: Look up payments by order id
    :type order_id: str

    """
    return web.Response(status=200)


async def my_payments_selling_id_get(request: web.Request, id) -> web.Response:
    """Get payment

    Get payment

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_payouts_get(request: web.Request, ) -> web.Response:
    """Get a list of payouts

    Get a list of payouts


    """
    return web.Response(status=200)


async def my_payouts_id_line_items_get(request: web.Request, id) -> web.Response:
    """Read the line items of a payout

    Read the line items of a payout

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_refund_requests_selling_get(request: web.Request, ) -> web.Response:
    """Get a list of refund requests as a seller

    Get a list of refund requests as a seller


    """
    return web.Response(status=200)


async def my_refund_requests_selling_id_put(request: web.Request, id) -> web.Response:
    """Update a refund request for a sold order

    Update a refund request for a sold order

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_viewed_listings_get(request: web.Request, ) -> web.Response:
    """Get a list of your recently viewed listings.

    Get a list of your recently viewed listings.


    """
    return web.Response(status=200)


async def my_wishlist_get(request: web.Request, ) -> web.Response:
    """Get a list of wishlisted items

    Get a list of wishlisted items


    """
    return web.Response(status=200)


async def my_wishlist_id_delete(request: web.Request, id) -> web.Response:
    """Remove a listing from your wishlist

    Remove a listing from your wishlist

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def my_wishlist_id_put(request: web.Request, id) -> web.Response:
    """Add a listing to your wishlist

    Add a listing to your wishlist

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
