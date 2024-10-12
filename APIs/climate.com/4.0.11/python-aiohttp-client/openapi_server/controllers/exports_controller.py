from typing import List, Dict
from aiohttp import web

from openapi_server.models.created_export import CreatedExport
from openapi_server.models.error import Error
from openapi_server.models.export import Export
from openapi_server.models.export_contents import ExportContents
from openapi_server.models.export_status import ExportStatus
from openapi_server import util


async def fetch_export_contents_by_id(request: web.Request, accept, export_id, range) -> web.Response:
    """Retrieve the binary contents of a processed export request.

    Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).

    :param accept: Must be either \\*/* or application/octet-stream,application/json
    :type accept: str
    :param export_id: Unique identifier of an Export.
    :type export_id: str
    :type export_id: str
    :param range: Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    :type range: str

    """
    return web.Response(status=200)


async def fetch_export_status_by_id(request: web.Request, export_id) -> web.Response:
    """Retrieve the status of an Export.

    Check the status of an **Export** by ID.

    :param export_id: Unique identifier of an Export.
    :type export_id: str
    :type export_id: str

    """
    return web.Response(status=200)


async def post_export(request: web.Request, body=None) -> web.Response:
    """Initiate a new export request.

    Step one in requesting a data product. The method will return an **Export** ID which the caller will use in subsequent &#x60;GET&#x60; requests. The following &#x60;contentTypes&#x60; may be requested:   * __application/vnd.climate.acrsi.geojson__ (Beta)      Exports the planting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * plantingStartDate        * plantingEndDate        * resourceOwnerId       Requires &#x60;exports:read&#x60; and &#x60;plantingActivitySummary:read&#x60; scope.      * __application/vnd.climate.harvest.geojson__      Exports the harvesting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * harvestStartDate        * harvestEndDate        * resourceOwnerId       Requires &#x60;exports:read&#x60; and &#x60;plantingActivitySummary:read&#x60; scope.

    :param body: 
    :type body: dict | bytes

    """
    body = Export.from_dict(body)
    return web.Response(status=200)
