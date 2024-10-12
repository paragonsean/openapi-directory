# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_field_type_field_value import AutopilotV1AssistantFieldTypeFieldValue
from openapi_server.models.list_field_value_response import ListFieldValueResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_field_value(client):
    """Test case for create_field_value

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'language': 'language_example',
        'synonym_of': 'synonym_of_example',
        'value': 'value_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues'.format(assistant_sid='assistant_sid_example', field_type_sid='field_type_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_field_value(client):
    """Test case for delete_field_value

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}'.format(assistant_sid='assistant_sid_example', field_type_sid='field_type_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_field_value(client):
    """Test case for fetch_field_value

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}'.format(assistant_sid='assistant_sid_example', field_type_sid='field_type_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_field_value(client):
    """Test case for list_field_value

    
    """
    params = [('Language', 'language_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues'.format(assistant_sid='assistant_sid_example', field_type_sid='field_type_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

