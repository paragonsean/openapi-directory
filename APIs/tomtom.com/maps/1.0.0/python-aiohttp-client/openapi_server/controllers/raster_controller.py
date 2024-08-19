from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def map_version_number_staticimage_get(request: web.Request, version_number, layer=None, style=None, format=None, zoom=None, center=None, width=None, height=None, bbox=None, view=None) -> web.Response:
    """Static Image

    The Static Image service renders a rectangular raster image in the style, size, and zoom level specified. The image can be requested using either a center point plus width and height or a bounding box.

    :param version_number: Version of the service to call. The current version is 1.
    :type version_number: int
    :param layer: Layer of image to be rendered. &lt;em&gt;Hybrid&lt;/em&gt; and &lt;em&gt;labels&lt;/em&gt; are intended for layering with other data and are only available in &lt;em&gt;png&lt;/em&gt; format.
    :type layer: str
    :param style: Map style to be returned
    :type style: str
    :param format: Image format to be returned
    :type format: str
    :param zoom: Zoom level of map image to be returned.
    :type zoom: int
    :param center: Coordinates for the center point of the image. Must be used with the &lt;strong&gt;width&lt;/strong&gt; and &lt;strong&gt;height&lt;/strong&gt; parameters; cannot be used with &lt;strong&gt;bbox&lt;/strong&gt;. Uses EPSG:3857 projection (functionally equivalent to EPSG:900910).
    :type center: str
    :param width: Width of the resulting image in pixels. Width must be a positive integer between 1 and 8192.
    :type width: int
    :param height: Height of the resulting image in pixels. Height must be a positive integer between 1 and 8192.
    :type height: int
    :param bbox: Bounding box for the image, using EPSG:3857 projection (functionally equivalent to EPSG:900910). Values &lt;strong&gt;must&lt;/strong&gt; be in the order of minLon, minLat, maxLon, maxLat. MaxLat must be greater than minLat. Longitude values can be on both sides of the 180th meridian. Cannot be used with &lt;strong&gt;center&lt;/strong&gt;, &lt;strong&gt;width&lt;/strong&gt;, or &lt;strong&gt;height&lt;/strong&gt; parameters.
    :type bbox: str
    :param view: Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-raster/raster-tile\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services.
    :type view: str

    """
    return web.Response(status=200)


async def map_version_number_tile_layer_style_zoom_xy_format_get(request: web.Request, version_number, layer, style, zoom, x, y, format, tile_size=None, view=None) -> web.Response:
    """Tile

    The Maps API Raster Service delivers raster tiles, which are representations of square sections of map data.

    :param version_number: Version of the service to call. The current version is 1.
    :type version_number: int
    :param layer: Layer of tile to be rendered. &lt;em&gt;Hybrid&lt;/em&gt; and &lt;em&gt;labels&lt;/em&gt; are intended for layering with other data and are only available in &lt;em&gt;png&lt;/em&gt; format.
    :type layer: str
    :param style: Style of tile to be rendered
    :type style: str
    :param zoom: Zoom level of tile to be rendered
    :type zoom: int
    :param x: x coordinate of tile on zoom grid
    :type x: int
    :param y: y coordinate of tile on zoom grid
    :type y: int
    :param format: Format of the response.
    :type format: str
    :param tile_size: Tile dimensions in pixels. &lt;em&gt;512&lt;/em&gt; is only available for the &lt;em&gt;main&lt;/em&gt; style and &lt;em&gt;basic&lt;/em&gt; or &lt;em&gt;labels&lt;/em&gt; layers.
    :type tile_size: int
    :param view: Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-sdk-web/functional-examples#geopolitical-views\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services.
    :type view: str

    """
    return web.Response(status=200)
