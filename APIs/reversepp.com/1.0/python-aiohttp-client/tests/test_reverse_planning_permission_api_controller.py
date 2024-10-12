# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_applicant_single_applicant_multi_request import PostApplicantSingleApplicantMultiRequest
from openapi_server.models.post_free_end_point_free_request import PostFreeEndPointFreeRequest
from openapi_server.models.post_partial_address_multi_partial_address_multi_request import PostPartialAddressMultiPartialAddressMultiRequest
from openapi_server.models.post_postcode_multi_postcode_multi_request import PostPostcodeMultiPostcodeMultiRequest
from openapi_server.models.post_proposal_multi_proposal_request import PostProposalMultiProposalRequest


pytestmark = pytest.mark.asyncio

async def test_post_applicant_single_applicant_multi(client):
    """Test case for post_applicant_single_applicant_multi

    
    """
    payload = openapi_server.PostApplicantSingleApplicantMultiRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/applicant_multi',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_applicant_single_applicant_single(client):
    """Test case for post_applicant_single_applicant_single

    
    """
    payload = openapi_server.PostApplicantSingleApplicantMultiRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/applicant_single',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_free_end_point_free(client):
    """Test case for post_free_end_point_free

    
    """
    payload = openapi_server.PostFreeEndPointFreeRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/free',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_partial_addres_single_partial_address_single(client):
    """Test case for post_partial_addres_single_partial_address_single

    
    """
    payload = openapi_server.PostPartialAddressMultiPartialAddressMultiRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/partial_address_single',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_partial_address_multi_partial_address_multi(client):
    """Test case for post_partial_address_multi_partial_address_multi

    
    """
    payload = openapi_server.PostPartialAddressMultiPartialAddressMultiRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/partial_address_multi',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_postcode_multi_postcode_multi(client):
    """Test case for post_postcode_multi_postcode_multi

    
    """
    payload = openapi_server.PostPostcodeMultiPostcodeMultiRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/postcode_multi',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_postcode_single_postcode_single(client):
    """Test case for post_postcode_single_postcode_single

    
    """
    payload = openapi_server.PostPostcodeMultiPostcodeMultiRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/postcode_single',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_proposal_multi_proposal(client):
    """Test case for post_proposal_multi_proposal

    
    """
    payload = openapi_server.PostProposalMultiProposalRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/proposal',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

