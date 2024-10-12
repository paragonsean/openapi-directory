# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.peppol_identifier import PeppolIdentifier
from openapi_server.models.peppol_identifier_create import PeppolIdentifierCreate


pytestmark = pytest.mark.asyncio

async def test_create_peppol_identifier(client):
    """Test case for create_peppol_identifier

    Create a new PeppolIdentifier
    """
    body = {"identifier":"identifier","corppass":{"client_redirect_success_url":"client_redirect_success_url","signer_name":"signer_name","flow_type":"corppass_flow_redirect","simulate_corppass":False,"client_redirect_fail_url":"client_redirect_fail_url","signer_email":"signer_email","enabled":True},"scheme":"scheme","superscheme":"superscheme"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/legal_entities/{legal_entity_id}/peppol_identifiers'.format(legal_entity_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_peppol_identifier(client):
    """Test case for delete_peppol_identifier

    Delete PeppolIdentifier
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/legal_entities/{legal_entity_id}/peppol_identifiers/{superscheme}/{scheme}/{identifier}'.format(legal_entity_id=56, superscheme='superscheme_example', scheme='scheme_example', identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

