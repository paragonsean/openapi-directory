# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.integration_account_partner import IntegrationAccountPartner
from openapi_server.models.integration_account_partner_list_result import IntegrationAccountPartnerListResult
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl


pytestmark = pytest.mark.asyncio

async def test_partners_create_or_update(client):
    """Test case for partners_create_or_update

    
    """
    partner = {"properties":{"metadata":"{}","createdTime":"2000-01-23T04:56:07.000+00:00","changedTime":"2000-01-23T04:56:07.000+00:00","partnerType":"NotSpecified","content":{"b2b":{"businessIdentities":[{"qualifier":"qualifier","value":"value"},{"qualifier":"qualifier","value":"value"}]}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners/{partner_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', partner_name='partner_name_example'),
        headers=headers,
        json=partner,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partners_delete(client):
    """Test case for partners_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners/{partner_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', partner_name='partner_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partners_get(client):
    """Test case for partners_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners/{partner_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', partner_name='partner_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partners_list_by_integration_accounts(client):
    """Test case for partners_list_by_integration_accounts

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partners_list_content_callback_url(client):
    """Test case for partners_list_content_callback_url

    
    """
    list_content_callback_url = {"notAfter":"2000-01-23T04:56:07.000+00:00","keyType":"NotSpecified"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners/{partner_name}/listContentCallbackUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', partner_name='partner_name_example'),
        headers=headers,
        json=list_content_callback_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

