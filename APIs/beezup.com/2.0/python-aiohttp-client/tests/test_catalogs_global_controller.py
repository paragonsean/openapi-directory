# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_column_configuration import BeezUPColumnConfiguration
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.catalog_index import CatalogIndex


pytestmark = pytest.mark.asyncio

async def test_catalog_get_beez_up_columns(client):
    """Test case for catalog_get_beez_up_columns

    Get the BeezUP columns
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/beezupColumns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_index(client):
    """Test case for catalog_index

    Get the index of the catalog API
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

