# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_payment_dispute_request import AcceptPaymentDisputeRequest
from openapi_server.models.add_evidence_payment_dispute_request import AddEvidencePaymentDisputeRequest
from openapi_server.models.add_evidence_payment_dispute_response import AddEvidencePaymentDisputeResponse
from openapi_server.models.contest_payment_dispute_request import ContestPaymentDisputeRequest
from openapi_server.models.dispute_summary_response import DisputeSummaryResponse
from openapi_server.models.file_evidence import FileEvidence
from openapi_server.models.payment_dispute import PaymentDispute
from openapi_server.models.payment_dispute_activity_history import PaymentDisputeActivityHistory
from openapi_server.models.update_evidence_payment_dispute_request import UpdateEvidencePaymentDisputeRequest


pytestmark = pytest.mark.asyncio

async def test_accept_payment_dispute(client):
    """Test case for accept_payment_dispute

    Accept Payment Dispute
    """
    body = {"returnAddress":{"country":"country","primaryPhone":{"number":"number","countryCode":"countryCode"},"stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","county":"county","addressLine1":"addressLine1","fullName":"fullName","addressLine2":"addressLine2"},"revision":0}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/accept'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_evidence(client):
    """Test case for add_evidence

    Add an Evidence File
    """
    body = {"lineItems":[{"itemId":"itemId","lineItemId":"lineItemId"},{"itemId":"itemId","lineItemId":"lineItemId"}],"evidenceType":"evidenceType","files":[{"fileId":"fileId"},{"fileId":"fileId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/add_evidence'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contest_payment_dispute(client):
    """Test case for contest_payment_dispute

    Contest Payment Dispute
    """
    body = {"note":"note","returnAddress":{"country":"country","primaryPhone":{"number":"number","countryCode":"countryCode"},"stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","county":"county","addressLine1":"addressLine1","fullName":"fullName","addressLine2":"addressLine2"},"revision":0}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/contest'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_evidence_content(client):
    """Test case for fetch_evidence_content

    Get Payment Dispute Evidence File
    """
    params = [('evidence_id', 'evidence_id_example'),
                    ('file_id', 'file_id_example')]
    headers = { 
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/fetch_evidence_content'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_activities(client):
    """Test case for get_activities

    Get Payment Dispute Activity
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/activity'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_dispute(client):
    """Test case for get_payment_dispute

    Get Payment Dispute Details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_dispute_summaries(client):
    """Test case for get_payment_dispute_summaries

    Search Payment Dispute by Filters
    """
    params = [('order_id', 'order_id_example'),
                    ('buyer_username', 'buyer_username_example'),
                    ('open_date_from', 'open_date_from_example'),
                    ('open_date_to', 'open_date_to_example'),
                    ('payment_dispute_status', 'payment_dispute_status_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/payment_dispute_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_evidence(client):
    """Test case for update_evidence

    Update evidence
    """
    body = {"lineItems":[{"itemId":"itemId","lineItemId":"lineItemId"},{"itemId":"itemId","lineItemId":"lineItemId"}],"evidenceId":"evidenceId","evidenceType":"evidenceType","files":[{"fileId":"fileId"},{"fileId":"fileId"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/update_evidence'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_evidence_file(client):
    """Test case for upload_evidence_file

    Upload an Evidence File
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/upload_evidence_file'.format(payment_dispute_id='payment_dispute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

