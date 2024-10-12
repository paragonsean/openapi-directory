from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def g_et_version_locations_format(request: web.Request, occurred_before=None, occurred_after=None, incident_type=None, proximity=None, proximity_square=None, query=None, limit=None, all=None) -> web.Response:
    """Unpaginated geojson response

    &lt;p&gt;&lt;strong&gt;This endpoint behaves exactly like&lt;/strong&gt; &lt;code&gt;incidents&lt;/code&gt;, but returns a valid geojson &lt;code&gt;FeatureCollection&lt;/code&gt; that looks like this:&lt;/p&gt;  &lt;pre&gt;&lt;code&gt;{   type: \&quot;FeatureCollection\&quot;,   features: [     {       type: \&quot;Feature\&quot;,       properties: {       id: 4474199,       type: \&quot;Theft\&quot;,       occurred_at: 1428536937     },       geometry: {       type: \&quot;Point\&quot;,       coordinates: [ -122.6244177, 45.5164386 ]     }   } } &lt;/code&gt;&lt;/pre&gt;  &lt;p&gt;It doesn’t paginate. If you pass the &lt;code&gt;all&lt;/code&gt; parameter it returns all matches (which can be big, &amp;gt; 4mb), otherwise it returns the 100 most recent.&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Go forth and make maps!&lt;/strong&gt;&lt;/p&gt; 

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
    :param limit: &lt;p&gt;Max number of results to return. Defaults to 100&lt;/p&gt; 
    :type limit: int
    :param all: &lt;p&gt;Give ‘em all to me. Will ignore limit&lt;/p&gt; 
    :type all: bool

    """
    return web.Response(status=200)


async def g_et_version_locations_markers_format(request: web.Request, occurred_before=None, occurred_after=None, incident_type=None, proximity=None, proximity_square=None, query=None, limit=None, all=None) -> web.Response:
    """Unpaginated geojson response with simplestyled markers

    &lt;p&gt;This behaves exactly like the root &lt;code&gt;locations&lt;/code&gt; endpoint, but returns &lt;a href&#x3D;\&quot;https://github.com/mapbox/simplestyle-spec\&quot;&gt;simplestyled markers&lt;/a&gt; (&lt;a href&#x3D;\&quot;https://www.mapbox.com/guides/markers/#simple-style\&quot;&gt;mapbox styled markers&lt;/a&gt;)&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Go forth and make maps!&lt;/strong&gt;&lt;/p&gt; 

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
    :param limit: &lt;p&gt;Max number of results to return. Defaults to 100&lt;/p&gt; 
    :type limit: int
    :param all: &lt;p&gt;Give ‘em all to me. Will ignore limit&lt;/p&gt; 
    :type all: bool

    """
    return web.Response(status=200)
