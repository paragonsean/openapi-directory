# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_ssl_certificate_request import CreateSslCertificateRequest
from openapi_server.models.ssl_certificate_request import SslCertificateRequest
from openapi_server.models.ssl_certificate_request_detail import SslCertificateRequestDetail


pytestmark = pytest.mark.asyncio

async def test_add_ssl_certificate_request(client):
    """Test case for add_ssl_certificate_request

    Add a SSL certificate request
    """
    body = {"additional_validation_attributes":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"csr":"csr","certificate_type":"standard","validation_level":"domain_validated"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/sslcertificaterequests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ssl_certificate_request(client):
    """Test case for get_ssl_certificate_request

    Detail of a SSL certificate request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/sslcertificaterequests/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ssl_certificate_requests(client):
    """Test case for get_ssl_certificate_requests

    Overview of SSL certificate requests
    """
    params = [('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/sslcertificaterequests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_ssl_certificate_request_domain_validations(client):
    """Test case for verify_ssl_certificate_request_domain_validations

    Verify the SSL certificate request domain validations
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/sslcertificaterequests/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

