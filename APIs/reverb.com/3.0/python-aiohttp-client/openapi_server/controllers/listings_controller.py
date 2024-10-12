from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_id_offer_post_request import ConversationsIdOfferPostRequest
from openapi_server.models.listings_listing_id_conversations_post_request import ListingsListingIdConversationsPostRequest
from openapi_server.models.listings_post_request import ListingsPostRequest
from openapi_server.models.listings_slug_flag_post_request import ListingsSlugFlagPostRequest
from openapi_server import util


async def listings_all_get(request: web.Request, query=None, auction_price_max=None, category=None, product_type=None, conditions=None, decade=None, finish=None, handmade=None, item_city=None, item_country=None, item_region=None, item_state=None, make=None, model=None, must_not=None, price_max=None, price_min=None, currency=None, year_max=None, year_min=None, accepts_gift_cards=None, preferred_seller=None, shop=None, shop_id=None, listing_type=None, ships_to=None, exclude_auctions=None, accepts_payment_plans=None, watchers_count_min=None, not_ids=None, local_pickup=None, page=None, per_page=None, offset=None) -> web.Response:
    """All listings including used, handmade, and brand new

    All listings including used, handmade, and brand new

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
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def listings_facets_seller_location_get(request: web.Request, ) -> web.Response:
    """Individual facets

    Individual facets


    """
    return web.Response(status=200)


async def listings_get(request: web.Request, query=None, auction_price_max=None, category=None, product_type=None, conditions=None, decade=None, finish=None, handmade=None, item_city=None, item_country=None, item_region=None, item_state=None, make=None, model=None, must_not=None, price_max=None, price_min=None, currency=None, year_max=None, year_min=None, accepts_gift_cards=None, preferred_seller=None, shop=None, shop_id=None, listing_type=None, ships_to=None, exclude_auctions=None, accepts_payment_plans=None, watchers_count_min=None, not_ids=None, local_pickup=None, page=None, per_page=None, offset=None) -> web.Response:
    """Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint.

    Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint.

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
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def listings_id_negotiation_get(request: web.Request, id) -> web.Response:
    """Returns the latest negotiation for the requesting user given a listing id

    Returns the latest negotiation for the requesting user given a listing id

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def listings_id_offer_post(request: web.Request, id, body=None) -> web.Response:
    """Make an offer to the seller of a listing

    Make an offer to the seller of a listing

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ConversationsIdOfferPostRequest.from_dict(body)
    return web.Response(status=200)


async def listings_listing_id_bump_budget_type_post(request: web.Request, listing_id, budget_type) -> web.Response:
    """Bump a listing

    Bump a listing

    :param listing_id: 
    :type listing_id: str
    :param budget_type: 
    :type budget_type: str

    """
    return web.Response(status=200)


async def listings_listing_id_bump_get(request: web.Request, listing_id) -> web.Response:
    """View available bump tiers and stats for a listing

    View available bump tiers and stats for a listing

    :param listing_id: 
    :type listing_id: str

    """
    return web.Response(status=200)


async def listings_listing_id_conversations_post(request: web.Request, listing_id, body=None) -> web.Response:
    """Start a conversation with a seller

    Start a conversation with a seller

    :param listing_id: 
    :type listing_id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ListingsListingIdConversationsPostRequest.from_dict(body)
    return web.Response(status=200)


async def listings_listing_id_images_get(request: web.Request, listing_id) -> web.Response:
    """View the images associated with a particular listing

    View the images associated with a particular listing

    :param listing_id: 
    :type listing_id: str

    """
    return web.Response(status=200)


async def listings_listing_id_images_image_id_delete(request: web.Request, listing_id, image_id) -> web.Response:
    """Delete an image from a listing

    Delete an image from a listing

    :param listing_id: 
    :type listing_id: str
    :param image_id: 
    :type image_id: str

    """
    return web.Response(status=200)


async def listings_listing_id_sales_get(request: web.Request, listing_id) -> web.Response:
    """See all sales that include a listing.

    See all sales that include a listing.

    :param listing_id: 
    :type listing_id: str

    """
    return web.Response(status=200)


async def listings_post(request: web.Request, body=None) -> web.Response:
    """Create a listing

    Create a listing

    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ListingsPostRequest.from_dict(body)
    return web.Response(status=200)


async def listings_slug_delete(request: web.Request, slug) -> web.Response:
    """Delete a draft listing. Cannot be used on non-drafts.

    Delete a draft listing. Cannot be used on non-drafts.

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def listings_slug_edit_get(request: web.Request, slug) -> web.Response:
    """Edit listing.

    Edit listing.

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def listings_slug_flag_post(request: web.Request, slug, body=None) -> web.Response:
    """Flag a listing for inappropriate content or fraud

    Flag a listing for inappropriate content or fraud

    :param slug: 
    :type slug: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ListingsSlugFlagPostRequest.from_dict(body)
    return web.Response(status=200)


async def listings_slug_get(request: web.Request, slug) -> web.Response:
    """Listing details

    Listing details

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def listings_slug_put(request: web.Request, slug, body=None) -> web.Response:
    """Update a listing

    Update a listing

    :param slug: 
    :type slug: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ListingsPostRequest.from_dict(body)
    return web.Response(status=200)


async def listings_slug_reviews_get(request: web.Request, slug) -> web.Response:
    """View reviews of a listing

    View reviews of a listing

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def listings_slug_reviews_post(request: web.Request, slug) -> web.Response:
    """Create a review for a listing

    Create a review for a listing

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def listings_slug_similar_listings_get(request: web.Request, slug) -> web.Response:
    """Listing details

    Listing details

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)
