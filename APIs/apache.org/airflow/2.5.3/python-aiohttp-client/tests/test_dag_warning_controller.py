# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dag_warning_collection import DagWarningCollection
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_dag_warnings(client):
    """Test case for get_dag_warnings

    List dag warnings
    """
    params = [('dag_id', 'dag_id_example'),
                    ('warning_type', 'warning_type_example'),
                    ('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dagWarnings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

