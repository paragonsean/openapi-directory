# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.remediation_request import RemediationRequest
from openapi_server.models.remediation_response import RemediationResponse
from openapi_server.models.request_failed_exception import RequestFailedException
from openapi_server.models.verification_parameters import VerificationParameters
from openapi_server.models.verification_response import VerificationResponse


pytestmark = pytest.mark.asyncio

async def test_create_backup_remediation_async_task(client):
    """Test case for create_backup_remediation_async_task

    Reschedule unsuccessful backup tasks
    """
    body = {"config":{"runNow":True},"spec":[{"eventSeriesId":"eventSeriesId","objectId":"objectId"},{"eventSeriesId":"eventSeriesId","objectId":"objectId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/backup/retry',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_backup_remediation_async_task_status(client):
    """Test case for get_backup_remediation_async_task_status

    Get status of reschedule attempt
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/backup/retry/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_backup_verification_async_request_status(client):
    """Test case for get_backup_verification_async_request_status

    Get asynchronous request details for Backup Verification
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/backup/verify/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_snapshot(client):
    """Test case for verify_snapshot

    Trigger a job for snapshot verification
    """
    body = {"shouldVerifyAfterOpt":"2000-01-23T04:56:07.000+00:00","snapshotIdsOpt":["snapshotIdsOpt","snapshotIdsOpt"],"objectId":"objectId","locationIdOpt":"locationIdOpt"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/backup/verify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

