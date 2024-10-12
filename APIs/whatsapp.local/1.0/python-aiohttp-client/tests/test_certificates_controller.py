# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_delete_webhook_ca_certificate(client):
    """Test case for delete_webhook_ca_certificate

    Delete Webhook CA Certificate
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/certificates/webhooks/ca',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_ca_certificate(client):
    """Test case for download_ca_certificate

    Download-CA-Certificate
    """
    headers = { 
        'Accept': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/certificates/external/ca',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_webhook_ca_certificate(client):
    """Test case for download_webhook_ca_certificate

    Download Webhook CA Certificate
    """
    headers = { 
        'Accept': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/certificates/webhooks/ca',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_upload_certificate(client):
    """Test case for upload_certificate

    Upload-Certificate
    """
    body = '/path/to/file'
    headers = { 
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/certificates/external',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_upload_webhook_ca_certificate(client):
    """Test case for upload_webhook_ca_certificate

    Upload Webhook CA Certificate
    """
    body = '/path/to/file'
    headers = { 
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/certificates/webhooks/ca',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

