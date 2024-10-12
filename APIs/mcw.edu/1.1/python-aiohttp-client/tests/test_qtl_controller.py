# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mapped_qtl import MappedQTL
from openapi_server.models.qtl import QTL


pytestmark = pytest.mark.asyncio

async def test_get_mapped_qtlby_position_using_get(client):
    """Test case for get_mapped_qtlby_position_using_get

    Returns a list QTL for given position and assembly map
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/qtls/mapped/{chr}/{start}/{stop}/{map_key}'.format(chr='chr_example', start=56, stop=56, map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_qtl_list_by_position_using_get(client):
    """Test case for get_qtl_list_by_position_using_get

    Returns a list QTL for given position and assembly map
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/qtls/{chr}/{start}/{stop}/{map_key}'.format(chr='chr_example', start=56, stop=56, map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_qtlby_rgd_id_using_get(client):
    """Test case for get_qtlby_rgd_id_using_get

    Return a QTL for provided RGD ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/qtls/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

