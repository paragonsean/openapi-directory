# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model_and_view import ModelAndView


pytestmark = pytest.mark.asyncio

async def test_get_single_record_json(client):
    """Test case for get_single_record_json

    get a single record in JSON format
    """
    params = [('callback', 'param_callback_example'),
                    ('lang', 'lang_example'),
                    ('profile', 'standard'),
                    ('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/{collection_id}/{record_id_jso}'.format(collection_id='collection_id_example', record_id='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_record_json_ld(client):
    """Test case for get_single_record_json_ld

    get single record in JSON LD format
    """
    params = [('callback', 'param_callback_example'),
                    ('lang', 'lang_example'),
                    ('profile', 'standard'),
                    ('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/ld+json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/{collection_id}/{record_id_jsonl}'.format(collection_id='collection_id_example', record_id='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_record_rdf(client):
    """Test case for get_single_record_rdf

    get single record in RDF format)
    """
    params = [('lang', 'lang_example'),
                    ('profile', 'standard'),
                    ('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/rdf+xml;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/{collection_id}/{record_id_rd}'.format(collection_id='collection_id_example', record_id='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_record_schema_org(client):
    """Test case for get_single_record_schema_org

    get single record in Schema.org JSON LD format
    """
    params = [('callback', 'param_callback_example'),
                    ('lang', 'lang_example'),
                    ('profile', 'standard'),
                    ('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/ld+json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/{collection_id}/{record_id_schema_jsonl}'.format(collection_id='collection_id_example', record_id='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_record_turtle(client):
    """Test case for get_single_record_turtle

    get single record in turtle format)
    """
    params = [('lang', 'lang_example'),
                    ('profile', 'standard'),
                    ('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/turtle',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/{collection_id}/{record_id_tt}'.format(collection_id='collection_id_example', record_id='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

