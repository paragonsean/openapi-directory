from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_type_info import ArtifactTypeInfo
from openapi_server.models.error import Error
from openapi_server import util


async def list_artifact_types(request: web.Request, ) -> web.Response:
    """List artifact types

    Gets a list of all the configured artifact types.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)
