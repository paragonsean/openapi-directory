# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.administration import Administration
from openapi_server.models.administration_create import AdministrationCreate
from openapi_server.models.administration_update import AdministrationUpdate
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_create_administration(client):
    """Test case for create_administration

    Create a new Administration
    """
    body = {"legal_entity_id":0,"sender_email_identity_id":6,"package_version":"peppol_bis_v3","packaging":"ubl","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/legal_entities/{legal_entity_id}/administrations'.format(legal_entity_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_administration(client):
    """Test case for delete_administration

    Delete Administration
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/legal_entities/{legal_entity_id}/administrations/{id}'.format(legal_entity_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_administration(client):
    """Test case for get_administration

    Get Administration
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/legal_entities/{legal_entity_id}/administrations/{id}'.format(legal_entity_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_administration(client):
    """Test case for update_administration

    Update Administration
    """
    body = {"sender_email_identity_id":0,"package_version":"peppol_bis_v3","packaging":"ubl","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/legal_entities/{legal_entity_id}/administrations/{id}'.format(legal_entity_id=56, id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

