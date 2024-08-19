# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hybrid_use_benefit_model import HybridUseBenefitModel


pytestmark = pytest.mark.asyncio

async def test_hybrid_use_benefit_create(client):
    """Test case for hybrid_use_benefit_create

    
    """
    body = {"etag":0,"sku":{"name":"name"},"properties":{"lastUpdatedDate":"2000-01-23T04:56:07.000+00:00","createdDate":"2000-01-23T04:56:07.000+00:00","provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{plan_id}'.format(scope='scope_example', plan_id='plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hybrid_use_benefit_delete(client):
    """Test case for hybrid_use_benefit_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{plan_id}'.format(scope='scope_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hybrid_use_benefit_get(client):
    """Test case for hybrid_use_benefit_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{plan_id}'.format(scope='scope_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hybrid_use_benefit_update(client):
    """Test case for hybrid_use_benefit_update

    
    """
    body = {"etag":0,"sku":{"name":"name"},"properties":{"lastUpdatedDate":"2000-01-23T04:56:07.000+00:00","createdDate":"2000-01-23T04:56:07.000+00:00","provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{plan_id}'.format(scope='scope_example', plan_id='plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

