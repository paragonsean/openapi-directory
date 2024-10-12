# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_dispute_response import AcceptDisputeResponse
from openapi_server.models.create_dispute_evidence_text_request import CreateDisputeEvidenceTextRequest
from openapi_server.models.create_dispute_evidence_text_response import CreateDisputeEvidenceTextResponse
from openapi_server.models.delete_dispute_evidence_response import DeleteDisputeEvidenceResponse
from openapi_server.models.list_dispute_evidence_response import ListDisputeEvidenceResponse
from openapi_server.models.list_disputes_response import ListDisputesResponse
from openapi_server.models.retrieve_dispute_evidence_response import RetrieveDisputeEvidenceResponse
from openapi_server.models.retrieve_dispute_response import RetrieveDisputeResponse
from openapi_server.models.submit_evidence_response import SubmitEvidenceResponse


pytestmark = pytest.mark.asyncio

async def test_accept_dispute(client):
    """Test case for accept_dispute

    AcceptDispute
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/disputes/{dispute_id}/accept'.format(dispute_id='dispute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_dispute_evidence_text(client):
    """Test case for create_dispute_evidence_text

    CreateDisputeEvidenceText
    """
    body = {"request_body":{"evidence_text":"1Z8888888888888888","evidence_type":"TRACKING_NUMBER","idempotency_key":"ed3ee3933d946f1514d505d173c82648"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/disputes/{dispute_id}/evidence-text'.format(dispute_id='dispute_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dispute_evidence(client):
    """Test case for delete_dispute_evidence

    DeleteDisputeEvidence
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/disputes/{dispute_id}/evidence/{evidence_id}'.format(dispute_id='dispute_id_example', evidence_id='evidence_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_dispute_evidence(client):
    """Test case for list_dispute_evidence

    ListDisputeEvidence
    """
    params = [('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/disputes/{dispute_id}/evidence'.format(dispute_id='dispute_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_disputes(client):
    """Test case for list_disputes

    ListDisputes
    """
    params = [('cursor', 'cursor_example'),
                    ('states', 'states_example'),
                    ('location_id', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/disputes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_dispute(client):
    """Test case for retrieve_dispute

    RetrieveDispute
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/disputes/{dispute_id}'.format(dispute_id='dispute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_dispute_evidence(client):
    """Test case for retrieve_dispute_evidence

    RetrieveDisputeEvidence
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/disputes/{dispute_id}/evidence/{evidence_id}'.format(dispute_id='dispute_id_example', evidence_id='evidence_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_evidence(client):
    """Test case for submit_evidence

    SubmitEvidence
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/disputes/{dispute_id}/submit-evidence'.format(dispute_id='dispute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

