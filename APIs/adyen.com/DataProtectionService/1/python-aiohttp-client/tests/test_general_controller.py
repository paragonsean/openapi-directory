# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.subject_erasure_by_psp_reference_request import SubjectErasureByPspReferenceRequest
from openapi_server.models.subject_erasure_response import SubjectErasureResponse


pytestmark = pytest.mark.asyncio

async def test_post_request_subject_erasure(client):
    """Test case for post_request_subject_erasure

    Submit a Subject Erasure Request.
    """
    body = {"merchantAccount":"merchantAccount","forceErasure":True,"pspReference":"pspReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ca/services/DataProtectionService/v1/requestSubjectErasure',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

