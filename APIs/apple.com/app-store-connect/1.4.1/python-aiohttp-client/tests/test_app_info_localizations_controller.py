# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_info_localization_create_request import AppInfoLocalizationCreateRequest
from openapi_server.models.app_info_localization_response import AppInfoLocalizationResponse
from openapi_server.models.app_info_localization_update_request import AppInfoLocalizationUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_info_localizations_create_instance(client):
    """Test case for app_info_localizations_create_instance

    
    """
    body = {"data":{"relationships":{"appInfo":{"data":{"id":"id","type":"appInfos"}}},"attributes":{"subtitle":"subtitle","name":"name","privacyPolicyText":"privacyPolicyText","locale":"locale","privacyPolicyUrl":"privacyPolicyUrl"},"type":"appInfoLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appInfoLocalizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_info_localizations_delete_instance(client):
    """Test case for app_info_localizations_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appInfoLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_info_localizations_get_instance(client):
    """Test case for app_info_localizations_get_instance

    
    """
    params = [('fields[appInfoLocalizations]', ['fields_app_info_localizations_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfoLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_info_localizations_update_instance(client):
    """Test case for app_info_localizations_update_instance

    
    """
    body = {"data":{"attributes":{"subtitle":"subtitle","name":"name","privacyPolicyText":"privacyPolicyText","privacyPolicyUrl":"privacyPolicyUrl"},"id":"id","type":"appInfoLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appInfoLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

