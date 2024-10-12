# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.legal_entity import LegalEntity
from openapi_server.models.legal_entity_create import LegalEntityCreate
from openapi_server.models.legal_entity_update import LegalEntityUpdate


pytestmark = pytest.mark.asyncio

async def test_create_legal_entity(client):
    """Test case for create_legal_entity

    Create a new LegalEntity
    """
    body = {"tenant_id":"tenant_id","zip":"zip","country":"AD","city":"city","county":"county","rea":{"identifier":"identifier","capital":6.027456183070403,"province":"AG","partners":"SU","liquidation_status":"LN"},"advertisements":["invoice","invoice"],"third_party_password":"third_party_password","party_name":"party_name","public":True,"third_party_username":"third_party_username","line2":"line2","line1":"line1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/legal_entities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_legal_entity(client):
    """Test case for delete_legal_entity

    Delete LegalEntity
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/legal_entities/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_legal_entity(client):
    """Test case for get_legal_entity

    Get LegalEntity
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/legal_entities/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_legal_entity(client):
    """Test case for update_legal_entity

    Update LegalEntity
    """
    body = {"tenant_id":"tenant_id","zip":"zip","country":"AD","city":"city","county":"county","rea":{"identifier":"identifier","capital":6.027456183070403,"province":"AG","partners":"SU","liquidation_status":"LN"},"smart_inbox":"smart_inbox","advertisements":["invoice","invoice"],"third_party_password":"third_party_password","party_name":"party_name","public":True,"third_party_username":"third_party_username","id":0,"line2":"line2","line1":"line1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/legal_entities/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

