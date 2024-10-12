from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def all_fares(request: web.Request, catalogues, origin, destination, travel_date, return_date=None, cabin_class=None, travelers=None, fare_family=None, trackingid=None, accept=None) -> web.Response:
    """All Fares

    Retrieves all available fares for a specific Origin &amp; Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS

    :param catalogues: Specifies in which catalogue the fares need to be searched (e.g.&#39;4U;OS&#39;).
    :type catalogues: str
    :param origin: Enter journey origin (e.g &#39;FRA&#39;).
    :type origin: str
    :param destination: Enter journey destination (e.g &#39;MAD&#39;).
    :type destination: str
    :param travel_date: Enter journey travel-date (e.g 2016-10-20)
    :type travel_date: str
    :param return_date: Enter journey return-date (e.g 2016-10-31)&#39;.
    :type return_date: str
    :param cabin_class: Enter the required cabin class (e.g econonmy, business etc.). (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;)
    :type cabin_class: str
    :param travelers: Specifies the type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) For LH only (adult&#x3D;1) possible.
    :type travelers: str
    :param fare_family: Mandatory for 4U. Specifies, which fares to be returned, such as basic, smart, best, smartflex, bestflex . (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;)
    :type fare_family: str
    :param trackingid: Austrian Airlines only - specify the web tracking id to be used in OS Deep link.
    :type trackingid: str
    :param accept: Mandatory http header:  application/xml or application/json
    :type accept: str

    """
    return web.Response(status=200)


async def best_fares(request: web.Request, catalogues, origin, destination, travel_date, trip_duration, range, accept, cabin_class=None, country=None, trackingid=None, fare_family=None) -> web.Response:
    """Best Fares

    Retrieve best fares for the requested journey across multiple days or multiple months.

    :param catalogues: Search fares from these carriers&#39; catalogues (e.g. &#39;4U;OS;LH&#39;)
    :type catalogues: str
    :param origin: Journey origin. 3-letter IATA airport code (e.g. &#39;FRA&#39;)
    :type origin: str
    :param destination: Journey destination. 3-letter IATA airport code (e.g. &#39;MAD&#39;)
    :type destination: str
    :param travel_date: Journey travel-date (YYYY-MM-DD)
    :type travel_date: str
    :param trip_duration: Trip duration in days (e.g. &#39;7&#39;)
    :type trip_duration: str
    :param range: Fare range: &#39;byday&#39; or &#39;bymonth&#39; (Acceptable values are: \&quot;byday\&quot;, \&quot;bymonth\&quot;)
    :type range: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param cabin_class: Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;)
    :type cabin_class: str
    :param country: Country code of requestor. 2-letter ISO 3166-1 country code (e.g. &#39;de&#39;)
    :type country: str
    :param trackingid: Austrian Airlines only - specify the web tracking id to be used in OS Deep link.
    :type trackingid: str
    :param fare_family: Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;)
    :type fare_family: str

    """
    return web.Response(status=200)


async def deep_links(request: web.Request, catalogues, trackingid, country, lang, accept, origin=None, origin_name=None, destination=None, destination_name=None, travel_date=None, return_date=None, cabin_class=None, outbound_segments=None, return_segments=None, travelers=None, fare=None, net_fare=None, fare_currency=None, partnerid=None, encryption_key=None) -> web.Response:
    """Deep Links

    Returns valid deep links for the provided input parameters

    :param catalogues: Carrier for which the deep link will be created (e.g. &#39;LH&#39;)
    :type catalogues: str
    :param trackingid: Deep link tracking ID
    :type trackingid: str
    :param country: 2-letter ISO 3166-1 country code
    :type country: str
    :param lang: 2-letter ISO 3166-1 language code
    :type lang: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param origin: Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;)
    :type origin: str
    :param origin_name: Journey origin airport or city name (e.g. &#39;frankfurt&#39;)
    :type origin_name: str
    :param destination: Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;)
    :type destination: str
    :param destination_name: Journey destination airport or city name (e.g. &#39;madrid&#39;)
    :type destination_name: str
    :param travel_date: Journey travel-date (YYYY-MM-DD)
    :type travel_date: str
    :param return_date: Journey return-date (YYYY-MM-DD)
    :type return_date: str
    :param cabin_class: Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;)
    :type cabin_class: str
    :param outbound_segments: Outbound flight segments in the sequence of travel (e.g. &#39;LH096;LH480&#39;)
    :type outbound_segments: str
    :param return_segments: Flight segments in the sequence of travel (e.g. &#39;LH7465;LH431&#39;)
    :type return_segments: str
    :param travelers: Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;)
    :type travelers: str
    :param fare: Travel fare (e.g. &#39;1341.45&#39;)
    :type fare: str
    :param net_fare: Travel net fare. Total fare less taxes and charges (e.g. &#39;1140&#39;)
    :type net_fare: str
    :param fare_currency: Fare currency (e.g. &#39;EUR&#39;)
    :type fare_currency: str
    :param partnerid: Deep link partner id (e.g. &#39;1247&#39;)
    :type partnerid: str
    :param encryption_key: Deep link encryption-key
    :type encryption_key: str

    """
    return web.Response(status=200)


