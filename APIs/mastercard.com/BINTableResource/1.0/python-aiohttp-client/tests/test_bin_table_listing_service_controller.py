# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bin_table_response import BinTableResponse
from openapi_server.models.no_resource import NoResource


pytestmark = pytest.mark.asyncio

async def test_binlisting_get(client):
    """Test case for binlisting_get

    BIN Table Listing file
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/fraud/mtf/bintable/v1/binlisting',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

