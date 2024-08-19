from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_version_number_geocode_query_ext_get(request: web.Request, version_number, query, ext, store_result=None, typeahead=None, limit=None, ofs=None, country_set=None, lat=None, lon=None, radius=None, top_left=None, btm_right=None, language=None, extended_postal_codes_for=None, view=None) -> web.Response:
    """Geocode

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
    :param store_result: If the \&quot;storeResult\&quot; flag is set, the query will be interpreted as a stored geocode and will be billed according to the terms of use.
    :type store_result: bool
    :param typeahead: If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode.
    :type typeahead: bool
    :param limit: Maximum number of search results that will be returned.
    :type limit: int
    :param ofs: Starting offset of the returned results within the full result set.
    :type ofs: int
    :param country_set: Comma separated string of country codes. This will limit the search to the specified countries.
    :type country_set: str
    :param lat: Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    :type lat: float
    :param lon: Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    :type lon: float
    :param radius: If radius &lt;b&gt;and&lt;/b&gt; position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    :type radius: int
    :param top_left: Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    :type top_left: str
    :param btm_right: Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    :type btm_right: str
    :param language: Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive.
    :type language: str
    :param extended_postal_codes_for: Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type extended_postal_codes_for: str
    :param view: Geopolitical View.
    :type view: str

    """
    return web.Response(status=200)


async def search_version_number_structured_geocode_ext_get(request: web.Request, version_number, ext, country_code, limit=None, ofs=None, street_number=None, street_name=None, cross_street=None, municipality=None, municipality_subdivision=None, country_tertiary_subdivision=None, country_secondary_subdivision=None, country_subdivision=None, postal_code=None, language=None, extended_postal_codes_for=None) -> web.Response:
    """Structured Geocode

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param ext: Expected response format.
    :type ext: str
    :param country_code: 2 or 3 letter country code (e.g.: FR, ES).
    :type country_code: str
    :param limit: Maximum number of search results that will be returned.
    :type limit: int
    :param ofs: Starting offset of the returned results within the full result set.
    :type ofs: int
    :param street_number: The street number for the structured address.
    :type street_number: str
    :param street_name: The street name for the structured address.
    :type street_name: str
    :param cross_street: The cross street name for the structured address.
    :type cross_street: str
    :param municipality: The municipality (city/town) for the structured address.
    :type municipality: str
    :param municipality_subdivision: The municipality subdivision (sub/super city) for the structured address.
    :type municipality_subdivision: str
    :param country_tertiary_subdivision: The named area for the structured address.
    :type country_tertiary_subdivision: str
    :param country_secondary_subdivision: The county for the structured address.
    :type country_secondary_subdivision: str
    :param country_subdivision: The state or province for the structured address.
    :type country_subdivision: str
    :param postal_code: The zip code or postal code for the structured address.
    :type postal_code: str
    :param language: Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive.
    :type language: str
    :param extended_postal_codes_for: Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type extended_postal_codes_for: str

    """
    return web.Response(status=200)
