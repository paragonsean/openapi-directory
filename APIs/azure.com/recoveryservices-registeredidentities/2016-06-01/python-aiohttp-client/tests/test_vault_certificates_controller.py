# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_request import CertificateRequest
from openapi_server.models.vault_certificate_response import VaultCertificateResponse


pytestmark = pytest.mark.asyncio

async def test_vault_certificates_create(client):
    """Test case for vault_certificates_create

    
    """
    certificate_request = {"properties":{"certificate":"certificate","authType":"Invalid"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        json=certificate_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

