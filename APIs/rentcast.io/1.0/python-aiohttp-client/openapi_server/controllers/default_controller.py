from typing import List, Dict
from aiohttp import web

from openapi_server.models.market_statistics200_response import MarketStatistics200Response
from openapi_server.models.property_records200_response_inner import PropertyRecords200ResponseInner
from openapi_server.models.property_records_random200_response_inner import PropertyRecordsRandom200ResponseInner
from openapi_server.models.rent_estimate_long_term200_response import RentEstimateLongTerm200Response
from openapi_server.models.rental_listing_long_term_by_id200_response import RentalListingLongTermById200Response
from openapi_server.models.rental_listings_long_term200_response_inner import RentalListingsLongTerm200ResponseInner
from openapi_server.models.sale_listing_by_id200_response import SaleListingById200Response
from openapi_server.models.sale_listings200_response_inner import SaleListings200ResponseInner
from openapi_server.models.value_estimate200_response import ValueEstimate200Response
from openapi_server import util


async def market_statistics(request: web.Request, zip_code, history_range=None) -> web.Response:
    """Market Statistics

    Returns aggregate rental statistics and listing trends for a single US zip code.

    :param zip_code: A valid 5-digit US zip code
    :type zip_code: str
    :param history_range: The time range for historical record entries, in months. Defaults to 12 if not provided
    :type history_range: int

    """
    return web.Response(status=200)


async def property_record_by_id(request: web.Request, id) -> web.Response:
    """Property Record by Id

    Returns a single property record matching the specified id.

    :param id: The id of the property record to return
    :type id: str

    """
    return web.Response(status=200)


async def property_records(request: web.Request, address=None, city=None, state=None, zip_code=None, latitude=None, longitude=None, radius=None, property_type=None, bedrooms=None, bathrooms=None, limit=None, offset=None) -> web.Response:
    """Property Records

    Search for property records in a geographical area, or by a specific address.

    :param address: The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for properties in a specific area
    :type address: str
    :param city: The name of the city, used to search for properties in a specific city. This parameter is case-sensitive
    :type city: str
    :param state: The 2-character state abbreviation, used to search for properties in a specific state. This parameter is case-sensitive
    :type state: str
    :param zip_code: The 5-digit zip code, used to search for properties in a specific zip code
    :type zip_code: str
    :param latitude: The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for properties in a specific area
    :type latitude: float
    :param longitude: The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for properties in a specific area
    :type longitude: float
    :param radius: The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for properties in a specific area
    :type radius: float
    :param property_type: The type of the property, used to search for properties matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    :type property_type: str
    :param bedrooms: The number of bedrooms, used to search for properties matching this criteria. Use &#x60;0&#x60; to indicate a studio layout
    :type bedrooms: float
    :param bathrooms: The number of bathrooms, used to search for properties matching this criteria. Supports fractions to indicate partial bathrooms
    :type bathrooms: float
    :param limit: The maximum number of property records to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    :type limit: int
    :param offset: The index of the first property record to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    :type offset: int

    """
    return web.Response(status=200)


async def property_records_random(request: web.Request, limit=None) -> web.Response:
    """Random Property Records

    Returns a list of property records selected at random.

    :param limit: The number of records to return, between 1 and 500. Defaults to 50 if not provided
    :type limit: int

    """
    return web.Response(status=200)


async def rent_estimate_long_term(request: web.Request, address=None, latitude=None, longitude=None, property_type=None, bedrooms=None, bathrooms=None, square_footage=None, max_radius=None, days_old=None, comp_count=None) -> web.Response:
    """Rent Estimate

    Returns a property rent estimate and comparable properties.

    :param address: The full property address, in the format of &#x60;Street, City, State, Zip&#x60;. You need to provide either the &#x60;address&#x60; or the &#x60;latitude&#x60;/&#x60;longitude&#x60; parameters
    :type address: str
    :param latitude: The latitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter
    :type latitude: float
    :param longitude: The longitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter
    :type longitude: float
    :param property_type: The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    :type property_type: str
    :param bedrooms: The number of bedrooms in the property. Use &#x60;0&#x60; to indicate a studio layout
    :type bedrooms: float
    :param bathrooms: The number of bathrooms in the property. Supports fractions to indicate partial bathrooms
    :type bathrooms: float
    :param square_footage: The total living area size of the property, in square feet
    :type square_footage: float
    :param max_radius: The maximum distance between comparable listings and the subject property, in miles
    :type max_radius: float
    :param days_old: The maximum number of days since comparable listings were last seen on the market, with a minimum of 1
    :type days_old: float
    :param comp_count: The number of comparable listings to use when calculating the rent estimate, between 5 and 25. Defaults to 10 if not provided
    :type comp_count: int

    """
    return web.Response(status=200)


