# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_family_details200_response import GetFamilyDetails200Response
from openapi_server.models.list_hypernyms200_response_inner_inner import ListHypernyms200ResponseInnerInner
from openapi_server.models.list_inflected_forms200_response_inner import ListInflectedForms200ResponseInner
from openapi_server.models.list_word_senses200_response_inner import ListWordSenses200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_family_details(client):
    """Test case for get_family_details

    Get family details
    """
    params = [('id', '{family_id}')]
    headers = { 
        'Accept': 'application/json',
        'ocp_apim_subscription_key': '{{apiKey}}',
    }
    response = await client.request(
        method='GET',
        path='/lm/family',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_feature_values(client):
    """Test case for list_feature_values

    List feature values
    """
    params = [('language', '{language_code}'),
                    ('type', '{Grammar/Style/Semantics}'),
                    ('description', '{feature_list_name}')]
    headers = { 
        'Accept': 'application/json',
        'ocp_apim_subscription_key': '{{apiKey}}',
    }
    response = await client.request(
        method='GET',
        path='/values',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hypernyms(client):
    """Test case for list_hypernyms

    List hypernyms
    """
    params = [('family', '{family_id}'),
                    ('maxLevel', '{max_number_of_levels}')]
    headers = { 
        'Accept': 'application/json',
        'ocp_apim_subscription_key': '{{apiKey}}',
    }
    response = await client.request(
        method='GET',
        path='/hypernyms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hyponyms(client):
    """Test case for list_hyponyms

    List hyponyms
    """
    params = [('family', '{family_id}'),
                    ('maxLevel', '{max_number_of_levels}')]
    headers = { 
        'Accept': 'text/plain',
        'ocp_apim_subscription_key': '{{apiKey}}',
    }
    response = await client.request(
        method='GET',
        path='/hyponyms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_inflected_forms(client):
    """Test case for list_inflected_forms

    List inflected forms
    """
    params = [('language', '{language_code}'),
                    ('lexeme', '{lexeme_id}'),
                    ('family', '{family_id}')]
    headers = { 
        'Accept': 'application/json',
        'ocp_apim_subscription_key': '{{apiKey}}',
    }
    response = await client.request(
        method='GET',
        path='/inflections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_word_senses(client):
    """Test case for list_word_senses

    List word senses
    """
    params = [('language', '{language_code}'),
                    ('word', '{word}')]
    headers = { 
        'Accept': 'application/json',
        'ocp_apim_subscription_key': '{{apiKey}}',
    }
    response = await client.request(
        method='GET',
        path='/senses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

