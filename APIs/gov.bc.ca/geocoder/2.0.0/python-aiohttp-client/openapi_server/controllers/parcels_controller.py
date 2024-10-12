from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def parcels_pids_site_id_output_format_get(request: web.Request, site_id, output_format) -> web.Response:
    """Get a comma-separated string of all pids for a given site

    Represents all parcel identifiers associated with an individual site

    :param site_id: A unique, but not immutable, site identifier.
    :type site_id: str
    :param output_format: Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326)
    :type output_format: str

    """
    return web.Response(status=200)
