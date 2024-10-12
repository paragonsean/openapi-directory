# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.site import Site
from openapi_server.models.site_setup import SiteSetup


pytestmark = pytest.mark.asyncio

async def test_create_site(client):
    """Test case for create_site

    
    """
    site = openapi_server.SiteSetup()
    params = [('configure_dns', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites',
        headers=headers,
        json=site,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_site_in_team(client):
    """Test case for create_site_in_team

    
    """
    site = openapi_server.SiteSetup()
    params = [('configure_dns', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{account_slug}/sites'.format(account_slug='account_slug_example'),
        headers=headers,
        json=site,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_site(client):
    """Test case for delete_site

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{site_id}'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site(client):
    """Test case for get_site

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sites(client):
    """Test case for list_sites

    
    """
    params = [('name', 'name_example'),
                    ('filter', 'filter_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sites_for_account(client):
    """Test case for list_sites_for_account

    
    """
    params = [('name', 'name_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{account_slug}/sites'.format(account_slug='account_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlink_site_repo(client):
    """Test case for unlink_site_repo

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/unlink_repo'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_site(client):
    """Test case for update_site

    
    """
    site = openapi_server.SiteSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/sites/{site_id}'.format(site_id='site_id_example'),
        headers=headers,
        json=site,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

