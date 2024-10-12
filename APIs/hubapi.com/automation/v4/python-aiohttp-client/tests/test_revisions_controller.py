# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_public_action_revision_forward_paging import CollectionResponsePublicActionRevisionForwardPaging
from openapi_server.models.error import Error
from openapi_server.models.public_action_revision import PublicActionRevision


pytestmark = pytest.mark.asyncio

async def test_get_automation_v4_actions_app_id_definition_id_revisions_get_page(client):
    """Test case for get_automation_v4_actions_app_id_definition_id_revisions_get_page

    Get all revisions for a given definition
    """
    params = [('limit', 56),
                    ('after', 'after_example')]
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/automation/v4/actions/{app_id}/{definition_id}/revisions'.format(definition_id='definition_id_example', app_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automation_v4_actions_app_id_definition_id_revisions_revision_id_get_by_id(client):
    """Test case for get_automation_v4_actions_app_id_definition_id_revisions_revision_id_get_by_id

    Gets a revision for a given definition by revision id
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/automation/v4/actions/{app_id}/{definition_id}/revisions/{revision_id}'.format(definition_id='definition_id_example', revision_id='revision_id_example', app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

