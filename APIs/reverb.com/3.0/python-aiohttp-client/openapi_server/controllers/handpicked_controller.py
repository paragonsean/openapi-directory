from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def handpicked_slug_get(request: web.Request, slug, query=None, auction_price_max=None, category=None, product_type=None, conditions=None, decade=None, finish=None, handmade=None, item_city=None, item_country=None, item_region=None, item_state=None, make=None, model=None, must_not=None, price_max=None, price_min=None, currency=None, year_max=None, year_min=None, accepts_gift_cards=None, preferred_seller=None, shop=None, shop_id=None, listing_type=None, ships_to=None, exclude_auctions=None, accepts_payment_plans=None, watchers_count_min=None, not_ids=None, local_pickup=None, page=None, per_page=None, offset=None) -> web.Response:
    """Get results from a handpicked collection

    Get results from a handpicked collection

    :param slug: 
    :type slug: str
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
