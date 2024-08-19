from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def addresses_output_format_get_0(request: web.Request, output_format, address_string=None, location_descriptor=None, max_results=None, interpolation=None, echo=None, brief=None, auto_complete=None, set_back=None, output_srs=None, min_score=None, match_precision=None, match_precision_not=None, site_name=None, unit_designator=None, unit_number=None, unit_number_suffix=None, civic_number=None, civic_number_suffix=None, street_name=None, street_type=None, street_direction=None, street_qualifier=None, locality_name=None, province_code=None, localities=None, not_localities=None, bbox=None, centre=None, max_distance=None, extrapolate=None, parcel_point=None) -> web.Response:
    """Geocode an address

    Represents the set of geocoded and standardized sites and intersections whose address best matches a given query address.

    :param output_format: Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326)
    :type output_format: str
    :param address_string: Civic or intersection address as a single string. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#addressString target&#x3D;\&quot;_blank\&quot;&gt;addressString&lt;/a&gt;
    :type address_string: str
    :param location_descriptor: Describes the nature of the address location. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target&#x3D;\&quot;_blank\&quot;&gt;locationDescriptor&lt;/a&gt;
    :type location_descriptor: str
    :param max_results: The maximum number of search results to return.
    :type max_results: int
    :param interpolation: accessPoint interpolation method. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#interpolation target&#x3D;\&quot;_blank\&quot;&gt;interpolation&lt;/a&gt;
    :type interpolation: str
    :param echo: If true, include unmatched address details such as site name in results.
    :type echo: bool
    :param brief: If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats.
    :type brief: bool
    :param auto_complete: If true, addressString is expected to contain a partial address that requires completion. Not supported for shp, csv, gml formats.
    :type auto_complete: bool
    :param set_back: The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    :type set_back: int
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param min_score: The minimum score required for a match to be returned. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#minScore target&#x3D;\&quot;_blank\&quot;&gt;minScore&lt;/a&gt;
    :type min_score: int
    :param match_precision: Example: street,locality.  A comma separated list of individual match precision levels to include in results. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecision target&#x3D;\&quot;_blank\&quot;&gt;matchPrecision&lt;/a&gt;
    :type match_precision: str
    :param match_precision_not: Example: street,locality.  A comma separated list of individual match precision levels to exclude from results. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecisionNot target&#x3D;\&quot;_blank\&quot;&gt;matchPrecisionNot&lt;/a&gt;
    :type match_precision_not: str
    :param site_name: A string containing the name of the building, facility, or institution (e.g., Duck Building, Casa Del Mar, Crystal Garden, Bluebird House).See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#siteName target&#x3D;\&quot;_blank\&quot;&gt;siteName&lt;/a&gt;
    :type site_name: str
    :param unit_designator: The type of unit within a house or building. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#unitDesignator target&#x3D;\&quot;_blank\&quot;&gt;unitDesignator&lt;/a&gt;
    :type unit_designator: str
    :param unit_number: The number of the unit, suite, or apartment within a house or building.
    :type unit_number: str
    :param unit_number_suffix: A letter that follows the unit number as in Unit 1A or Suite 302B.
    :type unit_number_suffix: str
    :param civic_number: The official number assigned to a site by an address authority. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumber target&#x3D;\&quot;_blank\&quot;&gt;civicNumber&lt;/a&gt;
    :type civic_number: str
    :param civic_number_suffix: A letter or fraction that follows the civic number (e.g., the A in 1039A Bledsoe St). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumberSuffix target&#x3D;\&quot;_blank\&quot;&gt;civicNumberSuffix&lt;/a&gt;
    :type civic_number_suffix: str
    :param street_name: The official name of the street as assigned by an address authority (e.g., the Douglas in 1175 Douglas Street). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetName target&#x3D;\&quot;_blank\&quot;&gt;streetName&lt;/a&gt;
    :type street_name: str
    :param street_type: The type of street as assigned by a municipality (e.g., the ST in 1175 DOUGLAS St). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetType target&#x3D;\&quot;_blank\&quot;&gt;streetType&lt;/a&gt;
    :type street_type: str
    :param street_direction: The abbreviated compass direction as defined by Canada Post and B.C. civic addressing authorities. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetDirection target&#x3D;\&quot;_blank\&quot;&gt;streetDirection&lt;/a&gt;
    :type street_direction: str
    :param street_qualifier: Example: the Bridge in Johnson St Bridge. The qualifier of a street name. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetQualifier target&#x3D;\&quot;_blank\&quot;&gt;streetQualifier&lt;/a&gt;
    :type street_qualifier: str
    :param locality_name: The name of the locality assigned to a given site by an address authority. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#localityName target&#x3D;\&quot;_blank\&quot;&gt;localityName&lt;/a&gt;
    :type locality_name: str
    :param province_code: The ISO 3166-2 Sub-Country Code. The code for British Columbia is BC.
    :type province_code: str
    :param localities: A comma separated list of locality names that matched addresses must belong to. For example, setting localities to Nanaimo only returns addresses in Nanaimo
    :type localities: str
    :param not_localities: A comma-separated list of localities to exclude from the search.
    :type not_localities: str
    :param bbox: Example: -126.07929,49.7628,-126.0163,49.7907.  A bounding box (xmin,ymin,xmax,ymax) that limits the search area. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target&#x3D;\&quot;_blank\&quot;&gt;bbox&lt;/a&gt;
    :type bbox: str
    :param centre: Example: -124.0165926,49.2296251 .  The coordinates of a centre point (x,y) used to define a bounding circle that will limit the search area. This parameter must be specified together with &#39;maxDistance&#39;. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#centre target&#x3D;&#39;_blank&#39;&gt;centre&lt;/a&gt;
    :type centre: str
    :param max_distance: The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
    :type max_distance: 
    :param extrapolate: If true, uses supplied parcelPoint to derive an appropriate accessPoint.           See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#extrapolate target&#x3D;\&quot;_blank\&quot;&gt;extrapolate&lt;/a&gt;
    :type extrapolate: bool
    :param parcel_point: The coordinates of a point (x,y) known to be inside the parcel containing a given address. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#parcelPoint target&#x3D;\&quot;_blank\&quot;&gt;parcelPoint&lt;/a&gt;
    :type parcel_point: str

    """
    return web.Response(status=200)


