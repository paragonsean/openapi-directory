# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.end_user_agreement import EndUserAgreement
from openapi_server.models.end_user_agreement_request import EndUserAgreementRequest
from openapi_server.models.enduser_acceptance_details_request import EnduserAcceptanceDetailsRequest
from openapi_server.models.paginated_end_user_agreement_list import PaginatedEndUserAgreementList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accept_eua(client):
    """Test case for accept_eua

    
    """
    body = {"ip_address":"ip_address","user_agent":"user_agent"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/agreements/enduser/{id}/accept'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_eua_v2(client):
    """Test case for create_eua_v2

    
    """
    body = {"access_scope":[["",""],["",""]],"access_valid_for_days":8,"institution_id":"institution_id","max_historical_days":440}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/agreements/enduser/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_eua_by_id_v2(client):
    """Test case for delete_eua_by_id_v2

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/agreements/enduser/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_all_euas_for_an_end_user_v2(client):
    """Test case for retrieve_all_euas_for_an_end_user_v2

    
    """
    params = [('limit', 100),
                    ('offset', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/agreements/enduser/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_eua_by_id_v2(client):
    """Test case for retrieve_eua_by_id_v2

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/agreements/enduser/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

