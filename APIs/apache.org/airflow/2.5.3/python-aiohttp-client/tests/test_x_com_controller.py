# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.x_com import XCom
from openapi_server.models.x_com_collection import XComCollection


pytestmark = pytest.mark.asyncio

async def test_get_xcom_entries(client):
    """Test case for get_xcom_entries

    List XCom entries
    """
    params = [('limit', 100),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_xcom_entry(client):
    """Test case for get_xcom_entry

    Get an XCom entry
    """
    params = [('deserialize', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example', xcom_key='xcom_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

