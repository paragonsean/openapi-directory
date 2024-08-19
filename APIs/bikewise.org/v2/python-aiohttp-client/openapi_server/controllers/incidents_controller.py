from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def g_et_version_incidents_format(request: web.Request, page=None, per_page=None, occurred_before=None, occurred_after=None, incident_type=None, proximity=None, proximity_square=None, query=None) -> web.Response:
    """Paginated incidents matching parameters

     &lt;p&gt;If you’d like more detailed information about bike incidents, use this endpoint. For mapping, &lt;code&gt;locations&lt;/code&gt; is probably a better bet.&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Notes on location searching&lt;/strong&gt;: &lt;br /&gt; - &lt;code&gt;proximity&lt;/code&gt; accepts an ip address, an address, zipcode, city, or latitude,longitude - i.e. &lt;code&gt;70.210.133.87&lt;/code&gt;, &lt;code&gt;210 NW 11th Ave, Portland, OR&lt;/code&gt;, &lt;code&gt;60647&lt;/code&gt;, &lt;code&gt;Chicago, IL&lt;/code&gt;, and &lt;code&gt;45.521728,-122.67326&lt;/code&gt; are all acceptable&lt;br /&gt; - &lt;code&gt;proximity_square&lt;/code&gt; sets the length of the sides of the square to find matches inside of. The square is centered on the location specified by &lt;code&gt;proximity&lt;/code&gt;. It defaults to 100.&lt;/p&gt; 

    :param page: &lt;p&gt;Page of results to fetch.&lt;/p&gt; 
    :type page: int
    :param per_page: &lt;p&gt;Number of results to return per page.&lt;/p&gt; 
    :type per_page: int
    :param occurred_before: &lt;p&gt;End of period&lt;/p&gt; 
    :type occurred_before: int
    :param occurred_after: &lt;p&gt;Start of period&lt;/p&gt; 
    :type occurred_after: int
    :param incident_type: &lt;p&gt;Only incidents of specific type&lt;/p&gt; 
    :type incident_type: str
    :param proximity: &lt;p&gt;Center of location for proximity search&lt;/p&gt; 
    :type proximity: str
    :param proximity_square: &lt;p&gt;Size of the proximity search&lt;/p&gt; 
    :type proximity_square: int
    :param query: &lt;p&gt;Full text search of incidents&lt;/p&gt; 
    :type query: str

    """
    return web.Response(status=200)


async def g_et_version_incidents_id_format(request: web.Request, id) -> web.Response:
    """g_et_version_incidents_id_format

    

    :param id: &lt;p&gt;Incident ID&lt;/p&gt; 
    :type id: int

    """
    return web.Response(status=200)
