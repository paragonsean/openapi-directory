from typing import List, Dict
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.search_groups200_response import SearchGroups200Response
from openapi_server import util


async def get_group(request: web.Request, group_id) -> web.Response:
    """Retrieve a group

    

    :param group_id: The ID of the group to retrieve.
    :type group_id: str

    """
    return web.Response(status=200)


async def get_groups_by_ids(request: web.Request, group_ids) -> web.Response:
    """Retrieve multiple groups

    

    :param group_ids: The IDs of the groups to retrieve.  If more than 20 group IDs are passed, only the first 20 groups will be returned.
    :type group_ids: str

    """
    return web.Response(status=200)


async def search_groups(request: web.Request, name=None, latitude=None, longitude=None, distance=None, country=None, region=None, postal_code=None, page=None, per_page=None) -> web.Response:
    """Search groups

    

    :param name: Find groups that have the given text somewhere in their name (case insensitive).
    :type name: str
    :param latitude: Find groups near the given latitude and longitude.
    :type latitude: 
    :param longitude: Find groups near the given latitude and longitude.
    :type longitude: 
    :param distance: When latitude and longitude are passed, distance can optionally be passed to only return groups within a certain distance (in kilometers) from the point specified by the latitude and longitude.  The distance must be &gt; 0 and &lt;&#x3D; 150 and will default to 100. 
    :type distance: 
    :param country: Find groups in the given country where country is a 2 letter country code for the country (see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 ). 
    :type country: str
    :param region: For countries with regions (AU, CA, GB, US), search groups in a specific region as specified by the region abbreviation.  The supported regions and their abbreviations are listed below. &lt;br /&gt;&lt;br /&gt; NOTE: The region and postal_code parameters cannot be used at the same time and if both are passed then the postal_code will take priority. &lt;br /&gt;&lt;br /&gt; --- &lt;br /&gt;&lt;br /&gt; **AU**&lt;br /&gt; - QLD: Queensland&lt;br /&gt; - SA: South Australia&lt;br /&gt; - TAS: Tasmania&lt;br /&gt; - VIC: Victoria&lt;br /&gt; - WA: Western Australia&lt;br /&gt; - NT: Northern Territory&lt;br /&gt; - NSW: New South Wales - ACT&lt;br /&gt; &lt;br /&gt; **CA**&lt;br /&gt; - AB: Alberta&lt;br /&gt; - BC: British Columbia&lt;br /&gt; - MB: Manitoba&lt;br /&gt; - NB: New Brunswick&lt;br /&gt; - NL: Newfoundland and Labrador&lt;br /&gt; - NS: Nova Scotia&lt;br /&gt; - ON: Ontario&lt;br /&gt; - QC: Quebec&lt;br /&gt; - SK: Saskatchewan&lt;br /&gt; - PE: Prince Edward Island&lt;br /&gt; &lt;br /&gt; **GB**&lt;br /&gt; - E: East&lt;br /&gt; - EM: East Midlands&lt;br /&gt; - LDN: London&lt;br /&gt; - NE: North East&lt;br /&gt; - NW: North West&lt;br /&gt; - NI: Northern Ireland&lt;br /&gt; - SC: Scotland&lt;br /&gt; - SE: South East&lt;br /&gt; - SW: South West&lt;br /&gt; - WA: Wales&lt;br /&gt; - WM: West Midlands&lt;br /&gt; - YH: Yorkshire and the Humber&lt;br /&gt; &lt;br /&gt; **US**&lt;br /&gt; All 50 states and the District of Columbia are supported.  For the abbreviations, see: https://github.com/jasonong/List-of-US-States/blob/master/states.csv 
    :type region: str
    :param postal_code: Find groups in the given postal code.  Only a few countries support postal code searches (US, CA, AU, GB).  The country parameter must be passed when the postal_code parameter is set. &lt;br /&gt;&lt;br /&gt; NOTE: The region and postal_code parameters cannot be used at the same time and if both are passed then the postal_code will take priority. 
    :type postal_code: str
    :param page: The page of groups to return.
    :type page: int
    :param per_page: The number of groups to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100).
    :type per_page: int

    """
    return web.Response(status=200)
