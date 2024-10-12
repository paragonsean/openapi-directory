# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.journal_expression_data_table import JournalExpressionDataTable


pytestmark = pytest.mark.asyncio

async def test_get_journal_expression_schema(client):
    """Test case for get_journal_expression_schema

    Gets the journal expression data schema
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/ReferenceData/JournalExpressionDataTable',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

