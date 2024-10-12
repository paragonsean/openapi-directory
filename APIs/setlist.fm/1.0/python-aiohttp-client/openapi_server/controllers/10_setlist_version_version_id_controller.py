from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_setlist import JsonSetlist
from openapi_server import util


async def resource10_setlist_version_version_id_get_setlist_version_get(request: web.Request, version_id) -> web.Response:
    """.

    &lt;p&gt; Returns a setlist for the given versionId. The setlist returned isn&#39;t necessarily the most recent version. E.g. if you pass the versionId of a setlist that got edited since you last accessed it, you&#39;ll get the same version as last time. &lt;/p&gt;

    :param version_id: the version id
    :type version_id: str

    """
    return web.Response(status=200)
