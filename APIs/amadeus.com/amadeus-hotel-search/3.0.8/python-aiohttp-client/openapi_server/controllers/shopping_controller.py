from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.multi_response import MultiResponse
from openapi_server.models.pricing_response import PricingResponse
from openapi_server import util


async def get_multi_hotel_offers(request: web.Request, hotel_ids, adults=None, check_in_date=None, check_out_date=None, country_of_residence=None, room_quantity=None, price_range=None, currency=None, payment_policy=None, board_type=None, include_closed=None, best_rate_only=None, lang=None) -> web.Response:
    """getMultiHotelOffers

    

    :param hotel_ids: Amadeus property codes on 8 chars. Mandatory parameter for a search by predefined list of hotels.
    :type hotel_ids: List[str]
    :param adults: Number of adult guests (1-9) per room.
    :type adults: int
    :param check_in_date: Check-in date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is the present date (no dates in the past). If not present, the default value will be today&#39;s date in the GMT time zone.
    :type check_in_date: str
    :param check_out_date: Check-out date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is checkInDate+1. If not present, it will default to checkInDate +1.
    :type check_out_date: str
    :param country_of_residence: Code of the country of residence of the traveler expressed using ISO 3166-1 format.
    :type country_of_residence: str
    :param room_quantity: Number of rooms requested (1-9).
    :type room_quantity: int
    :param price_range: Filter hotel offers by price per night interval (ex: 200-300 or -300 or 100). It is mandatory to include a currency when this field is set.
    :type price_range: str
    :param currency: Use this parameter to request a specific currency. ISO currency code (http://www.iso.org/iso/home/standards/currency_codes.htm). If a hotel does not support the requested currency, the prices for the hotel will be returned in the local currency of the hotel.
    :type currency: str
    :param payment_policy: Filter the response based on a specific payment type. NONE means all types (default).
    :type payment_policy: str
    :param board_type: Filter response based on available meals:         * ROOM_ONLY &#x3D; Room Only         * BREAKFAST &#x3D; Breakfast         * HALF_BOARD &#x3D; Diner &amp; Breakfast (only for Aggregators)         * FULL_BOARD &#x3D; Full Board (only for Aggregators)         * ALL_INCLUSIVE &#x3D; All Inclusive (only for Aggregators)
    :type board_type: str
    :param include_closed: Show all properties (include sold out) or available only. For sold out properties, please check availability on other dates.
    :type include_closed: bool
    :param best_rate_only: Used to return only the cheapest offer per hotel or all available offers.
    :type best_rate_only: bool
    :param lang: Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html).
    :type lang: str

    """
    check_in_date = util.deserialize_date(check_in_date)
    check_out_date = util.deserialize_date(check_out_date)
    return web.Response(status=200)


async def get_offer_pricing(request: web.Request, offer_id, lang=None) -> web.Response:
    """getOfferPricing

    

    :param offer_id: Unique identifier of an offer. Either the GDS booking code or the aggregator offerId with a limited lifetime.
    :type offer_id: str
    :param lang: Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html).
    :type lang: str

    """
    return web.Response(status=200)
