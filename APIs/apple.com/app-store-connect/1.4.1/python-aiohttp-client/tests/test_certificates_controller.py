# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_create_request import CertificateCreateRequest
from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.certificates_response import CertificatesResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_certificates_create_instance(client):
    """Test case for certificates_create_instance

    
    """
    body = {"data":{"attributes":{"csrContent":"csrContent","certificateType":"IOS_DEVELOPMENT"},"type":"certificates"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_delete_instance(client):
    """Test case for certificates_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/certificates/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_get_collection(client):
    """Test case for certificates_get_collection

    
    """
    params = [('filter[certificateType]', ['filter_certificate_type_example']),
                    ('filter[displayName]', ['filter_display_name_example']),
                    ('filter[serialNumber]', ['filter_serial_number_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[certificates]', ['fields_certificates_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_get_instance(client):
    """Test case for certificates_get_instance

    
    """
    params = [('fields[certificates]', ['fields_certificates_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

