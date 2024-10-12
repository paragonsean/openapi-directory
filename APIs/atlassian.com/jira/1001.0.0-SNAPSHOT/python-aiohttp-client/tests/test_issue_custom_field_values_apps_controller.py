# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field_value_update_details import CustomFieldValueUpdateDetails
from openapi_server.models.multiple_custom_field_values_update_details import MultipleCustomFieldValuesUpdateDetails


pytestmark = pytest.mark.asyncio

async def test_update_custom_field_value(client):
    """Test case for update_custom_field_value

    Update custom field value
    """
    body = {"updates":[{"issueIds":[0,0],"value":""},{"issueIds":[0,0],"value":""}]}
    params = [('generateChangelog', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/app/field/{field_id_or_key}/value'.format(field_id_or_key='field_id_or_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_multiple_custom_field_values(client):
    """Test case for update_multiple_custom_field_values

    Update custom fields
    """
    body = {"updates":[{"issueIds":[0,0],"value":"","customField":"customField"},{"issueIds":[0,0],"value":"","customField":"customField"}]}
    params = [('generateChangelog', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/app/field/value',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

