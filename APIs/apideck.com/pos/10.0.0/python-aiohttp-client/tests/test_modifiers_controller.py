# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_modifier_response import CreateModifierResponse
from openapi_server.models.delete_modifier_response import DeleteModifierResponse
from openapi_server.models.get_modifier_response import GetModifierResponse
from openapi_server.models.get_modifiers_response import GetModifiersResponse
from openapi_server.models.modifier import Modifier
from openapi_server.models.modifier_group_filter import ModifierGroupFilter
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_modifier_response import UpdateModifierResponse


pytestmark = pytest.mark.asyncio

async def test_modifiers_add(client):
    """Test case for modifiers_add

    Create Modifier
    """
    body = {"alternate_name":"Modifier New","available":True,"created_at":"2020-09-30T07:43:32Z","price_amount":10,"created_by":"12345","custom_mappings":"{}","modifier_group_id":"123","updated_at":"2020-09-30T07:43:32Z","name":"Modifier","updated_by":"12345","idempotency_key":"random_string","currency":"USD","id":"12345"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pos/modifiers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifiers_all(client):
    """Test case for modifiers_all

    List Modifiers
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pos/modifiers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifiers_delete(client):
    """Test case for modifiers_delete

    Delete Modifier
    """
    params = [('raw', False),
                    ('filter', openapi_server.ModifierGroupFilter())]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/pos/modifiers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifiers_one(client):
    """Test case for modifiers_one

    Get Modifier
    """
    params = [('raw', False),
                    ('filter', openapi_server.ModifierGroupFilter()),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pos/modifiers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifiers_update(client):
    """Test case for modifiers_update

    Update Modifier
    """
    body = {"alternate_name":"Modifier New","available":True,"created_at":"2020-09-30T07:43:32Z","price_amount":10,"created_by":"12345","custom_mappings":"{}","modifier_group_id":"123","updated_at":"2020-09-30T07:43:32Z","name":"Modifier","updated_by":"12345","idempotency_key":"random_string","currency":"USD","id":"12345"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/pos/modifiers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