async def fares(request: web.Request, catalogues, segments, carriers, accept, travelers=None, fare_types=None) -> web.Response:
    """Fares

    Retrieve all available fares per fare family for a specific Origin &amp; Destination on a given date

    :param catalogues: Search fares from these carriers&#39; catalogues - currently active for Germanwings only  (4U)
    :type catalogues: str
    :param segments: Journey details  e.g. (origin&#x3D;TXL;destination&#x3D;CGN;travel-date&#x3D;2016-12-15;return-date&#x3D;2016-12-20;cabin&#x3D;Economy)
    :type segments: str
    :param carriers: Include fares for these carriers e.g. (&#39;4U;LH&#39;)
    :type carriers: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param travelers: Type and number of travelers e.g. (adult&#x3D;1;child&#x3D;1;infant&#x3D;1)
    :type travelers: str
    :param fare_types: Fares family: basic,smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;)
    :type fare_types: str

    """
    return web.Response(status=200)


async def fares_subscriptions(request: web.Request, origin, destination, cabin_class, trip_duration, email, lang, accept, country=None, trackingid=None) -> web.Response:
    """Fares Subscriptions

    Create a subscription for best price O&amp;D. Receive regular updates on lowest fares

    :param origin: Journey origin. 3-leter IATA airport code (e.g. &#39;FRA&#39;)
    :type origin: str
    :param destination: Journey destination. 3-letter IATA airport code (e.g. &#39;MAD&#39;)
    :type destination: str
    :param cabin_class: Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;)
    :type cabin_class: str
    :param trip_duration: Trip duration in days (e.g. &#39;7&#39;)
    :type trip_duration: str
    :param email: Email Address&#39;)
    :type email: str
    :param lang: 2-letter ISO 3166-1 language code
    :type lang: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param country: 2-letter ISO 3166-1 country code
    :type country: str
    :param trackingid: Tracking parameter
    :type trackingid: str

    """
    return web.Response(status=200)


async def l_h_deep_links_ffp(request: web.Request, catalogues, origin, destination, travel_date, trackingid, country, lang, accept, return_date=None, cabin_class=None, travelers=None, partnerid=None, encryption_key=None) -> web.Response:
    """LH Deep Links - FFP

    Returns valid LH deep links (FFP - links to flight selection screen on LH.COM)

    :param catalogues: Carrier for which the deep link will be created (e.g. &#39;LH&#39;)
    :type catalogues: str
    :param origin: Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;)
    :type origin: str
    :param destination: Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;)
    :type destination: str
    :param travel_date: Journey travel-date (YYYY-MM-DD)
    :type travel_date: str
    :param trackingid: Deep link tracking ID
    :type trackingid: str
    :param country: 2-letter ISO 3166-1 country code
    :type country: str
    :param lang: 2-letter ISO 3166-1 language code
    :type lang: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param return_date: Journey return-date (YYYY-MM-DD)
    :type return_date: str
    :param cabin_class: Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;)
    :type cabin_class: str
    :param travelers: Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;)
    :type travelers: str
    :param partnerid: Deep link partner id (e.g. &#39;1247&#39;)
    :type partnerid: str
    :param encryption_key: Deep link encryption-key
    :type encryption_key: str

    """
    return web.Response(status=200)


