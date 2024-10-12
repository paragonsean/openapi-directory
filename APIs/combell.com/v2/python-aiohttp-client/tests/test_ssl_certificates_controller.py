# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ssl_certificate import SslCertificate
from openapi_server.models.ssl_certificate_detail import SslCertificateDetail
from openapi_server.models.ssl_certificate_file_format import SslCertificateFileFormat


pytestmark = pytest.mark.asyncio

async def test_download_certificate(client):
    """Test case for download_certificate

    Download a SSL certificate
    """
    params = [('sha1_fingerprint', 'sha1_fingerprint_example'),
                    ('file_format', openapi_server.SslCertificateFileFormat()),
                    ('password', 'password_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/sslcertificates/{sha1_fingerprint}/download'.format(sha1_fingerprint2='sha1_fingerprint_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ssl_certificate(client):
    """Test case for get_ssl_certificate

    Detail of a SSL certificate
    """
    params = [('sha1_fingerprint', 'sha1_fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/sslcertificates/{sha1_fingerprint}'.format(sha1_fingerprint2='sha1_fingerprint_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ssl_certificates(client):
    """Test case for get_ssl_certificates

    Overview of SSL certificates
    """
    params = [('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/sslcertificates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

