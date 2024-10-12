# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_bundle import CertificateBundle
from openapi_server.models.deleted_certificate_bundle import DeletedCertificateBundle
from openapi_server.models.deleted_certificate_list_result import DeletedCertificateListResult
from openapi_server.models.key_vault_error import KeyVaultError


pytestmark = pytest.mark.asyncio

async def test_get_deleted_certificate(client):
    """Test case for get_deleted_certificate

    Retrieves information about the specified deleted certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedcertificates/{certificate_name}'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deleted_certificates(client):
    """Test case for get_deleted_certificates

    Lists the deleted certificates in the specified vault currently available for recovery.
    """
    params = [('maxresults', 56),
                    ('includePending', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedcertificates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purge_deleted_certificate(client):
    """Test case for purge_deleted_certificate

    Permanently deletes the specified deleted certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/deletedcertificates/{certificate_name}'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_deleted_certificate(client):
    """Test case for recover_deleted_certificate

    Recovers the deleted certificate back to its current version under /certificates.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/deletedcertificates/{certificate_name}/recover'.format(certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

