from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing import Listing
from openapi_server.models.open_house import OpenHouse
from openapi_server import util


async def openhouses_get(request: web.Request, type=None, listing_id=None, cities=None, brokers=None, agent=None, minprice=None, startdate=None, offset=None, last_id=None, limit=None, sort=None, include=None) -> web.Response:
    """The SimplyRETS OpenHouses API

    This is the main endpoint for accessing openhouses. 

    :param type: Request listings by a specific property type. This defaults to Residential, and you can only specify one type in a single query. 
    :type type: str
    :param listing_id: Request openhouses for a specific &#x60;listingId&#x60;. 
    :type listing_id: str
    :param cities: Filter the openhouses returned by a list of valid cities.  The &#x60;cities&#x60; query parameter is case-insensitive.  The list of &#x60;cities&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses&#x60; 
    :type cities: List[str]
    :param brokers: Filter the listings returned by brokerage with a Broker ID. You can specific multiple broker parameters. Note, the Broker ID is provided by your MLS. 
    :type brokers: List[str]
    :param agent: Filter the listings returned by an agent ID.  Note, the Agent ID is provided by your MLS. 
    :type agent: str
    :param minprice: Filter listings by a minimum price. 
    :type minprice: int
    :param startdate: Scheduled date and time of the open house showing
    :type startdate: str
    :param offset: Increase the offset parameter by the limit to go to the next \&quot;page\&quot; of listings. Also take a look at the Link HTTP Header for pre-built pagination.  *NOTE:* Use the &#x60;lastId&#x60; parameter for pagination. 
    :type offset: int
    :param last_id: Used as a cursor for pagination. 
    :type last_id: int
    :param limit: Set the number of listings to return in the response. This defaults to 20 listings, and can be a maximum of 500. To paginate through to the next page of listings, take a look at the &#x60;offset&#x60; parameter, or the Link in the HTTP Header. 
    :type limit: int
    :param sort: Sort the response by a specific field. Values starting with a minus (-) denote descending order, while the others are ascending. 
    :type sort: str
    :param include: Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;taxAnnualAmount&#39; include the annual tax amount - &#39;taxYear&#39; include the tax year data - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an &#39;include&#39; may become available by default. 
    :type include: List[str]

    """
    startdate = util.deserialize_datetime(startdate)
    return web.Response(status=200)


async def openhouses_open_house_key_get(request: web.Request, open_house_key, include=None) -> web.Response:
    """Single OpenHouse Endpoint

    Use this endpoint for accessing a single OpenHouse. 

    :param open_house_key: A unique OpenHouse identification key
    :type open_house_key: int
    :param include: Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;taxAnnualAmount&#39; include the annual tax amount - &#39;taxYear&#39; include the tax year data - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an &#39;include&#39; may become available by default. 
    :type include: List[str]

    """
    return web.Response(status=200)