async def rental_listing_long_term_by_id(request: web.Request, id) -> web.Response:
    """Rental Listing by Id

    Returns a single rental listing matching the specified id.

    :param id: The id of the property listing to return
    :type id: str

    """
    return web.Response(status=200)


async def rental_listings_long_term(request: web.Request, address=None, city=None, state=None, zip_code=None, latitude=None, longitude=None, radius=None, property_type=None, bedrooms=None, bathrooms=None, status=None, days_old=None, limit=None, offset=None) -> web.Response:
    """Rental Listings

    Search for rental listings in a geographical area, or by a specific address.

    :param address: The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for listings in a specific area
    :type address: str
    :param city: The name of the city, used to search for listings in a specific city. This parameter is case-sensitive
    :type city: str
    :param state: The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive
    :type state: str
    :param zip_code: The 5-digit zip code, used to search for listings in a specific zip code
    :type zip_code: str
    :param latitude: The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area
    :type latitude: float
    :param longitude: The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area
    :type longitude: float
    :param radius: The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for listings in a specific area
    :type radius: float
    :param property_type: The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    :type property_type: str
    :param bedrooms: The number of bedrooms, used to search for listings matching this criteria. Use &#x60;0&#x60; to indicate a studio layout
    :type bedrooms: float
    :param bathrooms: The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms
    :type bathrooms: float
    :param status: The current listing status, used to search for listings matching this criteria
    :type status: str
    :param days_old: The maximum number of days since a property was listed on the market, with a minimum of 1
    :type days_old: float
    :param limit: The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    :type limit: int
    :param offset: The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    :type offset: int

    """
    return web.Response(status=200)


async def sale_listing_by_id(request: web.Request, id) -> web.Response:
    """Sale Listing by Id

    Returns a single sale listing matching the specified id.

    :param id: The id of the property listing to return
    :type id: str

    """
    return web.Response(status=200)


async def sale_listings(request: web.Request, address=None, city=None, state=None, zip_code=None, latitude=None, longitude=None, radius=None, property_type=None, bedrooms=None, bathrooms=None, status=None, days_old=None, limit=None, offset=None) -> web.Response:
    """Sale Listings

    Search for sale listings in a geographical area, or by a specific address.

    :param address: The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for listings in a specific area
    :type address: str
    :param city: The name of the city, used to search for listings in a specific city. This parameter is case-sensitive
    :type city: str
    :param state: The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive
    :type state: str
    :param zip_code: The 5-digit zip code, used to search for listings in a specific zip code
    :type zip_code: str
    :param latitude: The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area
    :type latitude: float
    :param longitude: The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area
    :type longitude: float
    :param radius: The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for listings in a specific area
    :type radius: float
    :param property_type: The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    :type property_type: str
    :param bedrooms: The number of bedrooms, used to search for listings matching this criteria. Use &#x60;0&#x60; to indicate a studio layout
    :type bedrooms: float
    :param bathrooms: The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms
    :type bathrooms: float
    :param status: The current listing status, used to search for listings matching this criteria
    :type status: str
    :param days_old: The maximum number of days since a property was listed on the market, with a minimum of 1
    :type days_old: float
    :param limit: The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    :type limit: int
    :param offset: The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    :type offset: int

    """
    return web.Response(status=200)


async def value_estimate(request: web.Request, address=None, latitude=None, longitude=None, property_type=None, bedrooms=None, bathrooms=None, square_footage=None, max_radius=None, days_old=None, comp_count=None) -> web.Response:
    """Value Estimate

    Returns a property value estimate and comparable properties.

    :param address: The full property address, in the format of &#x60;Street, City, State, Zip&#x60;. You need to provide either the &#x60;address&#x60; or the &#x60;latitude&#x60;/&#x60;longitude&#x60; parameters
    :type address: str
    :param latitude: The latitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter
    :type latitude: float
    :param longitude: The longitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter
    :type longitude: float
    :param property_type: The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    :type property_type: str
    :param bedrooms: The number of bedrooms in the property. Use &#x60;0&#x60; to indicate a studio layout
    :type bedrooms: float
    :param bathrooms: The number of bathrooms in the property. Supports fractions to indicate partial bathrooms
    :type bathrooms: float
    :param square_footage: The total living area size of the property, in square feet
    :type square_footage: float
    :param max_radius: The maximum distance between comparable listings and the subject property, in miles
    :type max_radius: float
    :param days_old: The maximum number of days since comparable listings were last seen on the market, with a minimum of 1
    :type days_old: float
    :param comp_count: The number of comparable listings to use when calculating the value estimate, between 5 and 25. Defaults to 10 if not provided
    :type comp_count: int

    """
    return web.Response(status=200)
