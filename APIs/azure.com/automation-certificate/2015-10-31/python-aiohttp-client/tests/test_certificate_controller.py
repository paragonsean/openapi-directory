# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_create_or_update_parameters import CertificateCreateOrUpdateParameters
from openapi_server.models.certificate_list_by_automation_account_default_response import CertificateListByAutomationAccountDefaultResponse
from openapi_server.models.certificate_list_result import CertificateListResult
from openapi_server.models.certificate_update_parameters import CertificateUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_certificate_create_or_update(client):
    """Test case for certificate_create_or_update

    
    """
    parameters = {"name":"name","properties":{"isExportable":True,"base64Value":"base64Value","thumbprint":"thumbprint","description":"description"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/certificates/{certificate_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', certificate_name='certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_delete(client):
    """Test case for certificate_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/certificates/{certificate_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', certificate_name='certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_get(client):
    """Test case for certificate_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/certificates/{certificate_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', certificate_name='certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_list_by_automation_account(client):
    """Test case for certificate_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/certificates'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificate_update(client):
    """Test case for certificate_update

    
    """
    parameters = {"name":"name","properties":{"description":"description"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/certificates/{certificate_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', certificate_name='certificate_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