async def properties_get(request: web.Request, q=None, status=None, type=None, subtype=None, agent=None, brokers=None, minprice=None, maxprice=None, minarea=None, maxarea=None, minbaths=None, maxbaths=None, minbeds=None, maxbeds=None, maxdom=None, minyear=None, limit=None, offset=None, last_id=None, vendor=None, postal_codes=None, features=None, water=None, neighborhoods=None, cities=None, counties=None, points=None, include=None, sort=None, count=None) -> web.Response:
    """The SimplyRETS Listings API

    This is the main endpoint for accessing your properties. View all of the available query parameters and make requests below! The API uses Basic Authentication, which most HTTP libraries will handle for you. To use the test data (which is what this pages uses), you can use the api key &#x60;simplyrets&#x60; and secret &#x60;simplyrets&#x60;. Note that these test listings are not live MLS listings but the data, query parameters, and response bodies will all work the same. 

    :param q: A textual keyword search. This parameter will search  the following fields, when available:   - listingId (This does _not_ search the &#x60;mlsId&#x60; field in the SimplyRETS response body)   - street number   - street name   - mls area (major)   - city   - subdivision name   - postal code 
    :type q: str
    :param status: Request listings by a specific status. This parameter defaults to active and you can specify multiple statuses in a single query.  Listing statuses depend on your MLS&#39;s availability. Below is a brief description of each status with possible synonyms which may map to your MLS-specific statuses - *Active*: Active Listing which is still on the market - *ActiveUnderContract*: An offer has been accepted but the listing is still on market. Synonyms: Accepting Backup Offers, Backup Offer, Active With Accepted. Synonyms: Offer, Backup, Contingent - *Pending*: An offer has been accepted and the listing is no longer on market. Synonyms: Offer Accepted, Under Contract - *Hold*: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - *Withdrawn*: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - *Closed*: The purchase agreement has been fulfilled or the lease   agreement has been executed. Synonyms: Sold, Leased, Rented, Closed Sale - *Expired*: The listing contract has expired - *Delete*: The listing contract was never valid or other reason for the contract to be nullified. Synonyms: Kill, Zap - *Incomplete*: The listing has not yet be completely entered and is not yet   published in the MLS. Synonyms: Draft, Partially Complted - *ComingSoon* 
    :type status: List[str]
    :param type: Request listings by a specific property type. This defaults to Residential and Rental. You can specify multiple property types in a single query. 
    :type type: List[str]
    :param subtype: Request listings by a specific property sub type.  *NOTE* not all sub type filters are available for all vendors. 
    :type subtype: List[str]
    :param agent: Filter the listings returned by an agent ID.  Note, the Agent ID is provided by your MLS.  The co-listing agent is not included in this query parameter. 
    :type agent: str
    :param brokers: Filter the listings returned by brokerage with a Broker ID. For some MLS areas, this is the ListOfficeId (Listing Office ID).  You can specific multiple broker parameters. Note, this query parameter is only available if a Broker ID is provided by your MLS. 
    :type brokers: List[str]
    :param minprice: Filter listings by a minimum price. 
    :type minprice: int
    :param maxprice: Filter listings by a maximum price 
    :type maxprice: int
    :param minarea: Filter listings by a minimum area size in Sq Ft. 
    :type minarea: int
    :param maxarea: Filter listings by a maximum area size in Sq Ft. 
    :type maxarea: int
    :param minbaths: Filter listings by a minimum number of bathrooms. 
    :type minbaths: int
    :param maxbaths: Filter listings by a maximum number of bathrooms. 
    :type maxbaths: int
    :param minbeds: Filter listings by a minimum number of bedrooms. 
    :type minbeds: int
    :param maxbeds: Filter listings by a maximum number of bedrooms. 
    :type maxbeds: int
    :param maxdom: Filter listings by a maximum number of days on market. _Note that your MLS must provide Days on Market data._ 
    :type maxdom: int
    :param minyear: Filter listings by a setting a minimum year built. 
    :type minyear: int
    :param limit: Set the number of listings to return in the response. This defaults to 20 listings, and can be a maximum of 500. To paginate through to the next page of listings, take a look at the &#x60;offset&#x60; parameter, or the Link in the HTTP Header. 
    :type limit: int
    :param offset: Increase the offset parameter by the limit to go to the next \&quot;page\&quot; of listings. Also take a look at the Link HTTP Header for pre-built pagination.  *NOTE:* Use the &#x60;lastId&#x60; field to paginate response  *NOTE:* If you&#39;re offset is too high, you will receive an &#x60;HTTP 400 offset too high&#x60; error message. 
    :type offset: int
    :param last_id: Used as a cursor for pagination. When using &#x60;lastId&#x60;, the &#x60;sort&#x60; parameter will not work. 
    :type last_id: int
    :param vendor: Used to specify the vendor (MLS) to search from. This parameter is required on multi-MLS apps, and you can only query one vendor at a time. To get your vendor id&#39;s make an OPTIONS request to https://api.simplyrets.com.  &#x60;curl -XOPTIONS https://api.simplyrets.com/properties&#x60; 
    :type vendor: str
    :param postal_codes: Filter the listings returned by postal codes / zip code. You can specify multiple. 
    :type postal_codes: List[str]
    :param features: Filter the listings by specific interior features.  You can filter by multiple. For example, to filter trial listings by multiple features you can use, Return listings that are within a set of latitude longitude coordinates. For example,  &#x60;&#x60;&#x60; Wet Bar High Ceiling &#x60;&#x60;&#x60;  e.g. &#x60;https://simplyrets.com/services?features&#x3D;Wet%20Bar&amp;features&#x3D;High%20Ceiling&#x60;  The list of &#x60;features&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/properties&#x60; 
    :type features: List[str]
    :param water: Query water/waterfront listings only. Specify &#x60;true&#x60; to filter waterfront listings.  If you specify &#x60;water&#x3D;true&#x60;, all listings with any &#x60;waterfront&#x60; value will be queried.  If you specify &#x60;water&#x3D;false&#x60;, listings which are **NOT** waterfront listings will be queried.  If you specify &#x60;water&#x3D;LAKE+NAME&#x60; or another valid value contained in your feed, that value will be searched 
    :type water: str
    :param neighborhoods: Filter the listings returned by specific neighborhoods and subdivisions. You can specify multiple &#x60;neighborhoods&#x60; by using the query parameter multiple times.  The &#x60;neighborhoods&#x60; query parameter is case-insensitive.  The list of &#x60;neighborhoods&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/properties&#x60; 
    :type neighborhoods: List[str]
    :param cities: Filter the listings returned by specific cities. You can specify multiple &#x60;cities&#x60; query parameters.  The &#x60;cities&#x60; query parameter is case-insensitive.  The list of &#x60;cities&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses&#x60; 
    :type cities: List[str]
    :param counties: Filter the listings returned by specific counties. You can specify multiple &#x60;counties&#x60; parameters.  The &#x60;counties&#x60; query parameter is case-insensitive.  The list of &#x60;counties&#x60; provided by your RETS vendor can be seen by sending an &#x60;OPTIONS&#x60; request to the &#x60;/properties&#x60; endpoint:  &#x60;curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/openhouses&#x60; 
    :type counties: List[str]
    :param points: Return listings that are within a set of latitude longitude coordinates. For example; &#x60;&#x60;&#x60; 29.723837,-95.69778 29.938275,-95.69778 29.938275,-95.32974 29.723837,-95.32974 &#x60;&#x60;&#x60; Note that some MLS&#39;s do not provide latitude and longitude for their listings, which is required for this parameter to work. In these cases, SimplyRETS offers a [Geocoding Addon](https://simplyrets.com/services#geocoding).  Check out our [blog post](https://simplyrets.com/blog/interactive-map-search.html) on using the &#x60;points&#x60; parameter to build a map-based app in javascript. 
    :type points: List[str]
    :param include: Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;taxAnnualAmount&#39; include the annual tax amount - &#39;taxYear&#39; include the tax year data - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available in the API response.  In the future, fields which require an &#39;include&#39; may become available by default. 
    :type include: List[str]
    :param sort: Sort the response by a specific field. Values starting with a minus (-) denote descending order, while the others are ascending. 
    :type sort: str
    :param count: When set to &#x60;false&#x60;, The &#x60;X-Total-Count&#x60; header will not be returned  Counting the listings can contribute to slower API calls due to the extra queries that need to be run to get an exact count.  Disabling count can increase query speeds. 
    :type count: int

    """
    return web.Response(status=200)


