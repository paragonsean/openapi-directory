# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_app_localization_create_request import BetaAppLocalizationCreateRequest
from openapi_server.models.beta_app_localization_response import BetaAppLocalizationResponse
from openapi_server.models.beta_app_localization_update_request import BetaAppLocalizationUpdateRequest
from openapi_server.models.beta_app_localizations_response import BetaAppLocalizationsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_app_localizations_app_get_to_one_related(client):
    """Test case for beta_app_localizations_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppLocalizations/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_localizations_create_instance(client):
    """Test case for beta_app_localizations_create_instance

    
    """
    body = {"data":{"relationships":{"app":{"data":{"id":"id","type":"apps"}}},"attributes":{"marketingUrl":"marketingUrl","description":"description","locale":"locale","tvOsPrivacyPolicy":"tvOsPrivacyPolicy","privacyPolicyUrl":"privacyPolicyUrl","feedbackEmail":"feedbackEmail"},"type":"betaAppLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaAppLocalizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_localizations_delete_instance(client):
    """Test case for beta_app_localizations_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaAppLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_localizations_get_collection(client):
    """Test case for beta_app_localizations_get_collection

    
    """
    params = [('filter[locale]', ['filter_locale_example']),
                    ('filter[app]', ['filter_app_example']),
                    ('fields[betaAppLocalizations]', ['fields_beta_app_localizations_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppLocalizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_localizations_get_instance(client):
    """Test case for beta_app_localizations_get_instance

    
    """
    params = [('fields[betaAppLocalizations]', ['fields_beta_app_localizations_example']),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_localizations_update_instance(client):
    """Test case for beta_app_localizations_update_instance

    
    """
    body = {"data":{"attributes":{"marketingUrl":"marketingUrl","description":"description","tvOsPrivacyPolicy":"tvOsPrivacyPolicy","privacyPolicyUrl":"privacyPolicyUrl","feedbackEmail":"feedbackEmail"},"id":"id","type":"betaAppLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/betaAppLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

