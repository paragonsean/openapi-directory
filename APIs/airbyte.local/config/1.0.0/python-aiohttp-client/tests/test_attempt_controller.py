# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.internal_operation_result import InternalOperationResult
from openapi_server.models.save_attempt_sync_config_request_body import SaveAttemptSyncConfigRequestBody
from openapi_server.models.save_stats_request_body import SaveStatsRequestBody
from openapi_server.models.set_workflow_in_attempt_request_body import SetWorkflowInAttemptRequestBody


pytestmark = pytest.mark.asyncio

async def test_save_stats(client):
    """Test case for save_stats

    For worker to set sync stats of a running attempt.
    """
    body = {"attemptNumber":0,"jobId":6,"stats":{"recordsCommitted":2,"stateMessagesEmitted":9,"bytesEmitted":1,"estimatedBytes":5,"estimatedRecords":5,"recordsEmitted":7},"streamStats":[{"stats":{"recordsCommitted":2,"stateMessagesEmitted":9,"bytesEmitted":1,"estimatedBytes":5,"estimatedRecords":5,"recordsEmitted":7},"streamNamespace":"streamNamespace","streamName":"streamName"},{"stats":{"recordsCommitted":2,"stateMessagesEmitted":9,"bytesEmitted":1,"estimatedBytes":5,"estimatedRecords":5,"recordsEmitted":7},"streamNamespace":"streamNamespace","streamName":"streamName"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/attempt/save_stats',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_sync_config(client):
    """Test case for save_sync_config

    For worker to save the AttemptSyncConfig for an attempt.
    """
    body = {"attemptNumber":0,"jobId":6,"syncConfig":{"destinationConfiguration":{"user":"charles"},"sourceConfiguration":{"user":"charles"},"state":{"globalState":{"shared_state":"{}","streamStates":[{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"},{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"}]},"stateType":"global","connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","streamState":[{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"},{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"}],"state":"{}"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/attempt/save_sync_config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_workflow_in_attempt(client):
    """Test case for set_workflow_in_attempt

    For worker to register the workflow id in attempt.
    """
    body = {"attemptNumber":0,"jobId":6,"processingTaskQueue":"","workflowId":"workflowId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/attempt/set_workflow_in_attempt',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

