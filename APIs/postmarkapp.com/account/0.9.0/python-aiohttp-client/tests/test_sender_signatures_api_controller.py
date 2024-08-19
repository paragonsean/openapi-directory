# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sender_listing_results import SenderListingResults
from openapi_server.models.sender_signature_creation_model import SenderSignatureCreationModel
from openapi_server.models.sender_signature_editing_model import SenderSignatureEditingModel
from openapi_server.models.sender_signature_extended_information import SenderSignatureExtendedInformation
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_create_sender_signature(client):
    """Test case for create_sender_signature

    Create a Sender Signature
    """
    body = {"ReplyToEmail":"ReplyToEmail","FromEmail":"FromEmail","Name":"Name","ReturnPathDomain":"ReturnPathDomain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/senders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sender_signature(client):
    """Test case for delete_sender_signature

    Delete a Sender Signature
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/senders/{signatureid}'.format(signatureid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_sender_signature(client):
    """Test case for edit_sender_signature

    Update a Sender Signature
    """
    body = {"ReplyToEmail":"ReplyToEmail","Name":"Name","ReturnPathDomain":"ReturnPathDomain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/senders/{signatureid}'.format(signatureid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sender_signature(client):
    """Test case for get_sender_signature

    Get a Sender Signature
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='GET',
        path='/senders/{signatureid}'.format(signatureid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sender_signatures(client):
    """Test case for list_sender_signatures

    List Sender Signatures
    """
    params = [('count', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='GET',
        path='/senders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_new_dkim_key_for_sender_signature(client):
    """Test case for request_new_dkim_key_for_sender_signature

    Request a new DKIM Key
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/senders/{signatureid}/requestnewdkim'.format(signatureid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_spf_verification_for_sender_signature(client):
    """Test case for request_spf_verification_for_sender_signature

    Request DNS Verification for SPF
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/senders/{signatureid}/verifyspf'.format(signatureid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_sender_signature_confirmation_email(client):
    """Test case for resend_sender_signature_confirmation_email

    Resend Signature Confirmation Email
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/senders/{signatureid}/resend'.format(signatureid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

