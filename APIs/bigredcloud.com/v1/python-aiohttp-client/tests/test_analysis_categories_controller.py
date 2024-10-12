# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_analysis_category_dto import PageResultAnalysisCategoryDto


pytestmark = pytest.mark.asyncio

async def test_analysis_categories_get(client):
    """Test case for analysis_categories_get

    Returns a list of company's Analysis Categories. Supports OData querying protocol.  Filtering is allowed by \"categoryTypeId\" field.  Ordering is allowed by \"id\" and \"orderIndex\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/analysisCategories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

