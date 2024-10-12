# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_import_request import CertificateImportRequest
from openapi_server.models.certificate_patch_request import CertificatePatchRequest
from openapi_server.models.certificate_summary import CertificateSummary
from openapi_server.models.certificate_summary_list_response import CertificateSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_delete_certificate(client):
    """Test case for delete_certificate

    Delete imported certificate object
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/certificate/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_certificate(client):
    """Test case for export_certificate

    Get a certificate summary to export
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/certificate/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_certificate(client):
    """Test case for import_certificate

    Import a certificate
    """
    body = {"pemFile":"pemFile","privateKey":"privateKey","csrId":"csrId","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_certificates(client):
    """Test case for query_certificates

    Get all certificates
    """
    params = [('name', 'name_example'),
                    ('has_key', True),
                    ('description', 'description_example'),
                    ('expiration', 'expiration_example'),
                    ('include_expired', True),
                    ('sort_by', Name),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/certificate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_certificate(client):
    """Test case for update_certificate

    Update a certificate entry
    """
    body = {"pemFile":"pemFile","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/certificate/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

