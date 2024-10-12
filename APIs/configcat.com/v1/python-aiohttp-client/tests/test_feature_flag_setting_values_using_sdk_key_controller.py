# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_patch import JsonPatch
from openapi_server.models.setting_value_model import SettingValueModel
from openapi_server.models.setting_value_model_haljson import SettingValueModelHaljson
from openapi_server.models.update_setting_value_model import UpdateSettingValueModel


pytestmark = pytest.mark.asyncio

async def test_get_setting_value_by_sdkkey(client):
    """Test case for get_setting_value_by_sdkkey

    Get value
    """
    headers = { 
        'Accept': 'application/json',
        'x_configcat_sdkkey': 'x_configcat_sdkkey_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/settings/{setting_key_or_id}/value'.format(setting_key_or_id='setting_key_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_setting_value_by_sdkkey(client):
    """Test case for replace_setting_value_by_sdkkey

    Replace value
    """
    body = {"rolloutPercentageItems":[{"percentage":5,"value":""},{"percentage":5,"value":""}],"rolloutRules":[{"comparator":"isOneOf","comparisonValue":"comparisonValue","segmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","segmentComparator":"isIn","value":"","comparisonAttribute":"comparisonAttribute"},{"comparator":"isOneOf","comparisonValue":"comparisonValue","segmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","segmentComparator":"isIn","value":"","comparisonAttribute":"comparisonAttribute"}],"value":""}
    params = [('reason', 'reason_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'x_configcat_sdkkey': 'x_configcat_sdkkey_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v1/settings/{setting_key_or_id}/value'.format(setting_key_or_id='setting_key_or_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_setting_value_by_sdkkey(client):
    """Test case for update_setting_value_by_sdkkey

    Update value
    """
    body = {"operations":[{"op":"unknown","path":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"from":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"value":{"options":{"propertyNameCaseInsensitive":True}}},{"op":"unknown","path":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"from":{"isUriEncoded":True,"kind":"unspecified","source":"source","segments":[{"source":"source","value":"value"},{"source":"source","value":"value"}]},"value":{"options":{"propertyNameCaseInsensitive":True}}}]}
    params = [('reason', 'reason_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'x_configcat_sdkkey': 'x_configcat_sdkkey_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/settings/{setting_key_or_id}/value'.format(setting_key_or_id='setting_key_or_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

