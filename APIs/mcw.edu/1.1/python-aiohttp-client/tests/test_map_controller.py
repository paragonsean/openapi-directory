# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chromosome import Chromosome
from openapi_server.models.map import Map


pytestmark = pytest.mark.asyncio

async def test_get_chromosome_by_assembly_using_get_0(client):
    """Test case for get_chromosome_by_assembly_using_get_0

    Return a list of chromosomes
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/maps/chr/{chromosome}/{map_key}'.format(chromosome='chromosome_example', map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chromosomes_by_assembly_using_get_0(client):
    """Test case for get_chromosomes_by_assembly_using_get_0

    Return a list of chromosomes
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/maps/chr/{map_key}'.format(map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_maps_by_species_using_get(client):
    """Test case for get_maps_by_species_using_get

    Return a list of assemblies
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/maps/{species_type_key}'.format(species_type_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

