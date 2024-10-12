# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_an_organizations_entitlement_value(client):
    """Test case for get_an_organizations_entitlement_value

    Get an organization's entitlement value
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/entitlement/{entitlement_key}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', entitlement_key='reports'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_entitlements(client):
    """Test case for list_all_entitlements

    List all entitlements
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/entitlements'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

