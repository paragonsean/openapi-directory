# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quota import Quota
from openapi_server.models.quota_list import QuotaList


pytestmark = pytest.mark.asyncio

async def test_quotas_create_or_update(client):
    """Test case for quotas_create_or_update

    Creates or Updates a Quota.
    """
    new_quota = {"properties":{"vmScaleSetCount":0,"availabilitySetCount":0,"virtualMachineCount":0,"coresLimit":0}}
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quota_name}'.format(subscription_id='subscription_id_example', location='location_example', quota_name='quota_name_example'),
        headers=headers,
        json=new_quota,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quotas_delete(client):
    """Test case for quotas_delete

    Deletes specified quota
    """
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quota_name}'.format(subscription_id='subscription_id_example', location='location_example', quota_name='quota_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quotas_get(client):
    """Test case for quotas_get

    Returns the requested quota.
    """
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/quotas/{quota_name}'.format(subscription_id='subscription_id_example', location='location_example', quota_name='quota_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quotas_list(client):
    """Test case for quotas_list

    Lists all quotas.
    """
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/quotas'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

