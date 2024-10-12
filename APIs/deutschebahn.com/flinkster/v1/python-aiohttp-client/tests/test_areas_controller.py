# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.area_jo import AreaJO


pytestmark = pytest.mark.asyncio

async def test_get_area(client):
    """Test case for get_area

    Get area by UID.
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/areas/{area_uid}'.format(area_uid='area_uid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_areas(client):
    """Test case for list_areas

    List Areas by Criteria.
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('radius', 56),
                    ('offset', 56),
                    ('limit', 56),
                    ('expand', 'expand_example'),
                    ('type', 'type_example'),
                    ('provider', 'provider_example'),
                    ('providernetwork', 'providernetwork_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/areas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

