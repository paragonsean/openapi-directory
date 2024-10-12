# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.language import Language
from openapi_server.models.license_sfx_request import LicenseSFXRequest
from openapi_server.models.license_sfx_result_data_list import LicenseSFXResultDataList
from openapi_server.models.sfx import SFX
from openapi_server.models.sfx_data_list import SFXDataList
from openapi_server.models.sfx_search_results import SFXSearchResults
from openapi_server.models.sfx_url import SfxUrl


pytestmark = pytest.mark.asyncio

async def test_download_sfx(client):
    """Test case for download_sfx

    Download sound effects
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/sfx/licenses/{id}/downloads'.format(id='123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sfx_details(client):
    """Test case for get_sfx_details

    Get details about sound effects
    """
    params = [('language', openapi_server.Language()),
                    ('view', minimal),
                    ('library', 'shutterstock'),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/sfx/{id}'.format(id=442583),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sfx_license_list(client):
    """Test case for get_sfx_license_list

    List sound effects licenses
    """
    params = [('sfx_id', '12345678'),
                    ('license', 'standard'),
                    ('page', 1),
                    ('per_page', 20),
                    ('sort', newest),
                    ('username', 'aUniqueUsername'),
                    ('start_date', '2021-03-29T13:25:13.521Z'),
                    ('end_date', '2021-03-29T13:25:13.521Z'),
                    ('license_id', 'license_id_example'),
                    ('download_availability', all),
                    ('team_history', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/sfx/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sfx_list_details(client):
    """Test case for get_sfx_list_details

    List details about sound effects
    """
    params = [('id', ['[\"1110335168\",\"465011609\"]']),
                    ('view', minimal),
                    ('language', openapi_server.Language()),
                    ('library', 'shutterstock'),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/sfx',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_licenses_sfx(client):
    """Test case for licenses_sfx

    License sound effects
    """
    body = {"sound_effects":[{"format":"wav","metadata":{"customer_id":"12345","geo_location":"US","number_viewed":"15","search_term":"dog"},"sfx_id":"123456789","show_modal":True,"size":"ambisonic","subscription_id":"s12345678"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/sfx/licenses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_sfx(client):
    """Test case for search_sfx

    Search for sound effects
    """
    params = [('added_date', '2022-09-23'),
                    ('added_date_start', '2021-03-29'),
                    ('added_date_end', '2021-03-29'),
                    ('duration', 180),
                    ('duration_from', 30),
                    ('duration_to', 180),
                    ('page', 1),
                    ('per_page', 20),
                    ('query', 'drum'),
                    ('safe', True),
                    ('sort', popular),
                    ('view', minimal),
                    ('language', openapi_server.Language())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/sfx/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

