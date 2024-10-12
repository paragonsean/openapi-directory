from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.facilities_ids_response import FacilitiesIdsResponse
from openapi_server.models.facilities_response import FacilitiesResponse
from openapi_server.models.facility_read_response import FacilityReadResponse
from openapi_server.models.generic_error import GenericError
from openapi_server.models.geo_facilities_response import GeoFacilitiesResponse
from openapi_server.models.geo_facility_read_response import GeoFacilityReadResponse
from openapi_server.models.nearby_response import NearbyResponse
from openapi_server import util


async def get_all_facilities(request: web.Request, accept) -> web.Response:
    """Bulk download information for all facilities

    Retrieve all available facilities in a single operation, formatted as either a GeoJSON FeatureCollection or as a CSV. Due to the complexity of the facility resource type, the CSV response contains a subset of available facility data - specifically it omits the available services, patient satisfaction, and patient wait time data.

    :param accept: 
    :type accept: str

    """
    return web.Response(status=200)


async def get_facilities_by_location(request: web.Request, ids=None, zip=None, state=None, lat=None, long=None, radius=None, bbox=None, visn=None, type=None, services=None, mobile=None, page=None, per_page=None) -> web.Response:
    """Query facilities by location or IDs, with optional filters

    Query facilities by bounding box, latitude and longitude, state, visn, or zip code. Bounding box is specified as four &#x60;bbox[]&#x60; parameters, long1, lat1, long2, lat2. (Relative order is unimportant.)  A query by latitude and longitude returns all facilities in the system, sorted by distance from that location. Providing an optional radius in miles to this query will narrow the scope of the returned facilities to those falling within the specified radius from that location.  All location queries support filtering by facility type, available services, and mobile status.  One can also retrieve facilities by ID using a comma-separated list like &#x60;?ids&#x3D;id1,id2&#x60;. When requesting multiple facilities by ID, the API will return as many results as it can find matches for, omitting IDs where there is no match. It will not return an HTTP error code if it is unable to match a requested ID. Clients may supply IDs up to the limit their HTTP client enforces for URI path lengths. (Usually 2048 characters.)  Results are paginated. JSON responses include pagination information in the standard JSON API \&quot;links\&quot; and \&quot;meta\&quot; elements.   ### Parameter combinations You may optionally specify &#x60;page&#x60; and &#x60;per_page&#x60; with any query. You must specify one of the following parameter combinations:   - &#x60;bbox[]&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;ids&#x60;  - &#x60;lat&#x60; and &#x60;long&#x60;, with the option of any combination of &#x60;radius&#x60;, &#x60;ids&#x60;, &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;state&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;visn&#x60;  - &#x60;zip&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;   Invalid combinations will return &#x60;400 Bad Request&#x60;. 

    :param ids: List of comma-separated facility IDs to retrieve in a single request. Can be combined with lat and long parameters to retrieve facilities sorted by distance from a location.
    :type ids: List[str]
    :param zip: Zip code to search for facilities. More detailed zip codes can be passed in, but only the first five digits are used to determine facilities to return.
    :type zip: str
    :param state: State in which to search for facilities. Except in rare cases, this is two characters.
    :type state: str
    :param lat: Latitude of point to search for facilities, in WGS84 coordinate reference system.
    :type lat: float
    :param long: Longitude of point to search for facilities, in WGS84 coordinate reference system.
    :type long: float
    :param radius: Optional radial distance from specified latitude and longitude to filter facilities search in WGS84 coordinate reference system.
    :type radius: float
    :param bbox: Bounding box (longitude, latitude, longitude, latitude) within which facilities will be returned. (WGS84 coordinate reference system)
    :type bbox: List[float]
    :param visn: VISN search of matching facilities.
    :type visn: 
    :param type: Optional facility type search filter
    :type type: str
    :param services: Optional facility service search filter
    :type services: List[str]
    :param mobile: Optional facility mobile search filter
    :type mobile: bool
    :param page: Page of results to return per paginated response.
    :type page: int
    :param per_page: Number of results to return per paginated response.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_facility_by_id(request: web.Request, id) -> web.Response:
    """Retrieve a specific facility by ID

    

    :param id: Facility ID, in the form &#x60;&lt;prefix&gt;_&lt;station&gt;&#x60;, where prefix is one of \&quot;vha\&quot;, \&quot;vba\&quot;, \&quot;nca\&quot;, or \&quot;vc\&quot;, for health facility, benefits, cemetery, or vet center, respectively.
    :type id: str

    """
    return web.Response(status=200)


async def get_facility_ids(request: web.Request, type=None) -> web.Response:
    """Bulk download of all facility IDs

    Retrieves all available facility IDs only

    :param type: Optional facility type search filter
    :type type: str

    """
    return web.Response(status=200)


async def get_nearby_facilities(request: web.Request, lat=None, lng=None, street_address=None, city=None, state=None, zip=None, drive_time=None, services=None) -> web.Response:
    """Retrieve all VA health facilities reachable by driving within the specified time period

    Retrieve all VA health facilities that are located within a specified drive time from a specified location based on coordinates (lat and lng). Optional filter parameters include drive_time and services[]. Address (street_address, city, state, and zip) no longer returns results.  The \&quot;attributes\&quot; element has information about the drive-time band that contains the requested location for each facility in the response. The values of &#x60;min_time&#x60; and &#x60;max_time&#x60; are in minutes. For example, a facility returned with a matched &#x60;min_time&#x60; of 10 and &#x60;max_time&#x60; of 20 is a 10 to 20 minute drive from the requested location.  To retrieve full details for nearby facilities, see the documentation for &#x60;/facilities?ids&#x60;.

    :param lat: Latitude of the location from which drive time will be calculated.
    :type lat: float
    :param lng: Longitude of the location from which drive time will be calculated.
    :type lng: float
    :param street_address: Street address of the location from which drive time will be calculated.
    :type street_address: str
    :param city: City of the location from which drive time will be calculated.
    :type city: str
    :param state: Two character state code of the location from which drive time will be calculated.
    :type state: str
    :param zip: Zip code of the location from which drive time will be calculated.
    :type zip: str
    :param drive_time: Filter to only include facilities that are within the specified number of drive time minutes from the requested location.
    :type drive_time: int
    :param services: Optional facility service search filter
    :type services: List[str]

    """
    return web.Response(status=200)
