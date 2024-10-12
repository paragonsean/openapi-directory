# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_collection import CertificateCollection
from openapi_server.models.certificate_patch_resource import CertificatePatchResource
from openapi_server.models.certificates_list_default_response import CertificatesListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_certificates_create_or_update(client):
    """Test case for certificates_create_or_update

    Create or update a certificate.
    """
    certificate_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/certificates/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=certificate_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_delete(client):
    """Test case for certificates_delete

    Delete a certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/certificates/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_get(client):
    """Test case for certificates_get

    Get a certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/certificates/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_list(client):
    """Test case for certificates_list

    Get all certificates for a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/certificates'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_list_by_resource_group(client):
    """Test case for certificates_list_by_resource_group

    Get all certificates in a resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/certificates'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_update(client):
    """Test case for certificates_update

    Create or update a certificate.
    """
    certificate_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/certificates/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=certificate_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

