# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.found_users_and_groups import FoundUsersAndGroups


pytestmark = pytest.mark.asyncio

async def test_find_users_and_groups(client):
    """Test case for find_users_and_groups

    Find users and groups
    """
    params = [('query', 'query_example'),
                    ('maxResults', 50),
                    ('showAvatar', False),
                    ('fieldId', 'field_id_example'),
                    ('projectId', ['project_id_example']),
                    ('issueTypeId', ['issue_type_id_example']),
                    ('avatarSize', xsmall),
                    ('caseInsensitive', False),
                    ('excludeConnectAddons', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/groupuserpicker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

