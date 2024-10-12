# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fax_v1_fax import FaxV1Fax
from openapi_server.models.fax_v1_fax_fax_media import FaxV1FaxFaxMedia
from openapi_server.models.list_fax_media_response import ListFaxMediaResponse
from openapi_server.models.list_fax_response import ListFaxResponse


pytestmark = pytest.mark.asyncio

async def test_delete_fax(client):
    """Test case for delete_fax

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Faxes/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fax_media(client):
    """Test case for delete_fax_media

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Faxes/{fax_sid}/Media/{sid}'.format(fax_sid='fax_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_fax(client):
    """Test case for fetch_fax

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Faxes/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_fax_media(client):
    """Test case for fetch_fax_media

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Faxes/{fax_sid}/Media/{sid}'.format(fax_sid='fax_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_fax(client):
    """Test case for list_fax

    
    """
    params = [('From', '_from_example'),
                    ('To', 'to_example'),
                    ('DateCreatedOnOrBefore', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Faxes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_fax_media(client):
    """Test case for list_fax_media

    
    """
    params = [('PageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Faxes/{fax_sid}/Media'.format(fax_sid='fax_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

