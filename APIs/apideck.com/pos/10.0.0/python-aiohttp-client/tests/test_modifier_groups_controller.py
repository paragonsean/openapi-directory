# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_modifier_group_response import CreateModifierGroupResponse
from openapi_server.models.delete_modifier_group_response import DeleteModifierGroupResponse
from openapi_server.models.get_modifier_group_response import GetModifierGroupResponse
from openapi_server.models.get_modifier_groups_response import GetModifierGroupsResponse
from openapi_server.models.modifier_group import ModifierGroup
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_modifier_group_response import UpdateModifierGroupResponse


pytestmark = pytest.mark.asyncio

async def test_modifier_groups_add(client):
    """Test case for modifier_groups_add

    Create Modifier Group
    """
    body = {"alternate_name":"Modifier New","maximum_allowed":5,"created_at":"2020-09-30T07:43:32Z","modifiers":[{"alternate_name":"Modifier New","available":True,"name":"Modifier","price_amount":10,"currency":"USD","id":"12345"},{"alternate_name":"Modifier New","available":True,"name":"Modifier","price_amount":10,"currency":"USD","id":"12345"}],"created_by":"12345","custom_mappings":"{}","present_at_all_locations":False,"selection_type":"single","deleted":True,"updated_at":"2020-09-30T07:43:32Z","row_version":"1-12345","minimum_required":1,"name":"Modifier","updated_by":"12345","id":"12345"}
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
        path='/pos/modifier-groups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifier_groups_all(client):
    """Test case for modifier_groups_all

    List Modifier Groups
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
        path='/pos/modifier-groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifier_groups_delete(client):
    """Test case for modifier_groups_delete

    Delete Modifier Group
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/pos/modifier-groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifier_groups_one(client):
    """Test case for modifier_groups_one

    Get Modifier Group
    """
    params = [('raw', False),
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
        path='/pos/modifier-groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modifier_groups_update(client):
    """Test case for modifier_groups_update

    Update Modifier Group
    """
    body = {"alternate_name":"Modifier New","maximum_allowed":5,"created_at":"2020-09-30T07:43:32Z","modifiers":[{"alternate_name":"Modifier New","available":True,"name":"Modifier","price_amount":10,"currency":"USD","id":"12345"},{"alternate_name":"Modifier New","available":True,"name":"Modifier","price_amount":10,"currency":"USD","id":"12345"}],"created_by":"12345","custom_mappings":"{}","present_at_all_locations":False,"selection_type":"single","deleted":True,"updated_at":"2020-09-30T07:43:32Z","row_version":"1-12345","minimum_required":1,"name":"Modifier","updated_by":"12345","id":"12345"}
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
        path='/pos/modifier-groups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

