from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response_failure import ApiResponseFailure
from openapi_server.models.api_response_success import ApiResponseSuccess
from openapi_server.models.libre_office_convert_request import LibreOfficeConvertRequest
from openapi_server import util


async def libre_convert_post(request: web.Request, body=None) -> web.Response:
    """Convert office document or image to PDF

    Convert an office document (Word, Excel, Powerpoint) or an image (jpg, gif, png) to a PDF using LibreOffice on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

    :param body: A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;url&#x60; *(string, required)* - A direct URL to the file. Api2Pdf will consume the file at that URL and then convert it. - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. 
    :type body: dict | bytes

    """
    body = LibreOfficeConvertRequest.from_dict(body)
    return web.Response(status=200)
