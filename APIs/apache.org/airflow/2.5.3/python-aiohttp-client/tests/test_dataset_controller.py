# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.dataset_collection import DatasetCollection
from openapi_server.models.dataset_event_collection import DatasetEventCollection
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_dataset(client):
    """Test case for get_dataset

    Get a dataset
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/datasets/{uri}'.format(uri='uri_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_events(client):
    """Test case for get_dataset_events

    Get dataset events
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example'),
                    ('dataset_id', 56),
                    ('source_dag_id', 'source_dag_id_example'),
                    ('source_task_id', 'source_task_id_example'),
                    ('source_run_id', 'source_run_id_example'),
                    ('source_map_index', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/datasets/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datasets(client):
    """Test case for get_datasets

    List datasets
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example'),
                    ('uri_pattern', 'uri_pattern_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/datasets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upstream_dataset_events_0(client):
    """Test case for get_upstream_dataset_events_0

    Get dataset events for a DAG run
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

