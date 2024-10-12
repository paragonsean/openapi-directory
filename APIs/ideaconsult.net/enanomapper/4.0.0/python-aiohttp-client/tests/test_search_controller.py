# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.solr_response import SolrResponse
from openapi_server.models.solrquery_post_request import SolrqueryPostRequest


pytestmark = pytest.mark.asyncio

async def test_solrquery_get(client):
    """Test case for solrquery_get

    Apache Solr powered search
    """
    params = [('q', '*:*'),
                    ('fq', 'fq_example'),
                    ('fl', '*'),
                    ('start', 0),
                    ('rows', 10),
                    ('wt', xml)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/enanomapper/select',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solrquery_post(client):
    """Test case for solrquery_post

    Apache Solr powered search
    """
    body = openapi_server.SolrqueryPostRequest()
    params = [('wt', xml)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/enanomapper/select',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

