# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clear_dag_run import ClearDagRun
from openapi_server.models.clear_dag_run200_response import ClearDagRun200Response
from openapi_server.models.dag_run import DAGRun
from openapi_server.models.dag_run_collection import DAGRunCollection
from openapi_server.models.dataset_event_collection import DatasetEventCollection
from openapi_server.models.error import Error
from openapi_server.models.list_dag_runs_form import ListDagRunsForm
from openapi_server.models.set_dag_run_note import SetDagRunNote
from openapi_server.models.update_dag_run_state import UpdateDagRunState


pytestmark = pytest.mark.asyncio

async def test_clear_dag_run(client):
    """Test case for clear_dag_run

    Clear a DAG run
    """
    body = {"dry_run":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/clear'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dag_run(client):
    """Test case for delete_dag_run

    Delete a DAG run
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dag_run(client):
    """Test case for get_dag_run

    Get a DAG run
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dag_runs(client):
    """Test case for get_dag_runs

    List DAG runs
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('execution_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('execution_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('start_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('start_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('end_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('end_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('state', ['state_example']),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns'.format(dag_id='dag_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dag_runs_batch(client):
    """Test case for get_dag_runs_batch

    List DAG runs (batch)
    """
    body = {"end_date_lte":"2000-01-23T04:56:07.000+00:00","start_date_gte":"2000-01-23T04:56:07.000+00:00","execution_date_gte":"2000-01-23T04:56:07.000+00:00","page_limit":1,"execution_date_lte":"2000-01-23T04:56:07.000+00:00","order_by":"order_by","end_date_gte":"2000-01-23T04:56:07.000+00:00","page_offset":0,"start_date_lte":"2000-01-23T04:56:07.000+00:00","dag_ids":["dag_ids","dag_ids"],"states":["states","states"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dags/~/dagRuns/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upstream_dataset_events(client):
    """Test case for get_upstream_dataset_events

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


pytestmark = pytest.mark.asyncio

async def test_post_dag_run(client):
    """Test case for post_dag_run

    Trigger a new DAG run
    """
    body = {"end_date":"2000-01-23T04:56:07.000+00:00","note":"note","execution_date":"2000-01-23T04:56:07.000+00:00","external_trigger":True,"conf":"{}","data_interval_start":"2000-01-23T04:56:07.000+00:00","run_type":"backfill","data_interval_end":"2000-01-23T04:56:07.000+00:00","last_scheduling_decision":"2000-01-23T04:56:07.000+00:00","dag_run_id":"dag_run_id","dag_id":"dag_id","logical_date":"2000-01-23T04:56:07.000+00:00","state":"queued","start_date":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dags/{dag_id}/dagRuns'.format(dag_id='dag_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_dag_run_note(client):
    """Test case for set_dag_run_note

    Update the DagRun note.
    """
    body = {"note":"note"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/setNote'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_dag_run_state(client):
    """Test case for update_dag_run_state

    Modify a DAG run
    """
    body = {"state":"success"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