async def properties_mls_id_get(request: web.Request, mls_id, include=None) -> web.Response:
    """Single Listing Endpoint

    Use this endpoint for accessing a single listing. When you make a search to the &#x60;/properties&#x60; endpoint, each listing in the response will contain a unique &#x60;mlsId&#x60; field which should be used to request that listing on this route.  The &#x60;mlsId&#x60; field is a unique identifier for a listing which is specific to the SimplyRETS API only.  It is different from the &#x60;listingId&#x60; field is the public number given to a listing by the MLS and is not used here. 

    :param mls_id: The &#x60;mlsId&#x60; field is a unique identifier which is specific to the SimplyRETS API only.  This field is different from the &#x60;listingId&#x60; field (which is the public number given to a listing by the MLS and is not used here). 
    :type mls_id: int
    :param include: Include a extra fields which are not in the default response body - &#39;association&#39; includes additional HOA data - &#39;agreement&#39; information on the listing agreement - &#39;garageSpaces&#39; additional garage data - &#39;maintenanceExpense&#39; data on maintenance expenses - &#39;parking&#39; additional parking data - &#39;pool&#39; includes an additional pool description - &#39;rooms&#39; include parameter will include    any additional rooms as a list.  Note that your MLS must provide these fields in their RETS data for them to be available with valid data in the API response. If your MLS does not offer these fields, they will contain &#39;null&#39;.  In the future, fields which require an &#39;include&#39; may become available by default. 
    :type include: List[str]

    """
    return web.Response(status=200)
