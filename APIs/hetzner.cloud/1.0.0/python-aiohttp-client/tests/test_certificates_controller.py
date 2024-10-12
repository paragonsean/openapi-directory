# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.certificates_response import CertificatesResponse
from openapi_server.models.create_certificate_request import CreateCertificateRequest
from openapi_server.models.create_certificate_response import CreateCertificateResponse
from openapi_server.models.update_certificate_request import UpdateCertificateRequest


pytestmark = pytest.mark.asyncio

async def test_certificates_get(client):
    """Test case for certificates_get

    Get all Certificates
    """
    params = [('sort', 'sort_example'),
                    ('name', 'name_example'),
                    ('label_selector', 'label_selector_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_id_delete(client):
    """Test case for certificates_id_delete

    Delete a Certificate
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/certificates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_id_get(client):
    """Test case for certificates_id_get

    Get a Certificate
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_id_put(client):
    """Test case for certificates_id_put

    Update a Certificate
    """
    body = {"name":"my website cert","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/certificates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_post(client):
    """Test case for certificates_post

    Create a Certificate
    """
    body = {"certificate":"-----BEGIN CERTIFICATE-----\n...","name":"my website cert","private_key":"-----BEGIN PRIVATE KEY-----\n...","type":"uploaded","domain_names":["domain_names","domain_names"],"labels":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

