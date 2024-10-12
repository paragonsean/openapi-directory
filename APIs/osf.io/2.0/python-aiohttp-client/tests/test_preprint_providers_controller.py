# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.license import License
from openapi_server.models.preprint import Preprint
from openapi_server.models.preprint_providers import PreprintProviders
from openapi_server.models.taxonomy import Taxonomy


pytestmark = pytest.mark.asyncio

async def test_preprint_provider_detail(client):
    """Test case for preprint_provider_detail

    Retrieve a preprint provider
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprint_providers/{preprint_provider_id}'.format(preprint_provider_id='preprint_provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprint_provider_licenses_list(client):
    """Test case for preprint_provider_licenses_list

    List all licenses
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprint_providers/{preprint_provider_id}/licenses'.format(preprint_provider_id='preprint_provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprint_provider_list(client):
    """Test case for preprint_provider_list

    List all preprint providers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprint_providers/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprint_provider_taxonomies_list(client):
    """Test case for preprint_provider_taxonomies_list

    List all taxonomies
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprint_providers/{preprint_provider_id}/taxonomies'.format(preprint_provider_id='preprint_provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprint_providers_preprints_list(client):
    """Test case for preprint_providers_preprints_list

    List all preprints
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprint_providers/{preprint_provider_id}/preprints'.format(preprint_provider_id='preprint_provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