async def intersections_intersection_id_output_format_get(request: web.Request, intersection_id, output_format, output_srs=None) -> web.Response:
    """Get an intersection by its unique ID

    Represents a individual intersection

    :param intersection_id: A unique intersection identifier
    :type intersection_id: str
    :param output_format: Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326)
    :type output_format: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int

    """
    return web.Response(status=200)


async def intersections_near_output_format_get(request: web.Request, output_format, point, output_srs, max_distance=None, max_results=None, min_degree=None, max_degree=None) -> web.Response:
    """Find intersections near to a geographic point

    Represents intersections near a given point

    :param output_format: Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326)
    :type output_format: str
    :param point: The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the &#39;outputSRS&#39; parameter.
    :type point: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param max_distance: The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
    :type max_distance: int
    :param max_results: The maximum number of search results to return.
    :type max_results: int
    :param min_degree: The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1.
    :type min_degree: int
    :param max_degree: The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4.
    :type max_degree: int

    """
    return web.Response(status=200)


async def intersections_nearest_output_format_get(request: web.Request, output_format, point, max_distance=None, output_srs=None, min_degree=None, max_degree=None) -> web.Response:
    """Find nearest intersection to a geographic point

    Represents the closest intersection to a given point

    :param output_format: Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326)
    :type output_format: str
    :param point: Example: -122.377,50.121  The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the &#39;outputSRS&#39; parameter.
    :type point: str
    :param max_distance: The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
    :type max_distance: int
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param min_degree: The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1.
    :type min_degree: int
    :param max_degree: The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4.
    :type max_degree: int

    """
    return web.Response(status=200)


async def intersections_within_output_format_get(request: web.Request, output_format, bbox, output_srs=None, max_results=None, min_degree=None, max_degree=None) -> web.Response:
    """Find intersections in a geographic area

    Represents all intersections within a given area

    :param output_format: Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326)
    :type output_format: str
    :param bbox: A bounding box (xmin,ymin,xmax,ymax) used to limit the search area. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target&#x3D;\&quot;_blank\&quot;&gt;bbox&lt;/a&gt;
    :type bbox: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param max_results: The maximum number of search results
    :type max_results: int
    :param min_degree: The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1.
    :type min_degree: int
    :param max_degree: The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4.
    :type max_degree: int

    """
    return web.Response(status=200)
