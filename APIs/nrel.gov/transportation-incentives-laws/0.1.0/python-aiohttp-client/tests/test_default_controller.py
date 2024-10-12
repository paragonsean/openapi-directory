# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_results import CategoryResults
from openapi_server.models.law_result import LawResult
from openapi_server.models.laws_response import LawsResponse
from openapi_server.models.poc_results import PocResults


pytestmark = pytest.mark.asyncio

async def test_transportation_incentives_laws_all(client):
    """Test case for transportation_incentives_laws_all

    Return a full list of laws and incentives that match your query.
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('limit', 10),
                    ('jurisdiction', 'jurisdiction_example'),
                    ('technology', 'technology_example'),
                    ('incentive_type', 'incentive_type_example'),
                    ('regulation_type', 'regulation_type_example'),
                    ('user_type', 'user_type_example'),
                    ('poc', False),
                    ('recent', False),
                    ('expired', False),
                    ('law_type', 'law_type_example'),
                    ('keyword', 'keyword_example'),
                    ('local', False)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/transportation-incentives-laws/v1.{output_format}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transportation_incentives_laws_categories(client):
    """Test case for transportation_incentives_laws_categories

    Return the law categories for a given category type.
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/transportation-incentives-laws/v1/category-list.{output_format}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transportation_incentives_laws_id(client):
    """Test case for transportation_incentives_laws_id

    Fetch the details of a specific law given the law's ID.
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('poc', False),
                    ('expired', False)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/transportation-incentives-laws/v1/{id_output_format}'.format(output_format=json, id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transportation_incentives_laws_pocs(client):
    """Test case for transportation_incentives_laws_pocs

    Get the points of contact for a given jurisdiction.
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('jurisdiction', 'jurisdiction_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/transportation-incentives-laws/v1/pocs.{output_format}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

