# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field_configurations import CustomFieldConfigurations
from openapi_server.models.page_bean_contextual_configuration import PageBeanContextualConfiguration


pytestmark = pytest.mark.asyncio

async def test_get_custom_field_configuration(client):
    """Test case for get_custom_field_configuration

    Get custom field configurations
    """
    params = [('id', [56]),
                    ('fieldContextId', [56]),
                    ('issueId', 56),
                    ('projectKeyOrId', 'project_key_or_id_example'),
                    ('issueTypeId', 'issue_type_id_example'),
                    ('startAt', 0),
                    ('maxResults', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/app/field/{field_id_or_key}/context/configuration'.format(field_id_or_key='field_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field_configuration(client):
    """Test case for update_custom_field_configuration

    Update custom field configurations
    """
    body = {"configurations":[{"fieldContextId":"fieldContextId","schema":"","configuration":"","id":"id"},{"fieldContextId":"fieldContextId","schema":"","configuration":"","id":"id"},{"fieldContextId":"fieldContextId","schema":"","configuration":"","id":"id"},{"fieldContextId":"fieldContextId","schema":"","configuration":"","id":"id"},{"fieldContextId":"fieldContextId","schema":"","configuration":"","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/app/field/{field_id_or_key}/context/configuration'.format(field_id_or_key='field_id_or_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

