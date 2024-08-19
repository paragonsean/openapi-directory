from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_version_number_geometry_search_query_ext_post_request import SearchVersionNumberGeometrySearchQueryExtPostRequest
from openapi_server.models.search_version_number_search_along_route_query_ext_post_request import SearchVersionNumberSearchAlongRouteQueryExtPostRequest
from openapi_server import util


async def search_version_number_category_search_query_ext_get(request: web.Request, version_number, query, ext, typeahead=None, limit=None, ofs=None, country_set=None, lat=None, lon=None, radius=None, top_left=None, btm_right=None, language=None, extended_postal_codes_for=None, view=None) -> web.Response:
    """Category Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
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


async def search_version_number_cs_category_ext_get(request: web.Request, version_number, category, ext, typeahead=None, limit=None, ofs=None, country_set=None, lat=None, lon=None, radius=None, top_left=None, btm_right=None, language=None, idx_set=None, view=None) -> web.Response:
    """Low Bandwith Category Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param category: Query string. Must be properly URL encoded.
    :type category: str
    :param ext: Expected response format.
    :type ext: str
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
    :param idx_set: A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type idx_set: str
    :param view: Geopolitical View.
    :type view: str

    """
    return web.Response(status=200)


async def search_version_number_geometry_search_query_ext_get(request: web.Request, version_number, query, ext, geometry_list=None, limit=None, language=None, extended_postal_codes_for=None, idx_set=None) -> web.Response:
    """Geometry Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
    :param geometry_list: List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON.
    :type geometry_list: str
    :param limit: Maximum number of search results that will be returned.
    :type limit: int
    :param language: Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive.
    :type language: str
    :param extended_postal_codes_for: Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type extended_postal_codes_for: str
    :param idx_set: A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type idx_set: str

    """
    return web.Response(status=200)


async def search_version_number_geometry_search_query_ext_post(request: web.Request, version_number, query, ext, limit=None, language=None, extended_postal_codes_for=None, idx_set=None, body=None) -> web.Response:
    """Geometry Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
    :param limit: Maximum number of search results that will be returned.
    :type limit: int
    :param language: Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive.
    :type language: str
    :param extended_postal_codes_for: Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type extended_postal_codes_for: str
    :param idx_set: A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type idx_set: str
    :param body: 
    :type body: dict | bytes

    """
    body = SearchVersionNumberGeometrySearchQueryExtPostRequest.from_dict(body)
    return web.Response(status=200)


async def search_version_number_nearby_search_ext_get(request: web.Request, version_number, ext, lat, lon, limit=None, ofs=None, country_set=None, radius=None, top_left=None, btm_right=None, language=None, extended_postal_codes_for=None, min_fuzzy_level=None, max_fuzzy_level=None, idx_set=None, view=None) -> web.Response:
    """Nearby Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param ext: Expected response format.
    :type ext: str
    :param lat: Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    :type lat: float
    :param lon: Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    :type lon: float
    :param limit: Maximum number of search results that will be returned.
    :type limit: int
    :param ofs: Starting offset of the returned results within the full result set.
    :type ofs: int
    :param country_set: Comma separated string of country codes. This will limit the search to the specified countries.
    :type country_set: str
    :param radius: If radius and position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    :type radius: int
    :param top_left: Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    :type top_left: str
    :param btm_right: Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    :type btm_right: str
    :param language: Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive.
    :type language: str
    :param extended_postal_codes_for: Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type extended_postal_codes_for: str
    :param min_fuzzy_level: Minimum fuzziness level to be used.
    :type min_fuzzy_level: int
    :param max_fuzzy_level: Maximum fuzziness level to be used.
    :type max_fuzzy_level: int
    :param idx_set: A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type idx_set: str
    :param view: Geopolitical View.
    :type view: str

    """
    return web.Response(status=200)


async def search_version_number_poi_search_query_ext_get(request: web.Request, version_number, query, ext, typeahead=None, limit=None, ofs=None, country_set=None, lat=None, lon=None, radius=None, top_left=None, btm_right=None, language=None, extended_postal_codes_for=None, view=None) -> web.Response:
    """Points of Interest Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
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


async def search_version_number_routed_search_query_position_heading_ext_get(request: web.Request, version_number, query, position, heading, ext, typeahead=None, limit=None, multiplier=None, routing_timeout=None, language=None, extended_postal_codes_for=None, idx_set=None) -> web.Response:
    """Routed Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param position: This is specified as a comma separated string composed of lat., lon.
    :type position: str
    :param heading: The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    :type heading: float
    :param ext: Expected response format.
    :type ext: str
    :param typeahead: If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode.
    :type typeahead: bool
    :param limit: Maximum number of search results that will be returned.
    :type limit: int
    :param multiplier: Multiplies the limit by N to gather more candidate POIs, which will then be sorted by drive distance, returning only the top candidates according to the limit.
    :type multiplier: int
    :param routing_timeout: Only return results that arrive from routing engine within this time limit.
    :type routing_timeout: int
    :param language: Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive.
    :type language: str
    :param extended_postal_codes_for: Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type extended_postal_codes_for: str
    :param idx_set: A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type idx_set: str

    """
    return web.Response(status=200)


async def search_version_number_s_query_ext_get(request: web.Request, version_number, query, ext, typeahead=None, limit=None, ofs=None, country_set=None, lat=None, lon=None, radius=None, top_left=None, btm_right=None, language=None, idx_set=None, view=None) -> web.Response:
    """Low bandwith Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
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
    :param idx_set: A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type idx_set: str
    :param view: Geopolitical View.
    :type view: str

    """
    return web.Response(status=200)


async def search_version_number_search_along_route_query_ext_post(request: web.Request, version_number, query, ext, max_detour_time, limit=None, body=None) -> web.Response:
    """Along Route Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
    :param max_detour_time: Maximum detour time
    :type max_detour_time: int
    :param limit: Maximum number of search results that will be returned.
    :type limit: int
    :param body: 
    :type body: dict | bytes

    """
    body = SearchVersionNumberSearchAlongRouteQueryExtPostRequest.from_dict(body)
    return web.Response(status=200)


async def search_version_number_search_query_ext_get(request: web.Request, version_number, query, ext, typeahead=None, limit=None, ofs=None, country_set=None, lat=None, lon=None, radius=None, top_left=None, btm_right=None, language=None, extended_postal_codes_for=None, min_fuzzy_level=None, max_fuzzy_level=None, idx_set=None, view=None) -> web.Response:
    """Fuzzy Search

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param query: Query string. Must be properly URL encoded.  To perform a reverse geocode, the user can provide latitude and longitude coordinates directly in the query. More information can be found &lt;a href&#x3D;\&quot;/search-api/search-api-documentation-search/fuzzy-search#AdditionalInfo\&quot;&gt;here&lt;/a&gt;.
    :type query: str
    :param ext: Expected response format.
    :type ext: str
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
    :param min_fuzzy_level: Minimum fuzziness level to be used.
    :type min_fuzzy_level: int
    :param max_fuzzy_level: Maximum fuzziness level to be used.
    :type max_fuzzy_level: int
    :param idx_set: A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections)
    :type idx_set: str
    :param view: Geopolitical View.
    :type view: str

    """
    return web.Response(status=200)
