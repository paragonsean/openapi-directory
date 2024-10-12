from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response_failure import ApiResponseFailure
from openapi_server.models.api_response_success import ApiResponseSuccess
from openapi_server.models.merge_request import MergeRequest
from openapi_server import util


async def merge_post(request: web.Request, body=None) -> web.Response:
    """Merge multiple PDFs together

    Merge two or more PDFs together on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

    :param body: A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;urls&#x60; *(array of urls, required)* - A JSON array of direct URLs to PDFs. Api2Pdf will consume the PDF files in the list and then merge them all together.. - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. 
    :type body: dict | bytes

    """
    body = MergeRequest.from_dict(body)
    return web.Response(status=200)
