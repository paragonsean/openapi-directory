# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.sni_certificate import SniCertificate


pytestmark = pytest.mark.asyncio

async def test_provision_site_tls_certificate(client):
    """Test case for provision_site_tls_certificate

    
    """
    params = [('certificate', 'certificate_example'),
                    ('key', 'key_example'),
                    ('ca_certificates', 'ca_certificates_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/ssl'.format(site_id='site_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_site_tls_certificate(client):
    """Test case for show_site_tls_certificate

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/ssl'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

