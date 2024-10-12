# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_dispute_request import AcceptDisputeRequest
from openapi_server.models.accept_dispute_response import AcceptDisputeResponse
from openapi_server.models.defend_dispute_request import DefendDisputeRequest
from openapi_server.models.defend_dispute_response import DefendDisputeResponse
from openapi_server.models.defense_reasons_request import DefenseReasonsRequest
from openapi_server.models.defense_reasons_response import DefenseReasonsResponse
from openapi_server.models.delete_defense_document_request import DeleteDefenseDocumentRequest
from openapi_server.models.delete_defense_document_response import DeleteDefenseDocumentResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.supply_defense_document_request import SupplyDefenseDocumentRequest
from openapi_server.models.supply_defense_document_response import SupplyDefenseDocumentResponse


pytestmark = pytest.mark.asyncio

async def test_post_accept_dispute(client):
    """Test case for post_accept_dispute

    Accept a dispute
    """
    body = {"merchantAccountCode":"merchantAccountCode","disputePspReference":"disputePspReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ca/services/DisputeService/v30/acceptDispute',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_defend_dispute(client):
    """Test case for post_defend_dispute

    Defend a dispute
    """
    body = {"merchantAccountCode":"merchantAccountCode","defenseReasonCode":"defenseReasonCode","disputePspReference":"disputePspReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ca/services/DisputeService/v30/defendDispute',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_delete_dispute_defense_document(client):
    """Test case for post_delete_dispute_defense_document

    Delete a defense document
    """
    body = {"merchantAccountCode":"merchantAccountCode","disputePspReference":"disputePspReference","defenseDocumentType":"defenseDocumentType"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ca/services/DisputeService/v30/deleteDisputeDefenseDocument',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_retrieve_applicable_defense_reasons(client):
    """Test case for post_retrieve_applicable_defense_reasons

    Get applicable defense reasons
    """
    body = {"merchantAccountCode":"merchantAccountCode","disputePspReference":"disputePspReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ca/services/DisputeService/v30/retrieveApplicableDefenseReasons',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_supply_defense_document(client):
    """Test case for post_supply_defense_document

    Supply a defense document
    """
    body = {"merchantAccountCode":"merchantAccountCode","disputePspReference":"disputePspReference","defenseDocuments":[{"defenseDocumentTypeCode":"defenseDocumentTypeCode","contentType":"contentType","content":"content"},{"defenseDocumentTypeCode":"defenseDocumentTypeCode","contentType":"contentType","content":"content"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ca/services/DisputeService/v30/supplyDefenseDocument',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

