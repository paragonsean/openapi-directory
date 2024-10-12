# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_api_pdf_get(client):
    """Test case for api_pdf_get

    Basic method to verify api is up and running
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pdf',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_pdf_pdfconcat_post(client):
    """Test case for api_pdf_pdfconcat_post

    Concatenate multiple pdf files into single pdf file..
    """
    body = {"pdfDocumentsAsBase64String":["pdfDocumentsAsBase64String","pdfDocumentsAsBase64String"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pdf/pdfconcat',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_pdf_pdftoimage_post(client):
    """Test case for api_pdf_pdftoimage_post

    Generate an image of to provided pdf file
    """
    body = {"pdfFileBase64String":"pdfFileBase64String","options":{"imageFormat":"imageFormat","jpegQuality":1,"horizontalResolution":6.027456183070403,"pageNumber":5,"verticalResolution":2.3021358869347655,"width":7,"transparent":True,"height":0,"pngCompressionLevel":5}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pdf/pdftoimage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_pdf_pdfwritestring_post(client):
    """Test case for api_pdf_pdfwritestring_post

    Write text on a page in a pdf document.
    """
    body = {"pdfFileBase64String":"pdfFileBase64String","options":{"xPosition":9.301444,"pageNumber":1,"yOrigin":3,"yPosition":2.027123,"text":"text","xOrigin":7,"textColor":{"b":152,"r":58,"g":143},"font":{"size":0.8008282,"name":"name","style":6}},"fontFileBase64String":"fontFileBase64String"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pdf/pdfwritestring',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_pdf_wkhtmltopdf_post(client):
    """Test case for api_pdf_wkhtmltopdf_post

    Generate pdf file from url using the excellent tool wkhtmltopdf.
    """
    body = {"wkHtmlToPdfArguments":{"key":"wkHtmlToPdfArguments"},"htmlBase64String":"htmlBase64String","resources":{"key":"resources"},"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pdf/wkhtmltopdf',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_pdf_xslfo_post(client):
    """Test case for api_pdf_xslfo_post

    Create pdf-file from complete XSL-FO document.
    """
    body = {"metadata":{"ownerPassword":"ownerPassword","enablePrinting":True,"userPassword":"userPassword","keywords":["keywords","keywords"],"author":"author","subject":"subject","enableAdd":True,"enableCopy":True,"enableModify":True,"title":"title"},"foDocumentBase64String":"foDocumentBase64String","resources":{"key":"resources"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pdf/xslfo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_pdf_xslfowithtransform_post(client):
    """Test case for api_pdf_xslfowithtransform_post

    Create pdf-file from transforming xml document with Xsl-Fo transform document.
    """
    body = {"xmlDataDocumentBase64String":"xmlDataDocumentBase64String","metadata":{"ownerPassword":"ownerPassword","enablePrinting":True,"userPassword":"userPassword","keywords":["keywords","keywords"],"author":"author","subject":"subject","enableAdd":True,"enableCopy":True,"enableModify":True,"title":"title"},"foDocumentBase64String":"foDocumentBase64String","resources":{"key":"resources"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pdf/xslfowithtransform',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

