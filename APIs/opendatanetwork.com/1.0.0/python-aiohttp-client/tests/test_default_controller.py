# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_create_a_map(client):
    """Test case for create_a_map

    Create a map
    """
    params = [('variable', 'demographics.population.count'),
                    ('entity_id', '0400000US53,0400000US08'),
                    ('constraint', 'constraint_example'),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/map/new',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_all_available_data_for_some_entities(client):
    """Test case for find_all_available_data_for_some_entities

    Find all available data for some entities
    """
    params = [('entity_id', '0100000US,0400000US53'),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/availability/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_the_relatives_of_an_entity(client):
    """Test case for find_the_relatives_of_an_entity

    Find the relatives of an entity
    """
    params = [('entity_id', '0400000US53'),
                    ('variable_id', 'demographics.population.seattle'),
                    ('limit', 10),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/entity/v1/{relation}'.format(relation='parent'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_constraint_permutations_for_entities(client):
    """Test case for get_constraint_permutations_for_entities

    Get constraint permutations for entities
    """
    params = [('entity_id', '0100000US,0400000US53'),
                    ('constraint', 'year'),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/constraint/{variable}'.format(variable='demographics.population.count'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datasets(client):
    """Test case for get_datasets

    Get datasets
    """
    params = [('entity_id', '0100000US'),
                    ('dataset_id', 'demographics.population'),
                    ('limit', 10),
                    ('offset', 3.4),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/search/v1/dataset',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_entities(client):
    """Test case for get_entities

    Get Entities
    """
    params = [('entity_id', '0400000US53'),
                    ('entity_name', 'washington'),
                    ('entity_type', 'region.state'),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/entity/v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_questions(client):
    """Test case for get_questions

    Get questions
    """
    params = [('query', 'seattle'),
                    ('limit', 10),
                    ('offset', 3.4),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/search/v1/question',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suggestions(client):
    """Test case for get_suggestions

    Get suggestions
    """
    params = [('query', 'seattl'),
                    ('limit', 5),
                    ('variable_id', 'demographics.population.count'),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/suggest/v1/{type}'.format(type='entity'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_values_for_variables(client):
    """Test case for get_values_for_variables

    Get values for variables
    """
    params = [('variable', 'demographics.population.count'),
                    ('entity_id', '0100000US,0400000US53'),
                    ('forecast', 3),
                    ('describe', false),
                    ('format', 'format_example'),
                    ('app_token', 'cQovpGcdUT1CSzgYk0KPYdAI0')]
    headers = { 
        'Accept': 'application/json',
        'x_app_token': 'cQovpGcdUT1CSzgYk0KPYdAI0',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/values',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

