from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def geomarks_copy_post(request: web.Request, geomark_url, result_format=None, allow_overlap=None, param_callback=None, redirect_url=None, failure_redirect_url=None, buffer_metres=None, buffer_join=None, buffer_cap=None, buffer_mitre_limit=None, buffer_segments=None) -> web.Response:
    """Create a new geomark by copying the geometries from one or more existing geomarks from the current server.

    The source geomarks can be specified by with the geomarkUrl parameter.  Repeat the parameter if sourcing from multiple geomarks

    :param geomark_url: One or more geomark URLs or identifiers to create the new geomark from.
    :type geomark_url: str
    :param result_format: The file format the geomark info resource should be returned using.
    :type result_format: str
    :param allow_overlap: Select this option to allow overlapping geometries
    :type allow_overlap: bool
    :param param_callback: The callback function a JSON result format would be wrapped in to support Ajax requests.
    :type param_callback: str
    :param redirect_url: The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark.
    :type redirect_url: str
    :param failure_redirect_url: The url to redirect if the geomark could not be created. The URL will include a &lt;fieldName&gt;_Error parameter with the error message for the field that caused the error.
    :type failure_redirect_url: str
    :param buffer_metres: The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored.
    :type buffer_metres: int
    :param buffer_join: If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons.
    :type buffer_join: str
    :param buffer_cap: If bufferMetres is specified, The style of buffer to use at the ends of a buffered line.
    :type buffer_cap: str
    :param buffer_mitre_limit: If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be &gt; 0.
    :type buffer_mitre_limit: int
    :param buffer_segments: If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be &gt; 0.
    :type buffer_segments: int

    """
    return web.Response(status=200)


async def geomarks_new_post(request: web.Request, allow_overlap=None, body=None, buffer_cap=None, buffer_join=None, buffer_metres=None, buffer_mitre_limit=None, buffer_segments=None, param_callback=None, failure_redirect_url=None, format=None, multiple=None, redirect_url=None, result_format=None, srid=None) -> web.Response:
    """Create a new geomark

    Create a new geomark from the geometries read from the &#39;body&#39; parameter or file.

    :param allow_overlap: When multiple&#x3D;true select this option to allow overlapping geometries
    :type allow_overlap: bool
    :param body: The binary or character content representing the geometry or geometries
    :type body: str
    :param buffer_cap: If bufferMetres is specified, The style of buffer to use at the ends of a buffered line.
    :type buffer_cap: str
    :param buffer_join: If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons.
    :type buffer_join: str
    :param buffer_metres: The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored.
    :type buffer_metres: int
    :param buffer_mitre_limit: If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be &gt; 0.
    :type buffer_mitre_limit: int
    :param buffer_segments: If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be &gt; 0.
    :type buffer_segments: int
    :param param_callback: The callback function a JSON result format would be wrapped in to support Ajax requests.
    :type param_callback: str
    :param failure_redirect_url: The url to redirect if the geomark could not be created. The URL will include a &lt;fieldName&gt;_Error parameter with the error message for the field that caused the error.
    :type failure_redirect_url: str
    :param format: The file format name extension of the input geometry.
    :type format: str
    :param multiple: Boolean flag indicating if multiple geometries are to be used for the geomark (true) or only a single geometry from the first geometry (false).
    :type multiple: bool
    :param redirect_url: The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark.
    :type redirect_url: str
    :param result_format: The file format the geomark info resource should be returned using.
    :type result_format: str
    :param srid: The srid of the coordinate system the input geometries are in. If the file includes a coordinate system definition that will be used.
    :type srid: int

    """
    return web.Response(status=200)
