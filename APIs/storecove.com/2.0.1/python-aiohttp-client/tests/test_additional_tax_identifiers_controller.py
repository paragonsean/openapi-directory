# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.additional_tax_identifier import AdditionalTaxIdentifier
from openapi_server.models.additional_tax_identifier_create import AdditionalTaxIdentifierCreate
from openapi_server.models.additional_tax_identifier_update import AdditionalTaxIdentifierUpdate
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_create_additional_tax_identifier(client):
    """Test case for create_additional_tax_identifier

    Create a new AdditionalTaxIdentifier
    """
    body = {"country":"country","identifier":"identifier","third_party_password":"third_party_password","scheme":"scheme","county":"county","third_party_username":"third_party_username","superscheme":"superscheme"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/legal_entities/{legal_entity_id}/additional_tax_identifiers'.format(legal_entity_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_additional_tax_identifier(client):
    """Test case for delete_additional_tax_identifier

    Delete AdditionalTaxIdentifier
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/legal_entities/{legal_entity_id}/additional_tax_identifiers/{id}'.format(legal_entity_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_additional_tax_identifier(client):
    """Test case for get_additional_tax_identifier

    Get AdditionalTaxIdentifier
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/legal_entities/{legal_entity_id}/additional_tax_identifiers/{id}'.format(legal_entity_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_additional_tax_identifier(client):
    """Test case for update_additional_tax_identifier

    Update AdditionalTaxIdentifier
    """
    body = {"identifier":"identifier","third_party_password":"third_party_password","third_party_username":"third_party_username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/legal_entities/{legal_entity_id}/additional_tax_identifiers/{id}'.format(legal_entity_id=56, id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

