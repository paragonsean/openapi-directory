from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response_failure import ApiResponseFailure
from openapi_server.models.api_response_success import ApiResponseSuccess
from openapi_server.models.wk_html_to_pdf_html_to_pdf_request import WkHtmlToPdfHtmlToPdfRequest
from openapi_server.models.wk_html_to_pdf_url_to_pdf_request import WkHtmlToPdfUrlToPdfRequest
from openapi_server import util


async def wkhtmltopdf_from_html_post(request: web.Request, body=None) -> web.Response:
    """Convert raw HTML to PDF

    Convert HTML to a PDF using WkHtmlToPdf on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

    :param body: A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;html&#x60; *(string, required)* - raw HTML to convert to PDF - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - &#x60;options&#x60; *(object, optional)* - Include advanced WkHtmlToPdf options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-wkhtmltopdf/).
    :type body: dict | bytes

    """
    body = WkHtmlToPdfHtmlToPdfRequest.from_dict(body)
    return web.Response(status=200)


async def wkhtmltopdf_from_url_get(request: web.Request, url, output=None) -> web.Response:
    """Convert URL to PDF

    Convert a URL or Web Page to PDF using WkHtmlToPdf on AWS Lambda. This GET request is for convenience and does not support advanced options. Use the POST request for more flexibility. ### Authorize via Query String Parameter **apikey&#x3D;YOUR-API-KEY** ### Example &#x60;&#x60;&#x60; https://v2018.api2pdf.com/wkhtmltopdf/url?url&#x3D;{UrlToConvert}&amp;apikey&#x3D;{YourApiKey} &#x60;&#x60;&#x60; 

    :param url: Url of the page to convert to PDF. Must start with http:// or https://.
    :type url: str
    :param output: Specify output&#x3D;json to receive a JSON output. Defaults to PDF file.
    :type output: str

    """
    return web.Response(status=200)


async def wkhtmltopdf_from_url_post(request: web.Request, body=None) -> web.Response:
    """Convert URL to PDF

    Convert a URL or Web Page to PDF using WkHtmlToPdf on AWS Lambda.. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

    :param body: A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;url&#x60; *(string, required)* - Url to the web page to convert to PDF - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - &#x60;options&#x60; *(object, optional)* - Include advanced WkHtmlToPdf options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-wkhtmltopdf/).
    :type body: dict | bytes

    """
    body = WkHtmlToPdfUrlToPdfRequest.from_dict(body)
    return web.Response(status=200)
