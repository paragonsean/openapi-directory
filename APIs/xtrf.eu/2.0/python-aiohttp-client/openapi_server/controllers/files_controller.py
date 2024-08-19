from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def upload_file(request: web.Request, file=None) -> web.Response:
    """Uploads a temporary file (ie. for XML import). Returns token which can be used in other API calls.

    When a file is required by an operation (ie. task creation) it must be uploaded previously to the API. Uploading a file will result in a file token, which can be used to reference this file in other API calls.  Each file must be uploaded separately.  Keep in mind that file token has limited validity (ie. 10 minutes).  Therefore files must be uploaded just before issuing API call which reference them. 

    :param file: 
    :type file: str

    """
    return web.Response(status=200)
