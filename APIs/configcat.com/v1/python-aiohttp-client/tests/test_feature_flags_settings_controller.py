# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_setting_initial_values import CreateSettingInitialValues
from openapi_server.models.json_patch import JsonPatch
from openapi_server.models.setting_model import SettingModel
from openapi_server.models.setting_model_haljson import SettingModelHaljson


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_setting(client):
    """Test case for create_setting

    Create Flag
    """
    body = {"initialValues":[{"environmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","value":""},{"environmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","value":""}],"hint":"hint","name":"name","settingType":"boolean","key":"key","tags":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/configs/{config_id}/settings'.format(config_id='config_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_setting(client):
    """Test case for delete_setting

    Delete Flag
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/settings/{setting_id}'.format(setting_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_setting(client):
    """Test case for get_setting

    Get Flag
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/settings/{setting_id}'.format(setting_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settings(client):
    """Test case for get_settings

    List Flags
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/configs/{config_id}/settings'.format(config_id='config_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_setting(client):
    """Test case for update_setting

    Update Flag
    """
    body = {"operations":[{"op":"unknown","path":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"from":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"value":{"options":{"propertyNameCaseInsensitive":True}}},{"op":"unknown","path":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"from":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"value":{"options":{"propertyNameCaseInsensitive":True}}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/settings/{setting_id}'.format(setting_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

