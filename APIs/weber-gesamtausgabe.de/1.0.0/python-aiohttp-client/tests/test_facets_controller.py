# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.facet import Facet


pytestmark = pytest.mark.asyncio

async def test_facets_facet_get(client):
    """Test case for facets_facet_get

    Returns facets
    """
    params = [('scope', 'scope_example'),
                    ('term', 'term_example'),
                    ('docType', ['doc_type_example']),
                    ('offset', 1),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/facets/{facet}'.format(facet='facet_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

