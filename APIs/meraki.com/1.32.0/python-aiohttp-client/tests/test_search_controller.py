# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_organization_clients_search_2(client):
    """Test case for get_organization_clients_search_2

    Return the client details in an organization
    """
    params = [('mac', 'mac_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/clients/search'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

