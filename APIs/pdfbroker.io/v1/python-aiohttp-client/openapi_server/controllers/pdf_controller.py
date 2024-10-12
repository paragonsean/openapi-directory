from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_pdf_pdfconcat_post_request import ApiPdfPdfconcatPostRequest
from openapi_server.models.api_pdf_pdftoimage_post_request import ApiPdfPdftoimagePostRequest
from openapi_server.models.api_pdf_pdfwritestring_post_request import ApiPdfPdfwritestringPostRequest
from openapi_server.models.api_pdf_xslfo_post_request import ApiPdfXslfoPostRequest
from openapi_server.models.api_pdf_xslfowithtransform_post_request import ApiPdfXslfowithtransformPostRequest
from openapi_server.models.error_response_dto import ErrorResponseDto
from openapi_server.models.fo_request_dto import FoRequestDto
from openapi_server.models.fo_transform_request_dto import FoTransformRequestDto
from openapi_server.models.image_response_dto import ImageResponseDto
from openapi_server.models.pdf_concatenation_request_dto import PdfConcatenationRequestDto
from openapi_server.models.pdf_response_dto import PdfResponseDto
from openapi_server.models.pdf_to_image_request_dto import PdfToImageRequestDto
from openapi_server.models.pdf_write_string_request_dto import PdfWriteStringRequestDto
from openapi_server.models.wk_html_to_pdf_request_dto import WkHtmlToPdfRequestDto
from openapi_server import util


async def api_pdf_get(request: web.Request, ) -> web.Response:
    """Basic method to verify api is up and running

    


    """
    return web.Response(status=200)


async def api_pdf_pdfconcat_post(request: web.Request, body=None) -> web.Response:
    """Concatenate multiple pdf files into single pdf file..

    

    :param body: PdfConcat Request. Add two or more pdf files and concatenate pages into single pdf document.
    :type body: dict | bytes

    """
    body = PdfConcatenationRequestDto.from_dict(body)
    return web.Response(status=200)


async def api_pdf_pdftoimage_post(request: web.Request, body=None) -> web.Response:
    """Generate an image of to provided pdf file

    

    :param body: PdfToImage Request. Create an image of a page in an existing pdf document.
    :type body: dict | bytes

    """
    body = PdfToImageRequestDto.from_dict(body)
    return web.Response(status=200)


async def api_pdf_pdfwritestring_post(request: web.Request, body=None) -> web.Response:
    """Write text on a page in a pdf document.

    

    :param body: PdfWriteString Request. Write string on page in pdf document
    :type body: dict | bytes

    """
    body = PdfWriteStringRequestDto.from_dict(body)
    return web.Response(status=200)


async def api_pdf_wkhtmltopdf_post(request: web.Request, body=None) -> web.Response:
    """Generate pdf file from url using the excellent tool wkhtmltopdf.

    

    :param body: WkHtmlToPdf Request. Generate pdf from html, either from url or base64 encoded html string
    :type body: dict | bytes

    """
    body = WkHtmlToPdfRequestDto.from_dict(body)
    return web.Response(status=200)


async def api_pdf_xslfo_post(request: web.Request, body=None) -> web.Response:
    """Create pdf-file from complete XSL-FO document.

    

    :param body: XSL-FO Request, the basic XSL-FO request. Post your XSL-FO document and digital resources, either as &#39;multipart/form-data&#39; or &#39;application/json&#39;
    :type body: dict | bytes

    """
    body = FoRequestDto.from_dict(body)
    return web.Response(status=200)


async def api_pdf_xslfowithtransform_post(request: web.Request, body=None) -> web.Response:
    """Create pdf-file from transforming xml document with Xsl-Fo transform document.

    

    :param body: XSL-FO Transform Request. The XSL-FO is transformed on the supplied xml data document. Post your XSL-FO transform document and xml data document aloing with your digital resources, either as &#39;multipart/form-data&#39; or &#39;application/json&#39;
    :type body: dict | bytes

    """
    body = FoTransformRequestDto.from_dict(body)
    return web.Response(status=200)
