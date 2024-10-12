# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_add_parameter import CertificateAddParameter
from openapi_server.models.certificate_list_result import CertificateListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_certificate_add(client):
    """Test case for certificate_add

    
    """
    body = openapi_server.CertificateAddParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/certificates',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_cancel_deletion(client):
    """Test case for certificate_cancel_deletion

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})/canceldelete'.format(thumbprint_algorithm='thumbprint_algorithm_example', thumbprint='thumbprint_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_delete(client):
    """Test case for certificate_delete

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='DELETE',
        path='/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})'.format(thumbprint_algorithm='thumbprint_algorithm_example', thumbprint='thumbprint_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_get(client):
    """Test case for certificate_get

    
    """
    params = [('$select', 'select_example'),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})'.format(thumbprint_algorithm='thumbprint_algorithm_example', thumbprint='thumbprint_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_list(client):
    """Test case for certificate_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('maxresults', 56),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/certificates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

