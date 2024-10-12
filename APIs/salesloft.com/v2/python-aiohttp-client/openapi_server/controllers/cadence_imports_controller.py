from typing import List, Dict
from aiohttp import web

from openapi_server.models.cadence_import import CadenceImport
from openapi_server import util


async def v2_cadence_imports_json_post(request: web.Request, cadence_content=None, settings=None, sharing_settings=None) -> web.Response:
    """Import cadences from JSON

    New cadences can be created or steps can be imported onto existing cadences which do not have steps. &lt;a href&#x3D;\&quot;/cadence-imports.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;Visit here for more details&lt;/a&gt;. 

    :param cadence_content: Import data for cadence
    :type cadence_content: dict | bytes
    :param settings: Settings for a cadence
    :type settings: dict | bytes
    :param sharing_settings: The shared settings for a cadence
    :type sharing_settings: dict | bytes

    """
    cadence_content = object.from_dict(cadence_content)
    settings = object.from_dict(settings)
    sharing_settings = object.from_dict(sharing_settings)
    return web.Response(status=200)
