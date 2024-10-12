# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_organization_unit import AddOrganizationUnit
from openapi_server.models.add_organization_unit_response import AddOrganizationUnitResponse
from openapi_server.models.error import Error
from openapi_server.models.org_unit import OrgUnit
from openapi_server.models.org_units import OrgUnits
from openapi_server.models.update_organization_unit import UpdateOrganizationUnit


pytestmark = pytest.mark.asyncio

async def test_extorgunit_get(client):
    """Test case for extorgunit_get

    Get Organization Unit with External Id
    """
    params = [('extid', 'extid_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/extorgunit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_get(client):
    """Test case for orgunits_get

    Organization Units
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_get(client):
    """Test case for orgunits_orgid_get

    Get Organization Unit
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}'.format(orgid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_orgunits_orgid_patch(client):
    """Test case for orgunits_orgid_patch

    Updates an Organization Unit
    """
    body = openapi_server.UpdateOrganizationUnit()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/orgunits/{orgid}'.format(orgid='orgid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_orgunits_post(client):
    """Test case for orgunits_post

    Adds an Organization Unit
    """
    body = openapi_server.AddOrganizationUnit()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orgunits',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

