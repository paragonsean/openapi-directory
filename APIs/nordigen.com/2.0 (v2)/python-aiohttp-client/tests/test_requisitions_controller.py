# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.paginated_requisition_list import PaginatedRequisitionList
from openapi_server.models.requisition import Requisition
from openapi_server.models.requisition_request import RequisitionRequest
from openapi_server.models.spectacular_requisition import SpectacularRequisition


pytestmark = pytest.mark.asyncio

async def test_delete_requisition_by_id_v2(client):
    """Test case for delete_requisition_by_id_v2

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/requisitions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requisition_by_id(client):
    """Test case for requisition_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/requisitions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_requisition_created(client):
    """Test case for requisition_created

    
    """
    body = {"redirect":"https://openapi-generator.tech","reference":"reference","account_selection":False,"agreement":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","user_language":"user_language","redirect_immediate":False,"institution_id":"institution_id","ssn":"ssn"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/requisitions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_all_requisitions(client):
    """Test case for retrieve_all_requisitions

    
    """
    params = [('limit', 100),
                    ('offset', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/requisitions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

