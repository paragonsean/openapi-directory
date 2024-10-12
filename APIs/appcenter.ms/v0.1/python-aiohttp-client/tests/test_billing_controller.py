# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_aggregated_information_get_all200_response import BillingAggregatedInformationGetAll200Response
from openapi_server.models.billing_aggregated_information_get_by_app200_response import BillingAggregatedInformationGetByApp200Response
from openapi_server.models.billing_aggregated_information_get_by_app_default_response import BillingAggregatedInformationGetByAppDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_billing_aggregated_information_get_all(client):
    """Test case for billing_aggregated_information_get_all

    
    """
    params = [('service', 'service_example'),
                    ('period', 'period_example'),
                    ('showOriginalPlans', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/billing/allAccountsAggregated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_aggregated_information_get_by_app(client):
    """Test case for billing_aggregated_information_get_by_app

    
    """
    params = [('service', 'service_example'),
                    ('period', 'period_example'),
                    ('showOriginalPlans', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/billing/aggregated'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_aggregated_information_get_for_org(client):
    """Test case for billing_aggregated_information_get_for_org

    
    """
    params = [('service', 'service_example'),
                    ('period', 'period_example'),
                    ('showOriginalPlans', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/billing/aggregated'.format(org_name='org_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

