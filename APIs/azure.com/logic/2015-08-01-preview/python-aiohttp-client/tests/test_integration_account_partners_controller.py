# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.integration_account_partner import IntegrationAccountPartner
from openapi_server.models.integration_account_partner_list_result import IntegrationAccountPartnerListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_integration_account_partners_create_or_update(client):
    """Test case for integration_account_partners_create_or_update

    
    """
    partner = {"properties":{"metadata":"{}","createdTime":"2000-01-23T04:56:07.000+00:00","changedTime":"2000-01-23T04:56:07.000+00:00","partnerType":"NotSpecified","content":{"b2b":{"businessIdentities":[{"Value":"Value","Qualifier":"Qualifier"},{"Value":"Value","Qualifier":"Qualifier"}]}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
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

async def test_integration_account_partners_delete(client):
    """Test case for integration_account_partners_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners/{partner_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', partner_name='partner_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_partners_get(client):
    """Test case for integration_account_partners_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners/{partner_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', partner_name='partner_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_partners_list(client):
    """Test case for integration_account_partners_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/partners'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

