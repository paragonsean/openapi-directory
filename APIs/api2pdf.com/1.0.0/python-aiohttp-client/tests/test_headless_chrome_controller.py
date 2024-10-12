# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response_failure import ApiResponseFailure
from openapi_server.models.api_response_success import ApiResponseSuccess
from openapi_server.models.chrome_html_to_pdf_request import ChromeHtmlToPdfRequest
from openapi_server.models.chrome_url_to_pdf_request import ChromeUrlToPdfRequest


pytestmark = pytest.mark.asyncio

async def test_chrome_from_html_post(client):
    """Test case for chrome_from_html_post

    Convert raw HTML to PDF
    """
    body = {"fileName":"test.pdf","inlinePdf":True,"options":{"printBackground":False,"landscape":"true"},"html":"<p>Hello World</p>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/chrome/html',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chrome_from_url_get(client):
    """Test case for chrome_from_url_get

    Convert URL to PDF
    """
    params = [('url', 'url_example'),
                    ('output', 'output_example')]
    headers = { 
        'Accept': 'application/json',
        'QueryApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/chrome/url',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chrome_from_url_post(client):
    """Test case for chrome_from_url_post

    Convert URL to PDF
    """
    body = {"fileName":"test.pdf","inlinePdf":True,"options":{"printBackground":False,"landscape":"true"},"url":"https://www.github.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/chrome/url',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

