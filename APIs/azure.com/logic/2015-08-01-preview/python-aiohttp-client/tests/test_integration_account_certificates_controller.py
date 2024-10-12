# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.integration_account_certificate import IntegrationAccountCertificate
from openapi_server.models.integration_account_certificate_list_result import IntegrationAccountCertificateListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_integration_account_certificates_create_or_update(client):
    """Test case for integration_account_certificates_create_or_update

    
    """
    certificate = {"properties":{"metadata":"{}","createdTime":"2000-01-23T04:56:07.000+00:00","publicCertificate":"publicCertificate","changedTime":"2000-01-23T04:56:07.000+00:00","key":{"keyVault":{"name":"name","id":"id","type":"type"},"keyVersion":"keyVersion","keyName":"keyName"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        json=certificate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_certificates_delete(client):
    """Test case for integration_account_certificates_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_certificates_get(client):
    """Test case for integration_account_certificates_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_certificates_list(client):
    """Test case for integration_account_certificates_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/certificates'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

