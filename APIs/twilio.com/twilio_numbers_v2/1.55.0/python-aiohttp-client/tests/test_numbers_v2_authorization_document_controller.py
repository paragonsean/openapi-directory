# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorization_document_enum_status import AuthorizationDocumentEnumStatus
from openapi_server.models.list_authorization_document_response import ListAuthorizationDocumentResponse
from openapi_server.models.numbers_v2_authorization_document import NumbersV2AuthorizationDocument


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_authorization_document(client):
    """Test case for create_authorization_document

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'address_sid': 'address_sid_example',
        'cc_emails': ['cc_emails_example'],
        'contact_phone_number': 'contact_phone_number_example',
        'contact_title': 'contact_title_example',
        'email': 'email_example',
        'hosted_number_order_sids': ['hosted_number_order_sids_example']
        }
    response = await client.request(
        method='POST',
        path='/v2/HostedNumber/AuthorizationDocuments',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_authorization_document(client):
    """Test case for delete_authorization_document

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/HostedNumber/AuthorizationDocuments/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_authorization_document(client):
    """Test case for fetch_authorization_document

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/HostedNumber/AuthorizationDocuments/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_authorization_document(client):
    """Test case for list_authorization_document

    
    """
    params = [('Email', 'email_example'),
                    ('Status', openapi_server.AuthorizationDocumentEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/HostedNumber/AuthorizationDocuments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

