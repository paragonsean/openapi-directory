# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.connection import Connection


pytestmark = pytest.mark.asyncio

async def test_connections_list(client):
    """Test case for connections_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('state', 'state_example'),
                    ('state__is_not', 'state__is_not_example'),
                    ('mode', 'mode_example'),
                    ('mode__is_not', 'mode__is_not_example'),
                    ('name', 'name_example'),
                    ('metro_area_network', 'metro_area_network_example'),
                    ('pop', 'pop_example'),
                    ('facility', 'facility_example'),
                    ('external_ref', 'external_ref_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/connections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_read(client):
    """Test case for connections_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/connections/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

