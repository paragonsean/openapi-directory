# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_vat_analysis_type_dto import PageResultVatAnalysisTypeDto


pytestmark = pytest.mark.asyncio

async def test_vat_analysis_types_get(client):
    """Test case for vat_analysis_types_get

    Returns a list of global Vat Analysis Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vatAnalysisTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