async def l_h_deep_links_itco(request: web.Request, catalogues, origin, destination, travel_date, outbound_segments, fare, fare_currency, trackingid, country, lang, accept, return_date=None, cabin_class=None, return_segments=None, travelers=None, net_fare=None, partnerid=None, encryption_key=None) -> web.Response:
    """LH Deep Links - ITCO

    Returns valid LH deep links (ITCO - links to shopping cart on LH.COM)

    :param catalogues: Carrier for which the deep link will be created (e.g. &#39;LH&#39;)
    :type catalogues: str
    :param origin: Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;)
    :type origin: str
    :param destination: Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;)
    :type destination: str
    :param travel_date: Journey travel-date (YYYY-MM-DD)
    :type travel_date: str
    :param outbound_segments: Outbound flight segments in the sequence of travel (e.g. &#39;LH096;LH480&#39;)
    :type outbound_segments: str
    :param fare: Travel fare (e.g. &#39;1341.45&#39;)
    :type fare: str
    :param fare_currency: Fare currency (e.g. &#39;EUR&#39;)
    :type fare_currency: str
    :param trackingid: Deep link tracking ID
    :type trackingid: str
    :param country: 2-letter ISO 3166-1 country code
    :type country: str
    :param lang: 2-letter ISO 3166-1 language code
    :type lang: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param return_date: Journey return-date (YYYY-MM-DD)
    :type return_date: str
    :param cabin_class: Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;)
    :type cabin_class: str
    :param return_segments: Flight segments in the sequence of travel (e.g. &#39;LH7465;LH431&#39;)
    :type return_segments: str
    :param travelers: Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;)
    :type travelers: str
    :param net_fare: Travel net fare. Total fare less taxes and charges (e.g. &#39;1140&#39;)
    :type net_fare: str
    :param partnerid: Deep link partner id (e.g. &#39;1247&#39;)
    :type partnerid: str
    :param encryption_key: Deep link encryption-key
    :type encryption_key: str

    """
    return web.Response(status=200)


async def lowest_fares(request: web.Request, catalogues, origin, destination, travel_date, accept, return_date=None, cabin_class=None, travelers=None, fare_family=None, country=None) -> web.Response:
    """Lowest Fares

    Retrieve lowest fare for a specific Origin &amp; Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS &amp; LH

    :param catalogues: Search fares from these carriers&#39; catalogues e.g. &#39;4U;OS;LH&#39;
    :type catalogues: str
    :param origin: Journey origin. 3-letter IATA aiport code e.g. &#39;FRA&#39;
    :type origin: str
    :param destination: Journey destination. 3-letter IATA airport code e.g. &#39;MAD&#39;
    :type destination: str
    :param travel_date: Journey travel-date YYYY-MM-DD
    :type travel_date: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param return_date: Journey return-date - mandatory for OS and LH searches YYYY-MM-DD
    :type return_date: str
    :param cabin_class: Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;)
    :type cabin_class: str
    :param travelers: Type and number of travelers e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;. For LH only (adult&#x3D;1) possible
    :type travelers: str
    :param fare_family: Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;)
    :type fare_family: str
    :param country: Country code of requestor. 2-letter ISO 3166-1 country code (e.g. &#39;de&#39;)
    :type country: str

    """
    return web.Response(status=200)


async def o_nd_route(request: web.Request, origin, destination, accept, catalogues=None, limit=None, offset=None) -> web.Response:
    """OND Route

    Returns LH route origin &amp; destination information

    :param origin: Enter either the orgin city or orgin country code (e.g &#39;FRA&#39; or &#39;DE&#39;). Enter &#39;*&#39; for all
    :type origin: str
    :param destination: Enter either the destination city or country code (e.g &#39;MAD&#39; or &#39;ES&#39;). Enter &#39;*&#39; for all
    :type destination: str
    :param accept: Mandatory http header:  application/xml or application/json
    :type accept: str
    :param catalogues: Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;)
    :type catalogues: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def o_nd_status(request: web.Request, accept, catalogues=None, new_routes=None, old_routes=None) -> web.Response:
    """OND Status

    Returns LH network route status information. Search for recently added or retired routes

    :param accept: Mandatory http header:  application/xml or application/json
    :type accept: str
    :param catalogues: Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;)
    :type catalogues: str
    :param new_routes: Enter if newly added routes should be returned in the response. (Acceptable values are: \&quot;\&quot;, \&quot;true\&quot;, \&quot;false\&quot;)
    :type new_routes: str
    :param old_routes: Enter if old (deleted) routes should be returned in the response. (Acceptable values are: \&quot;\&quot;, \&quot;true\&quot;, \&quot;false\&quot;)
    :type old_routes: str

    """
    return web.Response(status=200)


async def top_ond(request: web.Request, accept, catalogues=None, origin=None) -> web.Response:
    """Top OND

    Returns LH Top routes per country or across all countries

    :param accept: Mandatory http header:  application/xml or application/json
    :type accept: str
    :param catalogues: Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;)
    :type catalogues: str
    :param origin: Enter the origin country code (e.g. &#39;DE&#39;). Leave empty to search Top OND across all countries
    :type origin: str

    """
    return web.Response(status=200)
