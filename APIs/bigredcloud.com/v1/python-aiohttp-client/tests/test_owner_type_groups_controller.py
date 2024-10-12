# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_owner_type_group_dto import PageResultOwnerTypeGroupDto


pytestmark = pytest.mark.asyncio

async def test_owner_type_groups_get(client):
    """Test case for owner_type_groups_get

    Returns a list of global Owner Type Groups. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ownerTypeGroups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

