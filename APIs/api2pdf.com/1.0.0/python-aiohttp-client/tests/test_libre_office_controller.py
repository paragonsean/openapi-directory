# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response_failure import ApiResponseFailure
from openapi_server.models.api_response_success import ApiResponseSuccess
from openapi_server.models.libre_office_convert_request import LibreOfficeConvertRequest


pytestmark = pytest.mark.asyncio

async def test_libre_convert_post(client):
    """Test case for libre_convert_post

    Convert office document or image to PDF
    """
    body = {"fileName":"test.pdf","inlinePdf":True,"url":"https://www.api2pdf.com/wp-content/themes/api2pdf/assets/samples/sample-word-doc.docx"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/libreoffice/convert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

