# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dkim_rotation_response import DKIMRotationResponse
from openapi_server.models.domain_creation_model import DomainCreationModel
from openapi_server.models.domain_editing_model import DomainEditingModel
from openapi_server.models.domain_extended_information import DomainExtendedInformation
from openapi_server.models.domain_listing_results import DomainListingResults
from openapi_server.models.domain_spf_result import DomainSPFResult
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_create_domain(client):
    """Test case for create_domain

    Create a Domain
    """
    body = {"Name":"Name","ReturnPathDomain":"ReturnPathDomain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/domains',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_domain(client):
    """Test case for delete_domain

    Delete a Domain
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/domains/{domainid}'.format(domainid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_domain(client):
    """Test case for edit_domain

    Update a Domain
    """
    body = {"ReturnPathDomain":"ReturnPathDomain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/domains/{domainid}'.format(domainid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain(client):
    """Test case for get_domain

    Get a Domain
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='GET',
        path='/domains/{domainid}'.format(domainid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_domains(client):
    """Test case for list_domains

    List Domains
    """
    params = [('count', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='GET',
        path='/domains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_dkim_verification_for_domain(client):
    """Test case for request_dkim_verification_for_domain

    Request DNS Verification for DKIM
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/domains/{domainid}/verifydkim'.format(domainid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_return_path_verification_for_domain(client):
    """Test case for request_return_path_verification_for_domain

    Request DNS Verification for Return-Path
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/domains/{domainid}/verifyreturnpath'.format(domainid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_spf_verification_for_domain(client):
    """Test case for request_spf_verification_for_domain

    Request DNS Verification for SPF
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/domains/{domainid}/verifyspf'.format(domainid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rotate_dkim_key_for_domain(client):
    """Test case for rotate_dkim_key_for_domain

    Rotate DKIM Key
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/domains/{domainid}/rotatedkim'.format(domainid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

