# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_request import CertificateRequest


pytestmark = pytest.mark.asyncio

async def test_get_certificate_pdf(client):
    """Test case for get_certificate_pdf

    Download the certificate in pdf format
    """
    body = {"mobile":"mobile","beneficiaryId":"beneficiaryId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/cert/external/pdf/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

