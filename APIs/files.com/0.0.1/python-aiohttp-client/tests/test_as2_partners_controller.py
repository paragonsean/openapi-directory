# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.as2_partner_entity import As2PartnerEntity


pytestmark = pytest.mark.asyncio

async def test_delete_as2_partners_id(client):
    """Test case for delete_as2_partners_id

    Delete As2 Partner
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/as2_partners/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_as2_partners(client):
    """Test case for get_as2_partners

    List As2 Partners
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/as2_partners',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_as2_partners_id(client):
    """Test case for get_as2_partners_id

    Show As2 Partner
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/as2_partners/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_as2_partners_id(client):
    """Test case for patch_as2_partners_id

    Update As2 Partner
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('enable_dedicated_ips', True)
    data.add_field('name', 'name_example')
    data.add_field('public_certificate', 'public_certificate_example')
    data.add_field('server_certificate', 'server_certificate_example')
    data.add_field('uri', 'uri_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/as2_partners/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_as2_partners(client):
    """Test case for post_as2_partners

    Create As2 Partner
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('as2_station_id', 56)
    data.add_field('enable_dedicated_ips', True)
    data.add_field('name', 'name_example')
    data.add_field('public_certificate', 'public_certificate_example')
    data.add_field('server_certificate', 'server_certificate_example')
    data.add_field('uri', 'uri_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/as2_partners',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

