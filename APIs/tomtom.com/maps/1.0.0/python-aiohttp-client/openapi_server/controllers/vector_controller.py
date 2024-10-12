from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def map_version_number_tile_layer_style_zoom_xy_pbf_get(request: web.Request, version_number, layer, style, zoom, x, y, view=None, language=None) -> web.Response:
    """Tile

    The Maps API Vector Service delivers vector tiles, which are representations of square sections of map data.

    :param version_number: Version of the service to call. The current version is 1
    :type version_number: int
    :param layer: Layer of tile to be rendered
    :type layer: str
    :param style: Style of tile to be rendered
    :type style: str
    :param zoom: Zoom level of tile to be rendered
    :type zoom: int
    :param x: x coordinate of tile on zoom grid
    :type x: int
    :param y: y coordinate of tile on zoom grid
    :type y: int
    :param view: Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-vector/tile\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services.
    :type view: str
    :param language: Language to be used for labels in the response. The default is NGT: Neutral Ground Truth, which uses each place&#39;s local official language and script (where available). See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-vector/tile\&quot;&gt;documentation&lt;/a&gt; for a full list of options.
    :type language: str

    """
    return web.Response(status=200)
