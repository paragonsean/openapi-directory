# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beta_build_localization_create_request import BetaBuildLocalizationCreateRequest
from openapi_server.models.beta_build_localization_response import BetaBuildLocalizationResponse
from openapi_server.models.beta_build_localization_update_request import BetaBuildLocalizationUpdateRequest
from openapi_server.models.beta_build_localizations_response import BetaBuildLocalizationsResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_build_localizations_build_get_to_one_related(client):
    """Test case for beta_build_localizations_build_get_to_one_related

    
    """
    params = [('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaBuildLocalizations/{id}/build'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_build_localizations_create_instance(client):
    """Test case for beta_build_localizations_create_instance

    
    """
    body = {"data":{"relationships":{"build":{"data":{"id":"id","type":"builds"}}},"attributes":{"whatsNew":"whatsNew","locale":"locale"},"type":"betaBuildLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaBuildLocalizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_build_localizations_delete_instance(client):
    """Test case for beta_build_localizations_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaBuildLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_build_localizations_get_collection(client):
    """Test case for beta_build_localizations_get_collection

    
    """
    params = [('filter[locale]', ['filter_locale_example']),
                    ('filter[build]', ['filter_build_example']),
                    ('fields[betaBuildLocalizations]', ['fields_beta_build_localizations_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaBuildLocalizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_build_localizations_get_instance(client):
    """Test case for beta_build_localizations_get_instance

    
    """
    params = [('fields[betaBuildLocalizations]', ['fields_beta_build_localizations_example']),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaBuildLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_build_localizations_update_instance(client):
    """Test case for beta_build_localizations_update_instance

    
    """
    body = {"data":{"attributes":{"whatsNew":"whatsNew"},"id":"id","type":"betaBuildLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/betaBuildLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

