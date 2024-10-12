# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attempt_normalization_status_read_list import AttemptNormalizationStatusReadList
from openapi_server.models.connection_state import ConnectionState
from openapi_server.models.connection_state_create_or_update import ConnectionStateCreateOrUpdate
from openapi_server.models.discover_catalog_result import DiscoverCatalogResult
from openapi_server.models.internal_operation_result import InternalOperationResult
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.job_id_request_body import JobIdRequestBody
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.save_attempt_sync_config_request_body import SaveAttemptSyncConfigRequestBody
from openapi_server.models.save_stats_request_body import SaveStatsRequestBody
from openapi_server.models.set_workflow_in_attempt_request_body import SetWorkflowInAttemptRequestBody
from openapi_server.models.source_discover_schema_write_request_body import SourceDiscoverSchemaWriteRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_or_update_state_0(client):
    """Test case for create_or_update_state_0

    Create or update the state for a connection.
    """
    body = {"connectionState":{"globalState":{"shared_state":"{}","streamStates":[{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"},{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"}]},"stateType":"global","connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","streamState":[{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"},{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"}],"state":"{}"},"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/state/create_or_update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attempt_normalization_statuses_for_job_0(client):
    """Test case for get_attempt_normalization_statuses_for_job_0

    Get normalization status to determine if we can bypass normalization phase
    """
    body = {"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/get_normalization_status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_stats_0(client):
    """Test case for save_stats_0

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

async def test_save_sync_config_0(client):
    """Test case for save_sync_config_0

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

async def test_set_workflow_in_attempt_0(client):
    """Test case for set_workflow_in_attempt_0

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


pytestmark = pytest.mark.asyncio

async def test_write_discover_catalog_result_0(client):
    """Test case for write_discover_catalog_result_0

    Should only called from worker, to write result from discover activity back to DB.
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","configurationHash":"configurationHash","catalog":{"streams":[{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}},{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}}]},"connectorVersion":"connectorVersion"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/write_discover_catalog_result',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

