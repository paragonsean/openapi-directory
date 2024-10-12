# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.onboarding_link import OnboardingLink
from openapi_server.models.onboarding_link_info import OnboardingLinkInfo
from openapi_server.models.onboarding_theme import OnboardingTheme
from openapi_server.models.onboarding_themes import OnboardingThemes
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_get_themes(client):
    """Test case for get_themes

    Get a list of hosted onboarding page themes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v1/themes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_themes_id(client):
    """Test case for get_themes_id

    Get an onboarding link theme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v1/themes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities_id_onboarding_links(client):
    """Test case for post_legal_entities_id_onboarding_links

    Get a link to an Adyen-hosted onboarding page
    """
    body = {"settings":{"key":True},"redirectUrl":"redirectUrl","themeId":"themeId","locale":"locale"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v1/legalEntities/{id}/onboardingLinks'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

