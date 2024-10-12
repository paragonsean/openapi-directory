from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_result import DocumentResult
from openapi_server import util


async def extract_get(request: web.Request, ) -> web.Response:
    """Test api response without api key

    


    """
    return web.Response(status=200)


async def extract_post(request: web.Request, request_doc) -> web.Response:
    """Document extraction service

    Sample request:                    POST /Extract      {         \&quot;DocumentText\&quot;: \&quot;Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.\&quot;,         \&quot;PrivateKey\&quot;: \&quot;your_api_key\&quot;,         \&quot;UserCategoryModelName\&quot;: \&quot;your_model_name\&quot;,         \&quot;Secret\&quot;: \&quot;\&quot;      }

    :param request_doc: 
    :type request_doc: dict | bytes

    """
    request_doc = Document.from_dict(request_doc)
    return web.Response(status=200)
